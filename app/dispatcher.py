class Dispatcher(object):

    def __init__(self):
        self.action_listeners = []
        self.render_listeners = []

    def dispatch_action(self, action_id, handler):
        self._dipatch(self.action_listeners, action_id, handler)

    def dispatch_render(self, action_id, handler):
        self._dipatch(self.render_listeners, action_id, handler)

    def action(self, action_id, *args, **kwargs):
        self._trigger(self.action_listeners, action_id, *args, **kwargs)

    def render(self, render_id, *args, **kwargs):
        self._trigger(self.render_listeners, render_id, *args, **kwargs)

    def _dipatch(self, listeners, action_id, handler):
        listeners.append({
            'id': action_id,
            'handler': handler
        })

    def _trigger(self, listeners, listener_id, *args, **kwargs):
        target_listeners = filter(lambda x: x['id'] == listener_id, listeners)
        for listener in target_listeners:
            listener['handler'](*args, **kwargs)
