import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pysox
import subprocess as sp
import time
import os
import re

from ._base_module import BaseModule

class FftAnalysis(BaseModule):
    def __init__(self, connector):
        super(FftAnalysis, self).__init__(connector)
        self.duration = False
        self.fs = 0

    def file_selected(self, file_path):
        info = self.connector.file_info.get_file_info(file_path)
        self.duration = info['duration']
        self.fs = int(info['frequency'] * 1000)
        self.connector.ui.fft_analysis.set_duration(self.duration)

    def analize(self, start, length, window, overlap):
        file_path = self.connector.selected_file.file_path
        target_path = self._get_dat_target_path(file_path)
        self.convert_to_dat(file_path)
        self.analize_dat(file_path, start, length, window, overlap)
        dat_created = os.path.isfile(target_path)
        if dat_created:
            os.remove(target_path)
        return dat_created

    def convert_to_dat(self, file_path):
        target_path = self._get_dat_target_path(file_path)
        sp.Popen(['sox', file_path, target_path], stdout = sp.PIPE)
        while not os.path.isfile(target_path):
            time.sleep(0.1)
        os.chmod(target_path, 0777)

    def _get_dat_target_path(self, file_path):
        file_base_name = os.path.basename(file_path)
        target_base_name = re.sub(r'(.*)\.([^\.]*)$', r'\1.dat', file_base_name)
        return self.connector.app_config.RESOURCES_TEMP_PATH + '/' + target_base_name

    def analize_dat(self, file_path, start, length, window, overlap):
        target_path = self._get_dat_target_path(file_path)
        start_sample = start * self.fs
        end_sample = start_sample + length * self.fs
        signal = []
        with open(target_path) as f:
            for i, line in enumerate(f):
                if len(line.strip()) and line[0] == ';':
                    continue
                if i < start_sample:
                    continue
                if i >= end_sample:
                    break
                vals = self._parse_line(line)
                if len(vals) > 2:
                    signal.append(vals[1])
        np_signal = np.array(signal)
        del signal
        plt.specgram(
            np_signal,
            NFFT = window,
            Fs = self.fs,
            window = mlab.window_hanning,
            scale_by_freq = True,
            noverlap = overlap)
        plt.draw()

    def show(self):
        plt.show()

    def _parse_line(self, line):
        parts = line.strip().split(' ')
        parts = filter(lambda p: bool(p), parts)
        parts = [float(s) for s in parts]
        return parts
