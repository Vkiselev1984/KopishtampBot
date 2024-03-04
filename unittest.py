import unittest
from aiogram import types
from app.handlers import send_welcome

class TestSendWelcome(unittest.TestCase):
    def test_send_welcome(self):
        message = types.Message(chat=types.Chat(id=1), from_user=types.User(id=1, first_name='John'))
        reply = send_welcome(message)
        self.assertEqual(reply.text, 'John')