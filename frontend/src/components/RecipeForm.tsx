import { useState } from "react";
import styles from "./RecipeForm.module.css";

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
                "https://ai-recipe-generator-9deg.onrender.com",
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
        <div className={styles.pageWrapper}>
            <div className={styles.container}>

                <h1>🤖 Generador de Recetas 👨‍🍳</h1>

                <p>Dime que ingredientes tienes en la nevera y te diré que recetas puedes preparar:</p>

                <input
                    type="text"
                    value={ingredients}
                    onChange={(e) => setIngredients(e.target.value)}
                    placeholder="pollo, arroz, cebolla"
                    className={styles.input}
                />

                <button onClick={handleGenerate}>Generar receta</button>

                {loading && (<p>Generando receta...</p>)}

                {recipe && (
                    <div className={styles.recipeBox}>
                        <h2>Receta</h2>
                        <p>{recipe}</p>
                    </div>
                )}
            </div>
        </div>
    );
}