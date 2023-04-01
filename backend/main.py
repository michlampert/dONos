from app import app

from donos.views import views

app.register_blueprint(views)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
