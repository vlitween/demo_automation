class Page:
    def __init__(self, device):
        self.device = device

    @property
    def header_component(self):
        from framework.page_object.pages.components.header import Header
        return Header(self.device)

    @property
    def main_page(self):
        from framework.page_object.pages.main import MainPage
        return MainPage(self.device)

    @property
    def about_selenium_page(self):
        from framework.page_object.pages.about_selenium import \
            AboutSeleniumPage
        return AboutSeleniumPage(self.device)

    @property
    def structure_and_governance_page(self):
        from framework.page_object.pages.structure_and_governance import \
            StructureAndGovernancePage
        return StructureAndGovernancePage(self.device)

    @property
    def events_page(self):
        from framework.page_object.pages.events import EventsPage
        return EventsPage(self.device)

    @property
    def ecosystem_page(self):
        from framework.page_object.pages.ecosystem import EcosystemPage
        return EcosystemPage(self.device)

    @property
    def history_page(self):
        from framework.page_object.pages.history import HistoryPage
        return HistoryPage(self.device)

    @property
    def get_involved_page(self):
        from framework.page_object.pages.get_involved import GetInvolvedPage
        return GetInvolvedPage(self.device)

    @property
    def sponsors_page(self):
        from framework.page_object.pages.sponsors import SponsorsPage
        return SponsorsPage(self.device)

    @property
    def sponsor_us_page(self):
        from framework.page_object.pages.sponsor_us import SponsorUsPage
        return SponsorUsPage(self.device)

    @property
    def downloads_page(self):
        from framework.page_object.pages.downloads import DownloadsPage
        return DownloadsPage(self.device)

    @property
    def documentation_page(self):
        from framework.page_object.pages.documentation import DocumentationPage
        return DocumentationPage(self.device)

    @property
    def projects_page(self):
        from framework.page_object.pages.projects import ProjectsPage
        return ProjectsPage(self.device)

    @property
    def support_page(self):
        from framework.page_object.pages.support import SupportPage
        return SupportPage(self.device)

    @property
    def blog_page(self):
        from framework.page_object.pages.blog import BlogPage
        return BlogPage(self.device)
