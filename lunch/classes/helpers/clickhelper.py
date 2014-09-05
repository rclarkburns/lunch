import click
import random


class ClickHelper:

    @staticmethod
    def yes_no(message):
        click.echo(message + '[y or n] RESPOND!', nl=False)
        _c = click.getchar().lower()
        _positiveResponses = ['Away we go.', 'Wonderful news.', 'Fantastic.']
        _negativeResponses = ['I\'m rather sad about that.', 'Have a beer and cheer up.', 'Perhaps another time.']
        click.echo()
        if _c == 'y':
            click.echo(random.choice(_positiveResponses))
            return True
        elif _c == 'n':
            click.echo(random.choice(_negativeResponses) + ' Skipping or aborting.')
            return False
        else:
            click.echo(
                "[y or n] It's simple. Either press the 'y' key to proceed or the 'n' key to skip or abort. RESPOND!")
            ClickHelper.yes_no(message)

    @staticmethod
    def input_prompt(message, hide=False, confirm=False):
        value = click.prompt(message, hide_input=hide, confirmation_prompt=confirm)
        return value