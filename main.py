from app.app import setup

import webview


if __name__ == '__main__':
    window = webview.create_window('Ficha RPG')
    webview.start(setup, window, debug=True)