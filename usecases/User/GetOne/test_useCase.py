import unittest
from unittest.mock import Mock
from usecases.User.GetOne.Service import GetOneUserService
from json import dumps,loads

class TestGetOneUser(unittest.TestCase):
    def setUp(self):
        self.repositoryMock=Mock()
    def test_return_user_when_found(self):
        service = GetOneUserService(self.repositoryMock)

        # Mock repository method to return some data
        self.repositoryMock.findOne.return_value = {"id": "123", "name": "John"}

        # Call the execute method
        result = service.execute("123")

        # Assert that the result is what we expect
        self.assertEqual(result, {"id": "123", "name": "John"})
    def test_return_none_when_not_found(self):
        service = GetOneUserService(self.repositoryMock)

        # Mock repository method to return some data
        self.repositoryMock.findOne.return_value = None

        # Call the execute method
        result = service.execute("123")

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()