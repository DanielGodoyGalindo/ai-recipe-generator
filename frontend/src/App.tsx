import RecipeForm from "./components/RecipeForm";

function App() {
    return (
        <div style={appStyle}>
                <RecipeForm />
            <footer style={footerStyle}>
                <p> Made with ❤️ by{" "} <a href="http://github.com/DanielGodoyGalindo" target="_blank" rel="noopener noreferrer" style={{ color: "#646cff", fontWeight: "bold" }}>Daniel Godoy</a></p>
            </footer>
        </div>
    );
}

const footerStyle: React.CSSProperties = {
    margin: "10px",
    textAlign: "center",
    fontSize: "14px",
    color: "#888",
};

const appStyle: React.CSSProperties = {
    display: "flex",
    flexDirection: "column",
    minHeight: "100vh",
}

export default App;