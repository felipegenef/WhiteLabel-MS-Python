from Global.Interfaces.Service import Service
from usecases.User.GetOne.Repositories import GetOneUserRepository


class GetOneUserService(Service):
    def __init__(self, respository: GetOneUserRepository):
        self.respository = respository
    def execute(self,id:str):
        data=self.respository.findOne(id)
        return data