from skywall.core.reports import AbstractReport, register_report


@register_report
class HostnameReport(AbstractReport):
    name = 'example'
    label = 'Example'

    def __init__(self):
        self.counter = 0

    def collect(self):
        self.counter += 1
        return 'example {}'.format(self.counter)
