class BaseGuiComponent(object):
    def __init__(self, parent_ui, connector):
        self.parent_ui = parent_ui
        self.connector = connector

    def add_element(self, name, element):
        self.__dict__[name] = element

    def setup_ui(self):
        pass

    def enable_all(self):
        pass

    def disable_all(self):
        pass
