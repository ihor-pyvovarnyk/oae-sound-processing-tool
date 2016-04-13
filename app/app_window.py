from PyQt4.QtGui import QMainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.setGeometry(100, 100, 400, 300)
