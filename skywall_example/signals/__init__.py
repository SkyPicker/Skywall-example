from skywall.core.signals import Signal


example_signal = Signal('example_signal')


@example_signal.connect
def example_signal_listener(value):
    print('Received example signal: {}'.format(value))
