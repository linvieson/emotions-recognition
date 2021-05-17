# Emotions recognition and analysis by photos on the Instargam profile

### Description
This project analyzes emotions on photos from the Instagram profile and provides user with the statistics and visual data. It also displays the comparison between the average 
percentage of different emotions on the photos of the Instagram profile and the average statistical distribution of emotions in life. 

Visual data provided:
* graphic with comparison between profile average emotions and average statistical distribution of emotions in life
* pie chart with representation of all the emotions in the Instagram profile
* csv file with data on the emotions' percentage in the Instagram profile
* the happiest photo in the Instagram profile

All data can be downloaded.

***

### Aim of the project
It allows to analyze the selected profile and provide statistics on its emotional range. The peculiarity of our application is the ability to see the differences between the percentage distribution of emotions of the Instagram profile and the average human emotions.

Most bloggers only share happy photos, so it creates the illusion that everyone on the web is always positive. This phenomenon negatively affects the consciousness and self-esteem of people who look at endlessly happy photos of people in the feed every day and think that something is wrong with them.

Our application allows to see exactly what emotions the Instagram profile hides from the camera and to what extent to help the user understand how distorted is the picture he sees. Some people may realize this on their own, but the lack of evidence leaves some doubt. Many influencers not only harm the acceptance of their own appearance by subscribers, but also the attitude towards their negative emotions. It seems as if it is abnormal to feel anger, sadness, disgust, which are a normal part of the life of any mentally healthy person.

Unfortunately, it is more difficult to prove the fakeness of emotions than to find distortions in photos, so our application comes in handy here, as it promotes healthy attitude to the own emotions of the users and improve the psychological state of them.

***

### Input and output data
* Input data:
    * nickname of the Instagram user
* Output data:
    * graphic with comparison between profile average emotions and average statistical distribution of emotions in life
    * pie chart with representation of all the emotions in the Instagram profile
    * csv file with data on the emotions' percentage in the Instagram profile
    * the happiest photo in the Instagram profile

***

### Structure
* [modules](https://github.com/linvieson/emotions-recognition/tree/main/modules) contains a [tests.py](https://github.com/linvieson/emotions-recognition/blob/main/modules/tests.py) module that contains module unittests for main ADT classes and a [classes.py](https://github.com/linvieson/emotions-recognition/blob/main/modules/classes.py) module that contains the next ADT classes:
  * Emotion - contains the next methods:
    * __get_life_average() - parse life average emotion percentage by name
    * emotion() - get private attribute __emotions
    * percentage() - get private attribute __percentage
    * life_average() - get private attribute __life_average
    * __str__() - returns string representation of the emotion ADT class

  * Image - contains the next methods:
    * __parse_image_info() - parse info of Instagram page
    * all_attributes() -  get privat attribute __all_attributes
    * emotions() - get private attribute __emotions
    * picture() - get private attribute __picture
    * rectangle() - get private attribute __rectangle

  * InstagramPage - contains the next methods:
    * __parce_page_info() - parse info of Instagram page
    * photos() - get private attribute __photos
    * happiest_photo() - get private attribute __happiest_photo
    * average_emotions() - get private attribute __average_emotions
    * relative_fakeness() - return the relative percentage of fake profile emotion compared to the average human emotions
    * write_to_file() - write to the file statistics of a particular Instagram profile
    * visualize() - display profile statistics in graphs and diagrams
    * zip_result() - create zip archive with analysed data

* [examples](https://github.com/linvieson/emotions-recognition/tree/main/examples) contains the next modules with examples of usage of different classes and their methods

  * [emotions.recognition.py](https://github.com/linvieson/emotions-recognition/blob/main/examples/example_emotion_recognition.py) - example of using azure API
  * [example_modules_usage.py](https://github.com/linvieson/emotions-recognition/blob/main/examples/example_modules_usage.py) - examples of module usage
  * [example_photo_links.py](https://github.com/linvieson/emotions-recognition/blob/main/examples/example_photo_links.py) - example of getting pictures urls with rapid api
  * [examples_django](https://github.com/linvieson/emotions-recognition/tree/main/examples/example_django) folder - example of Django usage

***



### Usage
To use the program, you need to go to the [EMOTIONS RECOGNITION WEBSITE](). Write down the Instagram nickname of the profile you want to analyze.
Press the "Get info" button. All the visual data will be provided to you. If you want to download certain files, click on the "Download" button below the file you want to 
download.

***

### Description of test examples
Unittest was used for module testing of the program. The TestADTs class has three methods for testing three main ADT classes used in the program:
* test_emotion() - has tests for emotion ADT class
* test_image() - has tests for Image ADT class
* test_instagram_page() - has tests for InstagramPage ADT class
The successsful module running demonstrates the correctness of the work of the program.

***

### Results
The result of the project is the visualized data, which includes the comparison between the average Instagram profile emotions and the average statistical life emotions.
After using the program, the user can understand that emotions on the Instagram are not always genuine, and there is no point in comparing themselves with the Instagram 
celebrities and other people.

***

### Used materials
* [Microsoft azure API](https://azure.microsoft.com/en-us/services/cognitive-services/face/#overview)
* [Instagram API By Prasadbro](https://rapidapi.com/Prasadbro/api/instagram47?endpoint=apiendpoint_57bf9598-e085-4947-89ff-ba5e520c59d7)
* ["Emotions in Real Life" study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4689475/)

***

### Credits
* [Alina Voronina](https://github.com/linvieson)
* [Anita Hrodzytska](https://github.com/caul1flower)
* [Mykhailo Pasichnyk](https://github.com/fox-flex)
* [Oleksandra Tsepilova](https://github.com/sasha-tsepilova)
* [Yaroslav Romanus](https://github.com/yarkoslav)

***

### License
[MIT](https://github.com/linvieson/emotions-recognition/blob/main/LICENSE)

***
