class SchemaCompileException(Exception):
    def __init__(self, *args, **kwargs):
        super(SchemaCompileException, self).__init__(*args, **kwargs)
