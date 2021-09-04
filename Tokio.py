#!/usr/bin/env python
#
#
#
#
#                          Created By Milez

from urllib2 import *
from platform import system
import sys
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('clear')
        os.system('color a')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
banner = '''

\033[96m
___________     __   .__        
\__    ___/___ |  | _|__| ____  
  |    | /  _ \|  |/ /  |/  _ \ 
  |    |(  <_> )    <|  (  <_> )
  |____| \____/|__|_ \__|\____/ 
                    \/          
Coded by Milez
        github.com/mile403
in memory of Tokio from 
LaCasa de papel

 Team : MillerSec || CyberXploitTeam
       https.fb.me/miller742
''' 
print banner
def menu():
   print'''
\033[92m
1. DNS LookUp
2. whois LookUp
3. Reverse IP locator
4. GeoIP LookUp
5. Subnet LookUp
6. Port Scanning
7. Extract Links 
8. Zone Transfering
9. HTTP header 
10. Host locator
11. IP locator 
12. Update 
13. About Me

'''
slowprint("\033[1;91m Welcome to Tokio, following are the info gathering tools by Professor Milez that you cam use: " + "\n Let's Start Tokio !")

menu()
def ext():
    ex = raw_input ('\033[92mContinue/Exit->')
    if ex[0].upper() == 'E' :
           print 'See you soon!!!'
           exit()
    else:
           clear()
           print banner
           menu()
           select()

def  select():
  try:
    DNS = input("\033[92mMilez@Tokio \033[92m/\033:~$")
    if DNS == 2:
      dz = raw_input('\033[91mEnter IP Address : \033[91m')
      whois = "http://api.hackertarget.com/whois/?q=" + dz
      dev = urlopen(whois).read()
      print (dev)
      ext()
    elif DNS == 3:
      dz = raw_input('\033[92mEnter IP Address : \033[92m')
      revrse = "http://api.hackertarget.com/reverseiplookup/?q=" + dz
      lookup = urlopen(revrse).read()
      print (lookup)
      ext()
    elif DNS == 1:
      dz = raw_input('\033[96mEnter Your Domain :\033[96m')
      dns = "http://api.hackertarget.com/dnslookup/?q=" + dz
      DNS = urlopen(dns).read()
      print (DNS)
      ext()
    elif DNS == 4:
      dz = raw_input('\033[91mEnter IP Address : \033[91m')
      geo = "http://api.hackertarget.com/geoip/?q=" + dz
      ip = urlopen(geo).read()
      print (ip)
      ext()
    elif DNS == 5:
      dz = raw_input('\033[92mEnter IP Address : \033[92m')
      sub = "http://api.hackertarget.com/subnetcalc/?q=" + dz
      net = urlopen(sub).read()
      print (net)
      ext()
    elif DNS == 6:
      dz = raw_input('\033[96mEnter IP Address : \033[96m')
      port = "http://api.hackertarget.com/nmap/?q=" + dz
      scan = urlopen(port).read()
      print (scan)
      ext()
    elif DNS == 7:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      get = "https://api.hackertarget.com/pagelinks/?q=" + dz
      page = urlopen(get).read()
      print(page)
      ext()
    elif DNS == 8:
      dz = raw_input('\033[92mEnter Your Domain :\033[92m')
      zon = "http://api.hackertarget.com/zonetransfer/?q=" + dz
      tran = urlopen(zon).read()
      print (tran)
      ext()
    elif DNS == 9:
      dz = raw_input('\033[96mEnter Your Domain :\033[96m')
      hea = "http://api.hackertarget.com/httpheaders/?q=" + dz
      der =  urlopen(hea).read()
      print (der)
      ext()
    elif DNS == 10:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      host = "http://api.hackertarget.com/hostsearch/?q=" + dz
      finder = urlopen(host).read()
      print (finder)
      ext()
    elif DNS == 11:
      dz = raw_input('\033[91mEnter Your IP Address :\033[91m')
      host = "http://ip-api.com/json/" + dz
      kader = urlopen(host).read()
      print (kader)
      ext()
    elif DNS == 12:
      print("no updates ")
      ext()
    elif DNS == 13:
      slowprint("..... ")
      slowprint("Name : Tokio \033[92m")
      slowprint(".....")
      slowprint("Version : 1.0 \033[91m")
      slowprint(".....")
      slowprint("Author: Milez  \033[96m")
      slowprint("Team: MillerSec")
      slowprint("Members")
      slowprint("Milez")
      slowprint("./Hanz")
      slowprint("Shaki")
      slowprint("Star-Ford")
      slowprint("Akash_Hamal")
      slowprint("Saitama")
      slowprint(" CyberXploitTeam ")
      slowprint("https://fb.me/miller742")
      slowprint("........")
      slowprint("...................... ")
      ext() 
    elif DNS == 0:
      print "See you soon!!"
      ext()
  except(KeyboardInterrupt):
    print "\nCtrl + C -> See you soon!!"
select()
