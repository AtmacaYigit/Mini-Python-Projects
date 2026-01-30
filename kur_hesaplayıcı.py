import requests
import json

api_key = "Api Key"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan Döviz Türü: ").upper()
alinan_doviz = input("Alınan Döviz Türü: ").upper()
miktar = float(input(f"Ne kadar {bozulan_doviz} bozmak istiyorsunuz: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

kur = sonuc_json["conversion_rates"][alinan_doviz]
sonuc_miktar = miktar * kur

print(f"1 {bozulan_doviz} = {kur} {alinan_doviz}")
print(f"{miktar} {bozulan_doviz} = {sonuc_miktar} {alinan_doviz}")
