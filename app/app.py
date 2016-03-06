import sys

from ffmpeg import FFmpeg

class Application(object):
    app_config = None
    @staticmethod
    def run(config):
        Application.app_config = config
        print "app is running"
        ffmpeg = FFmpeg(config.FFMPEG_PATH)
        ffmpeg.test()
