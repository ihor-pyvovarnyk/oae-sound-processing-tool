from PyQt4.QtGui import QFileDialog
from PyQt4 import QtCore
from gui import Ui_MainWindow



class AppUi(Ui_MainWindow):
    def __init__(self, connector):
        super(AppUi, self).__init__()
        self.connector = connector
        self.player_timer = QtCore.QTimer()

    def setupUi(self, MainWindow):
        super(AppUi, self).setupUi(MainWindow)
        self.select_file_btn.clicked.connect(self.own_select_file_dialog)
        self.fill_file_info()
        self.convert_target_ext_combo_box.activated.connect(self.change_target_extension_handler)
        self.invalid_file_label.setVisible(False)
        self.convert_btn.clicked.connect(self.convert_btn_handler)
        self.convert_status_label.setText('')
        self.disable_all()
        self.play_btn.clicked.connect(self.play_handler)
        self.pause_btn.clicked.connect(self.pause_handler)
        self.stop_btn.clicked.connect(self.stop_handler)
        self.player_slider.sliderPressed.connect(self.pause_handler)
        self.player_slider.sliderReleased.connect(self.slider_drop)
        self.player_timer.timeout.connect(self.connector.player.tick)
        self.player_timer.setSingleShot(True)

    def play_handler(self):
        self.connector.player.play()

    def pause_handler(self):
        self.player_timer.stop()
        self.connector.player.pause()

    def stop_handler(self):
        self.connector.player.stop()

    def slider_drop(self):
        position = self.player_slider.value()
        self.connector.player.slide_to(int(position))
        self.connector.player.play()

    def player_tick(self, position):
        self.move_player_slider(position)
        self.player_timer.start(1000)

    def move_player_slider(self, position):
        self.player_slider.setValue(position)

    def own_select_file_dialog(self):
        exts = self.connector.file_discoverer.get_allowed_exetnsions()
        exts = '; '.join(map(lambda e: '*.%s' % e, exts))
        file_path = QFileDialog.getOpenFileName(self.centralWidget,
            'Open sound', '/home/ihor-pyvovarnyk/', 'Sounds (%s)' % exts)
        file_path = str(file_path)
        self.connector.selected_file.select_file(file_path)
        self.connector.file_info.file_selected()
        self.connector.player.set_file(file_path)

    def change_target_extension_handler(self, index):
        text = self.convert_target_ext_combo_box.currentText()
        self.connector.converter.select_target_extension(text)

    def convert_btn_handler(self):
        self._prepare_convertion_ui()
        QtCore.QTimer.singleShot(100, self._convert_btn_handler_callback)

    def _convert_btn_handler_callback(self):
        result = self.connector.converter.convertion()
        self._post_convertion_ui(result)

    def _prepare_convertion_ui(self):
        self.set_convert_btn_state(False)
        self.set_convert_status('Converting')

    def _post_convertion_ui(self, result):
        self.set_convert_btn_state(True)
        self.set_temp_convert_status('Success' if result else 'Error')

    def disable_all(self):
        self.convert_btn.setEnabled(False)
        self.convert_target_ext_combo_box.setEnabled(False)
        self.convert_target_ext_combo_box.setEnabled(False)

    def enable_all(self):
        self.invalid_file_label.setVisible(False)
        self.convert_target_ext_combo_box.setEnabled(True)
        self.convert_btn.setEnabled(True)

    def fill_file_info(self, file_name='', frequency='',
                       duration='', bitrate='', channels=''):
        self.info_file_name_value.setText(str(file_name))
        self.info_sampling_frequency_value.setText(self._value_text(str(frequency), 'kHz'))
        self.info_bitrate_value.setText(self._value_text(str(bitrate), ' kbps'))
        self.info_duration_value.setText(self._value_text(str(duration), ' seconds'))
        self.info_channels_value.setText(str(channels))

    def _value_text(self, text, after):
        return (text + after) if text else ''

    def handle_invalid_file(self):
        self.invalid_file_label.setVisible(True)
        self.disable_all()

    def show_selected_file_path(self, path):
        self.selected_file.setText(path)
        self.enable_all()

    def fill_extensions_combo_box(self, extensions):
        self.convert_target_ext_combo_box.clear()
        self.convert_target_ext_combo_box.addItems(extensions)
        if len(extensions):
            self.change_target_extension_handler(1)

    def set_convert_btn_state(self, state):
        self.convert_btn.setEnabled(state)

    def set_convert_status(self, text):
        self.convert_status_label.setText(text)

    def set_temp_convert_status(self, text):
        self.set_convert_status(text)
        QtCore.QTimer.singleShot(2000,
            lambda: self.convert_status_label.setText(''))
