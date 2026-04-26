class Service:
    def __init__(self, config):
        self.config = config

    @property
    def people(self):
        from framework.api.resources.people import PeopleResource
        return PeopleResource(self.config)
