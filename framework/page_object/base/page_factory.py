class Page:
    def __init__(self, device):
        self.device = device

    @property
    def main_page(self):
        from framework.page_object.pages.main import MainPage
        return MainPage(self.device)

    @property
    def projects_page(self):
        from framework.page_object.pages.projects import ProjectsPage
        return ProjectsPage(self.device)
