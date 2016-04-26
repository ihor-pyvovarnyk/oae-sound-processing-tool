import re
import os

from ._base_module import BaseModule

class Converter(BaseModule):
    def __init__(self, connector):
        super(Converter, self).__init__(connector)
        self.target_extension = None

    def setup(self):
        allowed_formats = self.connector.app_config.ALLOWED_FORMATS
        exts = []
        for key, fmt in allowed_formats.iteritems():
            for ext in fmt['extensions']:
                exts.append(ext)
        self.connector.ui.convert.fill_extensions_combo_box(exts)

    def select_target_extension(self, target_ext):
        self.target_extension = target_ext

    def convertion(self):
        path = self.connector.selected_file.file_path
        ext = self.target_extension
        return path and ext and self._convert(path, ext)

    def _convert(self, file_path, new_ext):
        file_base_name = os.path.basename(file_path)
        target_base_name = re.sub(r'\.[^\.]*$', '', file_base_name) + '.' + new_ext
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
                .out(filename = target_path)\
                .execute()
        return target_path_free and os.path.isfile(target_path)
