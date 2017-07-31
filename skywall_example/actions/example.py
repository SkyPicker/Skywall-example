from skywall.core.signals import Signal
from skywall.core.actions import (
        AbstractServerAction, AbstractClientAction, register_server_action, register_client_action
        )


@register_client_action
class PingClientAction(AbstractClientAction):
    name = 'example-ping'
    before_send = Signal('PingClientAction.before_send')
    after_send = Signal('PingClientAction.after_send')
    before_receive = Signal('PingClientAction.before_receive')
    after_receive = Signal('PingClientAction.after_receive')
    after_confirm = Signal('PingClientAction.after_confirm')

    def execute(self, client):
        print('PingClientAction', self.payload)

@register_server_action
class PongServerAction(AbstractServerAction):
    name = 'example-pong'
    before_send = Signal('PongServerAction.before_send')
    after_send = Signal('PongServerAction.after_send')
    before_receive = Signal('PongServerAction.before_receive')
    after_receive = Signal('PongServerAction.after_receive')
    after_confirm = Signal('PongServerAction.after_confirm')

    def execute(self, connection):
        print('PongServerAction', self.payload)
