import json

from ._base_service import BaseService

class SchemasProviderService(BaseService):
    #_schema_method_prefix = '_schema_'
    def __init__(self):
        self.schemas = []
    def bootstrap(self):
        self._register_schema('out', self._schema_out)

        self._register_schema('L', self._schema_L)
        self._register_schema('h', self._schema_h)
        self._register_schema('help', self._schema_help)
        self._register_schema('version', self._schema_version)
        self._register_schema('devices', self._schema_devices)
        self._register_schema('codecs', self._schema_codecs)
        self._register_schema('decoders', self._schema_decoders)
        self._register_schema('encoders', self._schema_encoders)
        self._register_schema('bsfs', self._schema_bsfs)
        self._register_schema('protocols', self._schema_protocols)
        self._register_schema('filters', self._schema_filters)
        self._register_schema('pix_fmts', self._schema_pix_fmts)
        self._register_schema('sample_fmts', self._schema_sample_fmts)
        self._register_schema('layouts', self._schema_layouts)
        self._register_schema('colors', self._schema_colors)
        self._register_schema('sources', self._schema_sources)
        self._register_schema('sinks', self._schema_sinks)
        self._register_schema('loglevel', self._schema_loglevel)
        self._register_schema('report', self._schema_report)
        self._register_schema('hide_banner', self._schema_hide_banner)
        self._register_schema('cpuflags', self._schema_cpuflags)
        self._register_schema('opencl_bench', self._schema_opencl_bench)
        self._register_schema('opencl_options', self._schema_opencl_options)

        self._register_schema('f', self._schema_f)
        self._register_schema('i', self._schema_i)
        self._register_schema('y', self._schema_y)
        self._register_schema('n', self._schema_n)
        self._register_schema('stream_loop', self._schema_stream_loop)
        self._register_schema('c', self._schema_c)
        self._register_schema('codec', self._schema_codec)
        self._register_schema('t', self._schema_t)
        self._register_schema('to', self._schema_to)
        self._register_schema('fs', self._schema_fs)
        self._register_schema('ss', self._schema_ss)
        self._register_schema('sseof', self._schema_sseof)
        self._register_schema('itsoffset', self._schema_itsoffset)
        self._register_schema('timestamp', self._schema_timestamp)
        self._register_schema('metadata', self._schema_metadata)
        #self._register_schema('program', self._schema_program)
        self._register_schema('target', self._schema_target)
        self._register_schema('dframes', self._schema_dframes)
        self._register_schema('frames', self._schema_frames)
        self._register_schema('q', self._schema_q)
        self._register_schema('qscale', self._schema_qscale)
        self._register_schema('filter', self._schema_filter)
        self._register_schema('filter_script', self._schema_filter_script)
        self._register_schema('pre', self._schema_pre)
        self._register_schema('stats', self._schema_stats)
        self._register_schema('progress', self._schema_progress)
        self._register_schema('stdin', self._schema_stdin)
        self._register_schema('debug_ts', self._schema_debug_ts)
        self._register_schema('attach', self._schema_attach)
        self._register_schema('dump_attachment', self._schema_dump_attachment)
        self._register_schema('noautorotate', self._schema_noautorotate)

    def schema(self, name):
        target_schema = filter(lambda s: s["name"] == name, self.schemas)
        return None if not target_schema else target_schema[0]["handler"]()

    def _register_schema(self, option_name, handler):
        self.schemas.append({
            "name": option_name,
            "handler": handler
        })

    def _schema_OPTION(self, option_name):
        # -option_name
        return [
            ['=OPTION', option_name]
        ]
    def _schema_OPTION_DATA(self, option_name, data_name):
        # -option_name data_name
        return [
            ['=OPTION', option_name],
            ['@%s' % data_name]
        ]

    def _schema_out(self):
        return [
            ['@filename']
        ]

    def _schema_L(self):
        # -L
        return self._schema_OPTION('L')
    def _schema_h(self):
        # -h
        return self._schema_OPTION('h')
    def _schema_help(self):
        # -help
        return self._schema_h()
    def _schema_version(self):
        # -version
        return self._schema_OPTION('version')
    def _schema_devices(self):
        # -devices
        return self._schema_OPTION('devices')
    def _schema_codecs(self):
        # -codecs
        return self._schema_OPTION('codecs')
    def _schema_decoders(self):
        # -decoders
        return self._schema_OPTION('decoders')
    def _schema_encoders(self):
        # -encoders
        return self._schema_OPTION('encoders')
    def _schema_bsfs(self):
        # -bsfs
        return self._schema_OPTION('bsfs')
    def _schema_protocols(self):
        # -protocols
        return self._schema_OPTION('protocols')
    def _schema_filters(self):
        # -filters
        return self._schema_OPTION('filters')
    def _schema_pix_fmts(self):
        # -pix_fmts
        return self._schema_OPTION('pix_fmts')
    def _schema_sample_fmts(self):
        # -sample_fmts
        return self._schema_OPTION('sample_fmts')
    def _schema_layouts(self):
        # -layouts
        return self._schema_OPTION('layouts')
    def _schema_colors(self):
        # -colors
        return self._schema_OPTION('colors')
    def _schema_sources(self):
        # -sources device[,opt1=val1[,opt2=val2]...]
        return [
            ['=OPTION', 'sources'],
            ['=JOIN', ',', [
                ['@device'],
                ['=REPEAT', [
                    ['=JOIN', '=', [
                        ['@opt'],
                        ['@val']
                    ]]
                ]]
            ]]
        ]
    def _schema_sinks(self):
        # -sinks device[,opt1=val1[,opt2=val2]...]
        return [
            ['=OPTION', 'sinks'],
            ['=JOIN', ',', [
                ['@device'],
                ['=REPEAT', [
                    ['=JOIN', '=', [
                        ['@opt'],
                        ['@val']
                    ]]
                ]]
            ]]
        ]
    def _schema_loglevel(self):
        # -loglevel [repeat+]loglevel | -v [repeat+]loglevel
        return [
            ['=OPTION', 'loglevel']
            ['?#-v'],
            ['=JOIN', [
                ['#repeat+']
                ['@loglevel']
            ]]
        ]
    def _schema_report(self):
        # -report
        return self._schema_OPTION('report')
    def _schema_hide_banner(self):
        # -hide_banner
        return self._schema_OPTION('hide_banner')
    def _schema_cpuflags(self):
        # -cpuflags flags
        return self._schema_OPTION_DATA('cpuflags', 'flags')
    def _schema_opencl_bench(self):
        # -opencl_bench
        return self._schema_OPTION('opencl_bench')
    def _schema_opencl_options(self):
        # -opencl_options options
        return self._schema_OPTION_DATA('opencl_options', 'options')

    def _schema_f(self):
        # -f fmt
        return self._schema_OPTION_DATA('f', 'fmt')
    def _schema_i(self):
        # -i filename
        return self._schema_OPTION_DATA('i', 'filename')
    def _schema_y(self):
        # -y
        return self._schema_OPTION('y')
    def _schema_n(self):
        # -n
        return self._schema_OPTION('n')
    def _schema_stream_loop(self):
        # -stream_loop number
        return self._schema_OPTION_DATA('stream_loop', 'number')
    def _schema_c(self):
        # -c[:stream_specifier] codec
        return [
            ['=JOIN', [
                ['=OPTION', 'c'],
                ['=SPECIFIER', '@stream_specifier']
            ]],
            ['@codec']
        ]
    def _schema_codec(self):
        # -codec[:stream_specifier] codec
        return self._schema_c()
    def _schema_t(self):
        # -t duration
        return self._schema_OPTION_DATA('t', 'duration')
    def _schema_to(self):
        # -to position
        return self._schema_OPTION_DATA('to', 'position')
    def _schema_fs(self):
        # -fs limit_rate
        return self._schema_OPTION_DATA('fs', 'limit_size')
    def _schema_ss(self):
        # -ss position
        return self._schema_OPTION_DATA('ss', 'position')
    def _schema_sseof(self):
        # -sseof position
        return self._schema_OPTION_DATA('sseof', 'position')
    def _schema_itsoffset(self):
        # -itsoffset offset
        return self._schema_OPTION_DATA('itsoffset', 'offset')
    def _schema_timestamp(self):
        # -timestamp date
        return self._schema_OPTION_DATA('timestamp', 'date')
    def _schema_metadata(self):
        # -metadata[:metadata_specifier] key=value
        return [
            ['=JOIN', [
                ['=OPTION', 'matadata'],
                ['=SPECIFIER', '@metadata_specifier']
            ]],
            ['=JOIN', '=', [
                ['@key']
                ['@value']
            ]]
        ]
    def _schema_program(self):
        # -program [title=title:][program_num=program_num:]st=stream[:st=stream...]
        # TODO Implement
        return [
            #
        ]
    def _schema_target(self):
        # -target type
        return self._schema_OPTION_DATA('target', 'type')
    def _schema_dframes(self):
        # -sframes number
        return self._schema_OPTION_DATA('sframes', 'number')
    def _schema_frames(self):
        # -frames[:stream_specifier] framecount
        return [
            ['=JOIN', [
                ['=OPTION', 'frames']
                ['=SPECIFIER', '@stream_specifier']
            ]],
            ['@framecount']
        ]
    def _schema_q(self):
        # -q[:stream_specifier] q
        return [
            ['=JOIN', [
                ['=OPTION', 'q'],
                ['=SPECIFIER', '@stream_specifier']
            ]],
            ['@q']
        ]
    def _schema_qscale(self):
        # -qscale[:stream_specifier] q
        return _schema_q()
    def _schema_filter(self):
        # -filter[:stream_specifier] filtergraph
        return [
            ['=JOIN', [
                ['=OPTION', 'filter'],
                ['=SPECIFIER', '@stream_specifier']
            ]],
            ['@filtergraph']
        ]
    def _schema_filter_script(self):
        # -filter_script[:stream_specifier] filename
        return [
            ['=JOIN', [
                ['=OPTION', 'filter_script'],
                ['=SPECIFIER', '@stream_specifier']
            ]],
            ['@filename']
        ]
    def _schema_pre(self):
        # -pre[:stream_specifier] preset_name
        return [
            ['=JOIN', [
                ['=OPTION', 'pre'],
                ['=SPECIFIER', '@stream_specifier']
            ]],
            ['@preset_name']
        ]
    def _schema_stats(self):
        # -stats
        return self._schema_OPTION('stats')
    def _schema_progress(self):
        # -progress url
        return self._schema_OPTION_DATA('progress', 'url')
    def _schema_stdin(self):
        # -stdin
        return self._schema_OPTION('stdin')
    def _schema_debug_ts(self):
        # -debug_ts
        return self._schema_OPTION('debug_ts')
    def _schema_attach(self):
        # -attach filename
        return self._schema_OPTION_DATA('attach', 'filename')
    def _schema_dump_attachment(self):
        # -dump_attachment[:stream_specifier] filename
        return [
            ['=JOIN', [
                ['=OPTION', 'dump_attachment'],
                ['=SPECIFIER', '@stream_specifier']
            ]],
            ['@filename']
        ]
    def _schema_noautorotate(self):
        # -noautorotate
        return self._schema_OPTION('noautorotate')
