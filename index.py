from flask import Flask, Blueprint
from routes import user


app = Flask(__name__)
api = Blueprint('app', __name__, url_prefix="/py/api")

api.register_blueprint(user.userRoutes)
app.register_blueprint(api)

if __name__ == "__main__":

    app.run(port=8080)