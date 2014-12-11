import nose
from nose.plugins import Plugin

class test_plugin(Plugin):
    def options(self, parser, env):
        super(test_plugin, self).options(parser, env)
        parser.add_option("-T", "--test-plugin", action="store_true",
                          default=None,
                          dest="test_plugin",
                          help="this plugin should work")
        
    def configure(self, options, conf):

        super(test_plugin, self).configure(options, conf)
        if options.test_plugin:
            print 'WOOOOOOOORKS'

