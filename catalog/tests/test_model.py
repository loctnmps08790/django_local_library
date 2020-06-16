from django.test import TestCase


class TestOne(TestCase):

    def setUpTestData(cls):
        print('Run once only')
        pass

    def setUp(self) -> None:
        print('Begin set up')

    def tearDown(self) -> None:
        print('Stop ')

    def test_1(self):
        print('test 1')
        self.assertTrue(True)

    def test_2(self):
        print('test 2')
        self.assertTrue(False)