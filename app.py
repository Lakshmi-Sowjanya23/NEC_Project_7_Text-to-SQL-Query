from flask import Flask, render_template, request

from grok_generator import generate_sql_and_data
from database_executor import execute_query

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    generated_query = ""
    dataset = []
    results = []
    user_prompt = ""

    if request.method == "POST":

        prompt = request.form["prompt"]
        user_prompt = prompt

        response = generate_sql_and_data(prompt)

        generated_query = response["sql_query"]

        dataset = response["data"]

        table_name = response["table_name"]

        try:
            results = execute_query(
                table_name,
                dataset,
                generated_query
            )
        except Exception as e:
            results = [{"Error": str(e)}]

    return render_template(
    "index.html",
    generated_query=generated_query,
    dataset=dataset,
    results=results,
    user_prompt=user_prompt
)


if __name__ == "__main__":
    app.run(debug=True)