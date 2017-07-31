from skywall.core.signals import Signal
from skywall.core.commands import AbstractCommand, register_command
from skywall_example.signals import example_signal


@register_command
class ExampleCommand(AbstractCommand):
    name = 'example-echo'
    help = 'Example Skywall module command'
    before_run = Signal('ExampleCommand.before_run')
    after_run = Signal('ExampleCommand.after_run')

    @staticmethod
    def arguments(parser):
        parser.add_argument('names', metavar='names', nargs='+', help='Names to print')

    def run(self, args):
        print('This is example Skywall module command')
        example_signal.emit(value=args)
