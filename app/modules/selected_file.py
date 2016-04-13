class SelectedFile(object):

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def select_file(self, file_path):
        self.dispatcher.render('show_selected_file_path', file_path)
