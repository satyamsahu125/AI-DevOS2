class MemoryStorage:

    def __init__(self):

        self.records = {}

    def put(

        self,

        key,

        value,

    ):

        self.records[key] = value

    def get(

        self,

        key,

    ):

        return self.records.get(key)

    def delete(

        self,

        key,

    ):

        self.records.pop(

            key,

            None,

        )

    def all(self):

        return self.records