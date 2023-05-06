from injector import Module, SingletonScope
from domain.ports.secondary.gui import MainWindow
from infrastructure.gui.tkinter.main_window_adapter import MainWindowAdapter


class Configuration(Module):
    def configure(self, binder):
        binder.bind(MainWindow, to=MainWindowAdapter, scope=SingletonScope)
