from ._base_gui_component import BaseGuiComponent

class FileInfo(BaseGuiComponent):
    def setup_ui(self):
        self.fill_file_info()

    def fill_file_info(self, file_name='', frequency='',
                       duration='', bitrate='', channels=''):
        self.info_file_name_value.setText(str(file_name))
        self.info_sampling_frequency_value.setText(self._value_text(str(frequency), 'kHz'))
        self.info_bitrate_value.setText(self._value_text(str(bitrate), ' kbps'))
        self.info_duration_value.setText(self._value_text(str(duration), ' seconds'))
        self.info_channels_value.setText(str(channels))

    def _value_text(self, text, after):
        return (text + after) if text else ''
