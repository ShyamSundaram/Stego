import wave
from hashlib import sha256
import base64
from Crypto import Random
from Crypto.Cipher import AES
#from wave import open
# read wave audio file
from pydub import AudioSegment

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf8')

def EncodeToAudio(text_name,audio_name,f,password):
    # text_name=input("Enter text file name: ")
    text = open(text_name,"r")
    string = text.read()
    text.close()

    if(audio_name.split(".")[1]=="mp3"):
        sound=AudioSegment.from_mp3(audio_name)
        sound.export(audio_name.split(".")[0]+".wav",format="wav")
        audio_name=audio_name.split(".")[0]+".wav"
        print("conversion complete")

    cipher=AESCipher(password.zfill(16))
    string = cipher.encrypt(string)
    string=string.decode('utf-8')
    # audio_name=input("Enter Audio carrier name with extension: ")
    
    song = wave.open(audio_name, mode='rb')

    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # The "secret" text message

    # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)

    # Write bytes to a new wave audio file
    # with wave.open('song_embedded.wav', 'wb') as fd:
    # f=input('Enter file name (to be saved as): ')
    fd = wave.open(f, 'wb')
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
    song.close()

def DecodeFromAudio(file,outname,password):
    # file=input('Enter Audio file name: ')
    song = wave.open(file, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    string=string.split("###")[0]
    string=string.encode('utf-8')
    # Cut off at the filler characters
    cipher=AESCipher(password.zfill(16))
    string = cipher.decrypt(string)
    if(len(string)==0):
        raise ValueError('Password is incorrect')
    #decoded = string.split("###")[0]
    file1=open(outname,"w")
    file1.write(string)
    file1.close()
    # Print the extracted text
    # print("Text extracted:\n"+decoded)
    song.close()

# n=0
# while(n!=-1):
#     n=int(input('\n1. Merge with audio\n2. Extract from audio\nExit\nChoice: '))
#     if(n==1):
#         EncodeToAudio()
#     elif(n==2):
#         DecodeFromAudio()
#     else:
#         n=-1
#         break
