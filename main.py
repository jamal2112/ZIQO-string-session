
#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("an online StringSession generator for telethon")

print("https://GitHub.com/jamal2112/")

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)  
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️ This StringSession is generated using https://ZIQO-string-session.jamal2112.repl.run! ")

    print("please check your Telegram Saved Messages for the StringSession ")