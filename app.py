from flask import Flask
from dotenv import load_dotenv
import os
import openai
import markovify


app = Flask(__name__)
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class Result(object):
    index = ""
    message = 0

    def __init__(self, index: int, message: str) -> object:
        self.index = index
        self.message = message


@app.route('/gpt/<string:prompt>/')
@app.route('/gpt/<string:prompt>/<int:max_responce_length>')
def get_agro(prompt, max_responce_length=250):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_responce_length
    )
    message = completions.choices[0].text
    return message


@app.route('/treech-general')
def get_one_treech_general():
    return treech_general_model.make_sentence(tries=50)


@app.route('/treech-itan')
def get_one_treech_itan():
    return treech_itan_model.make_sentence(tries=50)


with open("treech_general_v2.txt", encoding="utf8") as f:
    text = f.read()
treech_general_model = markovify.Text(text, well_formed=False)


with open("treech_itan_v2.txt", encoding="utf8") as f:
    text = f.read()
treech_itan_model = markovify.Text(text, well_formed=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
