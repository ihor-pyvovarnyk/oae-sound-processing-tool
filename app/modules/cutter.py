import os
import re

from ._base_module import BaseModule

class Cutter(BaseModule):
    def __init__(self, connector):
        super(Cutter, self).__init__(connector)
        self.duration = False

    def file_selected(self, file_path):
        info = self.connector.file_info.get_file_info(file_path)
        self.duration = info['duration']
        self.connector.ui.cut.set_duration(self.duration)

    def cut(self, start, length):
        file_path = self.connector.selected_file.file_path
        file_base_name = os.path.basename(file_path)
        target_base_name = re.sub(r'(.*)\.([^\.]*)$', r'\1.cut.\2', file_base_name)
        target_path = self.connector.app_config.RESOURCES_OUT_PATH + '/' + target_base_name
        target_path_free = True
        if os.path.isfile(target_path):
            try:
                os.remove(target_path)
            except Exception:
                target_path_free = False
        if target_path_free:
            self.connector.ffmpeg.command()\
                .hide_banner()\
                .i(filename = file_path)\
                .ss(position = start)\
                .t(duration = length)\
                .c(stream_specifier = 'a', codec = 'copy')\
                .out(filename = target_path)\
                .execute()
        return target_path_free and os.path.isfile(target_path)
