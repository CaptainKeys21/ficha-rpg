from app.app import App

import webview


if __name__ == '__main__':
    window = webview.create_window('Ficha RPG')
    webview.start(App, window)