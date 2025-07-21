from flask import Blueprint, request, jsonify
from app.controllers.course_controller import (
    save_user_profile, get_user_profile,
    save_learning_goals, get_learning_goals,
    save_feedback, get_feedback,get_full_user_context
)

course_bp = Blueprint("course_bp", __name__)

@course_bp.route("/user-profile", methods=["POST"])
def user_profile():
    data = request.json
    email = data.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400
    save_user_profile(email, data)
    return jsonify({"message": "User profile saved"}), 200

@course_bp.route("/user-profile/<email>", methods=["GET"])
def get_user_profile_route(email):
    profile = get_full_user_context(email)
    if profile:
        return jsonify(profile), 200
    return jsonify({"error": "User profile not found"}), 404

@course_bp.route("/goals", methods=["POST"])
def goals():
    data = request.json
    email = data.get("email")
    goals = data.get("goals")
    if not email or goals is None:
        return jsonify({"error": "Email and goals are required"}), 400
    save_learning_goals(email, goals)
    return jsonify({"message": "Goals updated"}), 200

@course_bp.route("/goals/<email>", methods=["GET"])
def get_goals_route(email):
    goals = get_learning_goals(email)
    if goals:
        return jsonify(goals), 200
    return jsonify({"error": "Learning goals not found"}), 404

@course_bp.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    email = data.get("email")
    feedback_data = data.get("feedback")
    if not email or feedback_data is None:
        return jsonify({"error": "Email and feedback are required"}), 400
    save_feedback(email, feedback_data)
    return jsonify({"message": "Feedback saved"}), 200

@course_bp.route("/feedback/<email>", methods=["GET"])
def get_feedback_route(email):
    feedback_data = get_feedback(email)
    if feedback_data:
        return jsonify(feedback_data), 200
    return jsonify({"error": "Feedback not found"}), 404
