from webview import Window
from webview.dom.event import DOMEvent
import json

from app.utils.file_manager import FileManager
from app.utils.app_data import AppData
from app.components.file_menu import FileMenu
from app.components.data_menu import DataMenu

class App:
    def __init__(self, window: Window) -> None:
        self.__data = AppData()
        self.__window = window

        self.__window.load_html('<div id="app"></div>')
        self.__file_manager = FileManager()

        self.__file_menu = FileMenu(self.__window, self.__file_manager.files)
        self.__data_menu = None

        self.__file_menu.add_new_file_event(self.__new_file_event)
        self.__file_menu.add_list_item_events(self.__open_file_event)
        
    def __new_file_event(self):
        self.__data = AppData()
        del self.__file_menu

        self.__data_menu = DataMenu(self.__window, self.__data)

    def __open_file_event(self, evt):
        file = evt['target']['id']

        self.__data = AppData(self.__file_manager.load_data(file))

        del self.__file_menu

        self.__data_menu = DataMenu(self.__window, self.__data)