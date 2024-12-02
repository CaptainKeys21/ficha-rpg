from webview import Window
from webview.dom.event import DOMEvent
import json

from app.utils.file_manager import FileManager
from app.utils.app_data import AppData
from app.components.file_menu import FileMenu
from app.components.data_menu import DataMenu
from app.utils.styles import STYLES
from app.utils.template_data import TEMPLATE_SHEET

class App:
    def __init__(self, window: Window) -> None:
        self.__data = AppData()
        self.__window = window

        self.__window.load_html('<div id="app"></div>')
        self.__window.load_css(STYLES)
        self.__file_manager = FileManager()

        self.__file_menu = FileMenu(self.__window, self.__file_manager.files)
        self.__data_menu = None

        self.__file_menu.add_new_file_event(self.__new_file_event)
        self.__file_menu.add_list_item_events(self.__open_file_event)
        
    def __new_file_event(self, _):
        self.__data = AppData(TEMPLATE_SHEET)
        del self.__file_menu

        self.__data_menu = DataMenu(self.__window, self.__data)
        self.__data_menu.add_save_listener(self.__save_edit_event)
        self.__data_menu.add_cancel_listener(self.__cancel_edit_event)

    def __open_file_event(self, evt):
        file = evt['target']['id']

        self.__data = AppData(self.__file_manager.load_data(file))

        del self.__file_menu

        self.__data_menu = DataMenu(self.__window, self.__data)
        self.__data_menu.add_save_listener(self.__save_edit_event)
        self.__data_menu.add_cancel_listener(self.__cancel_edit_event)

    def __cancel_edit_event(self):
        self.__data_menu.__del__()

        self.__file_menu = FileMenu(self.__window, self.__file_manager.files)
        self.__file_menu.add_new_file_event(self.__new_file_event)
        self.__file_menu.add_list_item_events(self.__open_file_event)

    def __save_edit_event(self):
        self.__file_manager.save_data(self.__data_menu.filename, self.__data.__dict__)

        self.__data_menu.__del__()

        self.__file_menu = FileMenu(self.__window, self.__file_manager.files)
        self.__file_menu.add_new_file_event(self.__new_file_event)
        self.__file_menu.add_list_item_events(self.__open_file_event)