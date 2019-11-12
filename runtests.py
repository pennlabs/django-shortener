import sys

import django
from xmlrunner.extra.djangotestrunner import XMLTestRunner


django.setup()
test_runner = XMLTestRunner(verbosity=2)

failures = test_runner.run_tests(["tests"])
if failures:
    sys.exit(failures)
