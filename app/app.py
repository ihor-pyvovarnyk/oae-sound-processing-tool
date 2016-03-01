from ffmpeg import FFmpeg, Sound

class Application(object):
    app_config = None
    @staticmethod
    def run(config):
        Application.app_config = config
        print "app is running"
        ffmpeg = FFmpeg(config.FFMPEG_PATH)
        sound = Sound('/Users/ihor-pyvovarnyk/Documents/Workspace/oae-sound-processing-tool/resources/sound.wav')
        ffmpeg.convert(sound, 'mp3')
