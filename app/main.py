from flask import Flask
from flask import render_template
from flask import abort

app = Flask(__name__)



from data import Recipe, n_random_sorted, recipe_data

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", recipes=n_random_sorted(n=10))


@app.route("/recipe/<rid>/")
def recipe(rid=None):
    """
    This is the recipe view
    Will display ingredients, steps, and similar recipes with diffs
    """
    if rid is None:
        ValueError("The recipe id is not found.")

    # 404 not found
    if rid not in recipe_data:
        return f"I cannot find a reicpe with id {rid}.", 404

    rec = Recipe(int(rid))
    return render_template(
        "recipe.html", recipe=rec, similar_recs=rec.n_most_similar(n=10)
    )


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
