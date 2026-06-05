from flask import Blueprint, request, jsonify
from services.ai_service import generate_recipe

bp = Blueprint("recetas", __name__)


@bp.route("/receta", methods=["GET"])
def receta():
    ingredientes = request.args.get("ingredientes", "")
    prompt = f"Genera una receta creativa usando estos ingredientes: {ingredientes}"
    receta = generate_recipe(prompt)
    return jsonify({"receta": receta})
