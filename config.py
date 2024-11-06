# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23499948")

API_HASH = os.environ.get("API_HASH", "b92cd19ae415002b5c2285aa50885a4b")

BOT_TOKEN = os.environ.get("lisa_baby", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "lisa_baby") 

             # Don't Remove Credit @lisa_baby
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "lisa_baby")     

DB_URL = os.environ.get("vijaysharmag0005:<db_WY48C9Mr0lufvxns>@lisa.bwjtc.mongodb.net/?retryWrites=true&w=majority&appName=lisa", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '23499948').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
