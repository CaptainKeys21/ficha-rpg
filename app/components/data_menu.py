from webview import Window

from app.components import Component
from app.components.input import Input
from app.utils.app_data import AppData

class DataMenu(Component):
    _window: Window = None
    def __init__(self, window: Window, data: AppData) -> None:
        self._window = window
        self.__data = data
        self.__inputs: dict[str, Input] = dict()
        self.__data.subscribe(self.__change_input_rules)
        self._render()

        #self.__data.subscribe(self.__on_data_change)

    def __del__(self):
        menu = self._window.dom.get_element('#data-menu')
        if menu:
            menu.remove()

    @property
    def window(self):
        return self._window

    def _render(self):
        self.__del__()
        self._window.dom.create_element('<div id="data-menu"></div>', '#app')

        for key, data in vars(self.__data).items():
            input = Input(self._window, key, data, "#data-menu")
            input.add_listener('input', self.__on_input)
            input.add_listener('focus', self.__on_focus)

            self.__inputs[key] = input

        btn = self._window.dom.create_element('<button id="new-field">Novo Campo</button>', '#data-menu')

    def __change_input_rules(self, old, new):
        print(old, new)

    def __on_input(self, evt):
        name = evt['target']['name']
        value = evt['target']['value'] if 'value' in evt['target'] else ""

        input_data = self.__data[name]
        input_data['value'] = value

        setattr(self.__data, name, input_data)

    def __on_focus(self, evt):
        Input.focus = evt['target']['name']

    def rerender(self):
        self.__del__()
        self._render()
