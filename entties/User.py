from datetime import datetime

class User:
    def __init__(self, id:str,name:str,createdAt:datetime,updatedAt:datetime,deletedAt:datetime,):
        self.id = id
        self.name=name
        self.createdAt=createdAt
        self.updatedAt=updatedAt
        self.deletedAt=deletedAt