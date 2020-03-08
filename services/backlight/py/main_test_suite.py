import os
import unittest


def setup_runner(failfast=False):
    runner_ = unittest.TextTestRunner(verbosity=2)

    """exit test on first failure"""
    runner_.failfast = failfast

    return runner_


def run_test_suite(dir_path, search_pattern="*.test.py"):
    """we need __init__.py in dir-path with test files.
    else discover wont find them"""

    suite = unittest.TestLoader().discover(dir_path, search_pattern)
    setup_runner().run(suite)


if __name__ == '__main__':
    run_test_suite(os.getcwd(), '*_test.py')
