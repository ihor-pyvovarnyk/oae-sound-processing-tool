from gui import Ui_MainWindow

class AppUi(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(AppUi, self).setupUi(MainWindow)
        self.pushButton.clicked.connect(self.print_msg)
    def print_msg(self):
        print 'test'
