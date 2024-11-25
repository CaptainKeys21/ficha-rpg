from webview import Window

from app.utils.file_manager import FileManager
from app.components.file_menu import FileMenu

def setup(window: Window):
    window.load_html('<div id="app"></div>')
    file_manager = FileManager()

    file_menu = FileMenu(window, file_manager.files)

    print(window)
    print(file_manager.files)