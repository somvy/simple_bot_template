import torchvision
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def prepare_image(path):
    # читаем изображение
    image = torchvision.io.read_image(path).float()
    # нормализуем
    image /= 255.0
    # добавляем размерность батча, получаем батч из одной картинки
    return image.unsqueeze(0)


def form_reply_keyboard(buttons_info):
    keyboard = ReplyKeyboardMarkup()

    for i in range(len(buttons_info)):
        print(buttons_info[i])
        keyboard.add(KeyboardButton(str(buttons_info[i])))

    return keyboard
