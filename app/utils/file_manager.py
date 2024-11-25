import platform
import json
import os

class FileManager:
    files: 'list[str]'

    def __new__(cls): #Singleton pattern: garantir que só vai existir uma instância dessa classe durante a execução do programa inteiro.
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileManager, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        workdir = self.__get_work_dir()
        if not os.path.exists(workdir):
            os.makedirs(workdir, exist_ok=True)

        self.files = [file for file in os.listdir(workdir) if os.path.isfile(os.path.join(workdir, file))]

    def __get_work_dir(self) -> str:
        if platform.system() == "Windows":
            appdata = os.getenv('LOCALAPPDATA')
            return os.path.join(appdata, 'ficharpg')
        else:
            home = os.path.expanduser('~')
            return os.path.join(home, '.ficharpg')
        
    def load_data(self, filename: str) -> dict:
        if filename in self.files:
            workdir = self.__get_work_dir()

            with open(os.path.join(workdir, filename), 'r') as file:
                data = json.load(file)

            return data
        
        return dict()
    
    def save_data(self, filename: str, data: dict):
        workdir = self.__get_work_dir()
        if not filename.endswith('.json'):
            filename += '.json'

        with open(os.path.join(workdir, filename), "w") as file:
            json.dump(data, file)