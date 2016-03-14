from .kernel import Kernel

class Facade(object):
    ffmpeg_path = ''
    @classmethod
    def set_ffmpeg_home(cls, ffmpeg_path):
        cls.ffmpeg_path = ffmpeg_path
    @classmethod
    def command(cls):
        kernel = Kernel(cls.ffmpeg_path)
        kernel.bootstrap()
        return kernel
