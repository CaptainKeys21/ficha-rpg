from webview import Window
import traceback
from types import FunctionType

from app.components import Component

class Readonly(Component):
    _window: Window = None
    focus = None
    def __init__(self, window: Window, name: str, data: dict, parent: str) -> None:
        self._window = window
        self.__data = data
        self.__name = name
        self.__parent = parent
        self._render()

    # def __del__(self):
    #     input = self._window.dom.get_element(f'#input-{self.__name}')
    #     if input:
    #         input.remove()

    def _render(self):
        self._window.dom.create_element(f'<div id="readonly-{self.__name}" class="readonly-container"></div>', self.__parent)
        self._window.dom.create_element(f'<span>{self.__data["label"]}: {self.__data["value"]}</span>', ".readonly-container")

