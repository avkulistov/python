import csv
import requests

API_KEY = 'fcfb46b7fcfb46b7fcfb46b7a8fc8adc01ffcfbfcfb46b7a2561a8932ac93087f789fd2'
URL_API = 'https://api.vk.com/method/'
URL_WALL_GET = URL_API + 'wall.get'
VERSION = 5.103
DOMAIN = 'newslabru'


def get_publications(max_posts):
    count = 100
    offset = 0
    all_posts = []

    if max_posts < count:
        count = max_posts
    while offset < max_posts:
        params = {
            'access_token': API_KEY,
            'v': VERSION,
            'domain': DOMAIN,
            'count': count,
            'offset': offset
        }
        response = requests.get(URL_WALL_GET, params=params)
        if response.status_code != 200:
            raise Exception('Ошибка запроса')
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(posts):
    with open('posts.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(('likes', 'body', 'url'))
        for post in posts:
            try:
                img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
            except:
                img_url = 'none'
            writer.writerow((post['likes']['count'], post['text'], img_url))


all_posts = get_publications(200)
file_writer(all_posts)
