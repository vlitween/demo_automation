import allure

import variables
from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.projects import ProjectsPageLocators
from framework.page_object.pages.components.footer import Footer
from framework.page_object.pages.components.header import Header
from framework.page_object.pages.components.partners_and_sponsors import \
    PartnersAndSponsors
from framework.page_object.pages.components.support_project import \
    SupportProject


class ProjectsPage(BasePage):
    url = f'{variables.MAIN_URL}/projects/'

    @property
    def locators(self):
        return ProjectsPageLocators(self.device)

    @property
    def header(self):
        return Header(self.device)

    @property
    def footer(self):
        return Footer(self.device)

    @property
    def partners_and_sponsors(self):
        return PartnersAndSponsors(self.device)

    @property
    def support_project(self):
        return SupportProject(self.device)

    def check_page_presence(self, fast_check=False):
        with allure.step('Wait page title'):
            self.actions.wait_page_title(self.translator.get_translation('projects.page_title'))
        with allure.step('Check page url'):
            self.check_page_url()
        with allure.step('Check page header'):
            self.header.check_presence()
        with allure.step('Check head section'):
            self.check_presence_head_section()
        if fast_check:
            return
        with allure.step('Check projects'):
            self.check_projects()
        with allure.step('Check presence Partners and Sponsors section'):
            self.partners_and_sponsors.check_presence_partners_and_sponsors_section()
        with allure.step('Check presence Support Project section'):
            self.support_project.check_presence_partners_and_sponsors_section()
        with allure.step('Check page footer'):
            self.footer.check_presence()

    def check_presence_head_section(self):
        self.actions.check_item_exists(self.locators.head_section)

    def check_projects(self):
        expected_data = [
            {
                'header_title': self.translator.get_translation(
                    'projects.projects.webdriver.header.title'
                ),
                'header_description': self.translator.get_translation(
                    'projects.projects.webdriver.header.description'
                ),
                'features': [
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.webdriver.features.simple_and_concise.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.webdriver.features.simple_and_concise.description'
                        ),
                    },
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.webdriver.features.all_browsers.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.webdriver.features.all_browsers.description'
                        ),
                    },
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.webdriver.features.w3c_recommendation.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.webdriver.features.w3c_recommendation.description'
                        ),
                    },
                ],
                'links': [
                    self.translator.get_translation('projects.projects.webdriver.w3c_link'),
                    self.translator.get_translation('projects.projects.learn_more_link'),
                ],
            },
            {
                'header_title': self.translator.get_translation(
                    'projects.projects.ide.header.title'
                ),
                'header_description': self.translator.get_translation(
                    'projects.projects.ide.header.description'
                ),
                'features': [
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.ide.features.web_ready.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.ide.features.web_ready.description'
                        ),
                    },
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.ide.features.easy_debugging.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.ide.features.easy_debugging.description'
                        ),
                    },
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.ide.features.cross_browser_execution.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.ide.features.cross_browser_execution.description'
                        ),
                    },
                ],
                'links': [self.translator.get_translation('projects.projects.learn_more_link')],
            },
            {
                'header_title': self.translator.get_translation(
                    'projects.projects.grid.header.title'
                ),
                'header_description': self.translator.get_translation(
                    'projects.projects.grid.header.description'
                ),
                'features': [
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.grid.features.multiple_browsers.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.grid.features.multiple_browsers.description'
                        ),
                    },
                    {
                        'title': self.translator.get_translation(
                            'projects.projects.grid.features.reduce_execution_time.title'
                        ),
                        'description': self.translator.get_translation(
                            'projects.projects.grid.features.reduce_execution_time.description'
                        ),
                    },
                ],
                'links': [self.translator.get_translation('projects.projects.learn_more_link')],
            },
        ]

        for project in expected_data:
            with allure.step(f'Check presence {project['header_title']} section'):
                project_section = self.actions.check_item_exists(
                    self.locators.projects_list_item(project['header_title']))
            with allure.step(f'Scroll section to top'):
                self.actions.scroll_to_element(project_section)
            with allure.step('Check presence project header description'):
                self.actions.check_item_exists(self.locators.project_header_description(project['header_description']),
                                               project_section)
            with allure.step('Check presence project_image'):
                self.actions.check_item_exists(self.locators.project_image, project_section)
            with allure.step('Check project features'):
                for feature in project['features']:
                    self.actions.check_item_exists(
                        self.locators.project_feature(feature['title'], feature['description']), project_section)
            with allure.step('Check presence project links'):
                for link in project['links']:
                    self.actions.check_item_exists(self.locators.project_link(link), project_section)
