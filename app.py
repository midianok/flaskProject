from flask import Flask
import markovify

app = Flask(__name__)


class Result(object):
    index = ""
    message = 0

    def __init__(self, index: int, message: str) -> object:
        self.index = index
        self.message = message


@app.route('/treech-general')
@app.route('/treech-general/<int:count>')
def treech_general(count=5):
    strings = []
    for i in range(1, count + 1):
        strings.append({"id": i, "message": treech_general_model.make_sentence(tries=50)})
    return strings


@app.route('/treech-itan')
@app.route('/treech-itan/<int:count>')
def treech_itan(count=5):
    strings = []
    for i in range(1, count + 1):
        strings.append({"id": i, "message": treech_itan_model.make_sentence(tries=50)})
    return strings


with open("treech_general_v2.txt", encoding="utf8") as f:
    text = f.read()
treech_general_model = markovify.Text(text, well_formed=False)


with open("treech_itan_v2.txt", encoding="utf8") as f:
    text = f.read()
treech_itan_model = markovify.Text(text, well_formed=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
