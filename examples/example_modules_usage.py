"""
This module have examples of module usage
"""
import pprint
import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import requests


try:
    # example of requests usage
    URL = "https://instagram47.p.rapidapi.com/user_posts"

    username = input('Enter Instagram username: ')
    KEY = input('Enter your rapidapi key: ')

    querystring = {"username": username}

    headers = {
        'x-rapidapi-key': KEY,
        'x-rapidapi-host': "instagram47.p.rapidapi.com"
    }

    response = requests.request(
        "GET", URL, headers=headers, params=querystring)
    data = response.json()

    ###################################################################################

    # example of json module usage - saving data to file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    ###################################################################################

    # example of os usage - joining path wisely(can be used on Linux, Windows, macOS)
    path = os.path.join(os.getcwd(), "data.json")
    with open(path, "r") as file:
        json_data = json.load(file)
        pprint.pprint(json_data)

    ###################################################################################

    # example of pandas usage - saving to csv file DataFrame object
    # here is possible result of emotions recognition
    # photo:https://scontent-frt3-2.cdninstagram.com/v/t51.2885-15/e35/s373x373/42068961_1985555641507878_3030530967165112879_n.jpg?tp=1&_nc_ht=scontent-frt3-2.cdninstagram.com&_nc_cat=106&_nc_ohc=BL5vXu8kh6YAX_IhoaX&edm=ACWDqb8AAAAA&ccb=7-4&oh=4b81d5c537139916e72c56e151f24a4f&oe=609A0A27&_nc_sid=1527a3&ig_cache_key=MTg3Mjc1OTM5NTAxMzQ4OTAyOQ%3D%3D.2-ccb7-4
    emotions = {'additional_properties': {}, 'anger': 0.0, 'contempt': 0.002, 'disgust': 0.0, \
               'fear': 0.0, 'happiness': 0.135, 'neutral': 0.861, 'sadness': 0.001, 'surprise': 0.0}
    emotions.pop('additional_properties')
    emotions = {key: [value] for key, value in emotions.items()}
    df = pd.DataFrame.from_dict(emotions)
    print(df)
    with open("emotions.csv", "w") as file:
        file.write(df.to_csv(index = False))
    print(df.idxmax(axis="columns")[0])
    print(round(df.sum(axis=1)[0], 2))

    ###################################################################################

    # example of matplotlib usage - pie chart
    labels = [key for key in emotions.keys() if emotions[key][0] >= 0.03]
    sizes = [emotions[label][0] for label in labels]
    labels.append("others")
    sizes.append(1-sum(sizes))
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

except Exception as err:
    print(err)
