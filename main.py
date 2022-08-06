import json
from flask import request
from config import app
from service import init_db, get_all_users, get_all_orders, get_all_offers, put_user_data


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        get_all_users()
        return app.response_class(
            response=json.dumps(get_all_users()),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            put_user_data(request.json)
        elif isinstance(request.json, dict):
            put_user_data([request.json])

    return app.response_class(
            response=json.dumps(request.json),
            status=200,
            mimetype='application/json'
            )


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = get_all_users()
    for row in data:
        if row.get('id') == user_id:
            return app.response_class(
                response=json.dumps(row),
                status=200,
                mimetype='application/json'
            )


@app.route('/orders', methods=['GET'])
def get_orders():
    get_all_orders()
    return app.response_class(
        response=json.dumps(get_all_orders()),
        status=200,
        mimetype='application/json'
    )


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    data = get_all_orders()
    for row in data:
        if row.get('id') == order_id:
            return app.response_class(
                response=json.dumps(row),
                status=200,
                mimetype='application/json'
            )


@app.route('/offers', methods=['GET'])
def get_offers():
    get_all_offers()
    return app.response_class(
        response=json.dumps(get_all_offers()),
        status=200,
        mimetype='application/json'
    )


@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    data = get_all_offers()
    for row in data:
        if row.get('id') == offer_id:
            return app.response_class(
                response=json.dumps(row),
                status=200,
                mimetype='application/json'
            )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
