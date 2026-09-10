from flask import Flask
from routes.evento import evento_bp
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventos.db"

db.init_app(app)

app.register_blueprint(evento_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, use_reloader=False)