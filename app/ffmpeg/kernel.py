import functools

from . import config
from .services import CommandBuilderService
from .services import SchemaCompilerService
from .services import SchemasProviderService

class Kernel(object):
    def __init__(self, ffmpeg_home_dir):
        self.ffmpeg_home = ffmpeg_home_dir
        self.command_builder_service = CommandBuilderService(config)
        self.schema_compiler_service = SchemaCompilerService()
        self.schemas_provider_service = SchemasProviderService()
        self.options_stack = []
    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif self.has_option(name):
            return functools.partial(self.option, name)
        else:
            raise AttributeError, name
    def bootstrap(self):
        self.command_builder_service.bootstrap()
        self.schema_compiler_service.bootstrap()
        self.schemas_provider_service.bootstrap()
    def has_option(self, option_name):
        return bool(self.schemas_provider_service.schema(option_name))
    def option(self, name, **kwargs):
        schema = self.schemas_provider_service.schema(name)
        if not schema:
            return None
        else:
            compiled_option = self.schema_compiler_service.compile(schema, kwargs)
            self.options_stack.append(compiled_option)
            return self
    def execute(self):
        command_parts = map(lambda o: o.split(' '), self.options_stack)
        command_parts = reduce(lambda x, y: x + y, command_parts)
        self.command_builder_service.push(self.ffmpeg_home)
        for part in command_parts:
            self.command_builder_service.push(part)
        print self.command_builder_service.command_parts_stack
        self.command_builder_service.run()
        self.command_stack = []
