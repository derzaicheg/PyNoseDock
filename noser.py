import nose
from test_plugin import test_plugin

if __name__ == "__main__":
    nose.main(addplugins=[test_plugin()])

