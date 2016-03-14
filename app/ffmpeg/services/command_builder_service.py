import subprocess as sp

from ._base_service import BaseService

class CommandBuilderService(BaseService):
    def __init__(self, config):
        super(CommandBuilderService, self).__init__(config)
        self.command_parts_stack = []
    def bootstrap(self):
        pass
    def push(self, command_part):
        self.command_parts_stack.append(command_part)
        return self
    def clear(self):
        self.command_parts_stack = []
        return self
    def run(self):
        print '[RUN] ' + ' '.join(self.command_parts_stack)
        pipe = sp.Popen(self.command_parts_stack, stdout = sp.PIPE)
        self.clear()
        # TODO return stdout for parser, not all output
        return pipe.stdout.read()
