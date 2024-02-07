from Global.Interfaces.Controller import Controller
from useCases.User.GetOne.Service import GetOneUserService
from flask import  jsonify
from Auth.auth import jwt_required

class GetOneUserController(Controller):
    def __init__(self, service: GetOneUserService):
        self.service = service
    # @jwt_required
    def handle(self,id:str):
        response= self.service.execute(id)
        if response is None:
            return jsonify({"message":"not found"}),404
        return jsonify(vars(response)),200