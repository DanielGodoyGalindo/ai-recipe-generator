from flask import Flask, request, jsonify
from flask_cors import CORS
from services.ai_service import generate_recipe

app = Flask(__name__)
CORS(app)  # Permite llamadas desde tu frontend


@app.route("/")
def home():
    return {"message": "API Flask funcionando correctamente"}


@app.route("/generate-recipe", methods=["POST"])
def generate_recipe_endpoint():
    data = request.get_json()

    if not data or "ingredients" not in data:
        return jsonify({"error": "Debes enviar 'ingredients'"}), 400

    ingredients = data["ingredients"]
    ingredientes_texto = ", ".join(ingredients)

    prompt = (
        f"Genera una receta creativa usando estos ingredientes: {ingredientes_texto}"
    )
    receta = generate_recipe(prompt)

    return jsonify({"recipe": receta})


if __name__ == "__main__":
    app.run(debug=True)
