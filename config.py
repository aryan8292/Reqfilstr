#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler

#update for req channel
SESSION_STRING = os.environ.get("SESSION_STRING", "BQA1ENIAMcfNEIS2NxnMj1ZQOrg6-tkCZmz2hrwmyyLS9kwNMv5op504B3ok1mEUqGTAr-Xdxd5pyr5o0onmKZWQ8oRS5ZN_kOpYxJzNWAivWsQrUvnbZj12SP9wdLPzwkDoEhW2mXVGoRR8T8unJ6CWV_II7hj_LqEFeKZen_XlAX6Qv_uCeAF28NdFTLSh7zxlz2xTm5KxIa0InVc-r34lyp3IMjVs7uS-7FdU1GInjgKWsBQ2kwlvUc3vJmaU-rcOZtXTXemm2vfea8og3ej7m_K-4UNmNaBniV6Yi5DaNMcnxM2iW5oJBdsT7wfZU_2TlK5-VwPTnDKhO__1Z8Sblhf7vQAAAABpspdLAA")
REQUEST_CHANNEL_ID = int(os.environ.get("REQUEST_CHANNEL_ID", "-1002037171802"))
REQUEST_CHANNEL_LINK = os.environ.get("REQUEST_CHANNEL_LINK", "https://t.me/+Ibcahprx3eszYTVl")


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6426574425:AAGmfRlGgUI-h48hQ0xtlmI1hqXdS_F3_Pw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "3477714"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1264d2d7d397c4635147ee25ab5808d1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001593914815"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1773311819"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://colab:colab@colab.okoqygn.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "shikarikabot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002037171802"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
REQUEST_JOIN_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1979647570").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Click the  𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 and then click 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 and you will get the serial & movie File...😜\n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 क्लिक करें और फिर 𝐓𝐫𝐲 𝐀𝐠𝐢𝐢𝐧 क्लिक करें और आपको सीरियल & मूवी फ़ाइल मिल जाएगी...😜")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
