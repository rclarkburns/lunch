from pyfiglet import Figlet
import pkg_resources

def lunch_text():
    _version = pkg_resources.require("lunch")[0].version
    f = Figlet(font='smkeyboard')

    print f.renderText('LUNCH')
    print 'Lunch doesn\'t really do much of anything.'
    print 'Version ' + _version
    print 'Run lunch --help for a lacking list of arguments.'

def setup_text():
    f = Figlet(font='smkeyboard')
    print f.renderText('LUNCH')
    print f.renderText('SETUP')