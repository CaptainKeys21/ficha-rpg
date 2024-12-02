from webview import Window
import traceback
from types import FunctionType

from app.components import Component

class Input(Component):
    _window: Window = None
    focus = None
    def __init__(self, window: Window, name: str, data: dict, parent: str, custom_data: list[str] = []) -> None:
        self._window = window
        self.__data = data
        self.__name = name
        self.__parent = parent
        self.__custom_data = custom_data
        self._render()

    # def __del__(self):
    #     input = self._window.dom.get_element(f'#input-{self.__name}')
    #     if input:
    #         input.remove()

    @property
    def value(self):
        input = self._window.dom.get_element(f'input[name="{self.__name}"]')
        if input:
            return input.value
        
        return ""

    def _render(self):
        formated_data = ' '.join(self.__custom_data) if len(self.__custom_data) > 0 else ""

        self._window.dom.create_element(f'<div id="input-{self.__name}" class="input-container"></div>', self.__parent)
        self._window.dom.create_element(f'<label for="{self.__name}">{self.__data["label"]}:</label>', f"#input-{self.__name}")
        self._window.dom.create_element(f'<input name="{self.__name}" type="{self.__data["type"] or "text"}" value="{self.__data["value"]}" {formated_data}/>', f"#input-{self.__name}")

    def add_listener(self, event_name: str, func: FunctionType):
        input = self._window.dom.get_element(f'#input-{self.__name} input')
        if input:
            selected_event = getattr(input.events, event_name)
            selected_event += func
            
            setattr(input.events, event_name, selected_event)

