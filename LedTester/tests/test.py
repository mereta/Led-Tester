from nose.tools import *

from LedTester.main import main
from numpy.ma.testutils import assert_equal

def test_main():
    assert_equal(main("turn on", "turn off", "switch"))
