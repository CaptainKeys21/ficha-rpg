from webview import Window
import traceback
from types import FunctionType

from app.components import Component
from app.components.input import Input

class Perk(Component):
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
        self._window.dom.create_element(f'<div id="input-{self.__name}" class="input-container"></div>', f"#perk-{self.__name}")
        self._window.dom.create_element(f'<label for="{self.__name}">{self.__data["label"]}:</label>', f"#input-{self.__name}")
        self._window.dom.create_element(f'<input name="{self.__name}" type="number" value="{self.__data["value"]}"/>', f"#input-{self.__name}")

        if "subperks" in self.__data:
            self._window.dom.create_element(f'<div id="{self.__name}-subperks" class="subperk-container"></div>', f"#perk-{self.__name}")
            for key, value in self.__data['subperks'].items():
                input = Input(self._window, key, value, f"#{self.__name}-subperks", [f'data-perk="{self.__name}"'])

                self.__subperks[key] = input


    def add_listener(self, event_name: str, func: FunctionType):
        input = self._window.dom.get_element(f'#perk-{self.__name} input')
        if input:
            selected_event = getattr(input.events, event_name)
            selected_event += func
            
            setattr(input.events, event_name, selected_event)

    def add_subperks_listener(self, event_name: str, func: FunctionType):
        for _, input in self.__subperks.items():
            input.add_listener(event_name, func)