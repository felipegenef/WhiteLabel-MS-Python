import os

def capitalizeFirstLetter(word):
    if not word:
        return word
    return word[0].upper() + word[1:]

domainName = input("What's the domain name? ")
useCaseName = input("What's the useCase name? ")

useCasesPath = "./useCases"
domainPath = os.path.join(useCasesPath, domainName)
useCasePath = os.path.join(useCasesPath, domainName, useCaseName)

# Crie a pasta ./useCases se não existir
if not os.path.exists(useCasesPath):
    os.mkdir(useCasesPath)

# Crie a pasta ./useCases/domainName se não existir
if not os.path.exists(domainPath):
    os.mkdir(domainPath)

os.mkdir(useCasePath)

# Crie os arquivos dentro da pasta do domainName
with open(os.path.join(useCasePath, "Controller.py"), "w") as f:
    f.write("""            
from Global.Interfaces.Controller import Controller
from useCases.{0}.{1}.Service import {1}Service
from flask import  jsonify
from Auth.auth import jwt_required

class {1}Controller(Controller):
    def __init__(self, service: {1}Service):
        self.service = service
    # @jwt_required
    def handle(self):
        response= self.service.execute()
        if response is None:
            return jsonify({{"message":"not found"}}),404
        return jsonify(vars(response)),200
""".format(capitalizeFirstLetter(domainName), capitalizeFirstLetter(useCaseName)))

with open(os.path.join(useCasePath, "Service.py"), "w") as f:
    f.write("""        
from Global.Interfaces.Service import Service
from useCases.{0}.{1}.Repositories import {1}Repository

class {1}Service(Service):
    def __init__(self, repository: {1}Repository):
        self.repository = repository

    def execute(self,id:str):
        data = self.repository.findOne(id)
        return data
""".format(capitalizeFirstLetter(domainName), capitalizeFirstLetter(useCaseName)))

with open(os.path.join(useCasePath, "DTOs.py"), "w") as f:
    f.write("""
class DTO:
    def __init__(self, id: str):
        self.id = id
""")

with open(os.path.join(useCasePath, "Repositories.py"), "w") as f:
    f.write("""
from useCases.{0}.{1}.DTOs import DTO
#from data.database import {1}

class {1}Repository:
    def findOne(self, id:str):
        try:
            #entityFound = {1}.get_by_id(id)
            entity = DTO(id, "Jhon")
            return entity
        except:
            return None
""".format(capitalizeFirstLetter(domainName), capitalizeFirstLetter(useCaseName)))

with open(os.path.join(domainPath, "__init__.py"), "w") as f:
    f.write("")

with open(os.path.join(useCasePath, "__init__.py"), "w") as f:
    f.write("")
            
with open(os.path.join(useCasePath, "index.py"), "w") as f:
    f.write("""
from useCases.{0}.{1}.Controller import {1}Controller
from useCases.{0}.{1}.Service import {1}Service
from useCases.{0}.{1}.Repositories import {1}Repository

repository = {1}Repository()
service = {1}Service(repository)
controller = {1}Controller(service)
""".format(capitalizeFirstLetter(domainName), capitalizeFirstLetter(useCaseName)))

with open(os.path.join(useCasePath, "test_useCase.py"), "w") as f:
    f.write("""
import unittest
from unittest.mock import Mock
from useCases.{0}.{1}.Service import {1}Service
from json import dumps, loads

class Test{1}(unittest.TestCase):
    def setUp(self):
        self.repositoryMock = Mock()

    def test_return_when_found(self):
        service = {1}Service(self.repositoryMock)

        # Mock repository method to return some data
        self.repositoryMock.findOne.return_value = {{"id": "123", "name": "John"}}

        # Call the execute method
        result = service.execute("123")

        # Assert that the result is what we expect
        self.assertEqual(result, {{"id": "123", "name": "John"}})

    def test_return_none_when_not_found(self):
        service = {1}Service(self.repositoryMock)

        # Mock repository method to return some data
        self.repositoryMock.findOne.return_value = None

        # Call the execute method
        result = service.execute("123")

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
""".format(capitalizeFirstLetter(domainName), capitalizeFirstLetter(useCaseName)))

print("Finished generating files.")
