import unittest
from unittest.mock import Mock

from infrastructure.gui.tkinter.main_window_adapter import MainWindowAdapter


class MainWindowTestCase(unittest.TestCase):

    def setUp(self):
        self.root = Mock()
        self.root.winfo_screenwidth.return_value = 1920
        self.root.winfo_screenheight.return_value = 1080
        self.window = MainWindowAdapter(self.root)

    def test_window_title(self):
        self.root.title.assert_called_with(self.window.MAIN_WINDOW_TITLE)

    def test_window_background_color(self):
        self.root.configure.assert_called_with(bg=self.window.MAIN_WINDOW_BACKGROUND_COLOR)

    def test_window_centered_on_screen(self):
        expected_x = int(self.root.winfo_screenwidth() / 2 - self.window.MAIN_WINDOW_WIDTH / 2)
        expected_y = int(self.root.winfo_screenheight() / 2 - self.window.MAIN_WINDOW_HEIGHT / 2)
        self.root.geometry.assert_called_with("{}x{}+{}+{}".format(
            self.window.MAIN_WINDOW_WIDTH, self.window.MAIN_WINDOW_HEIGHT, expected_x, expected_y
        ))

    def test_window_is_showed(self):
        self.window.show()
        self.root.mainloop.assert_called()

    def tearDown(self):
        self.root.destroy()


if __name__ == '__main__':
    unittest.main()
