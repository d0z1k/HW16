import json

from models import *
from config import db


def put_user_data(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get('id'),
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                age=row.get('age'),
                email=row.get('email'),
                role=row.get('role'),
                phone=row.get('phone')
            )
        )

    db.session.commit()


def put_order_data(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get('id'),
                name=row.get('name'),
                description=row.get('description'),
                start_date=row.get('start_date'),
                end_date=row.get('end_date'),
                address=row.get('address'),
                price=row.get('price'),
                customer_id=row.get('customer_id'),
                executor_id=row.get('executor_id')
            )
        )

    db.session.commit()


def put_offer_data(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get('id'),
                order_id=row.get('order_id'),
                executor_id=row.get('executor_id')
            )
        )

    db.session.commit()


def get_all_users():
    result = []
    for row in User.query.all():
        result.append(row.to_dict())
    return result


def get_all_orders():
    result = []
    for row in Order.query.all():
        result.append(row.to_dict())
    return result


def get_all_offers():
    result = []
    for row in Offer.query.all():
        result.append(row.to_dict())
    return result


def init_db():
    db.drop_all()
    db.create_all()
    with open("data/Users.json", encoding='utf-8') as file:
        data = json.load(file)
        put_user_data(data)

    with open("data/Orders.json", encoding='utf-8') as file:
        data = json.load(file)
        put_order_data(data)

    with open("data/Offers.json") as file:
        data = json.load(file)
        put_offer_data(data)


def update_user(model, user_id, values):
    try:
        data = db.session.query(model).get(user_id)
        data.id = values.get('id')
        data.first_name = values.get('first_name')
        data.last_name = values.get('last_name')
        data.age = values.get('age')
        data.email = values.get('email')
        data.role = values.get('role')
        data.phone = values.get('phone')

        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def update_order(model, order_id, values):
    try:
        data = db.session.query(model).get(order_id)
        data.id = values.get('id')
        data.name = values.get('name')
        data.description = values.get('description')
        data.start_date = values.get('start_date')
        data.end_date = values.get('end_date')
        data.address = values.get('address')
        data.price = values.get('price')
        data.customer_id = values.get('customer_id')
        data.executor_id = values.get('executor_id')

        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def update_offer(model, offer_id, values):
    try:
        data = db.session.query(model).get(offer_id)
        data.id = values.get('id')
        data.id = values.get('id')
        data.order_id = values.get('order_id')
        data.executor_id = values.get('executor_id')

        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_user(model, user_id):
    try:
        db.session.query(model).filter(model.id == user_id).delete()

        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_order(model, order_id):
    try:
        db.session.query(model).filter(model.id == order_id).delete()

        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_offer(model, offer_id):
    try:
        db.session.query(model).filter(model.id == offer_id).delete()

        db.session.commit()
    except Exception as e:
        print(e)
        return {}
