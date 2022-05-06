import argparse
import struct
parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

f = open(args.file, "rb")
f.seek(1024,0)

g = open("inputs", "w")
g.write("")
g.close()
g = open("inputs", "a")

count = 1
ltms = "|K"
byte = f.read(1)

while byte:
    
    if (byte.hex()=="08"):
        ltms+="ff08:"
    elif (byte.hex()=="09"):
        ltms+="ff09:"
    elif (byte.hex()=="0c"):
        ltms+="ff0b:"
    elif (byte.hex()=="0d"):
        ltms+="ff0d:"
    elif (byte.hex()=="10"):
        ltms+="ffe1:"
    elif (byte.hex()=="11"):
        ltms+="ffe3:"
    elif (byte.hex()=="12"):
        ltms+="ffe9:"
    elif (byte.hex()=="13"):
        ltms+="ff13:"
    elif (byte.hex()=="14"):
        ltms+="ffe5:"
    elif (byte.hex()=="1b"):
        ltms+="ff1b:"
    elif (byte.hex()=="20"):
        ltms+="ff80:"
    elif (byte.hex()=="21"):
        ltms+="ff55:"
    elif (byte.hex()=="22"):
        ltms+="ff56:"
    elif (byte.hex()=="23"):
        ltms+="ff57:"
    elif (byte.hex()=="24"):
        ltms+="ff50:"
    elif (byte.hex()=="25"):
        ltms+="ff51:"
    elif (byte.hex()=="26"):
        ltms+="ff52:"
    elif (byte.hex()=="27"):
        ltms+="ff53:"
    elif (byte.hex()=="28"):
        ltms+="ff54:"
    elif (byte.hex()=="29"):
        ltms+="ff60:"
    elif (byte.hex()=="2a"):
        ltms+="ff61:"
    elif (byte.hex()=="2b"):
        ltms+="ff62:"
    elif (byte.hex()=="2c"):
        ltms+="fd1d:"
    elif (byte.hex()=="2d"):
        ltms+="ff63:"
    elif (byte.hex()=="2e"):
        ltms+="ffff:"
    elif (byte.hex()=="2f"):
        ltms+="ff6a:"
    elif (byte.hex()=="30"):
        ltms+="30:"
    elif (byte.hex()=="31"):
        ltms+="31:"
    elif (byte.hex()=="32"):
        ltms+="32:"
    elif (byte.hex()=="33"):
        ltms+="33:"
    elif (byte.hex()=="34"):
        ltms+="34:"
    elif (byte.hex()=="35"):
        ltms+="35:"
    elif (byte.hex()=="36"):
        ltms+="36:"
    elif (byte.hex()=="37"):
        ltms+="37:"
    elif (byte.hex()=="38"):
        ltms+="38:"
    elif (byte.hex()=="39"):
        ltms+="39:"
    elif (byte.hex()=="41"):
        ltms+="41:"
    elif (byte.hex()=="42"):
        ltms+="42:"
    elif (byte.hex()=="43"):
        ltms+="43:"
    elif (byte.hex()=="44"):
        ltms+="44:"
    elif (byte.hex()=="45"):
        ltms+="45:"
    elif (byte.hex()=="46"):
        ltms+="46:"
    elif (byte.hex()=="47"):
        ltms+="47:"
    elif (byte.hex()=="48"):
        ltms+="48:"
    elif (byte.hex()=="49"):
        ltms+="49:"
    elif (byte.hex()=="4a"):
        ltms+="4a:"
    elif (byte.hex()=="4b"):
        ltms+="4b:"
    elif (byte.hex()=="4c"):
        ltms+="4c:"
    elif (byte.hex()=="4d"):
        ltms+="4d:"
    elif (byte.hex()=="4e"):
        ltms+="4e:"
    elif (byte.hex()=="4f"):
        ltms+="4f:"
    elif (byte.hex()=="50"):
        ltms+="50:"
    elif (byte.hex()=="51"):
        ltms+="51:"
    elif (byte.hex()=="52"):
        ltms+="52:"
    elif (byte.hex()=="53"):
        ltms+="53:"
    elif (byte.hex()=="54"):
        ltms+="54:"
    elif (byte.hex()=="55"):
        ltms+="55:"
    elif (byte.hex()=="56"):
        ltms+="56:"
    elif (byte.hex()=="57"):
        ltms+="57:"
    elif (byte.hex()=="58"):
        ltms+="58:"
    elif (byte.hex()=="59"):
        ltms+="59:"
    elif (byte.hex()=="5a"):
        ltms+="5a:"
    elif (byte.hex()=="5b"):
        ltms+="ffeb:"
    elif (byte.hex()=="5c"):
        ltms+="ffec:"
    elif (byte.hex()=="5f"):
        ltms+="50:"
    elif (byte.hex()=="60"):
        ltms+="ffb0:"
    elif (byte.hex()=="61"):
        ltms+="ffb1:"
    elif (byte.hex()=="62"):
        ltms+="ffb2:"
    elif (byte.hex()=="63"):
        ltms+="ffb3:"
    elif (byte.hex()=="64"):
        ltms+="ffb4:"
    elif (byte.hex()=="65"):
        ltms+="ffb5:"
    elif (byte.hex()=="66"):
        ltms+="ffb6:"
    elif (byte.hex()=="67"):
        ltms+="ffb7:"
    elif (byte.hex()=="68"):
        ltms+="ffb8:"
    elif (byte.hex()=="69"):
        ltms+="ffb9:"
    elif (byte.hex()=="6a"):
        ltms+="ffaa:"
    elif (byte.hex()=="6b"):
        ltms+="ffab:"
    elif (byte.hex()=="6c"):
        ltms+="ffac:"
    elif (byte.hex()=="6d"):
        ltms+="ffad:"
    elif (byte.hex()=="6e"):
        ltms+="ffae:"
    elif (byte.hex()=="6f"):
        ltms+="ffaf:"
    elif (byte.hex()=="70"):
        ltms+="ffbe:"
    elif (byte.hex()=="71"):
        ltms+="ffbf:"
    elif (byte.hex()=="72"):
        ltms+="ffc0:"
    elif (byte.hex()=="73"):
        ltms+="ffc1:"
    elif (byte.hex()=="74"):
        ltms+="ffc2:"
    elif (byte.hex()=="75"):
        ltms+="ffc3:"
    elif (byte.hex()=="76"):
        ltms+="ffc4:"
    elif (byte.hex()=="77"):
        ltms+="ffc5:"
    elif (byte.hex()=="78"):
        ltms+="ffc6:"
    elif (byte.hex()=="79"):
        ltms+="ffc7:"
    elif (byte.hex()=="7a"):
        ltms+="ffc8:"
    elif (byte.hex()=="7b"):
        ltms+="ffc9:"
    elif (byte.hex()=="7c"):
        ltms+="ffca:"
    elif (byte.hex()=="7d"):
        ltms+="ffcb:"
    elif (byte.hex()=="7e"):
        ltms+="ffcc:"
    elif (byte.hex()=="7f"):
        ltms+="ffcd:"
    elif (byte.hex()=="80"):
        ltms+="ffce:"
    elif (byte.hex()=="81"):
        ltms+="ffcf:"
    elif (byte.hex()=="82"):
        ltms+="ffd0:"
    elif (byte.hex()=="83"):
        ltms+="ffd1:"
    elif (byte.hex()=="84"):
        ltms+="ffd2:"
    elif (byte.hex()=="85"):
        ltms+="ffd3:"
    elif (byte.hex()=="86"):
        ltms+="ffd4:"
    elif (byte.hex()=="87"):
        ltms+="ffd5:"
    elif (byte.hex()=="90"):
        ltms+="ff7f:"
    elif (byte.hex()=="90"):
        ltms+="ff7f:"
    elif (byte.hex()=="91"):
        ltms+="ff14:"
    elif (byte.hex()=="90"):
        ltms+="ff7f:"
    elif (byte.hex()=="a0"):
        ltms+="ffe1:"
    elif (byte.hex()=="a1"):
        ltms+="ffe2:"
    elif (byte.hex()=="a2"):
        ltms+="ffe3:"
    elif (byte.hex()=="a3"):
        ltms+="ffe4:"
    elif (byte.hex()=="a4"):
        ltms+="ff67:"
    elif (byte.hex()=="a5"):
        ltms+="ff67:"
    elif (byte.hex()=="bc"):
        ltms+="2c:"
    elif (byte.hex()=="be"):
        ltms+="2e:"
    elif (byte.hex()=="bf"):
        ltms+="2f:"
    elif (byte.hex()=="c0"):
        ltms+="60:"
    elif (byte.hex()=="db"):
        ltms+="5b:"
    elif (byte.hex()=="dc"):
        ltms+="5c:"
    elif (byte.hex()=="dd"):
        ltms+="5d:"
    elif (byte.hex()=="de"):
        ltms+="5e:"
    elif (byte.hex()=="f6"):
        ltms+="fd0e:"
    elif (byte.hex()=="f7"):
        ltms+="fd1c:"
    elif (byte.hex()=="f8"):
        ltms+="fd1b:"
    elif (byte.hex()=="f9"):
        ltms+="fd06:"
    elif (byte.hex()=="fa"):
        ltms+="fd16:"
    elif (byte.hex()=="fd"):
        ltms+="fd0a:"
    else:
        if (ltms == "|K"):
            ltms+=":"
       
    if (count == 8):
        g.write(ltms[:-1]+"|\n")
        count = 0
        ltms = "|K"
    
    byte = f.read(1)
    count+=1

f.close()
g.close()