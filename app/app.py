import sys

from ffmpeg import FFmpeg

class Application(object):
    app_config = None
    @staticmethod
    def run(config):
        Application.app_config = config
        print "app is running"
        base_path = '/Users/ihor-pyvovarnyk/Documents/Workspace/oae-sound-processing-tool/resources'
        FFmpeg.set_ffmpeg_home(config.FFMPEG_PATH)
        FFmpeg.command()\
            .i(filename = '%s/in1.wav' % base_path)\
            .out(filename = '%s/out1.mp3' % base_path)\
            .execute()
