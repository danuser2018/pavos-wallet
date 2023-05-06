from injector import Module, SingletonScope
from domain.ports.secondary.gui import MainWindow
from infrastructure_gui_tkinter import MainWindowAdapter


class Configuration(Module):
    def configure(self, binder):
        binder.bind(MainWindow, to=MainWindowAdapter, scope=SingletonScope)
