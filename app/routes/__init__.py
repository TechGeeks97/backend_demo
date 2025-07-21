from flask import Blueprint
from app.routes.course import course_bp
from app.routes.order import order_bp
from app.routes.style import style_bp

api_bp = Blueprint("api", __name__)

api_bp.register_blueprint(course_bp, url_prefix="/api")
api_bp.register_blueprint(order_bp, url_prefix="/api")
api_bp.register_blueprint(style_bp, url_prefix="/api")
