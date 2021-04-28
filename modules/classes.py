""" module with implementation ADT, which are used in project """
from typing import List

import requests
from PIL import Image as Picture


class Emotion:
    """ class Emotion """
    def __init__(self, emotion: str, percentage: float):
        self.__emotions = emotion
        self.__percentage = percentage
        self.__life_average = None  # type - float
        self.__get_life_average()

    def __get_life_average(self):
        """ parse life average emotion percentage by name """
        if self.__emotions == '':
            self.__life_average = 1.
        else:
            raise ValueError

    @property
    def emotions(self):
        """ get privat attribute __emotions """
        return self.__emotions

    @property
    def percentage(self):
        """ get privat attribute __percentage """
        return self.__percentage

    @property
    def life_average(self):
        """ get privat attribute __life_average """
        return self.__life_average

    def __str__(self):
        return \
          f'emotion name:                    {self.emotions}\n'\
          f'emotion percentage:              {round(100*self.percentage,1)}\n'\
          f'life average emotion percentage: {round(100*self.life_average,1)}'


class Image:
    """ class InstagramPage """
    def __init__(self, link: str):
        self.__link = link
        self.__all_attributes = {}  # type - dict
        self.__emotions = []        # type - List[Emotion]
        self.__picture = None       # type - Picture
        self.__rectangle = None     # type  - Coordinate
        self.__parse_image_info()

    def __parse_image_info(self):
        """ parse info of Instagram page """
        self.__all_attributes = {}
        self.__emotions = []
        self.__picture = Picture.open(requests.get(self.__link, stream=True).raw)
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
    def __init__(self, link: str):
        self.__link = link
        self.__photos = []              # type - List[Image]
        self.__happiest_photo = None    # type - Picture
        self.__average_emotions = []    # type - List[Emotion]
        self.__parse_page_info()

    def __parse_page_info(self):
        """ parse info of Instagram page """
        self.__photos = []
        self.__happiest_photo = None
        self.__average_emotions = []

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
        return 1.

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
