from flask import Flask, render_template

from database import db
from views import views
from sso_views import sso_views

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = "averylongsecretkey"

db.init_app(app)

app.register_blueprint(views)
app.register_blueprint(sso_views)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
