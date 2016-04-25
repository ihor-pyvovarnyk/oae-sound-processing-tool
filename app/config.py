import os

FFMPEG_PATH = '/usr/local/Cellar/ffmpeg/2.8.3/bin/ffmpeg'
PROJECT_PATH = os.path.abspath(os.curdir)
APP_PATH = PROJECT_PATH + '/app'
RESOURCES_PATH = PROJECT_PATH + '/resources'
RESOURCES_IN_PATH = RESOURCES_PATH + '/in'
RESOURCES_OUT_PATH = RESOURCES_PATH + '/out'
RESOURCES_TEMP_PATH = RESOURCES_PATH + '/temp'

ALLOWED_FORMATS = {
    'wav': {
        'label': 'wav',
        'mime': 'audio/x-wav',
        'extensions': ['wav'],
        'codecs': []
    },
    'mp4': {
        'label': 'mp4',
        'mime': 'video/mp4',
        'extensions': ['mp4'],
        'codecs': ['libx264']
    },
    'mp3': {
        'label': 'mp3',
        'mime': 'audio/mpeg',
        'extensions': ['mp3'],
        'codecs': ['libmp3lame', 'libshine']
    }
}
