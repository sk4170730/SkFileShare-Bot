import os
from typing import List

# Ye sab environment variables se lo, hardcode mat karo
API_ID: int = int(os.environ.get("API_ID", 34254284))          # sirf int() laga do
API_HASH: str = os.environ.get("API_HASH", "7985190165:AAHr4aHlPmJFOZSTr3xxYMzPgby88ke8W9E")           # quotes hata do
BOT_TOKEN: str = os.environ.get("BOT_TOKEN", " 746da987fd34ef8d8363c55f42d00aef")         # quotes hata do

# Baaki sab aise hi thik hai, bas inko bhi env se lo
OWNER_ID: int = int(os.environ.get("OWNER_ID", "5181487987"))  # default apna ID daal sakte ho test ke liye
DB_URI: str = os.environ.get("DB_URI", "mongodb+srv://sk4170730:Sumit@2003@cluster0.d0w1y7n.mongodb.net/?appName=Cluster0")  # apna MongoDB URL daal dena
LOG_CHANNEL: int = int(os.environ.get("LOG_CHANNEL", "-1002721017177"))
AUTO_DELETE_MINUTES: int = int(os.environ.get("AUTO_DELETE", "30"))  # 30 minute default

# Agar koi bhi important variable nahi mila to seedha band
for var in ["API_ID", "API_HASH", "BOT_TOKEN"]:
    if not os.environ.get(var):
        print(f"[ERROR] {var} not found in environment variables!")
        exit(1)
