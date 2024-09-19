import requests
import re
import json
import os
from configobj import ConfigObj

current_directory = os.getcwd()
conf_ini = current_directory + "\\conf\\config.ini"
config = ConfigObj(conf_ini, encoding='UTF-8')
prox = config['ipv4']['prox']
proxyMeta = f"{prox}"
proxysdata = {
    'http': proxyMeta,
    'https': proxyMeta
}


def re_domain(url):
    pattern_domain = r"https?://([^/]+)"
    match = re.search(pattern_domain, url)
    if match:
        domain = match.group(1)
        return domain
    else:
        return None


def getwithp(url, password):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    response = requests.get(url, headers=headers)
    url_pattern = re.compile(r"url\s*:\s*'(/ajaxm\.php\?file=\d+)'")
    url_match = url_pattern.search(response.text).group(1)
    skdklds_pattern = re.compile(r"var\s+skdklds\s*=\s*'([^']*)';")
    skdklds_match = skdklds_pattern.search(response.text).group(1)
    data = {
        'action': 'downprocess',
        'sign': skdklds_match,
        'p': password,
    }
    headers = {
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    response2 = requests.post(f"https://{domain}{url_match}", headers=headers, data=data, proxies=proxysdata)
    data = json.loads(response2.text)
    full_url = data['dom'] + "/file/" + data['url']
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "down_ip=1"
    }
    response3 = requests.get(full_url, headers=headers, allow_redirects=False, proxies=proxysdata)
    return response3.headers['Location']


def getwithoutp(url):
    domain = re_domain(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    response = requests.get(url, headers=headers, proxies=proxysdata)
    iframe_pattern = re.compile(
        r'<iframe\s+class="ifr2"\s+name="\d+"\s+src="([^"]+)"\s+frameborder="0"\s+scrolling="no"></iframe>')
    matches = iframe_pattern.findall(response.text)
    response2 = requests.get(f"https://{domain}{matches[0]}", headers=headers, proxies=proxysdata)
    pattern = r"'sign'\s*:\s*'([^']+)'"
    sign = re.search(pattern, response2.text).group(1)
    pattern2 = r"url\s*:\s*'([^']+)'"
    url2 = re.search(pattern2, response2.text).group(1)
    data = {
        'action': 'downprocess',
        'signs': '?ctdf',
        'sign': sign,
        'websign': '',
        'websignkey': 'bL27',
        'ves': 1
    }
    headers = {
        "Referer": matches[0],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    response3 = requests.post(f"https://{domain}{url2}", headers=headers, data=data, proxies=proxysdata)
    data = json.loads(response3.text)
    full_url = data['dom'] + "/file/" + data['url']
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "down_ip=1"
    }
    response4 = requests.get(full_url, headers=headers, allow_redirects=False, proxies=proxysdata)
    print(response4.headers['Location'])
    return response4.headers['Location']


def run(url):
    result = getwithoutp(url)
    return result


import zipfile
import os


def down(url):
    response = requests.get(url, proxies=proxysdata)
    with open('123.zip', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    # url = "https://2fzb.lanzn.com/iQiwp27fjdmj"
    url = "https://www.lanzoux.com/i42e0ch"
    run(url)
    # down(run(url))
