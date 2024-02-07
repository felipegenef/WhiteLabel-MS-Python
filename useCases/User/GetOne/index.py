
from useCases.User.GetOne.Controller import GetOneUserController
from useCases.User.GetOne.Service import GetOneUserService
from useCases.User.GetOne.Repositories import GetOneUserRepository

repository = GetOneUserRepository()
service = GetOneUserService(repository)
controller = GetOneUserController(service)