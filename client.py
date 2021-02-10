import dlib
import os
import cv2
from PIL import Image

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def get_face_detect(image):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    flag = False

    # change this as you see fit
    image_path = default_storage.save("tmp/temp.jpg", ContentFile(image.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, image_path)

    detector = dlib.get_frontal_face_detector()

    img = cv2.imread(tmp_file)

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    det = detector(gray)
    print(len(det))

    if len(det)==0:
        response = {"message": "No Face found!" }
        pass
    elif len(det)>1:
        response = {"message": "Multiple Face Detected!"}
        pass
    elif len(det)==1:
        response = {"message": "Single Face Detected!"}
        pass

    default_storage.delete(f'tmp/temp.jpg')

    return response