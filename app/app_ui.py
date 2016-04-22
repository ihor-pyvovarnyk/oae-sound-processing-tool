from PyQt4.QtGui import QFileDialog
from PyQt4 import QtCore
from gui import Ui_MainWindow

import time

class AppUi(Ui_MainWindow):
    def __init__(self, connector):
        super(AppUi, self).__init__()
        self.connector = connector

    def setupUi(self, MainWindow):
        super(AppUi, self).setupUi(MainWindow)
        self.select_file_btn.clicked.connect(self.own_select_file_dialog)
        self.convert_target_ext_combo_box.activated.connect(self.change_target_extension_handler)
        self.invalid_file_label.setVisible(False)
        self.convert_btn.clicked.connect(self.convert_btn_handler)
        self.convert_status_label.setText('')
        self.disable_all()

    def own_select_file_dialog(self):
        exts = self.connector.file_discoverer.get_allowed_exetnsions()
        exts = '; '.join(map(lambda e: '*.%s' % e, exts))
        file_path = QFileDialog.getOpenFileName(self.centralWidget,
            'Open sound', '/home/ihor-pyvovarnyk/', 'Sounds (%s)' % exts)
        self.connector.selected_file.select_file(str(file_path))

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

    def handle_invalid_file(self):
        self.invalid_file_label.setVisible(True)
        self.disable_all()

    def show_selected_file_path(self, path):
        self.selected_file.setText(path)
        self.enable_all()

    def fill_extensions_combo_box(self, extensions):
        self.convert_target_ext_combo_box.clear()
        self.convert_target_ext_combo_box.addItems(extensions)
        self.change_target_extension_handler(1)

    def set_convert_btn_state(self, state):
        self.convert_btn.setEnabled(state)

    def set_convert_status(self, text):
        self.convert_status_label.setText(text)

    def set_temp_convert_status(self, text):
        self.set_convert_status(text)
        QtCore.QTimer.singleShot(2000,
            lambda: self.convert_status_label.setText(''))
