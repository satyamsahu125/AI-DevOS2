from collections import defaultdict

from app.kernel.events import KernelEvent


class EventBus:

    def __init__(self):

        self.listeners = defaultdict(list)

    def subscribe(

        self,

        event_name: str,

        callback,

    ):

        self.listeners[event_name].append(callback)

    def publish(

        self,

        event: KernelEvent,

    ):

        callbacks = self.listeners.get(

            event.name,

            [],

        )

        for callback in callbacks:

            callback(event)