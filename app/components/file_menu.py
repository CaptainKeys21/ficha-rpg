from webview import Window

class FileMenu:
    def __init__(self, window: Window, files: list[str]) -> None:
        self.__window = window
        self.__files = files
        self.__render()

    def __del__(self):
        menu = self.__window.dom.get_element('#file-menu')
        if menu:
            menu.remove()

    def __render(self):
        app_container = self.__window.dom.get_element('#app')
        item_list = self.__window.dom.create_element('<div id="file-menu"><ul id="file-list"></ul></div>', '#app')

        for i in range(len(self.__files)):
            self.__window.dom.create_element(f'<li class="list-item"><button value="{i}">{self.__files[i]}</button></li>', '#file-list')

        app_container.append(item_list)
        