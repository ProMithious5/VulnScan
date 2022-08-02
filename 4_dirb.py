import os
class dirb():
    def dir(self,ip_addr):
        var=4
        sc="""
    _____                       _             
  / ____|                     (_)            
 | (___   ___ __ _ _ __  _ __  _ _ __   __ _ 
  \___ \ / __/ _` | '_ \| '_ \| | '_ \ / _` |
  ____) | (_| (_| | | | | | | | | | | | (_| |
 |_____/ \___\__,_|_| |_|_| |_|_|_| |_|\__, |
                                        __/ |
                                       |___/ 
"""
example="""
Examples: -h http://url
"""
while var==4:
    print("\033[1;35m", sc)
    print("\033[1;33m", example)
    print("\033[1;92m")
    print("What type of website do you have: ")
    print("1. With IP Address: ")
    print("2. With DNS: ")
    vf=int(input("Enter Your Option: "))
    if(vf==1):
        os.system("sudo nikto -h http://"+ip_addr)
    elif(vf==2):
        gh=input("Enter your website name(without http): ")
        os.system("sudo nikto -h http://"+gh)
