from models import (
    model_user,
    model_user_order,
    model_user_review,
    model_user_order_details,
)


def controller_user(id):
    return model_user(id)


def controller_user_order(id):
    return model_user_order(id)


def controller_user_review(id):
    return model_user_review(id)


def controller_user_order_details(id, order_id):
    return model_user_order_details(id, order_id)
