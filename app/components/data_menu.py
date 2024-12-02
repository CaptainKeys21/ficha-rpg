from webview import Window
from app.components import Component
from app.components.input import Input
from app.components.fieldset import Fieldset
from app.components.perks import Perk
from app.components.read_only import Readonly
from app.utils.app_data import AppData

class DataMenu(Component):
    _window: Window = None
    def __init__(self, window: Window, data: AppData) -> None:
        self._window = window
        self.__data = data
        self.__inputs: dict[str, Input|Readonly|Perk] = dict()
        self.__save_listeners = []
        self.__cancel_listeners = []
        self._render()

    def __del__(self):
        menu = self._window.dom.get_element('#data-menu')
        if menu:
            menu.remove()

    @property
    def filename(self):
        return self.__data["name"]["value"].replace(" ", "_") + ".json"

    @property
    def window(self):
        return self._window

    def _render(self):
        self._window.dom.create_element('<div id="data-menu"></div>', '#app')

        self.__inputs["name"] = Input(self._window, "name", self.__data["name"], "#data-menu")

        self.__inputs["biggerPoints"] = Readonly(self._window, "biggerPoints", self.__data["biggerPoints"], "#data-menu")
        self.__inputs["smallerPoints"] = Readonly(self._window, "smallerPoints", self.__data["smallerPoints"], "#data-menu")
        perk_group = Fieldset(self._window, "perks", self.__data["perks"], "#data-menu")

        for key, _ in self.__data["perks"]["value"].items():
            perk = Perk(self._window, key, self.__data["perks"]["value"][key], perk_group.id)
            perk.add_listener('input', self.__on_perk_change)
            perk.add_subperks_listener('input', self.__on_subperk_change)
            self.__inputs[key] = perk

        buttonTray = self._window.dom.create_element('<div class="button-tray"></div>', "#data-menu")

        cancelBtn = self._window.dom.create_element('<button id="btn-cancel">Cancelar</button>', buttonTray)
        cancelBtn.events.click += self.__on_cancel

        saveBtn = self._window.dom.create_element('<button id="btn-save">Salvar</button>', buttonTray)
        saveBtn.events.click += self.__on_save

    def __on_input(self, evt):
        name = evt['target']['name']
        value = evt['target']['value'] if 'value' in evt['target'] else ""

        input_data = self.__data[name]
        input_data['value'] = value

        setattr(self.__data, name, input_data)

    def __on_perk_change(self, evt):
        name = evt['target']['name']
        value = evt['target']['value'] if 'value' in evt['target'] else ""

        input_data = self.__data["perks"]
        input_data["value"][name]['value'] = value

        setattr(self.__data, "perks", input_data)

        total_points = 0
        for _, p in self.__data["perks"]["value"].items():
            total_points += int(p['value'])

        perk_data = self.__data["biggerPoints"]
        perk_data["value"] = 20 - total_points

        setattr(self.__data, "biggerPoints", perk_data)

        self.__inputs["biggerPoints"].update(self.__data["biggerPoints"])

    def __on_subperk_change(self, evt):
        name = evt['target']['name']
        perk = evt['target']['attributes']['data-perk']
        value = evt['target']['value'] if 'value' in evt['target'] else ""

        input_data = self.__data["perks"]
        input_data["value"][perk]['subperks'][name]['value'] = value

        setattr(self.__data, "perks", input_data)

        total_points = 0
        for _, p in self.__data["perks"]["value"].items():
            total_points += int(sum([int(sb["value"]) for _, sb in p["subperks"].items()]))

        perk_data = self.__data["smallerPoints"]
        perk_data["value"] = 45 - total_points

        setattr(self.__data, "smallerPoints", perk_data)

        self.__inputs["smallerPoints"].update(self.__data["smallerPoints"])

    def __on_cancel(self, _):
        for func in self.__cancel_listeners:
            func()

    def __on_save(self, _):
        self.__data['name']['value'] = self.__inputs['name'].value

        for func in self.__save_listeners:
            func()

    def add_cancel_listener(self, fn):
        self.__cancel_listeners.append(fn)

    def add_save_listener(self, fn):
        self.__save_listeners.append(fn)