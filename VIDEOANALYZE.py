import time
t_begin = time.time()

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pathlib
from deepface import DeepFace

path_to_photo = 'F:\\WOMEN'

count_man = count_women = 0

dir_photo = pathlib.Path(path_to_photo)
for path in dir_photo.iterdir():
    print(path)

    def face_analyze(imgpath):
        try:
            result_dict = DeepFace.analyze(img_path=imgpath, actions=['gender'])
            return result_dict[0].get('dominant_gender')
        except Exception as ex:
            print('Ошибка на фото нет ни мужчины, ни женщины')
            return ex


    PATH = path
    GENDER = face_analyze(PATH)
    if GENDER == 'Man':
        count_man += 1
        print('На фото Мужчина')
    elif GENDER == "Woman":
        count_women += 1
        print('На фото Женщина')

if count_man >= count_women:
    print("ВЕРОЯТНЕЕ ВСЕГО НА ВИДЕО МУЖЧИНА")
else:
    print("ВЕРОЯТНЕЕ ВСЕГО НА ВИДЕО ЖЕНЩИНА")

t_finish = time.time()
print(f'Время выполненния программы: {t_finish - t_begin}')
