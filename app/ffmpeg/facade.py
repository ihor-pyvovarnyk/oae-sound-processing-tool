from . import config

from .services import CommandBuilderService

# TODO Facade should connect models and services
class Facade(object):
    def __init__(self, ffmpegHomeDir):
        self.ffmpegHome = ffmpegHomeDir
        self.commandBuilderService = CommandBuilderService(config)
    def test(self):
        # think about returning new service after each chain step
        self.commandBuilderService\
            .push('%s/%s' % (self.ffmpegHome, config.FFMPEG_NAME))\
            .push('-i')\
            .push('/Users/ihor-pyvovarnyk/Documents/Workspace/oae-sound-processing-tool/resources/sound.wav')\
            .push('/Users/ihor-pyvovarnyk/Documents/Workspace/oae-sound-processing-tool/resources/sound.mp3')\
            .run()
