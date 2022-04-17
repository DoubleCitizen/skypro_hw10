from flask import Flask

from utils import get_candidates
from utils import get_candidates_info
from utils import get_candidate_by_id
from utils import get_candidates_by_skills

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates_list = get_candidates("candidates.json")
    result = get_candidates_info(candidates_list)
    return result


@app.route("/candidates/<int:id_candidate>")
def page_candidates(id_candidate):
    candidates_list = get_candidates("candidates.json")
    candidate = get_candidate_by_id(candidates_list, id_candidate)
    result = f"<img src={candidate['picture']}>"
    result += get_candidates_info([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates_list = get_candidates("candidates.json")
    candidates_list = get_candidates_by_skills(candidates_list, skill)
    result = get_candidates_info(candidates_list)
    return result


app.run()
