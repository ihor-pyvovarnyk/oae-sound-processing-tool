from PyQt4.QtCore import QTimer

from ._base_gui_component import BaseGuiComponent

class FftAnalysis(BaseGuiComponent):
    def setup_ui(self):
        self.fft_audio_duration_value.setText('')
        self.fft_invalid_values_label.setVisible(False)
        self.fft_overlap_error_label.setVisible(False)
        self.fft_analysis_status_label.setText('')
        self.fft_analysis_btn.clicked.connect(self.analize_handler)

    def analize_handler(self):
        self.fft_invalid_values_label.setVisible(False)
        self.fft_overlap_error_label.setVisible(False)
        if self._validate_fft_values():
            self._prepare_analysis_ui()
            QTimer.singleShot(100, self._analyze_btn_handler_callback)

    def _prepare_analysis_ui(self):
        self._set_analyze_btn_state(False)
        self.fft_analysis_status_label.setText('Preparing')

    def _analyze_btn_handler_callback(self):
        start = self._str_to_int(self.fft_start_from_edit.text(), 0)
        length = self._str_to_int(self.fft_length_edit.text(), 1)
        window = self._str_to_int(self.fft_window_size_edit.text(), 1024)
        overlap = self._str_to_int(self.fft_overlap_size_edit.text(), 512)
        result = self.connector.fft_analysis.analize(start, length, window,
            overlap)
        self._post_analysis_ui(result)
        self.connector.fft_analysis.show()

    def _post_analysis_ui(self, result):
        self._set_analyze_btn_state(True)
        self._set_temp_analysis_status('Success' if result else 'Error')

    def _validate_fft_values(self):
        start = self._str_to_int(self.fft_start_from_edit.text(), 0)
        length = self._str_to_int(self.fft_length_edit.text(), 1)
        is_valid = self.connector.fft_analysis.duration is not False and\
            (start + length) <= self.connector.fft_analysis.duration
        if not is_valid:
            self.fft_invalid_values_label.setVisible(True)
        else:
            window = self._str_to_int(self.fft_window_size_edit.text(), 1024)
            overlap = self._str_to_int(self.fft_overlap_size_edit.text(), 512)
            is_valid = window > overlap
            if not is_valid:
                self.fft_overlap_error_label.setVisible(True)
        return is_valid

    def _str_to_int(self, val, def_val):
        int_val = def_val
        try:
            int_val = int(val)
        except Exception: pass
        return int_val

    def set_duration(self, duration = False):
        val = str(duration) if duration is not False else ''
        self.fft_audio_duration_value.setText(val)

    def _set_analyze_btn_state(self, state = True):
        self.fft_analysis_btn.setEnabled(state)


    def _set_analysis_status(self, text):
        self.fft_analysis_status_label.setText(text)

    def _set_temp_analysis_status(self, text):
        self._set_analysis_status(text)
        QTimer.singleShot(2000,
            lambda: self.fft_analysis_status_label.setText(''))

    def disable_all(self):
        self.fft_start_from_edit.setEnabled(False)
        self.fft_length_edit.setEnabled(False)
        self.fft_window_size_edit.setEnabled(False)
        self.fft_overlap_size_edit.setEnabled(False)
        self._set_analyze_btn_state(False)

    def enable_all(self):
        self.fft_start_from_edit.setEnabled(True)
        self.fft_length_edit.setEnabled(True)
        self.fft_window_size_edit.setEnabled(True)
        self.fft_overlap_size_edit.setEnabled(True)
        self._set_analyze_btn_state(True)
