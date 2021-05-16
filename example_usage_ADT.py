from pprint import pprint

import requests
from PIL import Image as Picture

from modules.classes import InstagramPage, Image, Emotion

# try:
###########################################################################
#                     example of usage Emotion ADT                        #
###########################################################################
print('test Emotion ADT')

emotion_ex = Emotion('anger', 1.)

print(emotion_ex)
'''
emotion name:                    angry
emotion percentage:              100.0%
life average emotion percentage: 99.9%'
'''

###########################################################################
#                      example of usage Image ADT                         #
###########################################################################
print('\n' + '-' * 89 + '\ntest Image ADT')

url_photo = 'https://img.apmcdn.org/d947173a53458e5298472d9450325e7adc13468f/widescreen/60636c-20190625-angry.jpg'
picture = Image(url_photo)

print('show pictures')
picture.picture.show()

print('num of emotions:', len(picture.emotions))  # 8
# next loop print info about 8 types of emotion in this photo:
# anger, contempt, disgust, fear, happiness, neutral, sadness, surprise
print('info about emotion')
for emotion in picture.emotions:
    print(emotion)
    print('---------------------------------------')

print(f'info about rectangle\n'
      f'The distance to the left side of the image from rectangle is: {picture.rectangle.left}\n'
      f'The distance to the top of the image from rectangle is: {picture.rectangle.top}\n'
      f'The height of rectangle is: {picture.rectangle.height}\n'
      f'The width of rectangle is: {picture.rectangle.width}')

###########################################################################
#                  example of usage InstagramPage ADT                     #
###########################################################################
print('\n' + '-' * 89 + '\ntest InstagramPage ADT')

page = InstagramPage('f.o.x.109')

print('show pictures')
page.photos[0].picture.show()  # show first photo from this profile
page.happiest_photo.show()  # show happiest photo from this profile

print('info about emotion')
# next loop print info about average emotions in Instagram page
# anger, contempt, disgust, fear, happiness, neutral, sadness, surprise
for emotion in page.average_emotions:
    print(emotion)
    print('---------------------------------------')

print(f'relative fakeness percentage: {round(100 * page.relative_fakeness(), 1)}')

print('print report into the file')
page.write_to_file()

print('visualise report')
page.visualize()

page.zip_result()
#
# except Exception as err:
#     print(err)
