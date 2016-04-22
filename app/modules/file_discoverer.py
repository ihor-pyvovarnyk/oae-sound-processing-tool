import magic
import re

from ._base_module import BaseModule

class FileDiscoverer(BaseModule):
    def check_file_mime(self, file_path):
        mime = ''
        try:
            mime = magic.from_file(file_path, mime=True)
        except Exception: pass
        return self.is_mime_allowed(mime)

    def is_mime_allowed(self, mime):
        result = False
        if mime:
            for key, fmt in self.connector.app_config.ALLOWED_FORMATS.iteritems():
                if mime == fmt['mime']:
                    result = True
                    break
        return result

    def get_allowed_exetnsions(self):
        exts = []
        for key, fmt in self.connector.app_config.ALLOWED_FORMATS.iteritems():
            for ext in fmt['extensions']:
                exts.append(ext)
        return exts
