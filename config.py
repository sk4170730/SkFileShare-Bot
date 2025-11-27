import os
from typing import List

API_ID = int(os.getenv("API_ID", "34254284")
API_HASH = os.getenv("API_HASH", "746da987fd34ef8d8363c55f42d00aef")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7985190165:AAHr4aHlPmJFOZSTr3xxYMzPgby88ke8W9E")
ADMINS = [int(x) for x in os.getenv("ADMINS", "5181487987").split() if x.isdigit()]
DB_URI = os.getenv("DB_URI", "mongodb+srv://sk4170730:Sumit@2003@cluster0.d0w1y7n.mongodb.net/?appName=Cluster0")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002721017177")
AUTO_DELETE_MINUTES = int(os.getenv("AUTO_DELETE", "30"))

if not all([API_ID, API_HASH, BOT_TOKEN, DB_URI]):
    print("Error: Required environment variables missing!")
    exit(1)
