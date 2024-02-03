from usecases.User.GetOne.DTO import UserDTO

class GetOneUserRepository:
    def findOne(self,id:str):
        user=UserDTO(id,"Jhon")
        return user