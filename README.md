# Evil-Eye
Evil Eye is a tool for Audio Steganography.



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
python3 extract.py  -f outputfile (with .wav extension)
```

![Screenshot at 2022-08-22 23-58-20](https://user-images.githubusercontent.com/88737074/185993280-cd7f13e7-44a9-4d2d-a360-2ff4e2764b94.png)


![Screenshot at 2022-08-22 23-59-23](https://user-images.githubusercontent.com/88737074/185993515-c45c226d-d37e-4a37-b787-31a6b2edd418.png)




### Video Demo
[![How to control android camera](https://img.youtube.com/vi/HNM9HYhHc3E/0.jpg)](https://www.youtube.com/watch?v=UPQD7L9FNrk)



###For More Video subcribe <a href="https://www.youtube.com/channel/UCuulPn_llK3PpK4mA9P6bjQ/videost">Cyber Octopus YouTube Channel</a>

