class Dispatcher:

    def __init__(self):

        self.handlers = {}

    def register(

        self,

        name,

        handler,

    ):

        self.handlers[name] = handler

    def dispatch(

        self,

        name,

        *args,

        **kwargs,

    ):

        handler = self.handlers.get(name)

        if handler is None:

            raise ValueError(

                f"No handler registered for '{name}'."

            )

        return handler(

            *args,

            **kwargs,

        )