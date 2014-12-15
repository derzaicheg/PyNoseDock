from nose.tools import with_setup
from HttpHelper import HttpHelper
import unittest
import sys
import logging
from tappy import Tappy

log = logging.getLogger(__name__)

class my_test(unittest.TestCase):

    def setup(self):
        print "set up test fixtures"

    def teardown(self):
        print "tear down test fixtures"

    @with_setup(setup, teardown)
    def test(self):
        url = 'http://httpbin.org'
        params = None
        headers = None
        h = HttpHelper()
        res = h.get(url, params, headers)
        print("Hello, world!")
        self.assertEqual(201, res.status_code, 'Expected status: ' + str(201) + ' does not equal to actual: ' + str(res.status_code))
        print res.status_code
        
    @with_setup(setup, teardown)
    def test1(self):
        url = 'http://httpbin.org'
        params = None
        headers = None
        h = HttpHelper()
        res = h.get(url, params, headers)
        print("Hello, world!")
        self.assertEqual(1, 2)
        log.info(res.status_code)
        
    @with_setup(setup, teardown)
    def test2(self):
        url = 'http://httpbin.org'
        params = None
        headers = None
        h = HttpHelper()
        res = h.get(url, params, headers)
        sys.stderr.write("world\n")
        self.assertEqual(200, res.status_code, 'Expected status: ' + str(200) + ' does not equal to actual: ' + str(res.status_code))
        print res.status_code
        
    @with_setup(setup, teardown)
    def test3(self):
        url = 'http://httpbin.org'
        params = None
        headers = None
        h = HttpHelper()
        res = h.get(url, params, headers)
        self.assertEqual(200, res.status_code, 'Expected status: ' + str(200) + ' does not equal to actual: ' + str(res.status_code))
        print res.status_code
        
