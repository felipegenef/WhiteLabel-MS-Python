from flask import  Blueprint
from  usecases.User.GetOne.index import  controller

userRoutes = Blueprint('user', __name__,url_prefix="/user")

userRoutes.add_url_rule("/<id>",view_func=controller.handle)

