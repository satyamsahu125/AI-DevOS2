class MemoryBootstrap:

    _manager = None

    def __init__(self):

        self.factory = MemoryFactory()

    def build(self):

        if MemoryBootstrap._manager is not None:

            return MemoryBootstrap._manager

        manager = MemoryManager()

        memories = [

            "business",
            "architecture",
            "workflow",
            "review",
            "decision",
            "issues",
            "runtime",
            "knowledge",
            "artifact",
            "workspace",
            "session",
            "dependency",
            "qa",

        ]

        for name in memories:

            manager.register(

                name,

                self.factory.create(name),

            )

        MemoryBootstrap._manager = manager

        return manager