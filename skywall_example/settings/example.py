from skywall.core.settings import IntegerSetting, register_setting


@register_setting
class ExampleSetting(IntegerSetting):
    name = 'example'
    help = 'Example Skywall module setting (Default: 47)'

    def default(self):
        return 47
