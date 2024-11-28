from webview import Window
import traceback
from types import FunctionType

from app.components import Component

class Input(Component):
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
        self._window.dom.create_element(f'<div id="input-{self.__name}" class="input-container"></div>', self.__parent)
        self._window.dom.create_element(f'<label for="{self.__name}">{self.__data["label"]}:</label>', ".input-container")
        input = self._window.dom.create_element(f'<input name="{self.__name}" type="{self.__data["type"] or "text"}" value="{self.__data["value"] or ""}"/>', ".input-container")

        if self.__name == Input.focus:
            input.focus()

    def add_listener(self, event_name: str, func: FunctionType):
        input = self._window.dom.get_element(f'#input-{self.__name} input')
        if input:
            selected_event = getattr(input.events, event_name)
            selected_event += func
            
            setattr(input.events, event_name, selected_event)
            #input.events.input += func

