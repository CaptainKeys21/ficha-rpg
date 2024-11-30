from webview import Window

from app.components import Component
from app.components.input import Input
from app.components.fieldset import Fieldset
from app.components.perks import Perks
from app.components.read_only import Readonly
from app.utils.app_data import AppData

class DataMenu(Component):
    _window: Window = None
    def __init__(self, window: Window, data: AppData) -> None:
        self._window = window
        self.__data = data
        self.__inputs: dict[str, Input|Readonly|Perks] = dict()
        self.__data.subscribe(self.__update_inputs)
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

        self.__inputs["name"] = Input(self._window, "name", self.__data["name"], "data-menu")
        self.__inputs["biggerPoints"] = Readonly(self._window, "biggerPoints", self.__data["biggerPoints"], "data-menu")
        self.__inputs["smallerPoints"] = Readonly(self._window, "smallerPoints", self.__data["smallerPoints"], "data-menu")
        perk_group = Fieldset(self._window, "perks", self.__data["perks"], "#data-menu")

        for key, data in self.__data["perks"]["value"].items():
            self.__inputs[key] = Perks(self._window, key, data, perk_group.ida)

        for input in self.__inputs.values():
            if isinstance(input, Input):
                input.add_listener('input', self.__on_input)
                input.add_listener('focusout', self.__on_focus)


    def __on_input(self, evt):
        name = evt['target']['name']
        value = evt['target']['value'] if 'value' in evt['target'] else ""

        input_data = self.__data[name]
        input_data['value'] = value

        setattr(self.__data, name, input_data)

    def __on_focus(self, evt):
        Input.focus = evt['target']['name']
