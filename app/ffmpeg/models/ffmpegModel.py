import subprocess as sp

# TODO Rewrite
class FfmpegModel(object):
    ffmpeg_name = 'ffmpeg'
    def __init__(self, config, ffmpeg_home):
        self.config = config
        self.ffmpeg_path = ffmpeg_home
    def execute(self, ffmpeg_arguments):
        command = [self.ffmpeg_bin_path()] + ffmpeg_arguments + ['-loglevel', 'quiet']
        pipe = sp.Popen(command, stdout = sp.PIPE)
        print pipe.stdout.read()
    def convert(self, sound, target_extension):
        original_path = sound.get_sound_path()
        convert_path = sound.get_convert_path(target_extension)
        self.execute(['-i', original_path, convert_path])
    def ffmpeg_bin_path(self):
        return '%s/%s' % (self.ffmpeg_path, self.config.FFMPEG_NAME)
