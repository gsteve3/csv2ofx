from operator import itemgetter
from time import strptime


#
# python bin/csv2ofx -qm eqbank-ca data/test/eqbank-ca.csv data/converted/eqbank-ca.qif && cat data/converted/eqbank-ca.qif
#


#
# @since 2022-03-19
# @author https://github.com/gsteve3
#
# Based on eqbank.py which did not work  for my
# www.eqbank.ca accounts circa 2021-12 to 2022-03
# Date format was wrong.
# Import would not work in Quicken or QuickBooks Online.
#
#
# Example Data
# Few different types (Interest, Tansfer, Dirct Deposit, Bill Payment)
#
# Date,Description,Transfer,Balance
# 01 FEB 2022,Interest received,$12.2,$13097.1
# 29 JAN 2022,Transfer from  101769844  to  101372782,-$4000,$13084.9
# 28 JAN 2022,Direct deposit from CDW CANADA ET,$7182,$17084.9
# 24 JAN 2022,Payment to  CAPITAL ONE MASTERCARD,-$3000,$9902.9
# ... (snipped) ...
#


# USAGE
# python bin/csv2ofx -qm eqbank-ca data/test/eqbank-ca.csv
#

# $ python bin/csv2ofx -qm eqbank-ca data/test/eqbank-ca.csv data/converted/eqbank-ca.qif
# https://en.wikipedia.org/wiki/Quicken_Interchange_Format



DEBUG = True


# from rabobank.py 🙏
# Chop up the date from ridiculous DD MMM YYYY format
# example:  01 FEB 2022
def date_func(trxn):
    tag = trxn["Date"].split(" ")
    # thx for strptime(... https://stackoverflow.com/a/5158964
    # Convert JAN to 01 for example.
    monthNum = strptime(tag[1],'%b').tm_mon
    return "{}/{}/{}".format(tag[2], monthNum, tag[0])


# Try to parse payee from description
def payee_func(trxn):
    desc = trxn["Description"]
    # payee = desc.maketrans({
    #     "Direct deposit from": ""
    # })

    payee = desc
    payee = payee.replace("Direct deposit from ", "")
    payee = payee.replace("Payment to ", "")

    if ("Interac e-Transfer sent" in desc):
        payee = ""
    elif ("Transfer from " in desc):
        # payee = "Transfer " + desc.split(" ")[-1]
        payee = desc.split(" ")[-1]
    #
    # NOTE: "Payment to " is handled with a replace before we get here.
    # elif ("Payment to " in desc):
    #     payee = desc.split(" ")[-1]
    return payee


def category_func(trxn):
    # payee = payee_func(trxn)
    desc = trxn["Description"]
    category = ""

    # if ("Interest received" in desc):
    #     category = "Interest"
    # elif ("Direct deposit" in desc):
    #     category = "Payment"
    #

    if ("Interac e-Transfer sent" in desc):
        category = desc.strip()
    elif ("Direct deposit from " in desc):
        category = "Direct Deposit" # Default from new Quicken File
    elif ("Interest received" in desc):
        category = "Interest Inc" # Default from new Quicken File
        # "Inteest Inc" from new Quicken File default Categories 2022-03-19
        # Using to ensure this is Category Type INCOME instead of EXPENSE.
        # Noticed because of reports.
    elif ("Payment to " in desc):
        category = "Bills & Utilities" # Default from new Quicken File
    else:
        descSplit = desc.split(" ")

        if ("Transfer from " in desc):
            # e.g. Transfer from  101769844  to  101572463
            # square brackets from/for Quicken.
            category = "[" + descSplit[-1] + "]"
            # Related...
            # [Quicken Interchange Format - Wikipedia](https://en.wikipedia.org/wiki/Quicken_Interchange_Format)
            # > When editing the QIF file, check for any transaction Category (the field starting with 'L') for an account name contained in brackets, such as \[Checking Account\]. The brackets reference another quicken account, and if left in place will post a transaction in that account in addition to the account being imported to, with potentially troublesome results. Avoid this by removing the text including the brackets and replacing with another category if desired. The only exception to this is an opening balance transaction, identified by 'Opening Balance' in the 'P' field (POpening Balance). In this case, the brackets need to be left in place, and the account name between the brackets must exactly match the account name in the 'N' field.
        else:
            category = descSplit[0] or ""

    return category


def desc_func(trxn):
    # payee = payee_func(trxn)
    desc = trxn["Description"]

    if (DEBUG):
        desc = desc + "; Balance: " + trxn["Balance"]

        # args = parser.parse_args()  # pylint: disable=C0103
        # desc = desc + "; File: " + args.source

    return desc



mapping = {
    "has_header": True,
    "bank": "EQBank.ca",
    "currency": "CAD",
    "delimiter": ",",
    "account": lambda tr: "EQ",
    "date": date_func,
    "desc": desc_func,
    # "notes": desc_func,
    "check_num": itemgetter("Balance"),
    "payee": payee_func,

    # "category": category_func,
    "class": category_func,
    # class (str): the transaction classification (source: `/csv2ofx/qif.py:169`)
    # PROTIP:    "class" = "Category" but Category may be something else in OFX?
    # https://en.wikipedia.org/wiki/Quicken_Interchange_Format

    # "type": lambda tr: "DEBIT" if tr.get("Out") else "CREDIT",
    #
    # EXAMPLE LINE FROM CSV FILE
    #
    #    09 OCT 2021,Transfer from  101769844  to  101523357,-$201.87,$0
    #
    # -$201.87,$0 --- check for negative in first character.
    # UPPER CASE DEBIT and CREDIT is REQUIRED -- not a sloppy mistake.
    "type": lambda tr: "DEBIT" if tr.get("Transfer")[0] == "-" else "CREDIT",
    # "type": "debit",
    "amount": lambda tr: tr.get("Transfer"),
    "balance": itemgetter("Balance"),

}


def get_category_from_desc(description):
    """Detect the account type of a given account

    Args:
        account (str): The account name
        account_types (dict): The account types with matching account names.
        def_type (str): The default account type.

    Returns:
        (str): The resulting account type.

    Examples:
        >>> get_account_type('somecash', {'Cash': ('cash',)}) == 'Cash'
        True
        >>> get_account_type('account', {'Cash': ('cash',)}) == 'n/a'
        True
    """
    _description = description

    category_map = {
        "Invst": ("roth", "ira", "401k", "vanguard"),
        "Bank": ("checking", "savings", "market", "income"),
        "Oth A": ("receivable",),
        "Oth L": ("payable",),
        "CCard": ("visa", "master", "express", "discover", "platinum"),
        "Cash": ("cash", "expenses"),
    }

    for key, values in account_types.items():
        if any(v in account.lower() for v in values):
            _type = key
            break

    return _type

