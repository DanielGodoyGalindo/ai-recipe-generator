import { useState } from "react";

export default function RecipeForm() {
    const [ingredients, setIngredients] = useState("");
    const [recipe, setRecipe] = useState("");
    const [loading, setLoading] = useState(false);

    const handleGenerate = async () => {
        if (!ingredients.trim()) {
            alert("Introduce al menos un ingrediente");
            return;
        }

        try {
            setLoading(true);

            const response = await fetch(
                "http://localhost:5000/generate-recipe",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        ingredients: ingredients
                            .split(",")
                            .map((item) => item.trim()),
                    }),
                }
            );

            const data = await response.json();

            setRecipe(data.recipe);
        } catch (error) {
            console.error(error);
            setRecipe("Error al generar la receta");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ maxWidth: "800px", margin: "0 auto", padding: "2rem" }}>
            <h1>🍳 Generador de Recetas con IA</h1>

            <p>
                Escribe ingredientes separados por comas.
            </p>

            <input
                type="text"
                value={ingredients}
                onChange={(e) => setIngredients(e.target.value)}
                placeholder="pollo, arroz, cebolla"
                style={{
                    width: "100%",
                    padding: "12px",
                    marginBottom: "1rem",
                }}
            />

            <button onClick={handleGenerate}>
                Generar receta
            </button>

            {loading && (
                <p>Generando receta...</p>
            )}

            {recipe && (
                <div
                    style={{
                        marginTop: "2rem",
                        textAlign: "left",
                        whiteSpace: "pre-wrap",
                    }}
                >
                    <h2>Receta</h2>
                    <p>{recipe}</p>
                </div>
            )}
        </div>
    );
}