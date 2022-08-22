# Evil Eye v1.0 
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')
parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
parser.add_argument('-p', help='Path of your output file', dest='path')
args = parser.parse_args()
af = args.audiofile
string = args.secretmsg
output = args.outputfile
arged = False
if af and string and output:
    arged = True
def cls():
  os.system("clear")
def help():
  print("\033[92m Hide   Secret Text Message in Audio Wave File.\033[0m")
  print ('''usage: bind.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE] [-p OUTPUTPATH]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File
  -m SECRETMSG  Enter your message
  -o OUTPUTFILE Your output file path and name
  -p Path of your output file ''')
  
def banner():
    print ('''
\
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             """"          """"""" 
           ┌─────────────────────┐
           │▛▀▘▌ ▌▜▘▌   ▛▀▘▌ ▌▛▀▘│
           │▙▄ ▚▗▘▐ ▌   ▙▄ ▝▞ ▙▄ │
           │▌  ▝▞ ▐ ▌   ▌   ▌ ▌  │
           │▀▀▘ ▘ ▀▘▀▀▘ ▀▀▘ ▘ ▀▀▘│
           └─────────────────────#
           
                      | Cyber Octopus |v1.0 \033
                   
[EvilEye v1.0 Coded by @codewithharit 

[GitHub : https://github.com/codewithharit ]\033 ''')



def em_audio(af, string, output):
    if not arged:
      help()
    else:
      print ("m Please wait...")
      waveaudio = wave.open(af, mode='rb')
      frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
      string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
      waveaudio.close()
      print ("Done...")
cls()
banner()
try:
  em_audio(af, string, output)
except:
  print ("Something went wrong!! try again")
  quit('')
