'''
A module example of using azure API.
'''
import os

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

if __name__ == '__main__':
    try:
        KEY = input('Enter your key: ')
        ENDPOINT = input('Enter your endpoint: ')

        single_face_image_url = input('Enter photo url: ')
        single_image_name = os.path.basename(single_face_image_url)

        face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

        detected_faces = face_client.face.detect_with_url(
            url=single_face_image_url, detection_model='detection_01',
            return_face_attributes=['emotion'])
        if not detected_faces:
            raise Exception(
                'No face detected from image {}'.format(single_image_name))

        for face in detected_faces:
            print(face.face_attributes.emotion)

    except Exception:
        print('There is no faces on that image or incorrect input')
        print()
