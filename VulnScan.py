import os
ip_addr = input("Enter the IP Address; ")
response = os.system("ping -c 10 "+ip_addr+" > abc.txt")
# if condition

os.system("whois "+ip_addr)
os.system("dnsrecon ")
os.system("sudo nmap -O "+ip_addr)
os.system("dirb -h http://"+ip_addr)
os.system("nikto http://"+ip_addr)
os.system("hydra -L  -P  "+ip_addr+" ssh")
os.system("hydra -L  -P  "+ip_addr+" ftp")
os.system("sudo nmap --script=vuln "+ip_addr)
os.system("sudo nmap -sX -A -sS -Pn "+ip_addr)
os.system("sudo wpscan -U -P --url http://"+ip_addr+"/wp-admin")
os.system("sudo sqlmap ")
# ip_address->ping
#whois
#up : nmap
# down : nmap and other not possible
# 80, 443port : dirb, nikto: if wordpress (check using wp-login, wp-admin)
# ssh: hydra
# ftp login hydra
# nmap --script=vuln scan
# nmap XMAS scan
# wpscan basic
# sqlmap
# get website XSS <script>alert(1)</script>
# post phpreverseshell
