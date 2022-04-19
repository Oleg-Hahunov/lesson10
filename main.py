import json

from flask import Flask, jsonify

app = Flask(__name__)


def read_json():  # считывание джейсон файла с базой кандидатов


    with open('candidate.json', 'r', encoding="utf8") as File:
        return json.load(File)


@app.route("/")
def profile():  # основной список кандидатов
    temp = read_json()
    candidate = f'<pre>\n'
    for i in range(len(temp)):
        candidate += f'Имя кандидата - {temp[i]["name"]}\n'
        candidate += f'позиция кандидата - {temp[i]["position"]}\n'
        candidate += f'Навыки - {temp[i]["skills"]}\n'
        candidate += f'\n<pre>'
    return candidate


@app.route('/candidates/<int:id>')
def personal_page(id):# модуль возвращает информацию о каждом кандидате с аватаркой
    temp = read_json()
    personal_p = f'<img src= "{temp[id - 1]["picture"]}"\n>'
    personal_p += f'<pre>\n'
    personal_p += f'Имя кандидата - {temp[id - 1]["name"]}\n'
    personal_p += f'позиция кандидата - {temp[id - 1]["position"]}\n'
    personal_p += f'Навыки - {temp[id - 1]["skills"]}\n'
    personal_p += f'\n<pre>'
    return personal_p


@app.route('/skills/<skills>')
def search_skills(skills): # модуль возвращает список кандидатов подходящих по указанному навыку
    temp = read_json()
    candidate = f'<pre>\n'
    for i in range(len(temp)):
        skills_temp = temp[i]['skills']
        skills_temp.split(', ')
        if skills in skills_temp:
            candidate += f'Имя кандидата - {temp[i]["name"]}\n'
            candidate += f'позиция кандидата - {temp[i]["position"]}\n'
            candidate += f'Навыки - {temp[i]["skills"]}\n<pre>'
    return candidate


app.run()
