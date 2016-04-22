class Connector(object):

    def __init__(self):
        self.action_listeners = []
        self.render_listeners = []
        self.sources = {}

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self.sources:
            return self.sources[name]
        else:
            raise AttributeError, name

    def register_source(self, source_id, source_instance):
        self.sources[source_id] = source_instance
