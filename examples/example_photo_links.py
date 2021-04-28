"""
The module example of getting pictures urls with rapid api.
"""
import requests


if __name__ == "__main__":
    try:
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

        urls = []
        for post in response.json()['body']['items']:
            urls.append(post['image_versions2']['candidates'][0]['url'])

        print(urls)

    except Exception:
        print('Oops, something went wrong(')
