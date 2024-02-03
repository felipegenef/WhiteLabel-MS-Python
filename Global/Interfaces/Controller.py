import abc


class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handle(self, input):
        return NotImplementedError()