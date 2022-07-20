import sqlite3
import flask
import json

app = flask.Flask(__name__)


def get_by_index(index):
    with sqlite3.connect("animal.db") as conn:
        conn.row_factory = sqlite3.Row
        result = conn.execute(f'''Select name, animal_type, breed, date_of_birth, color1, color2, outcome_type 
                        FROM my_table
                        JOIN animal_type
                        JOIN color
                        JOIN breeds
                        JOIN outcome_type
                        JOIN outcome_subtype
                        WHERE "index" = {index}''').fetchone()

        return dict(result)


@app.get('/<itemid>')
def response(itemid):
    return app.response_class(response=
                              json.dumps(get_by_index(itemid),ensure_ascii=False),
                              status=200,
                              mimetype='application/json')


if __name__ == '__main__':
    app.run()