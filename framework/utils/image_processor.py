import math
import os
from io import BytesIO

from PIL import Image, ImageChops, ImageFilter


class ImageProcessor:
    @staticmethod
    def _prepare_image(data: str | bytes) -> Image.Image:
        """
        Helper to load image from path or bytes and flatten transparency.
        """
        if isinstance(data, str):
            img = Image.open(data)
        else:
            img = Image.open(BytesIO(data))

        # Handle transparency by pasting onto a white background
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert('RGBA')
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])
            return background

        return img.convert('RGB')

    @staticmethod
    def get_image_similarity_index(actual_image_data: str | bytes,
                                   expected_image_data: str | bytes,
                                   save_debug: bool = False):
        """
        Calculates the RMSE between two images.
        0.0 is a perfect match.
        """
        actual = ImageProcessor._prepare_image(actual_image_data)
        expected = ImageProcessor._prepare_image(expected_image_data)

        # 1. Resize expected to match actual using high-quality LANCZOS
        if actual.size != expected.size:
            expected = expected.resize(actual.size, Image.Resampling.LANCZOS)

        # 2. Apply a light blur to mitigate sub-pixel rendering/antialiasing noise
        actual = actual.filter(ImageFilter.GaussianBlur(radius=1))
        expected = expected.filter(ImageFilter.GaussianBlur(radius=1))

        # 3. Optional: Save debug images to current script directory
        if save_debug:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            actual.save(os.path.join(base_dir, 'debug_actual.png'))
            expected.save(os.path.join(base_dir, 'debug_expected.png'))

        # 4. Calculate Difference
        diff = ImageChops.difference(actual, expected)
        h = diff.histogram()

        # 5. Calculate the RMSE (Root Mean Square Error)
        # Multiply num_pixels by 3 because the histogram contains 3 channels (RGB)
        sq_diff = sum((value * ((idx % 256) ** 2) for idx, value in enumerate(h)))
        num_pixels = actual.size[0] * actual.size[1]
        rmse = math.sqrt(sq_diff / (num_pixels * 3))

        return rmse
