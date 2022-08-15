import requests #line:1
import discord #line:2
import os #line:3
from colorama import Fore #line:4
import time #line:5
bot =discord .Client ()#line:7
token =input ("Token >>> : ")#line:9
guild =input ("Server ID >>> : ")#line:10
def ping ():#line:12
    while True :#line:13
        O0OO0OO00O0O00000 =requests .get (f"https://discord.com/api/v9/guilds/{guild}/channels",headers ={"authorization":token }).json ()#line:17
        OOOO00OO0O00OO000 =list ()#line:18
        for OOOO00OO0O00OO000 in O0OO0OO00O0O00000 :#line:19
            O0OO0OO00O0O00000 =requests .post (f"https://discord.com/api/v9/channels/{OOOO00OO0O00OO000['id']}/messages",headers ={"Authorization":token },json ={"content":"@everyone","tts":True })#line:20
            if 'retry_after'in O0OO0OO00O0O00000 .text :#line:21
                time .sleep (O0OO0OO00O0O00000 .json ()['retry_after'])#line:22
            print (f""" Mass Ping >>> {OOOO00OO0O00OO000['id']}""")#line:23
            if O0OO0OO00O0O00000 .status_code ==200 :#line:24
                requests .delete (f"https://discord.com/api/v9/channels/{O0OO0OO00O0O00000.json()['channel_id']}/messages/{O0OO0OO00O0O00000.json()['id']}",headers ={"Authorization":token })#line:25
ping ()