import time
t_begin = time.time()

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from deepface import DeepFace

def face_analyze(imgpath):
    try:
        result_dict = DeepFace.analyze(img_path=imgpath, actions=['gender'], detector_backend='opencv')
        return result_dict[0].get('dominant_gender')
    except Exception as ex:
        print('Ошибка на фото нет ни мужчины, ни женщины')
        return ex

PATH_to_FHOTO = 'cf8ad2940cd7.jpg'
GENDER = face_analyze(PATH_to_FHOTO)
if GENDER == 'Man':
    print('На фото Мужчина')
elif GENDER == "Woman":
    print('На фото Женщина')

t_finish = time.time()
print(f'Время выполненния программы: {t_finish - t_begin}')