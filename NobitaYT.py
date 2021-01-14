# author : @Exa21
# -*- coding: utf-8 -*-


import os
import sys
import fileinput
os.system("clear")

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'
wait = Y + '[' + W + "Wait" + Y + ']' + W
banner = """
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{} ˢᶜᴿᴵᴾᵀ ᴮʸ {} : {} N̮o̮b̮i̮t̮a̮Y̮T̮🇮🇩
{}ᵀᴱᴸᴱᴳᴿᴬᴹ {} : {} ⛔ @b̮a̮n̮g̮s̮a̮t̮k̮a̮u̮u̮ ⛔
{}ʸᴼᵁᵀᵁᴮᴱ{} : {} N̮o̮b̮i̮t̮a̮Y̮T̮
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""".format(G,Y,W,B,Y,W,B,Y,W,B,G)
banner2 = """
   {}[{}1{}]{} ᴿᵁᴺ ᶠᴼᴿ ᴬᴸᴸ ᴾᵁᴮᴳ     
   {}[{}2{}]{}  ᵀʸᴾᴱ ᴺᴼᴹᴱᴿ ¹
   
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""".format(G,W,G,W,G,W,G,W,G)

print banner
print banner2

def darkingenc():
   try:
        sc = raw_input(ask + W + "TYPE PUBG(GL.sh | KR.sh | VN.sh | TW.sh) " + G + "> " + W)
        f = open(sc,'r')
        filedata = f.read()
        f.close()
        
        newdata = filedata.replace("eval $@","echo $@")
        renameback = filedata.replace("echo $@","eval $@")

        f = open(sc,'w')
        f.write(newdata)
        f.close()
       
        print (wait + "Proccecing")
        
        os.system("touch nobita_Tools.sh")
        os.system("bash " + sc)
        os.system("clear")
        print "Wait for run game"
        os.system("bash " + sc + " > nobita_Tools.sh")
        os.rename("nobita_Tools.sh","[Dec].)" + sc)
        
        f = open(sc,'w')
        f.write(renameback)
        f.close()
        
        print (sukses + "DONE FOR RUN SH")

   except KeyboardInterrupt:
       print (eror + " sᴛᴏᴘᴘᴇᴅ!")
   except IOError:
       print (eror + " ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ!")
       
def simpleenc():
   try:
       sc = raw_input(ask + W + "TYPE PUBG(GL.sh | KR.sh | VN.sh | TW.sh) " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")
       renameback = filedata.replace("echo","eval")
       
       f = open(sc,'w')
       f.write(newdata)
       f.close()

       os.system("touch nobita_Proccecing.sh")
       os.system("bash " + sc)
       os.system("clear")
       print "Wait for run game"
       os.system("bash " + sc + " > nobita_ᴘʀᴏᴄᴇss.sh")
       
       f = open(sc,'w')
       f.write(renameback)
       f.close()
       
       os.rename("nobita_ᴘʀᴏᴄᴇss.sh","[Dec]" + sc)
       print (sukses + "DONE FOR RUN SH")

   except KeyboardInterrupt:
       print (eror + " sᴛᴏᴘᴘᴇᴅ!")
   except IOError:
       print (eror + " ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ!")

makim = raw_input(W + "ᴄʜᴏᴏsᴇ" + G + " > ")
if makim == "1" or makim == "01":
   darkingenc()
elif makim == "2" or makim == "02":
   simpleenc()
else:
        print (eror + " ᴡʀᴏɴɢ ɪɴᴘᴜᴛ !")