from flask import Blueprint, request, jsonify
from app.controllers.style_controller import (
    save_style,
    save_weather,
    save_occasion,
    get_user_style_profile
  
)

style_bp = Blueprint("style_bp", __name__)


@style_bp.route("/style", methods=["POST"])
def style():
    data = request.json
    save_style(data["email"], data["style"])
    return jsonify({"message": "Style saved"}), 200


@style_bp.route("/weather", methods=["POST"])
def weather():
    data = request.json
    save_weather(data["email"], data["weather"])
    return jsonify({"message": "Weather saved"}), 200


@style_bp.route("/occasion", methods=["POST"])
def occasion():
    data = request.json
    save_occasion(data["email"], data["occasion"])
    return jsonify({"message": "Occasion saved"}), 200

@style_bp.route("/style-profile/<email>", methods=["GET"])
def get_style_profile_route(email):
    profile = get_user_style_profile(email)
    
    if not profile:
        return jsonify({"error": "Style profile not found"}), 404

    return jsonify(profile), 200