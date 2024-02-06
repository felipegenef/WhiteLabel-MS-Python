import unittest
from unittest.mock import Mock
from usecases.User.GetOne.Service import GetOneUserService


class TestGetOneUser(unittest.TestCase):
    def test_shoudGetAnUser(self):
        repositoryMock = Mock()
        service = GetOneUserService(repositoryMock)

        # Mock repository method to return some data
        repositoryMock.findOne.return_value = {"id": "123", "name": "John"}

        # Call the execute method
        result = service.execute("123")

        # Assert that the result is what we expect
        self.assertEqual(result, {"id": "123", "name": "John"})
    def test_shoudNotGetAnUser(self):
        repositoryMock = Mock()
        service = GetOneUserService(repositoryMock)

        # Mock repository method to return some data
        repositoryMock.findOne.return_value = {"id": "123", "name": "John"}

        # Call the execute method
        result = service.execute("123")

        # Assert that the result is what we expect
        self.assertNotEqual(result, {"id": "122", "name": "John"})

if __name__ == '__main__':
    unittest.main()