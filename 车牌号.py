import re
import requests
from lxml import etree
import time
from os import remove
import aiofiles
from aiohttp import ClientSession, ClientTimeout
import asyncio
from colorama import init


def len_str(string):
    count = 0
    for ch in string:
        if ch >= '\u007f':
            count += 1
    return count


def width(string, length):
    if length < len_str(string):
        return 0
    else:
        return length - len_str(string)


# 获取小说书名、目录、章节链接
def get_book_info(url):
    try:
        response1 = requests.get(url, cookies=cookies, headers=headers)
        html1 = etree.HTML(response1.text, parser=etree.HTMLParser(encoding='utf-8'))
        chapter_name1 = html1.xpath('/html/body/div[5]/dl/dd/a/text()')
        chapter_name2 = html1.xpath('/html/body/div[5]/dl/span/dd/a/text()')
        chapter_url1 = html1.xpath('/html/body/div[5]/dl/dd/a/@href')
        chapter_url2 = html1.xpath('/html/body/div[5]/dl/span/dd/a/@href')
        chapter_names = chapter_name1[0:10] + chapter_name2 + chapter_name1[-10:]
        chapter_urls = chapter_url1[0:10] + chapter_url2 + chapter_url1[-10:]  # 拼接完整章节目录和链接
        novel_name = html1.xpath('/html/body/div[4]/div[2]/h1/text()')  # 获取小说书名
        return chapter_names, chapter_urls, novel_name
    except Exception as e:
        print(f'\033[31m获取小说书名出错，出错原因\033[0m：{e}')
        return [], [], ['error']


# 单章小说内容下载
async def singe_chapter_download(url1, name1, sem):
    chapter_url = f"https://www.biqg.cc/{url1}"  # 拼接章节网址
    i = 0
    async with sem:
        while i < 5:
            i += 1
            try:
                timeout = ClientTimeout(total=20)
                async with ClientSession(headers=headers, cookies=cookies, timeout=timeout) as session:
                    async with session.get(chapter_url) as resp1:
                        html2 = etree.HTML(await resp1.text(), parser=etree.HTMLParser(encoding='utf-8'))
                        singe_content = html2.xpath('//*[@id="chaptercontent"]/text()')  # 获取小说章节内容
                        result = re.findall(r'第(.*?)章', singe_content[0])
                        if len(result):
                            del singe_content[0]  # 去除可能出现的重复标题
                        content = singe_content[0:-2]  # 去除网站附带的广告链接
                        name2 = strinfo.sub('_', name1)  # 去除小说章节书名中的特殊字符，避免生成章节文件时出错
                        async with aiofiles.open(f"./小说/{name2}.txt", "w", encoding="utf-8") as f:  # 在小说目录下创建临时的单章txt
                            await f.write(name2 + '\r\r\r')
                            for lists in content:
                                await f.write(lists + '\r\r')
                        name2_width = 60 - len_str(name2)
                        print(f'{name2:<{name2_width}}finish')
                        break
            except Exception as e:
                print(f'{name1}                               false        {i}/5')
                print(e)


# 创建异步任务
async def create_tasks(name_chapter, url_chapter, lens):
    tasks = []
    if lens > 1000:
        sema = 1000
    else:
        sema = lens
    sem = asyncio.Semaphore(sema)  # 设置同时进行的异步数量，可以根据上面自行设定，数量越大，下载越快
    for url4, name3 in zip(url_chapter, name_chapter):
        tasks.append(asyncio.create_task(singe_chapter_download(url4, name3, sem)))  # 创建任务
    await asyncio.gather(*tasks)


def start_download(url):
    chapter_name, chapter_url, novel_name = get_book_info(f'https://www.biqg.cc/{url}')  # 获取小说目录，对应的网页链接，书名
    length = len(chapter_name)
    if length:
        print(f"\033[31m《{novel_name[0]}》共{length}章, 开始下载！！\033[0m\n\n")
        time1 = time.time()
        loop.run_until_complete(create_tasks(chapter_name, chapter_url, length))  # 提交任务
        time2 = time.time()
        with open(f'./小说/{novel_name[0]}.txt', 'w', encoding='utf-8') as f1:  # 将分散的小说章节写入一个{书名}.txt中
            for chapter_names in chapter_name:
                chapter_name2 = strinfo.sub("_", chapter_names)
                try:
                    with open(f'./小说/{chapter_name2}.txt', 'r', encoding='utf-8') as f2:
                        text1 = f2.read()
                        f1.write(text1)
                    remove(f"./小说/{chapter_name2}.txt")  # 移除已写入{书名}.txt的临时章节
                except Exception as e:
                    print(f'{chapter_names}  false 错误原因:{e}')
            print('==============================下载完成==============================\n')
        print(f'共耗时：\033[33m{time2 - time1:.2f}s\033[0m\n\n')
        print(f'\033[32m《{novel_name[0]}》已下载！！！！\033[0m\n\n\n')
    else:
        print('error')


if __name__ == '__main__':
    cookies = {
    }

    headers = {
        'authority': 'www.biqg.cc',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.biqg.cc/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"', 'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }
    # get_title('https://www.bige3.cc/book/66/') 7293788896888884263
    init(autoreset=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    strinfo = re.compile('[/:*?"<>|\\\\]')  # 匹配字符串中特殊的字符
    print('小说保存在exe同目录下的小说文件夹下')
    a = input('笔趣阁本地搜索：    1\n笔趣阁书籍id下载：    2\n请选择：')
    if a == '1':
        with open('./小说/all_books.txt', 'r', encoding='utf-8') as f:
            books = f.read()
        books = eval(books)
        while True:
            k, target = 1, []
            a = input('本地搜索已启动:')
            for dic in books:
                result = re.findall(f'{a}', dic[0] + dic[1])
                if len(result):
                    target.append(dic)
                    print(f'{k:<4}{dic[0]:^{width(dic[0], 60)}}{dic[1]:<{width(dic[1], 40)}}')
                    k = k + 1
                    if k > 100:
                        break
            if len(target) == 0:
                print('小说不存在，请重新输入')
                continue
            choose = input('请输入序号(批量下载请使用空格分隔序号, 重新搜索请输入0, 全部下载请输入101)：')
            if choose == '0':
                continue
            elif choose == '101':
                for book in target:
                    start_download(book[2])
                    time.sleep(0.5)
            else:
                choose_list = choose.split(' ')
                for ids in choose_list:
                    if ids.isdigit():
                        if int(ids) <= len(target):
                            if int(ids):
                                start_download(target[int(ids) - 1][2])
                                time.sleep(0.5)
                            else:
                                continue
                        else:
                            print('\033[31m序号超出范围，请重新搜索！！\033[0m')
                    else:
                        print('\033[31m请输入正确格式的书籍序号！！！！\033[0m')
    elif a == '2':
        print('\n请到 \033[32mhttps://www.biqg.cc/\033[0m 网站搜索你想下的小说，并获取相应的的书籍id\n')
        while True:
            book_id = input('请输入书籍id(即小说链接数字部分):')
            start_download(f"/book/{book_id}/")
