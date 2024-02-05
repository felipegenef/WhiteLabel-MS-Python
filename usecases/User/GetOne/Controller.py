from Global.Interfaces.Controller import Controller
from usecases.User.GetOne.Service import GetOneUserService
from flask import  jsonify

class GetOneUserController(Controller):
    def __init__(self, service: GetOneUserService):
        self.service = service
    def handle(self,id:str):
        response= self.service.execute(id)
        if response is None:
            return jsonify({"message":"not found"}),404
        return jsonify(vars(response)),200