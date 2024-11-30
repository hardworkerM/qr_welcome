# from forms import ArticlesForm
import qrcode
import os
from PIL import Image


def make_qr(link, id):
    print(link)
    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="transparent")
    # i save it locally

    name =  f'qr_img{id}.png'
    print(name)
    img.save(name)
    return name

def add_qr_to_shirt_centered(shirt_image_path, user_id):
    """
    Размещает QR-код в центре футболки, используя точные координаты макета.

    :param shirt_image_path: Путь к изображению футболки (без QR-кода)
    :param qr_image_path: Путь к изображению QR-кода
    :param output_path: Путь для сохранения готового изображения
    """
    # Открыть изображение футболки
    shirt_image = Image.open(shirt_image_path)

    # Открыть изображение QR-кода
    link = f'https://t.me/qr_change_bot?start={user_id}'
    qr_file = make_qr(link, user_id)
    qr_image = Image.open(qr_file)
    qr_size = (650, 650)
    position = (455, 645)  # Верхний левый угол QR-кода на футболке

    shirt_image.paste(qr_image, position, qr_image)
    # Сохранить результат
    name = f'src/mokap_done{user_id}'
    shirt_image.save(name)

#
# # Пример использования
# add_qr_to_shirt_centered("мокап реди.png", "qr_img_white.png", "final_shirt_with_qr.png")
