from PyQt4 import QtCore
from gui import Ui_MainWindow

from gui_components import BaseGuiComponent
from gui_components import SelectFile
from gui_components import FileInfo
from gui_components import Convert
from gui_components import Player

class AppUi(Ui_MainWindow):
    def __init__(self, connector):
        super(AppUi, self).__init__()
        self.connector = connector
        self.select_file = SelectFile(self, connector)
        self.file_info = FileInfo(self, connector)
        self.convert = Convert(self, connector)
        self.player = Player(self, connector)

    def setupUi(self, MainWindow):
        super(AppUi, self).setupUi(MainWindow)
        self.select_file.add_element('centralWidget', self.centralWidget)
        self.select_file.add_element('selected_file', self.selected_file)
        self.select_file.add_element('select_file_btn', self.select_file_btn)
        self.select_file.add_element('invalid_file_label', self.invalid_file_label)
        self.select_file.setup_ui()

        self.file_info.add_element('info_file_name_value', self.info_file_name_value)
        self.file_info.add_element('info_sampling_frequency_value', self.info_sampling_frequency_value)
        self.file_info.add_element('info_bitrate_value', self.info_bitrate_value)
        self.file_info.add_element('info_duration_value', self.info_duration_value)
        self.file_info.add_element('info_channels_value', self.info_channels_value)
        self.file_info.setup_ui()

        self.convert.add_element('convert_target_ext_combo_box', self.convert_target_ext_combo_box)
        self.convert.add_element('convert_btn', self.convert_btn)
        self.convert.add_element('convert_status_label', self.convert_status_label)
        self.convert.setup_ui()

        self.player.add_element('play_btn', self.play_btn)
        self.player.add_element('pause_btn', self.pause_btn)
        self.player.add_element('stop_btn', self.stop_btn)
        self.player.add_element('player_slider', self.player_slider)
        self.player.setup_ui()

        self.disable_all()

    def disable_all(self):
        self.select_file.disable_all()
        self.file_info.disable_all()
        self.convert.disable_all()
        self.player.disable_all()

    def enable_all(self):
        self.select_file.enable_all()
        self.file_info.enable_all()
        self.convert.enable_all()
        self.player.enable_all()

    def handle_invalid_file(self):
        self.select_file.handle_invalid_file()
        self.disable_all()

    def show_selected_file_path(self, path):
        self.select_file.show_selected_file_path(path)
        self.enable_all()
