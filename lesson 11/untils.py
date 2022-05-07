import json



def load_cadidates_from_json(path):
    with open(path, "r", encoding='UTF-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    with open('candidates.json', encoding='UTF-8') as File:
        candidates = json.load(File)
    return candidates[candidate_id - 1]


def candidates_by_name(candidate_name):
    with open('candidates.json', encoding='UTF-8') as File:
        candidates = json.load(File)
    for i in candidates:
        if candidate_name in i['name']:
            return i

def candidates_by_skill(skill_name):
    with open('candidates.json', encoding='UTF-8') as File:
        candidates = json.load(File)
    for i in candidates:
        if skill_name in i['skills']:
            return i
