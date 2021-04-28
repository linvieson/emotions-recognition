""" module with implementation ADT, which are used in project """


class InstagramPage:
    """ class InstagramPage """
    def __init__(self, link):
        self.__link = link
        self.__photos = []
        self.__happiest_photo = None
        self.__average_emotions = None
        self.__parse_page_info()

    def __parse_page_info(self):
        """ parse info of Instagram page """
        self.__photos = []
        self.__happiest_photo = None
        self.__average_emotions = None

    @property
    def photos(self):
        """ get privet attribute __photos """
        return self.__photos

    @property
    def happiest_photo(self):
        """ get privet attribute __happiest_photo """
        return self.__happiest_photo

    @property
    def average_emotions(self):
        """ get privet attribute __average_emotions """
        return self.__average_emotions

    def relative_fakeness(self):
        """
        will return the relative percentage of fake profile emotion
        compared to the average human emotions
        """
        pass

    def analyze(self):
        """
        will analyze the profile photo and return the dictionary, where the
        key will be the emotion, and the value of its percentage in the profile
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


class Image:
    """ class InstagramPage """
    def __init__(self, link):
        self.__link = link
        self.__all_attributes = {}
        self.__emotions = []
        self.__picture = None
        self.__rectangle = None
        self.__parse_link()

    def __parse_image_info(self):
        """ parse info of Instagram page """
        self.__all_attributes = {}
        self.__emotions = []
        self.__picture = None
        self.__rectangle = None

    @property
    def all_attributes(self):
        """ get privet attribute __all_attributes """
        return self.__all_attributes

    @property
    def emotions(self):
        """ get privet attribute __emotions """
        return self.__emotions

    @property
    def picture(self):
        """ get privet attribute __picture """
        return self.__picture

    @property
    def rectangle(self):
        """ get privet attribute __rectangle """
        return self.__rectangle


class Emotion:
    """ class Emotion """
    def __init__(self, emotion, percentage):
        self.__emotions = emotion
        self.__percentage = percentage
        self.__life_average = None
        self.__get_life_average()

    def __get_life_average(self):
        """ parse life average emotion percentage by name """
        if self.__emotions == '':
            self.__life_average = 1.
        else:
            raise ValueError

    @property
    def emotions(self):
        """ get privet attribute __emotions """
        return self.__emotions

    @property
    def percentage(self):
        """ get privet attribute __percentage """
        return self.__percentage

    @property
    def life_average(self):
        """ get privet attribute __life_average """
        return self.__life_average
