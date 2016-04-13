from PyQt4.QtGui import QFileDialog
from gui import Ui_MainWindow

class AppUi(Ui_MainWindow):

    def __init__(self, dispatcher):
        super(AppUi, self).__init__()
        self.dispatcher = dispatcher

    def setupUi(self, MainWindow):
        super(AppUi, self).setupUi(MainWindow)
        self.selectFile.clicked.connect(self.own_select_file_dialog)

    def own_select_file_dialog(self):
        file_path = QFileDialog.getOpenFileName(self.centralWidget,\
            'Open sound', '/home/ihor-pyvovarnyk/', 'Sounds (*.wav)')
        self.dispatcher.action('select_file', file_path)

    def show_selected_file_path(self, path):
        self.lineEdit.setText(path)
