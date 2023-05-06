from injector import Injector

from config.configuration import Configuration
from domain.ports.secondary.gui import MainWindow

if __name__ == "__main__":
    injector = Injector(Configuration())
    mainWindow = injector.get(MainWindow)
    mainWindow.show()
