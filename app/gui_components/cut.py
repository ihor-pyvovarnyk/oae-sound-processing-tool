from PyQt4.QtCore import QTimer

from ._base_gui_component import BaseGuiComponent

class Cut(BaseGuiComponent):
    def setup_ui(self):
        self.cut_audio_duration_value.setText('')
        self.cut_invalid_values_label.setVisible(False)
        self.cut_status_label.setText('')
        self.cut_btn.clicked.connect(self.cut_handler)

    def cut_handler(self):
        if self._validate_cut_values():
            self._prepare_cutting_ui()
            QTimer.singleShot(100, self._cut_btn_handler_callback)
        else:
            self.cut_invalid_values_label.setVisible(True)

    def _cut_btn_handler_callback(self):
        start = self._str_to_int(self.cut_start_from_edit.text(), 0)
        length = self._str_to_int(self.cut_length_edit.text(), 0)
        result = self.connector.cutter.cut(start, length)
        self._post_cutting_ui(result)

    def _validate_cut_values(self):
        start = self._str_to_int(self.cut_start_from_edit.text(), 0)
        length = self._str_to_int(self.cut_length_edit.text(), 0)
        return self.connector.cutter.duration is not False and\
            (start + length) <= self.connector.cutter.duration

    def _prepare_cutting_ui(self):
        self.cut_invalid_values_label.setVisible(False)
        self._set_cut_btn_state(False)
        self._set_cut_status('Cutting')

    def _post_cutting_ui(self, result):
        self._set_cut_btn_state(True)
        self._set_temp_cut_status('Success' if result else 'Error')

    def _str_to_int(self, val, def_val):
        int_val = def_val
        try:
            int_val = int(val)
        except Exception: pass
        return int_val

    def _set_cut_btn_state(self, state):
        self.cut_btn.setEnabled(state)

    def _set_cut_status(self, text):
        self.cut_status_label.setText(text)

    def _set_temp_cut_status(self, text):
        self._set_cut_status(text)
        QTimer.singleShot(2000,
            lambda: self.cut_status_label.setText(''))

    def set_duration(self, duration = False):
        val = str(duration) if duration is not False else ''
        self.cut_audio_duration_value.setText(val)

    def disable_all(self):
        self.cut_start_from_edit.setEnabled(False)
        self.cut_length_edit.setEnabled(False)
        self._set_cut_btn_state(False)

    def enable_all(self):
        self.cut_start_from_edit.setEnabled(True)
        self.cut_length_edit.setEnabled(True)
        self._set_cut_btn_state(True)
