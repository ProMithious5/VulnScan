import os
class wpscan():
    def wpsc(self,ip_addr):
        var=8
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
Examples: -L userlist.txt -P passwordlist.txt http://url
"""
while var==8:
    print("\033[1;35m", sc)
    print("\033[1;33m", example)
    print("\033[1;92m")
    print("Enter the valid URL of your WordPress Website: ")
    wp_addr=input()
    os.system("sudo wpscan")
