""" module with implementation of ADT, which are used in project """
import os
import csv
import shutil
import zipfile
import requests
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from PIL import Image as Picture
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials


class Emotion:
    """
    Class for Emotion representation.

    Attributes
    ----------
    __emotions: str
        name of emotion
    __percentage: float
        percentage of emotion
    __life_average: float
        average percentage of emotion in life

    Modules
    -------
    __get_life_average()
        parse life average emotion percentage by name
    emotion()
        get private attribute __emotions
    percentage()
        get private attribute __percentage
    life_average()
        get private attribute __life_average
    __str__()
        returns string representation of the emotion ADT class
    """
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
    """
    Class for Image representation.

    Attributes
    ----------
    __link: str
        link of the image
    __all_attributes: azure.cognitiveservices.vision.face.models._models_py3.FaceAttributes
        all attributes of the image
    __emotions: list(Emotion)
        list of emotions on the photo, each emotion is a member of Emotion class
    __picture: Picture
        Picture object of the photo
    __rectangle: azure.cognitiveservices.vision.face.models._models_py3.FaceRectangle
        Rectangle object of the photo

    Methods
    -------
    __parse_image_info()
        parse info of Instagram page
    all_attributes()
        get privat attribute __all_attributes
    emotions()
        get private attribute __emotions
    picture()
        get private attribute __picture
    rectangle()
        get private attribute __rectangle
    """
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

        # if not detected_faces:
        #     raise Exception(
        #         'No face detected from image {}'.format(single_image_name))

        emotions_order = ['anger', 'contempt', 'disgust', 'fear',
        'happiness', 'neutral', 'sadness', 'surprise']

        if len(detected_faces) == 1:
            face = detected_faces[0]
            self.__all_attributes = face.face_attributes
            emotions = self.__all_attributes.emotion
            for emotion in emotions_order:
                self.__emotions.append(Emotion(emotion, eval(f'emotions.{emotion}')))

            self.__picture = Picture.open(requests.get(self.__link, stream=True).raw)
            self.__rectangle = face.face_rectangle
        else:
            raise ValueError
            # self.__all_attributes = {}
            # self.__emotions = []
            # self.__picture = None
            # self.__rectangle = None

    @property
    def all_attributes(self):
        """ get private attribute __all_attributes """
        return self.__all_attributes

    @property
    def emotions(self):
        """ get private attribute __emotions """
        return self.__emotions

    @property
    def picture(self):
        """ get private attribute __picture """
        return self.__picture

    @property
    def rectangle(self):
        """ get private attribute __rectangle """
        return self.__rectangle


class InstagramPage:
    """
    Class for InstagramPage representation.

    Attributes
    ----------
    __username: str
        username of the page
    __photos: list(Picture)
        list of photos of the page
    __happiest_photo: Picture
        the happiest photo of the page
    __average_emotions: list(Emotion)
        list of average emotions of the profile

    Methods
    -------
    __parce_page_info()
        parse info of Instagram page
    photos()
        get private attribute __photos
    happiest_photo()
        get private attribute __happiest_photo
    average_emotions()
        get private attribute __average_emotions
    relative_fakeness()
        return the relative percentage of fake profile emotion compared to
        the average human emotions
    write_to_file()
        write to the file statistics of a particular Instagram profile
    visualize()
        display profile statistics in graphs and diagrams
    zip_result()
        create zip archive with analysed data
    """
    __emotions_order = ['anger', 'contempt', 'disgust', 'fear', 'happiness',\
                        'neutral', 'sadness', 'surprise']
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
        # KEY = "c2480c722emsh51bc692f9b351bcp1a170ajsnb495557dbedf"
        # KEY = "623e807215msh15f665bc8db7ce2p1b409djsn2e81a08ef9c5"
        # KEY = "5acd5fe65bmshba7744cd8b34cfap117aafjsne6f930a8ef76"
        # KEY = "6a4879f288msh788d248e775c43cp1dcc6fjsnc6c8bc5c144a"

        querystring = {"username": self.__username}

        headers = {
            'x-rapidapi-key': KEY,
            'x-rapidapi-host': "instagram47.p.rapidapi.com"
        }

        response = requests.request(
            "GET", URL, headers=headers, params=querystring)
        for post in response.json()['body']['items']:
            try:
                self.__photos.append(Image(post['image_versions2']['candidates'][0]['url']))
            except ValueError:
                pass

        max_happiness = -1
        happiest_photo = None
        for photo in self.__photos:
            try:
                happiness = photo.emotions[4].percentage
                if happiness > max_happiness:
                    max_happiness = happiness
                    happiest_photo = photo
            except IndexError:
                print(photo.emotions)
        try:
            self.__happiest_photo = happiest_photo.picture
        except IndexError:
            self.__happiest_photo = Picture.open('../static/no-image.png')

        summary_emotions = [0] * 8
        for photo in self.__photos:
            for idx_emotion in range(8):
                summary_emotions[idx_emotion] += photo.emotions[idx_emotion].percentage

        num_photos = len(self.__photos)
        for idx_emotion in range(8):
            self.__average_emotions.append(Emotion(self.__emotions_order[idx_emotion],\
                 summary_emotions[idx_emotion] / num_photos))

    @property
    def username(self):
        """ get privat attribute __username """
        return self.__username

    @property
    def photos(self):
        """ get private attribute __photos """
        return self.__photos

    @property
    def happiest_photo(self):
        """ get private attribute __happiest_photo """
        return self.__happiest_photo

    @property
    def average_emotions(self):
        """ get private attribute __average_emotions """
        return self.__average_emotions

    def relative_fakeness(self) -> float:
        """
        return the relative percentage of fake profile emotion
        compared to the average human emotions
        """
        fakeness = 0
        for emotion in self.average_emotions:
            fakeness += abs(emotion.percentage - emotion.life_average)
        return round(fakeness, 1)

    def get_emoji(self):
        """ get emoji from most vivid emotion """
        biggest_emotion_num = 0
        biggest_emotion = None
        for emotion in self.average_emotions:
            if biggest_emotion_num < emotion.percentage:
                biggest_emotion = emotion
                biggest_emotion_num = emotion.percentage
        return f'../static/emotions/{biggest_emotion.emotions}.png'

    def write_to_file(self):
        """
        writing to the file statistics of a particular Instagram profile
        """
        with open('account_analysis.csv', 'w', encoding='utf-8') as out_file:
            emotions = self.__average_emotions
            csv_out = csv.writer(out_file)
            for emotion in emotions:
                csv_out.writerow([emotion.emotions, emotion.percentage])
            csv_out.writerow(['fakeness', self.relative_fakeness()])

    def visualize(self):
        """
        display profile statistics in graphs and diagrams
        """
        emotions = [item.percentage*100 for item in self.__average_emotions]

        # graphic
        average_emotions = []

        for one_emotion in self.__average_emotions:
            average_emotions.append(one_emotion.life_average * 100)

        x1 = np.array(self.__emotions_order)
        x2 = np.array(self.__emotions_order)
        y1 = np.array(emotions)
        y2 = np.array(average_emotions)
        plt.plot(x1, y1, x2, y2, marker='o')
        plt.xlabel('Emotions')
        plt.ylabel('Percentage')
        plt.title('Comparison of emotions in Instagram and in life')
        plt.legend(labels=('Instagram page emotions', 'Average life emotions'), loc='upper left')
        plt.savefig(f'{self.username}_emotion_graphic.png')
        plt.close()

        # piechart
        labels = [item.emotions for item in self.__average_emotions if item.percentage >= 0.03]
        y = [item.percentage*100 for item in self.__average_emotions if item.emotions in labels]
        labels.append('others')
        y.append(100 - sum(y))
        colors = ['#bcf8ec', '#aed9e0', '#a7ccd4', '#8b687f', '#7b435b',\
                  '#e8eddf', '#cfdbd5', '#aac8e6']
        plt.pie(y, startangle=90, shadow=True, autopct='%1.2f',
                colors=colors)
        plt.legend(title='Emotions', labels=labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
        plt.savefig(f'{self.username}_emotion_piechart.png')
        plt.close()

    def zip_result(self):
        """ create zip archive with analysed data """
        i = 0
        while True:
            try:
                Path(os.path.join(os.getcwd(), f'data_{i}')).mkdir()
                break
            except FileExistsError:
                i += 1
        temp_directory = Path(os.path.join(os.getcwd(), f'data_{i}'))

        os.chdir(temp_directory)
        self.write_to_file()
        self.visualize()
        os.chdir('..')

        with zipfile.ZipFile(f'{self.username}_analyzing.zip', 'w') as file:
            for filename in temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(temp_directory)
