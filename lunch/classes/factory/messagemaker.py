from __future__ import generators

class MessageMaker(object):
    @staticmethod
    def factory(type):
        if type == 'Fancy':
            return Fancy()
        if type == 'Simple':
            return Simple()
        assert 0, 'No configuration is available for: ' + type


class Fancy(MessageMaker):

    def __init__(self):
        Fancy.my_message = 'Fancy message.'
        self.my_font = 'roman'

    @property
    def my_message(self):
        return self.my_message

    @my_message.setter
    def my_message(self, value):
        self.my_message = value

    def print_message(self):
        from pyfiglet import Figlet
        f = Figlet(font=self.my_font)
        print f.renderText(self.my_message)


class Simple(MessageMaker):
    def __init__(self):
        Simple.my_message = 'Simple message.'

    @property
    def my_message(self):
        return self.my_message

    @my_message.setter
    def my_message(self, value):
        self.my_message = value

    def print_message(self):
        print self.my_message