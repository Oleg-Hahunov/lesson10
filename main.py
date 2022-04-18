import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def profile():
    candidate = f'<pre>\n'
    with open('candidate.json', 'r', encoding="utf8") as File:
        temp = json.load(File)
        for i in range(len(temp)):
            candidate += f'Имя кандидата - {temp[i]["name"]}\n'
            candidate += f'позиция кандидата - {temp[i]["position"]}\n'
            candidate += f'Навыки - {temp[i]["skills"]}\n'
            candidate += f'\n'

    return candidate + '<pre>'


@app.route('/candidates/<int:id>')
def personal_page(id):
    with open('candidate.json', 'r', encoding="utf8") as File:
        temp = json.load(File)
        personal_p = f'<img src= "{temp[id - 1]["picture"]}"\n>'
        personal_p += f'<pre>\n'
        personal_p += f'Имя кандидата - {temp[id - 1]["name"]}\n'
        personal_p += f'позиция кандидата - {temp[id - 1]["position"]}\n'
        personal_p += f'Навыки - {temp[id - 1]["skills"]}\n'
        personal_p += f'\n'

    return personal_p + '<pre>'


@app.route('/skills/<str:skills>')
def search_skills():
    with open('candidate.json', 'r', encoding="utf8") as File:
        temp = json.load(File)
        candidate = f'<pre>\n'
    for i in range(len(temp)):
        if skills in temp[i]['skills']:
            candidate += f'Имя кандидата - {temp[i]["name"]}\n'
            candidate += f'позиция кандидата - {temp[i]["position"]}\n'
            candidate += f'Навыки - {temp[i]["skills"]}\n'
        return candidate + '<pre>'


app.run()

#
# temp[i].pop('id')
# temp[i].pop('picture')
# temp[i].pop('gender')
# temp[i].pop('age')
# temp[i]['name'] = 'Имя кандидата - ' + temp[i]['name']
# temp[i]['position'] = 'позиция кандидата -' + temp[i]['position']
