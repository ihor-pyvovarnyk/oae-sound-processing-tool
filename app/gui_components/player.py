from PyQt4.QtCore import QTimer

from ._base_gui_component import BaseGuiComponent

class Player(BaseGuiComponent):
    def __init__(self, parent_ui, connector):
        super(Player, self).__init__(parent_ui, connector)
        self.player_timer = QTimer()
        self.tick_size = 1000

    def setup_ui(self):
        self.play_btn.clicked.connect(self.play_handler)
        self.pause_btn.clicked.connect(self.pause_handler)
        self.stop_btn.clicked.connect(self.stop_handler)
        self.player_slider.sliderPressed.connect(self.pause_handler)
        self.player_slider.sliderReleased.connect(self.slider_drop)
        self.player_timer.timeout.connect(self.connector.player.tick)
        self.player_timer.setSingleShot(True)

    def play_handler(self):
        self.connector.player.play()

    def pause_handler(self):
        self.player_timer.stop()
        self.connector.player.pause()

    def stop_handler(self):
        self.connector.player.stop()

    def slider_drop(self):
        position = self.player_slider.value()
        self.connector.player.slide_to(int(position))
        self.connector.player.play()

    def player_tick(self, position):
        self.move_player_slider(position)
        self.player_timer.start(self.tick_size)

    def move_player_slider(self, position):
        self.player_slider.setValue(position)

    def disable_all(self):
        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.player_slider.setEnabled(False)

    def enable_all(self):
        self.play_btn.setEnabled(True)
        self.pause_btn.setEnabled(True)
        self.stop_btn.setEnabled(True)
        self.player_slider.setEnabled(True)
