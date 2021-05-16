""" module with implementation of ADT, which are used in project """
from typing import List

import requests
from PIL import Image as Picture
import os
import matplotlib.pyplot as plt

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials


class Emotion:
    """ class Emotion """
    def __init__(self, emotion: str, percentage: float):
        """ initialize class parameters """
        self.__emotions = emotion
        self.__percentage = percentage
        self.__life_average = None  # type - float
        self.__get_life_average()


    def __get_life_average(self):
        """ parse life average emotion percentage by name """
        life_averages = {'anger': 0.1, 'contempt': 0.01, 'disgust': 0.11,\
                         'fear': 0.05, 'happiness': 0.35, 'neutral': 0.33,\
                         'sadness': 0.2, 'surprise': 0.05}
        try:
            self.__life_average = life_averages[self.__emotions]
        except KeyError as err:
            return err


    @property
    def emotions(self):
        """ get private attribute __emotions """
        return self.__emotions


    @property
    def percentage(self):
        """ get private attribute __percentage """
        return self.__percentage


    @property
    def life_average(self):
        """ get private attribute __life_average """
        return self.__life_average


    def __str__(self):
        """ returns string representation of the image ADT class"""
        return \
          f'emotion name:                    {self.emotions}\n'\
          f'emotion percentage:              {round(100*self.percentage,1)}\n'\
          f'life average emotion percentage: {round(100*self.life_average,1)}'


class Image:
    """ class Image """
    def __init__(self, link: str):
        self.__link = link
        self.__all_attributes = {}  # type - dict
        self.__emotions = []        # type - List[Emotion]
        self.__picture = None       # type - Picture
        self.__rectangle = None     # type  - Coordinate
        self.__parse_image_info()

    def __parse_image_info(self):
        """ parse info of Instagram page """
        KEY = '16901474877d4e85b4ba98a3505ab142'
        ENDPOINT = 'https://sashatsepilova.cognitiveservices.azure.com/'

        single_face_image_url = self.__link
        single_image_name = os.path.basename(single_face_image_url)

        face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

        detected_faces = face_client.face.detect_with_url(
            url=single_face_image_url, detection_model='detection_01',
            return_face_attributes=['emotion'])

        if not detected_faces:
            raise Exception(
                'No face detected from image {}'.format(single_image_name))

        emotions_order = ['anger', 'contempt', 'disgust', 'fear', 
        'happiness', 'neutral', 'sadness', 'surprise']

        if len(detected_faces) == 1:
            face = detected_faces[0]
            self.__all_attributes = face.face_attributes
            emotions = self.__all_attributes.emotion
            for emotion in emotions_order:
                self.__emotions.append(emotions[emotion])

            self.__picture = Picture.open(requests.get(self.__link, stream=True).raw)
            self.__rectangle = face.face_rectangle
        else:
            self.__all_attributes = {}
            self.__emotions = []
            self.__picture = None
            self.__rectangle = None

    @property
    def all_attributes(self):
        """ get privat attribute __all_attributes """
        return self.__all_attributes

    @property
    def emotions(self):
        """ get privat attribute __emotions """
        return self.__emotions

    @property
    def picture(self):
        """ get privat attribute __picture """
        return self.__picture

    @property
    def rectangle(self):
        """ get privat attribute __rectangle """
        return self.__rectangle


class InstagramPage:
    """ class InstagramPage """
    __emotions_order = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
    def __init__(self, username: str):
        self.__username = username
        self.__photos = []              # type - List[Image]
        self.__happiest_photo = None    # type - Picture
        self.__average_emotions = []    # type - List[Emotion]
        self.__parse_page_info()

    def __parse_page_info(self):
        """ parse info of Instagram page """

        URL = "https://instagram47.p.rapidapi.com/user_posts"
        # rapidapi key
        KEY = "2eff45ea8amshae726bb389e7279p113b54jsne071b6a20348"

        querystring = {"username": self.__username}

        headers = {
            'x-rapidapi-key': KEY,
            'x-rapidapi-host': "insta_gram47.p.rapidapi.com"
        }

        response = requests.request(
            "GET", URL, headers=headers, params=querystring)
        
        for post in response.json()['body']['items']:
            self.__photos.append(Image(post['image_versions2']['candidates'][0]['url']))
        
        max_happiness = 0
        for photo in self.__photos:
            happiness = photo.emotions[4].percentage
            if happiness > max_happiness:
                max_happiness = happiness
                happiest_photo = photo
        self.__happiest_photo = happiest_photo.picture

        summary_emotions = [0] * 8
        for photo in self.__photos:
            for idx_emotion in range(8):
                summary_emotions[idx_emotion] += photo.emotions[idx_emotion].percentage
        
        num_photos = len(self.__photos)
        for idx_emotion in range(8):
            self.__average_emotions.append(Emotion(self.__emotions_order[idx_emotion], summary_emotions[idx_emotion] / num_photos))

    @property
    def photos(self):
        """ get privat attribute __photos """
        return self.__photos

    @property
    def happiest_photo(self):
        """ get privat attribute __happiest_photo """
        return self.__happiest_photo

    @property
    def average_emotions(self):
        """ get privat attribute __average_emotions """
        return self.__average_emotions

    def relative_fakeness(self) -> float:
        """
        return the relative percentage of fake profile emotion
        compared to the average human emotions
        """
        fakeness = 0
        for emotion in self.average_emotions:
            fakeness += abs(emotion.percentage - emotion.life_average)
        return fakeness

    def analyze(self) -> List[Emotion]:
        """
        will analyze the profile photo and return a list with the Emotion
        objects, which describe the profile
        """
        pass

    def write_to_file(self):
        """
        writing to the file statistics of a particular Instagram profile
        """
        pass

    def visualize(self):
        """
        display profile statistics in graphs and diagrams
        """
        pass