
from usecases.User.GetOne.Controller import GetOneUserController
from usecases.User.GetOne.Service import GetOneUserService
from usecases.User.GetOne.Repositories import GetOneUserRepository

repository = GetOneUserRepository()
service = GetOneUserService(repository)
controller = GetOneUserController(service)