from webview import Window
import traceback
from types import FunctionType

from app.components import Component
from app.components.input import Input

class Perks(Component):
    _window: Window = None
    focus = None
    def __init__(self, window: Window, name: str, data: dict, parent: str) -> None:
        self._window = window
        self.__data = data
        self.__name = name
        self.__parent = parent
        self.__subperks: dict[str, Input] = dict()
        self._render()

    # def __del__(self):
    #     input = self._window.dom.get_element(f'#input-{self.__name}')
    #     if input:
    #         input.remove()

    def _render(self):
        self._window.dom.create_element(f'<div id="perk-{self.__name}" class="perk-container"></div>', self.__parent)
        self._window.dom.create_element(f'<label for="perk-{self.__name}">{self.__data["label"]}:</label>', ".perk-container")
        self._window.dom.create_element(f'<input name="{self.__name}" type="{self.__data["type"] or "text"}" value="{self.__data["value"] or ""}"/>', ".perk-container")

        if "subperks" in self.__data:
            self._window.dom.create_element(f'<div id="subperk-{self.__name}" class="subperk-container"></div>', ".perk-container")
            for key, value in self.__data['subperks'].items():
                self.__subperks[key] = Input(self._window, key, value, f"#subperk-{self.__name}")


