'''
Testing module for classes.py module.
'''
from unittest import TestCase
from classes import Emotion, Image, InstagramPage
import azure
import unittest


class TestValidator(TestCase):
    '''
    Test classes.py module.
    '''

    def test_emotion(self):
        '''
        Tests for emotion ADT class.
        '''
        self.anger = Emotion('anger', 0.03)

        self.assertEqual(self.anger.emotions, 'anger')
        self.assertEqual(self.anger.percentage, 0.03)
        self.assertEqual(self.anger.life_average, 0.1)
        text = 'emotion name:                   \
 anger\nemotion percentage:             \
 3.0\nlife average emotion percentage: 10.0'
        self.assertEqual(str(self.anger), text)

    def test_image(self):
        '''
        Tests for Image ADT class.
        '''
        url_photo =\
            'https://img.apmcdn.org/d947173a53458e5298472d9450325e7adc13468f/widescreen/60636c-20190625-angry.jpg'
        self.picture = Image(url_photo)
        self.assertEqual(type(self.picture.all_attributes),
                         azure.cognitiveservices.vision.face.models._models_py3.FaceAttributes)
        self.assertEqual(type(self.picture.emotions), list)
        self.assertEqual(type(self.picture.rectangle),
                         azure.cognitiveservices.vision.face.models._models_py3.FaceRectangle)
        self.assertEqual(len(self.picture.emotions), 8)

    def test_instagram_page(self):
        '''
        Tests for InstagramPage ADT class.
        '''
        self.page = InstagramPage('f.o.x.109')
        self.assertEqual(len(self.page.average_emotions), 8)
        self.assertEqual(self.page.relative_fakeness(), 1.266)
        self.assertEqual(type(self.page.photos[0]), Image)

        try:
            self.page.write_to_file()
            self.page.visualize()
            self.page.zip_result()
        except:
            raise AssertionError


if __name__ == '__main__':
    unittest.main()
