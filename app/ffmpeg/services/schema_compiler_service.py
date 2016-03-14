from ._base_service import BaseService

from ..exceptions.schema_compile_exceptions import SchemaCompileException

# TODO implement schema validation
class SchemaCompilerService(BaseService):
    _MACRO_PREFIX = '='
    _VALUE_PREFIX = '@'
    _KEY_PREFIX = '#'
    _OPTIONAL_PREFIX = '?'
    _ALLOWED_MACRO_ARGUMENTS = (int, float, str)
    def __init__(self):
        self.macros = []
    def bootstrap(self):
        self._register_schema_macro('JOIN', self._macro_join)
        self._register_schema_macro('OPTION', self._macro_option)
        self._register_schema_macro('SPECIFIER', self._macro_specifier)
        self._register_schema_macro('REPEAT', self._macro_repeat)
        self._register_schema_macro('OR', self._macro_or)
    def compile(self, schema, data):
        schema = self._compile_schema_wrap(schema)
        return self._compile_schema(schema, data)
    def _register_schema_macro(self, name, closure):
        self.macros.append({
            'name': name,
            'handler': closure
        })
    def _compile_schema_wrap(self, schemas_collection):
        filtered_items = filter(lambda s: isinstance(s, list), schemas_collection)
        return ['=JOIN', ' ', schemas_collection] \
            if len(schemas_collection) == len(filtered_items) \
            else schemas_collection
    def _compile_schema(self, schema, data):
        cls = self.__class__
        name, prefixes, attrs, children = self._parse_schema_node(schema)
        result = None
        if cls._MACRO_PREFIX in prefixes:
            result = self._compile_macro(data, name, prefixes, attrs, children)
        else:
            result = self._compile_data_schema(data, name, prefixes, attrs, children)
        if result is None and not cls._OPTIONAL_PREFIX in prefixes:
            raise SchemaCompileException
        return result
    def _parse_schema_node(self, schema_node):
        name, prefixes = self._parse_schema_name(schema_node[0])
        is_last_list = isinstance(schema_node[-1], list)
        attrs = schema_node[1:-1] if is_last_list else schema_node[1:]
        children = schema_node[-1] if is_last_list else []
        return name, prefixes, attrs, children
    def _parse_schema_name(self, schema_name):
        cls = self.__class__
        prefixes = []
        name = ''
        for i, ch in enumerate(schema_name):
            all_prefixes = [cls._MACRO_PREFIX, cls._VALUE_PREFIX, cls._KEY_PREFIX, cls._OPTIONAL_PREFIX]
            if not ch in all_prefixes:
                name = schema_name[i:]
                break
            prefixes.append(ch)
        return name, prefixes
    def _compile_data_schema(self, data, name, prefixes, attrs, children):
        cls = self.__class__
        result = None
        if cls._VALUE_PREFIX in prefixes:
            result = str(data[name])
        elif cls._KEY_PREFIX in prefixes and data[name]:
            result = str(name)
        else:
            raise SchemaCompileException
        return result
    def _compile_macro(self, data, name, prefixes, attrs, children):
        result = ''
        macro = self._get_macro_by_name(name)
        if macro:
            result += macro['handler'](data, children, *attrs)
        return result
    def _get_macro_by_name(self, macro_name):
        result = None
        macro = filter(lambda m: m['name'] == macro_name, self.macros)
        if macro:
            result = macro[0]
        return result
    def _macro_join(self, data, children, join_ch = ''):
        child_compilations = []
        for child in children:
            child_compilations.append(self._compile_schema(child, data))
        return join_ch.join(child_compilations)
    def _macro_option(self, data, children, option_name):
        return '-%s' % option_name
    def _macro_specifier(self, data, children, input_ref):
        return ':%s' % self._compile_schema([input_ref], data)
    def _macro_or(self, data, children):
        target_child = None
        for child in children:
            try:
                target_child = self._compile_schema(child, data)
                break
            except SchemaCompileException:
                continue
        return target_child
    def _macro_repeat(self, data, children, join_ch = ','):
        parts = []
        repeat_key = 'REPEAT'
        has_repeat_key = repeat_key in data
        for child in children:
            if has_repeat_key:
                for item in data[repeat_key]:
                    parts.append(self._compile_schema(child, item))
            else:
                parts.append(self._compile_schema(child, data))
        return join_ch.join(parts)
