import io
import uuid
from datetime import datetime
from threading import Lock, local

import allure
from PIL import Image

allure_attach_orig = allure.attach

test_context = local()

screenshot_buffer = {}
step_screenshot_buffer = {}
buffer_lock = Lock()


def image_half_resize(pic: bytes):
    result = io.BytesIO()
    im = Image.open(io.BytesIO(pic))

    if im.mode in ('RGBA', 'LA', 'P'):
        background = Image.new('RGB', im.size, (255, 255, 255))
        if im.mode == 'P':
            im = im.convert('RGBA')
        background.paste(im, mask=im.split()[-1] if im.mode == 'RGBA' else None)
        im = background

    scale_factor = 0.6
    new_width = int(im.width * scale_factor)
    new_height = int(im.height * scale_factor)

    im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
    im.save(result, format='JPEG', quality=75, optimize=True)
    return result.getvalue()


def allure_step_exit_wrapper(device, orig_func):
    def wrapper(self, exc_type, exc_val, exc_tb):
        if device.config.attach_screenshots:
            try:
                screenshot_data = device.get_screenshot()
                screenshot_data = image_half_resize(screenshot_data)
            except Exception as e:
                print(e)
                return
            step_name = f'screenshot-{uuid.uuid4()}'
            allure.attach(screenshot_data, step_name, attachment_type=allure.attachment_type.JPG)

        orig_func(self, exc_type, exc_val, exc_tb)

    return wrapper


def allure_step_enter_wrapper(device, orig_func):
    def wrapper(self):
        if device.config.log_steps:
            print(f'{datetime.now()}   {self.title}')
        orig_func(self)
    return wrapper
