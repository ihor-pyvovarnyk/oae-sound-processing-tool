from . import config

from .services import CommandBuilderService

# TODO Facade should connect models and services
class Facade(object):
    def __init__(self, ffmpeg_home_dir):
        self.ffmpeg_home = ffmpeg_home_dir
        self.command_builder_service = CommandBuilderService(config)
    def test(self):
        # think about returning new service after each chain step
        self.command_builder_service\
            .push('%s/%s' % (self.ffmpeg_home, config.FFMPEG_NAME))\
            .push('-i')\
            .push('/Users/ihor-pyvovarnyk/Documents/Workspace/oae-sound-processing-tool/resources/sound.wav')\
            .push('/Users/ihor-pyvovarnyk/Documents/Workspace/oae-sound-processing-tool/resources/sound.mp3')\
            .run()
