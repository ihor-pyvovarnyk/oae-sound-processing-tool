import sys

from PyQt4.QtGui import QApplication
from app_window import AppWindow
from app_ui import AppUi
from dispatcher import Dispatcher
import modules

from ffmpeg import FFmpeg

class Application(object):
    def __init__(self, config):
        self.app_config = config
        self.dispatcher = Dispatcher()

        self.qapp = QApplication(sys.argv)
        self.window = AppWindow()
        self.ui = AppUi(self.dispatcher)

        self.selected_file_module = modules.SelectedFile(self.dispatcher)

    def run(self):
        self.setup_dispatcher()
        self.setup_view()

    def setup_dispatcher(self):
        d = self.dispatcher
        d.dispatch_action('select_file', self.selected_file_module.select_file)
        d.dispatch_render('show_selected_file_path', self.ui.show_selected_file_path)

    def setup_view(self):
        self.ui.setupUi(self.window)
        self.window.show()
        sys.exit(self.qapp.exec_())
