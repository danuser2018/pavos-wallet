from abc import ABC, abstractmethod


class MainWindow(ABC):
    @abstractmethod
    def show(self):
        pass
