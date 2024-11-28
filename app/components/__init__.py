from abc import ABC, abstractmethod
class Component(ABC):

    @property
    @abstractmethod
    def _window(self):
        pass
    
    @abstractmethod
    def _render(self):
        pass