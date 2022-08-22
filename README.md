# Evil-Eye
Evil Eye is a tool of python based program for simple audio steganography.



![EvilEye](https://user-images.githubusercontent.com/88737074/185978331-3f9bbc2e-01bc-4d19-8205-7bd9ea2d144a.png)


## What is Audio steganography ?

Audio steganography is about hiding the secret message into the audio. It is a technique uses to secure the transmission of secret information or hide their existence. It also may provide confidentiality to secret message if the message is encrypted.

## Installation ( Linux )

```
git clone https://github.com/codewithharit/Evil-Eye.git
cd Evil-Eye
chmod +x *
bash linux.sh
python3 bind.py 
```

## Installation ( Termux )

```
git clone https://github.com/codewithharit/Evil-Eye.git
cd Evil-Eye
chmod +x *
bash termux.sh
python3 bind.py 
```


## Usage

```

usage: bind.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE] [-p OUTPUTPATH]


optional arguments:

-h, --help show this help message and exit
-f AUDIOFILE Select Audio File
-m SECRETMSG Enter your message
-o OUTPUTFILE Your output file path and name ( with .wav extension )
-p Path of your output file

```
## Extract Hidden Text Message  from Audio file

```
python3 ExWave.py -f outputfile (with .wav extension)
```



