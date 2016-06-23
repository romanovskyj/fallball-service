#!/usr/bin/env python
import os
import sys
from imp import reload

import django
from django.conf import settings
from django.test.utils import get_runner

import fallball

import sys
print(sys.path)



# As parent directory has also 'fallball' name it needs to specify the package explicitly:

os.environ['DJANGO_SETTINGS_MODULE'] = 'fallball.settings'
django.setup()

TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests(['fallballapp.tests'])
sys.exit(bool(failures))
