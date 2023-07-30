from app import create_app

app = create_app()
app.run(debug=True)  # Only for debug

if __name__ == "__main__":
    app.run(debug=True)
