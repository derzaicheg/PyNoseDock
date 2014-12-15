import nose
import os
import sys
current_path = os.getcwd()
sys.path.insert(1, current_path + '/src')
from test_plugin import test_plugin
from tappy import Tappy

if __name__ == "__main__":
    
    nose.main(addplugins=[test_plugin(), Tappy()])

