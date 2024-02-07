from useCases.User.GetOne.DTO import UserDTO
from data.database import User

class GetOneUserRepository:
    def findOne(self,id:str):
        try:
            userFound=User.get_by_id(id)
            user=UserDTO(userFound.id,userFound.name)
            return user
        except:
            return None