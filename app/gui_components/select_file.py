from PyQt4.QtGui import QFileDialog

from ._base_gui_component import BaseGuiComponent

class SelectFile(BaseGuiComponent):
    def setup_ui(self):
        self.select_file_btn.clicked.connect(self.own_select_file_dialog)
        self.invalid_file_label.setVisible(False)

    def own_select_file_dialog(self):
        exts = self.connector.file_discoverer.get_allowed_exetnsions()
        exts = '; '.join(map(lambda e: '*.%s' % e, exts))
        file_path = QFileDialog.getOpenFileName(self.centralWidget,
            'Open sound', '/home/ihor-pyvovarnyk/', 'Sounds (%s)' % exts)
        file_path = str(file_path)
        if file_path:
            self.connector.selected_file.select_file(file_path)
            self.connector.file_info.file_selected()
            self.connector.player.set_file(file_path)
            self.connector.cutter.file_selected(file_path)

    def handle_invalid_file(self):
        self.invalid_file_label.setVisible(True)

    def show_selected_file_path(self, path):
        self.selected_file.setText(path)
