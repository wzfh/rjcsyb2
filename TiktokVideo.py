import requests

url = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web" \
      "&sec_user_id=MS4wLjABAAAAbAJnWs7EwVE8JgWFKe87gnmzsAC9XCReyQ99vvM6oWmfmqFPSAs5ZtqhEcyYO1wl&max_cursor" \
      "=1723279019000&locate_item_id=7388761148507639094&locate_query=false&show_live_replay_strategy=1" \
      "&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2" \
      "&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true" \
      "&screen_width=1832&screen_height=314&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge" \
      "&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Android" \
      "&os_version=6.0&cpu_core_num=12&device_memory=8&platform=Android&downlink=10&effective_type=4g&round_trip_time" \
      "=150&webid=7347601222205687359&verifyFp=verify_lwllt9d5_131z6m2c_JOGv_4TDi_Aoje_kOMojbHCPw0e&fp" \
      "=verify_lwllt9d5_131z6m2c_JOGv_4TDi_Aoje_kOMojbHCPw0e&msToken" \
      "=MIOLSj1Hic1rlNKxvhty424gjUhagKo0ti6PK1s9uFfs0keS0miQ0metd3ZljkX0KjkQU_3nmJZm8tuYhMjIC1jntmfmuTRAfcZEbz1UzWZVqMDrHgg%3D" \
      "&a_bogus=Y6RZMQgfmDgifD6654ALfY3qVIq3Ykm80SVkMDheNdVzCy39HMYj9exow7zvMIubZsQdIemjy4hGapKgE5570NXV9mJx/2CDm68gtF-D-xSSs1feejumE0ho-JE3Cee8sv15E5mkw72eSYT0Aonn-hnAPfabYrtswyG7GflNv9smkf==" \
      "&verifyFp=verify_lwllt9d5_131z6m2c_JOGv_4TDi_Aoje_kOMojbHCPw0e&fp=verify_lwllt9d5_131z6m2c_JOGv_4TDi_Aoje_kOMojbHCPw0e"
cookie = "bd_ticket_guard_client_web_domain=2; xgplayer_user_id=300976970825; xgplayer_device_id=33693820609; SEARCH_RESULT_LIST_TYPE=%22single%22; UIFID_TEMP=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e3852802afe10dc759a4840b81140431eb63f5b7b9bf48388d5b2ea51d2c5499bf93eed4f464fc4a76e1d4f480f11523a92ed21; fpk1=U2FsdGVkX1+zE2LbMIyeNz1bUAgXGI+GV9C9WyJchdXBQ+btbZOeBnttBI4FeWUjU8NDIweP6c2iFxNRAl9NzA==; fpk2=5f4591689f71924dbd1e95e47aec4ed7; UIFID=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e3852802afe10dc759a4840b81140431eb63f5b25c36f37f88bb35edf57e7b457b5f0552d48a4805370c354b88614ee3785e7a8d8360ba6238aea0fe85f7065584d0a57c40df70e202458dc7c81352a7d3040448ff6ed7106b36bc97733c48387da93953c97d5d7d7e128afc2d0497e2a51e4da5cae0c627ce32ce055c1b4e50a7c6b2f; live_use_vvc=%22false%22; MONITOR_WEB_ID=afab5227-6082-416e-8d13-4726649b66f6; my_rd=2; n_mh=6qsCtbesTsTYa2VWVVJ_iDS1FnqjbMPK8LMlp_MgmCw; store-region=cn-js; store-region-src=uid; s_v_web_id=verify_lyztsoxl_cm7viiNt_PnCm_4G3G_BFlG_BvJPGMUdlwt6; passport_csrf_token=04e11dd767862677569fbfa79aff9ce4; passport_csrf_token_default=04e11dd767862677569fbfa79aff9ce4; is_staff_user=false; dy_swidth=1920; dy_sheight=1080; __live_version__=%221.1.2.3340%22; ttwid=1%7CdjUiwt-8iojVf89TbwdaPcsDLpn1fU00mKYaYCBRiHg%7C1725718917%7C87d33cf1bd1f760822c46b257126289031528fd303145282e08031e761f7fb43; SelfTabRedDotControl=%5B%5D; publish_badge_show_info=%220%2C0%2C0%2C1726120425547%22; pwa2=%220%7C0%7C3%7C0%22; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; strategyABtestKey=%221726466267.737%22; csrf_session_id=a0ce009727dd47110324ad4db888f198; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.861%7D; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAQLHhxY3paxW4UbaE00Kbk90MSwC7FhRliYg_fjY4Hq1N1OVEjed2bf3Jln8l1Df_%2F1726502400000%2F0%2F0%2F1726474425110%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAQLHhxY3paxW4UbaE00Kbk90MSwC7FhRliYg_fjY4Hq1N1OVEjed2bf3Jln8l1Df_%2F1726502400000%2F1726475194287%2F1726474910133%2F0%22; WallpaperGuide=%7B%22showTime%22%3A0%2C%22closeTime%22%3A0%2C%22showCount%22%3A0%2C%22cursor1%22%3A44%2C%22cursor2%22%3A10%7D; sso_uid_tt=2da59cc8806c372686dfe41be6446d52; sso_uid_tt_ss=2da59cc8806c372686dfe41be6446d52; toutiao_sso_user=e6843c5012c6450b9f94105ad67ae202; toutiao_sso_user_ss=e6843c5012c6450b9f94105ad67ae202; sid_ucp_sso_v1=1.0.0-KDVhMDExNGMyZGFkNjA0M2FmNWFlYzIwYzM3ZmEzMmI3MTg5Y2U5ZWUKCRDKr6C3BhjvMRoCbHEiIGU2ODQzYzUwMTJjNjQ1MGI5Zjk0MTA1YWQ2N2FlMjAy; ssid_ucp_sso_v1=1.0.0-KDVhMDExNGMyZGFkNjA0M2FmNWFlYzIwYzM3ZmEzMmI3MTg5Y2U5ZWUKCRDKr6C3BhjvMRoCbHEiIGU2ODQzYzUwMTJjNjQ1MGI5Zjk0MTA1YWQ2N2FlMjAy; sid_guard=a8a0c91dcb1ae639816a8d5d243b73bd%7C1726486474%7C21600%7CMon%2C+16-Sep-2024+17%3A34%3A34+GMT; uid_tt=5ec48fa58817f403813046887285ee87; uid_tt_ss=5ec48fa58817f403813046887285ee87; sid_tt=a8a0c91dcb1ae639816a8d5d243b73bd; sessionid=a8a0c91dcb1ae639816a8d5d243b73bd; sessionid_ss=a8a0c91dcb1ae639816a8d5d243b73bd; sid_ucp_v1=1.0.0-KDQzYzM1NDI5MmY5ZDliYjUyYzhiMWRlNDUwMzZjNWQ5ODljYjRlNTYKCBDKr6C3BhgNGgJobCIgYThhMGM5MWRjYjFhZTYzOTgxNmE4ZDVkMjQzYjczYmQ; ssid_ucp_v1=1.0.0-KDQzYzM1NDI5MmY5ZDliYjUyYzhiMWRlNDUwMzZjNWQ5ODljYjRlNTYKCBDKr6C3BhgNGgJobCIgYThhMGM5MWRjYjFhZTYzOTgxNmE4ZDVkMjQzYjczYmQ; __ac_nonce=066e817ca00aa2fb8fc70; __ac_signature=_02B4Z6wo00f01ZO72XAAAIDBpJ8dLDMRccGTm93AAAIHHnhTvKxHxIjXDJMTmk8sGsHdeZhd6BZxOJX17hjj.jE4.ohYORnxeHUNIPry9TaX8emlIsmKyNfsLZ7hP5m99.lUuwS6FK1i5Ua2d8; odin_tt=4942de547aeaa46d66b6e9d697788c8b7b62b77334932bf174f7e117a4854863b14704987b53f0e7d22c6ed37bbda4a7d235429087c353b4cb40feee7ff0b71b; passport_fe_beating_status=false; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; download_guide=%221%2F20240916%2F0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; xg_device_score=7.504168168360229; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; home_can_add_dy_2_desktop=%221%22; biz_trace_id=6de4713c; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQXpEQjRsSlMvUndUZkg0RC9MN2RCTnduN1ZRdStjU0J1YUsvQTVzZ2YyamovaWlzakpVWWgzRDY0QUE4eit5Smx5T0hmOGF6aEFWWWhEbGhRbmE3Y0E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.douyin.com",
    "Referer": "https://www.douyin.com/user/MS4wLjABAAAAvUIxmVOEO2g5F32m12-cXKi836UCa5FmbpQ4GGJ3k49yiZxvv16cxXA7h56TJ2nL",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.238.400 QQBrowser/12.4.5623.400",
    "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}

from bs4 import BeautifulSoup
import json

response = requests.get(url, headers=headers, cookies={"cookie": cookie})
soup = BeautifulSoup(response.text, 'html.parser')

data = json.loads(response.text)
# print(data['aweme_list'][2])
print(data['has_more'])
# print(data['aweme_list'][0]['video']['play_addr']['url_list'][0])
# print('\n')
# print(data['aweme_list'])
# # 在这里添加你需要爬取的内容的代码，例如：
# titles = soup.find_all('url_list')
# for title in titles:
#     print(title.text)

# print(soup.prettify())
