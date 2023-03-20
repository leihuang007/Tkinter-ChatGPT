import openai

import socket
import socks
import pickle
import time

from sseclient import SSEClient

OPENAI_API_KEY = pickle.load(open("./api_key", 'rb'))
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9988)
socket.socket = socks.socksocket

openai.api_key = OPENAI_API_KEY


def get_response(messages: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        # stream=True,
        max_tokens=3000,
        # top_p=0,
        # frequency_penalty=0.5,
        # presence_penalty=0.0
    )
    return(response)

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
    # response = get_image('木匠在满是烟尘的工作室中认真工作。卡通风格，要有科幻的效果。')
    # print(response)
    messages = [{
        "role": "system", "content": "You are a helpful assiatant who can help me write appealing emails for KOL.",
        "role": "user", "content": """Help me rewrite this email:'
        Hello there,

I hope this email finds you doing well.

It's Thursday and I wanted to reach out to you after coming across your social media account recently. Your content has truly caught my eye and I am absolutely obsessed with it!

I am writing to you on behalf of the Influencer Marketing team at Cupshe, which is a brand that primarily focuses on beachwear but also expands to clothing and accessories. I must say that your style is all about real women and real bodies, and we admire that authenticity as it aligns perfectly with Cupshe's concept.

We would love to explore the possibility of collaborating with you on social media. Please let me know if you are interested in working together.

Best regards,
        '"""
    }]
    

    # print(response['choices'][0]['message']['content'])
    with open('./cupshe-short.txt',"a") as f:
        for i in range(1):
            time.sleep(5)
            try:
                response = get_response(messages)
            except openai.error.RateLimitError as e:
                print("RateLimitError")
                time.sleep(10)
            print(f"Running {i}")
            f.write('--'*5+f"Template {i}"+'--'*5)
            f.write(response['choices'][0]['message']['content'])
            f.write('\n\n')
