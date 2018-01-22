# -*- coding:utf-8 -*-

import argparse
import json

import utils
from aip.speech import AipSpeech

api_cofig = utils.load_baidu_api_config()
aip_speech = AipSpeech(api_cofig['appId'], api_cofig['apiKey'], api_cofig['secretKey'])

def synthesis(text, output_file):
    speech = aip_speech.synthesis(
        text, options={
            'vol': 15,
            'per': 2,
            'pit': 7,
            'spd': 5
        })

    f = open(output_file, 'w')
    f.write(speech)
    f.close()

def main(output_dir):
    news = utils.load_news()
    audio_list = []

    for item in news:
        text = item['text']
        title = item['title']

        print 'title: ', title

        output_file = '%s/%s.mp3' % (output_dir, title)
        synthesis('%s \n %s' % (title, text), output_file)

        audio = {}
        audio['title'] = title
        audio['author'] = 'Audiohub'
        audio['url'] = '.%s/%s.mp3' % (output_dir, title)
        audio['pic'] = './images/logo.jpg'
        audio_list.append(audio)

    with open(utils.AUDIO_FILE, 'w') as f:
        f.write(json.dumps(audio_list, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str)

    args = parser.parse_args()

    print args

    main(args.output_dir)

