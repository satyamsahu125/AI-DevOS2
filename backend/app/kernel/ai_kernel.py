"""
AI Kernel

The AI Kernel is the central coordinator
of AI DevOS.

It does not execute business logic.

It only coordinates services.
"""

from app.kernel.dispatcher import Dispatcher
from app.kernel.event_bus import EventBus

from app.services.context_service import ContextService
from app.services.memory_service import MemoryService
from app.services.session_service import SessionService


class AIKernel:

    def __init__(self):

        self.dispatcher = Dispatcher()

        self.events = EventBus()

        self.context = ContextService()

        self.memory = MemoryService()

        self.session = SessionService()

    def register(
        self,
        name,
        handler,
    ):

        self.dispatcher.register(

            name,

            handler,

        )

    def dispatch(
        self,
        name,
        *args,
        **kwargs,
    ):

        return self.dispatcher.dispatch(

            name,

            *args,

            **kwargs,

        )