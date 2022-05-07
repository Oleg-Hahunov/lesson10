from flask import Flask, render_template
import untils

app = Flask(__name__)


@app.route("/")
def list_candidates():
    candidates = untils.load_cadidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


# @app.route("/candidate/<int:candidate_id>")
# def page_candidate(candidate_id):
#     candidate = untils.get_candidate(candidate_id)
#     return render_template("card.html", candidate=candidate)
#

app.run()
