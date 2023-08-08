# Enhanced QR

This is a simple script that allows you to generate a QR code for a URL, and then enhance it with an image in background.

Example:

![Just Another QR](https://github.com/ZappaBoy/enhanced-qr/blob/main/docs/result_example.png?raw=true)

## How to use

First of all clone the repo and install the requirements:
``` shell
git clone https://github.com/ZappaBoy/enhanced-qr.git
cd enhanced-qr
# Probably you want to create a virtual environment first
pip install -r requirements.txt
```

Then add an image called `background.png` in the same folder of the script, and run it:
``` shell
python enhanced_qr.py --url 'your_url_here'
```

Alternatively you can use define the path of the image you want to use as background:
``` shell
python enhanced_qr.py --bg /path/to/your/image.png
```

Finally, you can also define the background color of the image in RGB format:

``` shell
python enhanced_qr.py --color 255 255 255
```

You can also set the color transparency passing to `--color` a fourth value from 0 to 255

``` shell
python enhanced_qr.py --color 255 255 255 100
```

You can adjust the quality of the QR code by passing a value from 1 to 40 to `--quality`:

``` shell
python enhanced_qr.py --quality 30
```

Or generate all the qualities using `--all-qualities`:

``` shell
python enhanced_qr.py --all-qualities
```

## Options

```shell
> python enhanced_qr.py --help
usage: enhanced_qr.py [-h] [--url URL] [--bg BG] [--color COLOR [COLOR ...]] [--quality QUALITY]

options:
  -h, --help            show this help message and exit
  --url URL             URL to generate QR code for
  --bg BG               Path to background image
  --color COLOR [COLOR ...]
                        Background color (RGB) or (RGBA)
  --quality QUALITY     Quality of QR code (1-40)
```

## Acknowledgement

This is only a simple script that uses a very powerful
library [python-qrcode](https://github.com/lincolnloop/python-qrcode) say thanks to the community.