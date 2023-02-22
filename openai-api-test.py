import openai

import socket
import socks
import pickle

from sseclient import SSEClient

OPENAI_API_KEY = pickle.load(open("./api_key", 'rb'))
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9966)
socket.socket = socks.socksocket

openai.api_key = OPENAI_API_KEY


def get_response(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        stream=True,
        max_tokens=3000,
        top_p=0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    print(response)

def get_response_sse(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        stream=True,
        max_tokens=3000,
        top_p=0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response

def get_image(prompt:str):
    response = openai.Image.create(
        prompt=prompt,
        size='256x256',
        response_format = 'url'
    )
    return response

if __name__ == '__main__':
    # message = get_response_sse('生成一幅图片，小黄人蹦在半空中。')
    # for msg in message:
    #     print(msg['choices'][0]['text'], end='')
    response = get_image('木匠在满是烟尘的工作室中认真工作。卡通风格，要有科幻的效果。')
    print(response)
