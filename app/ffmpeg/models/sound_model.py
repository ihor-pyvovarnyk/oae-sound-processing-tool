import os

# TODO Rewrite, maybe add supporting all kind of streams, not only files
class SoundModel(object):
    def __init__(self, config, file_path):
        self.config = config
        self.sound_path = file_path
        self.post_init()
    def post_init(self):
        path, ext = self.get_split_path()
        if not ext[1:] in self.config.SUPPORTED_EXTENSIONS:
            raise Exception('Unsupported sound format')
    def get_sound_path(self):
        return self.sound_path
    def get_convert_path(self, target_extension):
        if not target_extension in self.config.SUPPORTED_EXTENSIONS:
            raise Exception('Unsupported sound format')
        path, ext = self.get_split_path()
        return '%s.%s' % (path, target_extension)
    def get_split_path(self):
        return os.path.splitext(self.sound_path)
