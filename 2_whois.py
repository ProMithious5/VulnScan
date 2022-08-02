import os
class whois():
    def (self,ip_addr):
        var=2
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
Examples:whois url
"""
while var==2:
    print("\033[1;35m", sc)
    print("\033[1;33m", example)
    print("\033[1;92m")
    print("Type your web address: ")
    vf=(input("Enter Your Web Address or IP: "))
    os.system("whois "+vf)
