import sys

from PyQt4.QtGui import QApplication
from app_window import AppWindow
from app_ui import AppUi
from connector import Connector
import pysox
import modules

from ffmpeg import FFmpeg

class Application(object):
    def __init__(self, config):
        self.app_config = config
        self.connector = Connector()

        self.qapp = QApplication(sys.argv)
        self.window = AppWindow()
        self.ui = AppUi(self.connector)

        self.file_discoverer_module = modules.FileDiscoverer(self.connector)
        self.file_info_module = modules.FileInfo(self.connector)
        self.selected_file_module = modules.SelectedFile(self.connector)
        self.converter_module = modules.Converter(self.connector)
        self.player_module = modules.Player(self.connector)

    def run(self):
        FFmpeg.set_ffmpeg_home(self.app_config.FFMPEG_PATH)
        self.setup_connector()
        self.setup_view()

    def setup_connector(self):
        c = self.connector
        c.register_source('app_config', self.app_config)
        c.register_source('ui', self.ui)
        c.register_source('ffmpeg', FFmpeg)
        c.register_source('pysox', pysox)
        c.register_source('file_discoverer', self.file_discoverer_module)
        c.register_source('file_info', self.file_info_module)
        c.register_source('selected_file', self.selected_file_module)
        c.register_source('converter', self.converter_module)
        c.register_source('player', self.player_module)

    def setup_view(self):
        self.ui.setupUi(self.window)
        self.setup_modules()
        self.window.show()
        sys.exit(self.qapp.exec_())

    def setup_modules(self):
        self.file_discoverer_module.setup()
        self.file_info_module.setup()
        self.selected_file_module.setup()
        self.converter_module.setup()
        self.player_module.setup()
