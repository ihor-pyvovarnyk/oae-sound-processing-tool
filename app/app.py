import sys

from PyQt4.QtGui import QApplication
from app_window import AppWindow
from app_ui import AppUi

from ffmpeg import FFmpeg

class Application(object):
    @staticmethod
    def run(config):
        app = QApplication(sys.argv)
        window = AppWindow()
        ui = AppUi()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec_())
