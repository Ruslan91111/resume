"""
Полностью тестовый тестовый файл, подлежит удалению
"""
from django.test import TestCase
from ..logic import operations

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings')



class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 7, '+')
        self.assertEqual(13, result)

    def test_minus(self):
        result = operations(26, 7, '-')
        self.assertEqual(19, result)

    def test_multiply(self):
        result = operations(26, 7, '*')
        self.assertEqual(182, result)






# Код для чисто учебных целей, чтобы понять, что такое os.environ
# import pprint
# env_var = os.environ
# pprint.pprint(dict(env_var))




