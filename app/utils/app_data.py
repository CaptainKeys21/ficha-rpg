from typing import Any, Callable


class AppData:
    __observers: list[Callable[[dict, dict], None]] = []
    def __init__(self, initial_data: dict = {}) -> None:
        for k, v in initial_data.items():
            self.__dict__[k] = v

        print(self.__dict__)
    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__[name] = value

        for func in self.__observers:
            func(self.__dict__, value)

    def __getitem__(self, name: str) -> Any:
        return getattr(self, name)
        
    def subscribe(self, fn: Callable[[dict, dict], None]):
        self.__observers.append(fn)

    def unsubscribe(self, fn: Callable[[dict, dict], None]):
        self.__observers.remove(fn)