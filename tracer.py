import requests

import json

print("/n ~| Kedy.Coder|~ /n")

target = input("Hedef İp Adresi => ")

r = requests.get("http://ip-api.com/json/"+target)

ipt = json.loads(r.text)

if ipt['status'] in 'success':

 print("[!] Bilgiler Bulundu")

 print("Country : "+ipt["country"])

 print("Country Code : "+ipt["countryCode"])

 print("Region : "+ipt["region"])

 print("Region Name : "+ipt["regionName"])

 print("City : "+ipt["city"])

 print("ISP : "+ipt["isp"])

 print("Query : "+ipt["query"])

else:

 print("Başarısız Oldu...")
