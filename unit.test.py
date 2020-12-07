from unittest import TestCase
import login


class Test_password_creator(TestCase):
    def test_password_creator(self):
        self.assertEqual(len(login.password_creator()), 10)
        self.assertEqual(type(login.password_creator()), str)
        self.assertIsNotNone(login.password_creator())
        for k in login.password_creator():
            self.assertIn(k, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
