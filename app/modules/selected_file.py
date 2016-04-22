from ._base_module import BaseModule

class SelectedFile(BaseModule):
    def __init__(self, connector):
        super(SelectedFile, self).__init__(connector)
        self.file_path = ''

    def select_file(self, file_path):
        if self.connector.file_discoverer.check_file_mime(file_path):
            self.file_path = file_path
            self.connector.ui.show_selected_file_path(self.file_path)
        else:
            self.connector.ui.handle_invalid_file()
