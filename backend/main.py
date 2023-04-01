from app import app

@app.get('/')
def home():
    return 'home1'


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
