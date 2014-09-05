import click
from classes.factory.messagemaker import MessageMaker
from classes.helpers.clickhelper import ClickHelper
import views.welcome as welcome


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        welcome.lunch_text()


# setup
@click.command('setup', short_help="A mock setup command.")
def setup(message='Hello. Would you like to continue with setup?'):
    click.clear()
    welcome.setup_text()
    click_helper = ClickHelper()
    if click_helper.yes_no(message):
        click.echo('Setup complete.')
    else:
        click.echo('Setup canceled.')


# print_simple
@click.command('print_simple', short_help='Outputs a message.')
@click.option('--message', '-m', required=True, help='The message to output.')
def print_simple(message):
    click_helper = ClickHelper()
    simple_message = MessageMaker.factory('Simple')

    if click_helper.yes_no('Would you like to see the default?'):
        simple_message.print_message()

    simple_message.my_message = message

    simple_message.print_message()

#print_fancy
@click.command('print_fancy', short_help='Outputs a fancy message.')
def print_fancy():
    click.clear()
    click_helper = ClickHelper()
    fancy_message = MessageMaker.factory('Fancy')

    if click_helper.yes_no('Would you like to see the default?'):
        fancy_message.print_message()

    fancy_message.my_message = click_helper.input_prompt('Type in the message you would like to display: ')

    if click_helper.yes_no('Would you like to choose the font?'):
        fancy_message.my_font = click_helper.input_prompt('Type in the font you want to use: ')

    fancy_message.print_message()


cli.add_command(setup)
cli.add_command(print_simple)
cli.add_command(print_fancy)