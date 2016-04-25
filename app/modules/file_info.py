import os

from ._base_module import BaseModule

class FileInfo(BaseModule):
    def file_selected(self):
        file_path = self.connector.selected_file.file_path
        base_name = os.path.basename(file_path)
        audio = self.connector.pysox.CSoxStream(file_path)
        signal = audio.get_signal()
        signal_info = signal.get_signalinfo()
        self.connector.ui.fill_file_info(file_name = base_name,
            frequency = signal_info['rate'] / 1000,
            bitrate = int(signal_info['rate'] * signal_info['precision'] / 1000),
            duration = int(signal_info['length'] / signal_info['rate'] / signal_info['channels']),
            channels = signal_info['channels'])
        audio.close()
