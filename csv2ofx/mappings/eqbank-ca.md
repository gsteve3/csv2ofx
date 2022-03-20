# README


    "payee": payee_func,


## Example Data (CSV File)
`eqbank-ca.csv`


### Validation

- 14 lines
- 14 Transactions imported


## TODO


### - [ ] $ 	Amount transferred, if cash is moved between accounts 	Investment 	$25,000.00

[Quicken Interchange Format - Wikipedia](https://en.wikipedia.org/wiki/Quicken_Interchange_Format)

> $ Amount transferred, if cash is moved between accounts Investment $25,000.00


### Opening Balance
[Quicken Interchange Format - Wikipedia](https://en.wikipedia.org/wiki/Quicken_Interchange_Format)

> opening balance transaction, identified by 'Opening Balance' in the 'P' field (POpening Balance)


[Quicken Interchange Format - Wikipedia](https://en.wikipedia.org/wiki/Quicken_Interchange_Format)

> **QIF File Content**
> ```
> !Type:Bank                       --------------------------------------------------------------
> D2/10'2020
> T0.00
> CX                                    ACCOUNT DETAILS
> POpening Balance
> L\[TestExport\]
> ^                                --------------------------------------------------------------
> D2/14'2020
> T67.50
> PT-Mobile
> LBills:Cell Phone                     T-Mobile Transaction
> SBills:Cell Phone                        (+/- split)
> Esign up credit                          (memos for splits, no overall memo)
> $-15.00
> SBills:Cell Phone
> Enew account
> $82.50
> ^                                --------------------------------------------------------------
> // /// /// ... (truncated, snipped, call-it-what-you-want?) ... // // //
> ```






```
GET /web/v1.1/payment/v1.0/order HTTP/1.1
Host: web-api.eqbank.ca
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://secure.eqbank.ca/
paymentOrderType: ETRANSFER
paymentOrderSubType: OUTGOING
fromDate: 2022-02-18T01:36:12.818Z
toDate: 2022-03-20T00:36:12.818Z
correlationId: 3e289d4e-242a-4263-b8b7-dbc904e136c4
authorization: Basic MDlmZjUwNTM0NzVmNDBkYmExNDNiNTIwOTc5ZmQ4MDk6QzkzMDRDN2FGMjJGNEJmQjk4N2EwNDRkYkUwMDMxOTc=
accessToken: eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5NGNhMDY2MC1hN2U1LTExZWMtOGEzOS0wMjQyNWNjZGNjNWQiLCJpYXQiOjE2NDc3MzY1MDIsInN1YiI6IkVxdWl0YWJsZSBCYW5rIiwiaXNzIjoiRXF1aXRhYmxlIEJhbmsiLCJleHAiOjE2NDc3Mzc0MDJ9._gyG1ZIY8Kc_BHv6pLVKexrDgx6hjae9chGPxEkT4Mk
email: greg@stevens.pro
Origin: https://secure.eqbank.ca
DNT: 1
Connection: keep-alive
Cookie: _abck=43964AD000F29547E33949B4ECA48FA6~0~YAAQjUq/zPhBp5d/AQAAsMS/pAfW4ZK3+3qY3MBW9toX8kuSPdLZMkfP66zx96Cc8yQVYQJ/rmSxMM+GJDzZyEAnCRLTOPDyGA0t9CHA4LO5kt/avKwNgBm32HJJ9lIQ54BMwicmh1+vGvoMEr0PV+ecIrWkmdrsKyJQl9BzgWpf2Jj8SyO1TQkT/qGnC5D7dO7S322AnuAKqNSaJsktmTfO0cITezs1I/muiCnJVGPPMhCJgwnfr4C0C5nuIEQuxVLSMHS3wYdhu9y4T12y8bMmO8rTx1wOfcypXBn6wgB4TgFVPAYEOdjcOP8geM1TKXCAF8zqvmLrW/Oh86897HdKwEXpxvS17a4eosHyliC7RXdbgyJi61gO4te/frvzN8trv318z8Z7CpY8og6U7dOTVZLL1ODB~-1~-1~-1; LPVID=BlYmFlYjE0Y2I2NTEwM2Iy; _gcl_au=1.1.1505791802.1640646592; _ga_M1FM37GN6F=GS1.1.1647733418.12.0.1647733418.60; _ga=GA1.1.489936694.1640646592; _rdt_uuid=1640646592182.ce6a1b37-c0df-49e1-858a-ba45cfd2441e; _hjid=3dd550a1-344e-4f65-a403-c2fbd86d0bbd; __utma=109394449.489936694.1640646592.1641404398.1642549502.3; __utmz=109394449.1640646593.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1640646593207.1656729106; _hjSessionUser_1450053=eyJpZCI6ImMzZmRhNjhiLWI3OGUtNTdmMi05YTczLTI3OTYxMzQyMThmNCIsImNyZWF0ZWQiOjE2NDA2NDY1OTI5MzEsImV4aXN0aW5nIjp0cnVlfQ==; bm_sz=3D82EB55AD7AF8D43A0E4072AF38DF62~YAAQZgy/zM7tCJ5/AQAAa6qQpA9sS+JiA/AYlxM6tsUU5JdVFedNU03a4DM0IbCDrnhi2TqY1Phs/An2ex+yji5JbbMjCCmnE87tw2Ug+LVIE76a3c8T7TCJAWfWhOMD0ftXkWSYoqtgxi8XfeVCqSIQsYmAlTpdkaXv8YNrd5IN+t54dAN0PVFOq8/TUw==; ak_bmsc=A0895F5032BD0BF4561B1F1C3587BF10~000000000000000000000000000000~YAAQZgy/zNDtCJ5/AQAAa6qQpA8wEupqmbs7O/5JS7K7tYvj32p/qHOXkT5B8xMs57WdAsOo++ZsbgfQu8tjppj8qS7BVFOG5arzoea1P3M+auX9kW0KsQmmZQuDU++vA2kPo/CFKjOZHsaUAFuJgUeiC1LkvL+JemiQkIPQ8EH9F09l9tW5uKKmX6cpHQSDGHPzv93ij4F86WJdibeoOtlBXrucXeiOPH0NIq91zsa+OS9GnRubEhsgyxRvzdnpGefg1pAjw6XnqcbUbf9SL5OR7UeUj1h0qiDsG3CzjOcteoFG1MDF3/4o577PTiBBjNMhHKQB6jkHjzmzaG5ERd3386esUdxv1JavNM0bNgHF3TP2eWaCG0DXI0BYiwCb6NMZDd6Yj9mtIg==; _uetsid=670317b0a7de11ec915fc9eeab06919a; _uetvid=630dac10ced811ebb9568936e11f87f3; bm_sv=C87E1D481D563A932331C9DF8C4CC20E~B2q7+7cuILjGEG0ADRApPyn9WanSRZC+0bufC8NSa1jQyGiUGPxTNRLG509mZKefh7B/ouf/mWNOe1C/Y85k+4QEN4ghcLae9JYMd4cjNDDjGYCPvKw8Q5f/ewkSy4EMKhrNrT99FlD/Hg8QSAzmYR1WyPYxvpQnJ+aI2la15WM=
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Pragma: no-cache
Cache-Control: no-cache
```



---
end