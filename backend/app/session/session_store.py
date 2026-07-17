class SessionStore:

    def __init__(self):

        self.sessions = {}

    def key(

        self,

        project,

        stage,

    ):

        return f"{project}:{stage}"

    def save(

        self,

        session,

    ):

        self.sessions[

            self.key(

                session.project,

                session.stage,

            )

        ] = session

    def get(

        self,

        project,

        stage,

    ):

        return self.sessions.get(

            self.key(

                project,

                stage,

            )

        )

    def remove(

        self,

        project,

        stage,

    ):

        self.sessions.pop(

            self.key(

                project,

                stage,

            ),

            None,

        )