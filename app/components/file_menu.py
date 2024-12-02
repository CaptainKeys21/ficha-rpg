from webview import Window
from types import FunctionType
from app.components import Component

class FileMenu(Component):
    _window: Window = None
    def __init__(self, window: Window, files: list[str]) -> None:
        self._window = window
        self.__files = files
        self._render()

    def __del__(self):
        menu = self._window.dom.get_element('#file-menu')
        if menu:
            menu.remove()

    def _render(self):
        self._window.dom.create_element('<div id="file-menu"><h1>Fichas de RPG</h1><h3>Selecione uma ficha</h3><ul id="file-list"></ul></div>', '#app')

        for file in self.__files:
            self._window.dom.create_element(f'<li class="list-item"><button id="{file}">{file[:-5]}</button></li>', '#file-list')

        self._window.dom.create_element('<button id="new-file">Nova Ficha</button>', '#file-menu')
        
    def add_list_item_events(self, func: FunctionType):
        buttons = self._window.dom.get_elements('.list-item button')
        for btn in buttons:
            btn.events.click += func

    def add_new_file_event(self, func: FunctionType):
        btn = self._window.dom.get_element('#new-file')
        if btn:
            btn.events.click += func