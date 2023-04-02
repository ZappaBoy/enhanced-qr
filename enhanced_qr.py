import argparse
import os

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

dir_path = os.path.dirname(os.path.realpath(__file__))
generated_image_path = os.path.join(dir_path, 'generated.png')

default_url = 'https://justanotherdomain.dev/'
default_embedded_image_path = os.path.join(dir_path, 'background.png')
default_back_color = (13, 19, 33)


class EnhancedQR:

    @staticmethod
    def generate(content=default_url, image_path=default_embedded_image_path, back_color=default_back_color):
        print('Generating: ', content)
        qr = qrcode.QRCode(version=30, error_correction=qrcode.constants.ERROR_CORRECT_H, border=4)
        qr.add_data(content)
        qr.make()
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
                            color_mask=ImageColorMask(color_mask_path=image_path, back_color=back_color))
        img.save(generated_image_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=False, default=default_url)
    parser.add_argument('--bg', type=str, required=False, default=default_embedded_image_path)
    parser.add_argument('--color', nargs='+', type=int, required=False, default=default_back_color)

    args = parser.parse_args()
    link = args.url
    background_image_path = os.path.abspath(args.bg)
    color = tuple(args.color)

    enhanced_qr = EnhancedQR()
    enhanced_qr.generate(link, background_image_path, color)
