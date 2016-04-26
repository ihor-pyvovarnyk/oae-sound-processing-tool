from PyQt4.QtCore import QTimer

from ._base_gui_component import BaseGuiComponent

class Convert(BaseGuiComponent):
    def setup_ui(self):
        self.convert_target_ext_combo_box.activated.connect(self.change_target_extension_handler)
        self.convert_btn.clicked.connect(self.convert_btn_handler)
        self.convert_status_label.setText('')

    def fill_extensions_combo_box(self, extensions):
        self.convert_target_ext_combo_box.clear()
        self.convert_target_ext_combo_box.addItems(extensions)
        if len(extensions):
            self.change_target_extension_handler(1)

    def change_target_extension_handler(self, index):
        text = self.convert_target_ext_combo_box.currentText()
        self.connector.converter.select_target_extension(text)

    def convert_btn_handler(self):
        self._prepare_convertion_ui()
        QTimer.singleShot(100, self._convert_btn_handler_callback)

    def _convert_btn_handler_callback(self):
        result = self.connector.converter.convertion()
        self._post_convertion_ui(result)

    def _prepare_convertion_ui(self):
        self.set_convert_btn_state(False)
        self.set_convert_status('Converting')

    def _post_convertion_ui(self, result):
        self.set_convert_btn_state(True)
        self.set_temp_convert_status('Success' if result else 'Error')

    def set_convert_status(self, text):
        self.convert_status_label.setText(text)

    def set_temp_convert_status(self, text):
        self.set_convert_status(text)
        QTimer.singleShot(2000,
            lambda: self.convert_status_label.setText(''))

    def set_convert_btn_state(self, state):
        self.convert_btn.setEnabled(state)

    def enable_all(self):
        self.convert_target_ext_combo_box.setEnabled(True)
        self.convert_btn.setEnabled(True)

    def disable_all(self):
        self.convert_btn.setEnabled(False)
        self.convert_target_ext_combo_box.setEnabled(False)
