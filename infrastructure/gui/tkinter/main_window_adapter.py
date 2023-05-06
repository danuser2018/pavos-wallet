from tkinter import Tk

from injector import inject

from domain.ports.secondary.gui import MainWindow


class MainWindowAdapter(MainWindow):
    MAIN_WINDOW_WIDTH = 800
    MAIN_WINDOW_HEIGHT = 600
    MAIN_WINDOW_BACKGROUND_COLOR = "black"
    MAIN_WINDOW_TITLE = "Monedero para guardar tus pavos"

    @inject
    def __init__(self, root: Tk):
        self.root = root
        self.configure_title()
        self.configure_background_color()
        self.center_window_on_screen()

    def configure_title(self):
        self.root.title(self.MAIN_WINDOW_TITLE)

    def configure_background_color(self):
        self.root.configure(bg=self.MAIN_WINDOW_BACKGROUND_COLOR)

    def center_window_on_screen(self):
        self.root.geometry(self._get_geometry(self._get_centered_x_coordinate(), self._get_centered_y_coordinate()))

    def _get_centered_x_coordinate(self):
        return int(self.root.winfo_screenwidth() / 2 - self.MAIN_WINDOW_WIDTH / 2)

    def _get_centered_y_coordinate(self):
        return int(self.root.winfo_screenheight() / 2 - self.MAIN_WINDOW_HEIGHT / 2)

    def _get_geometry(self, x_coordinate, y_coordinate):
        return "{}x{}+{}+{}".format(self.MAIN_WINDOW_WIDTH, self.MAIN_WINDOW_HEIGHT, x_coordinate, y_coordinate)

    def show(self):
        self.root.mainloop()
