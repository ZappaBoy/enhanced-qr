import argparse
import os
from typing import Union

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, GappedSquareModuleDrawer
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer, CircleModuleDrawer, \
    VerticalBarsDrawer, HorizontalBarsDrawer

dir_path = os.path.dirname(os.path.realpath(__file__))
generated_dir_path = os.path.join(dir_path, 'generated')

default_url = 'https://justanotherdomain.dev/'
default_embedded_image_path = os.path.join(dir_path, 'background.png')
default_back_color = (13, 19, 33)
default_quality = 30


class EnhancedQR:
    drawers = [
        SquareModuleDrawer(),
        GappedSquareModuleDrawer(),
        CircleModuleDrawer(),
        RoundedModuleDrawer(),
        VerticalBarsDrawer(),
        HorizontalBarsDrawer()
    ]

    @staticmethod
    def generate(content: str = default_url, image_path: str = default_embedded_image_path,
                 back_color: Union[tuple[int, int, int], tuple[int, int, int, int]] = default_back_color,
                 version: int = default_quality):
        print('Generating: ', content)
        generated_quality_dir_path = os.path.join(generated_dir_path, str(version))
        if not os.path.exists(generated_quality_dir_path):
            os.makedirs(generated_quality_dir_path)
        qr = qrcode.QRCode(version=version, error_correction=qrcode.constants.ERROR_CORRECT_H, border=4)
        qr.add_data(content)
        qr.make()
        for drawer in EnhancedQR.drawers:
            print('Generating with: ', drawer.__class__.__name__)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=drawer,
                                color_mask=ImageColorMask(color_mask_path=image_path, back_color=back_color))
            generated_image_path = os.path.join(generated_quality_dir_path, f'{drawer.__class__.__name__}.png')
            img.save(generated_image_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=False, default=default_url,
                        help='URL to generate QR code for')
    parser.add_argument('--bg', type=str, required=False, default=default_embedded_image_path,
                        help='Path to background image')
    parser.add_argument('--color', nargs='+', type=int, required=False, default=default_back_color,
                        help='Background color (RGB) or (RGBA)')
    parser.add_argument('--quality', type=int, required=False, default=default_quality,
                        help='Quality of QR code (1-40)')
    parser.add_argument('--all-qualities', type=bool, required=False, default=False,
                        action=argparse.BooleanOptionalAction,
                        help='Generate all quality of QR code (1-40)')

    args = parser.parse_args()
    link = args.url
    background_image_path = os.path.abspath(args.bg)
    color = tuple(args.color)
    quality = args.quality if 1 <= args.quality <= 40 else default_quality

    enhanced_qr = EnhancedQR()
    if not args.all_qualities:
        enhanced_qr.generate(link, background_image_path, color, quality)
    else:
        for i in range(1, 41):
            enhanced_qr.generate(link, background_image_path, color, i)
