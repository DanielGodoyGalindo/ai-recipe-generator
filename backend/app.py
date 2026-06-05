from flask import Flask, request, jsonify
from flask_cors import CORS

from dotenv import load_dotenv
from google import genai

import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


@app.route("/generate-recipe", methods=["POST"])
def generate_recipe():

    data = request.get_json()

    ingredients = data.get("ingredients", [])

    prompt = f"""
    Crea una receta completa usando:

    {", ".join(ingredients)}

    Incluye:

    - Nombre de la receta
    - Ingredientes
    - Pasos detallados
    - Tiempo aproximado
    """

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return jsonify({"recipe": response.text})


if __name__ == "__main__":
    app.run(debug=True)
