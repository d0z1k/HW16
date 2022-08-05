import json

from config import app
from service import init_db, get_all_users


@app.route('/users', methods=['GET'])
def get_users():
    get_all_users()
    return app.response_class(
        response=json.dumps(get_all_users()),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
