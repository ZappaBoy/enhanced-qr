# Enhanced QR

This is a simple script that allows you to generate a QR code for a URL, and then enhance it with an image in background.

Example:

![Just Another QR](https://github.com/ZappaBoy/enhanced-qr/blob/main/docs/result_example.png?raw=true)

## How to use

First of all clone the repo and install the requirements:
``` shell
git clone https://github.com/ZappaBoy/enhanced-qr.git
cd enhanced-qr
pip install -r requirements.txt
```

Then add an image called `background.png` in the same folder of the script, and run it:
``` shell
python enhanced_qr.py --url 'your_url_here'
```

Alternatively you can use define the path of the image you want to use as background:
``` shell
python enhanced_qr.py --url 'your_url_here' --bg /path/to/your/image.png
```

Finally you can also define the background color of the image in RGB format:
``` shell
python enhanced_qr.py --url  'your_url_here' --bg /path/to/your/image.png --color 255 255 255
```

You can also set the color transparency passing to `--color` a fourth value from 0 to 255
``` shell
python enhanced_qr.py --url  'your_url_here' --bg /path/to/your/image.png --color 255 255 255 100
```

## Acknowledgement
This is only a simple script that uses a very powerful library [python-qrcode](https://github.com/lincolnloop/python-qrcode) say thanks to the community.