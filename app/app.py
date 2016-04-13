import sys

from PyQt4.QtGui import QApplication
from app_window import AppWindow
from app_ui import AppUi

from ffmpeg import FFmpeg

class Application(object):
    def __init__(self, config):
        self.app_config = config
        self.qapp = QApplication(sys.argv)
        self.window = AppWindow()
        self.ui = AppUi()
    def run(self):
        self.ui.setupUi(self.window)
        self.window.show()
        sys.exit(self.qapp.exec_())
