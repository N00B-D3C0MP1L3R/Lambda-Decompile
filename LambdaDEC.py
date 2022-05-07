# -*- coding:utf8 -*-

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile
import requests
# warna
hijau  ="\x1b[1;92m"
cyan   ="\x1b[1;96m"
kuning ="\x1b[1;93m"
ungu   ="\x1b[1;95m"
putih  ="\x1b[1;97m"
biru   ="\x1b[1;94m"
merah  ='\x1b[1;91m'

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")


def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.01)


x = "g2yw9wosnh3u3iejrbdu2oj2behsoskwbwgey"

def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)

def s(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.02)


def baner():
        os.system("clear")
        print ("%s+───────────────────────────────────────────+"%(putih))
        print ("%s[%s~%s] %sAuthor  %s: %sRcXsec"%(hijau,cyan,hijau,putih,merah,hijau))
        print ("%s[%s~%s] %sGithub  %s: %sgithub.com/RcXsec"%(hijau,cyan,hijau,putih,merah,hijau))
        print ("%s[%s~%s] %sName sc %s: %sLambda Dec %s1,3   "%(hijau,cyan,hijau,putih,merah,hijau,kuning))
        print ("%s+───────────────────────────────────────────+"%(putih))
        print()
        print()

def login():
  os.system("clear")
  sp("\033[1;96m       ╔╗   ╔═══╗╔═══╗╔══╗╔═╗ ╔╗          ")
  sp("\033[1;96m       ║║   ║╔═╗║║╔═╗║╚╣─╝║║╚╗║║          ")
  sp("\033[1;96m       ║║   ║║ ║║║║ ╚╝ ║║ ║╔╗╚╝║          ")
  sp("\033[1;96m       ║║ ╔╗║║ ║║║║╔═╗ ║║ ║║╚╗║║ \033[1;97mBY RcXsec")
  sp("\033[1;96m       ║╚═╝║║╚═╝║║╚╩═║╔╣─╗║║ ║║║")
  sp("\033[1;96m       ╚═══╝╚═══╝╚═══╝╚══╝╚╝ ╚═╝")
# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "# Decypt Lambda By RcXsec\n# Makasih \n"
def ban(): # Program Bann
    os.system("clear")
    print(cyan+" FOLLOW MY GITHUB "+putih+" 🚬")
    time.sleep(2)
    os.system("xdg-open https://github.com/RcXsec/RcXsec/")
    time.sleep(4)
def banner():
    os.system("clear")
    print ("%s+───────────────────────────────────────────+"%(putih))
    print ("%s[%s~%s] %sAuthor  %s: %sRcXsec"%(hijau,cyan,hijau,putih,merah,hijau))
    print ("%s[%s~%s] %sGithub  %s: %sgithub.com/RcXsec"%(hijau,cyan,hijau,putih,merah,hijau))
    print ("%s[%s~%s] %sName sc %s: %sLambda Dec %s1,3   "%(hijau,cyan,hijau,putih,merah,hijau,kuning))
    print ("%s+───────────────────────────────────────────+"%(putih))
def menu():
    ketik ("%s{%s!%s}%s Note %s; %sCTRL+C%s / %sCTRL+Z Berhentikan Tools"%(putih,merah,putih,kuning,merah,putih,merah,putih))
    print()
    ketik ("%s{%s01%s} lambda %sDecypt %sMarshal"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s02%s} lambda %sDecypt %sZlib"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s03%s} lambda %sDecypt %sBase16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s04%s} lambda %sDecypt %sBase32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s05%s} lambda %sDecypt %sBase64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s06%s} lambda %sDecypt %sZlib&Base16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s07%s} lambda %sDecypt %sZlib&Base32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s08%s} lambda %sDecypt %sZlib&Base64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s09%s} lambda %sDecypt %sMarshal&Zlib"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s10%s} lambda %sDecypt %sMarshal&Base16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s11%s} lambda %sDecypt %sMarshal&Base32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s12%s} lambda %sDecypt %sMarshal&Base64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s13%s} lambda %sDecypt %sMarshal&Zlib&Base16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s14%s} lambda %sDecypt %sMarshal&Zlib&Base32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s15%s} lambda %sDecypt %sMarshal&Zlib&Base64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s16%s} %sDecypt %sHex 200kb"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s17%s} %sExitt"%(putih,hijau,putih,merah))
    print()
class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            ketik("\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Encoded File Size \x1b[1;91m:\x1b[1;92m %s\n" %self.datas(dts))
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % "\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} Encode Count \x1b[1;91m:\x1b[1;92m "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        ketik("\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Invalid Option!")
        time.sleep(3)
        ul()
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit("{!} TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        baner()
        menu()
        try:
            option = int(eval(_input % "\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} Option \x1b[1;91m:\x1b[1;92m "))
        except ValueError:
            ketik("\n\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Invalid Option !")
            time.sleep(3)
            ul()
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Thanks For Using this Tool")
            os.system('clear') # os.system('cls')
            banner()
        else:
            ketik('\n\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Invalid Option !')
            time.sleep(3)
            ul()
        try:
            ketik ("%s{%s!%s}%s Note%s :%s Namafile.py"%(putih,merah,putih,kuning,merah,hijau))
            print()
            file = eval(_input % "\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} File Name \x1b[1;91m:\x1b[1;92m ")
            data = open(file).read()
        except IOError:
            ketik("\n\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Not Found!")
            time.sleep(3)
            ul()
        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        ketik("\n\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Successfully Encrypted\x1b[1;93m %s" % file)
        ketik("\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Saved as\x1b[1;92m %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()
def ul():
    MainMenu()

if __name__ == "__main__":
    login()
    ban()
    MainMenu()