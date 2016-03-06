import subprocess as sp

class CommandBuilderService(object):
    def __init__(self, config):
        self.config = config
        self.commandPartsStack = []
    def push(self, commandPart):
        self.commandPartsStack.append(commandPart)
        return self
    def clear(self):
        self.commandPartsStack = []
        return self
    def run(self):
        pipe = sp.Popen(self.commandPartsStack, stdout = sp.PIPE)
        self.clear()
        # TODO return stdout for parser, not all output
        return pipe.stdout.read()
