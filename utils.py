import json


def get_candidates(path):
    """
    Загружает список словарей кандидатов из path.json
    :param path: путь до файла path.json
    :return: список словарей кандидатов
    """
    with open(path, "r", encoding="utf-8") as file:
        candidates_list = json.load(file)
        return candidates_list


def get_candidates_info(candidates_list):
    """
    Возвращает информацию о кандидатах
    :param candidates_list: список кандидатов
    :return: Возвращает информацию о кандидатах
    """
    result = "<pre>"
    for candidate in candidates_list:
        result += (
            f"Имя кандидата - {candidate['name']}\n"
            f"Позиция кандидата {candidate['position']}\n"
            f"Навыки через запятую {candidate['skills']}\n\n"
        )
    result += "</pre>"
    return result


def get_candidate_by_id(candidates_list, candidate_id):
    """
    Возвращает словарь кандидата по id
    :param candidates_list: список словарей кандидатов
    :param candidate_id: индификационный номер
    :return: словарь кандидата
    """
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_skills(candidates_list, skill):
    """
    Возвращает новый список словарей кандидатов, по навыку skill
    :param candidates_list: список словарей кандидатов
    :param skill: навык
    :return: новый список словарей кандидатов
    """
    new_candidates_list = []
    for candidate in candidates_list:
        skills_list = candidate['skills'].lower().split(", ")
        if skill.lower() in skills_list:
            new_candidates_list.append(candidate)
    return new_candidates_list
