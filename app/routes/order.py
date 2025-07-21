from flask import Blueprint, request, jsonify
from app.controllers.order_controller import (
    save_order, get_order,
    save_client_preferences, get_client_preferences,
    get_full_order_by_order_id,get_all_orders_by_email
)

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/order", methods=["POST"])
def order():
    data = request.json
    order_id = data.get("order_id")
    order_data = data.get("order")
    email = data.get("email") 

    if not order_id or order_data is None:
        return jsonify({"error": "order_id and order data are required"}), 400

    save_order(order_id, order_data,email)
    return jsonify({"message": "Order saved"}), 200

@order_bp.route("/order/<order_id>", methods=["GET"])
def get_order(order_id):
    data = get_full_order_by_order_id(order_id)
    if not data:
      return jsonify({"error": "Order not found"}), 404
    return jsonify(data), 200

@order_bp.route("/order/user/<email>", methods=["GET"])
def get_orders_by_email_route(email):
    orders = get_all_orders_by_email(email)

    if not orders:
        return jsonify({"error": "No orders found for this user"}), 404

    return jsonify({
        "email": email,
        "orders": orders
    }), 200


@order_bp.route("/client-preferences", methods=["POST"])
def client_preferences():
    data = request.json
    order_id = data.get("order_id")
    preferences = data.get("preferences")
    email = data.get("email")

    if not order_id or preferences is None:
        return jsonify({"error": "order_id and preferences are required"}), 400

    save_client_preferences(order_id, preferences,email)
    return jsonify({"message": "Preferences saved"}), 200

@order_bp.route("/client-preferences/<order_id>", methods=["GET"])
def get_client_preferences_route(order_id):
    preferences = get_client_preferences(order_id)
    if preferences:
        return jsonify(preferences), 200
    return jsonify({"error": "Client preferences not found"}), 404


@order_bp.route("/order-context/<order_id>", methods=["GET"])
def get_full_order_context_route(order_id):
    context = get_full_order_context(order_id)
    if context:
        return jsonify(context), 200
    return jsonify({"error": "Order context not found"}), 404
