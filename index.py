import pandas as pd
from vk_api import VkApi
import numpy as np


def auth_handler():
    key = input('Enter authentication code: ')
    return key, True


def main(id , password, login, post_count):
    vk_session = VkApi(login, password, auth_handler=auth_handler)
    vk_session.auth()

    vk = vk_session.get_api()

    posts = vk.wall.get(owner_id='-' + id, count= int(post_count))['items']
    posts_text = [post['text'] for post in posts]
    posts_img = []
    for i in range(len(posts)):
        if 'attachments' in posts[i]:
            arr = []
            if posts[i]['attachments'][0]['type'] == 'photo':
                for j in range(len(posts[i]['attachments'])):
                    if posts[i]['attachments'][j]['type'] == 'photo':
                        arr.append(posts[i]['attachments'][j]['photo']['sizes'][0]['url'])
                posts_img.append(arr)
            else:
                posts_img.append(0)
        else: posts_img.append(0)

    return posts_text , posts_img

main('208586567', 'password','login',100)
