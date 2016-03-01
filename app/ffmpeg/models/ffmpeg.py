import os

from .. import config

class FFmpeg(object):
    ffmpeg_name = 'ffmpeg'
    def __init__(self, ffmpeg_home):
        self.ffmpeg_path = ffmpeg_home
    def execute(self, ffmpeg_arguments):
        ffmpeg = self.ffmpeg_bin_path()
        os.system('%s %s -loglevel quiet' % (ffmpeg, ffmpeg_arguments))
    def convert(self, sound, target_extension):
        original_path = sound.get_sound_path()
        convert_path = sound.get_convert_path(target_extension)
        self.execute('-i %s %s' % (original_path, convert_path))
    def ffmpeg_bin_path(self):
        return '%s/%s' % (self.ffmpeg_path, config.FFMPEG_NAME)
