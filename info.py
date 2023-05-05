import re
import os
from os import environ
from pyrogram import enums
from Script import script
from dotenv import load_dotenv

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '11643051'))
API_HASH = environ.get('API_HASH', '7dfe39d9cf2054402e5a6c9a9439a610')
BOT_TOKEN = environ.get('BOT_TOKEN', '5956859260:AAFbliFh_55Q9iqmDYxqO_iRI3JpNHHw86Q')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/ad51af5d7b62b176dd4e8.jpg https://telegra.ph/file/337baddb6be47b02ce895.jpg https://telegra.ph/file/78e1de114681234d24c84.jpg https://telegra.ph/file/16aeb75f2aa9f1b4b38ee.jpg')).split()
SPELL_IMG = environ.get('SPELL_IMG',"https://telegra.ph/file/b66f3a65ce68e11e621cf.jpg")

# Welcome area
MELCOW_IMG = environ.get('MELCOW_IMG',"https://telegra.ph/file/f75dc5a5f440e2ffe43e7.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"https://telegra.ph/file/6347d3141f9791cc4f8ec.mp4")



# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1833209093').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001783681170 -1001762835884 -1001541252886 -1001879702504').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Rexie:Rexie@cluster0.ikahrzi.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", "-1001521285304")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1001636271003').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hᴇʟʟᴏ {mention}\nWᴇʟᴄᴏᴍᴇ Tᴏ {title}\n\nJᴏɪɴ Fᴏʀ Nᴇᴡ Mᴏᴠɪᴇꜱ @Ak_Links1")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = os.environ.get("PORT", "8080")
MAX_BTN = int(environ.get('MAX_BTN', "7"))
S_GROUP = environ.get('S_GROUP',"https://t.me/Ak_Links1")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/movies_channel001")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/+BVP4yf8HHEFmNmJl")
MSG_ALRT = environ.get('MSG_ALRT', '𝑻𝒉𝒂𝒏𝒌𝒔 𝒇𝒐𝒓 𝑨𝒌 𝒅𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓😍')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001506481594))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'czdbotz_support')
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
