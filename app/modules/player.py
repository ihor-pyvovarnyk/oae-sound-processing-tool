import subprocess as sp

from ._base_module import BaseModule

class Player(BaseModule):
    def __init__(self, connector):
        super(Player, self).__init__(connector)
        self.file = ''
        self.duration = 0
        self.pipe = None
        self.is_playing = False
        self.ticks = 0

    def set_file(self, file_path):
        self.file = file_path
        info = self.connector.file_info.get_file_info(self.file)
        self.duration = info['duration']

    def clear_file(self):
        self.set_file('', 0)

    def play(self):
        if self.file:
            self.pipe = sp.Popen([
                'ffplay',
                '-ss', str(self.ticks),
                #'-t', duration,
                '-hide_banner',
                '-nodisp',
                self.file,
            ], stdout=sp.PIPE)
            self.is_playing = True
            self.connector.ui.player.player_tick(
                self.ticks_to_position(self.ticks))

    def pause(self):
        if self.pipe:
            self.pipe.terminate()
            self.pipe = None
            self.is_playing = False

    def slide_to(self, position):
        self.ticks = self.position_to_ticks(position)

    def stop(self):
        if self.pipe:
            self.pause()
            self.ticks = 0
            self.connector.ui.player.move_player_slider(0)

    def tick(self):
        if self.is_playing:
            if self.ticks < self.duration:
                self.ticks += 1
                self.connector.ui.player.player_tick(
                    min(100, self.ticks_to_position(self.ticks)))
            else:
                self.stop()

    def get_tick(self):
        return self.ticks

    def get_position(self):
        return self.ticks_to_position(self.ticks)

    def ticks_to_position(self, ticks):
        return int(float(ticks) / self.duration * 100)

    def position_to_ticks(self, position):
        return int(position / 100.0 * self.duration)
