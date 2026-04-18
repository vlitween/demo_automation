import allure

import variables
from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.main import MainPageLocators
from framework.page_object.pages.components.footer import Footer
from framework.page_object.pages.components.header import Header
from framework.page_object.pages.components.partners_and_sponsors import \
    PartnersAndSponsors
from framework.page_object.pages.components.support_project import \
    SupportProject


class MainPage(BasePage):

    @property
    def url(self):
        if self.device.locale == 'en':
            locale = ''
        else:
            locale = f'{self.device.locale}/'
        return f'{variables.MAIN_URL}/{locale}'

    @property
    def locators(self):
        return MainPageLocators(self.device)

    @property
    def header(self):
        return Header(self.device, translation_supported=True)

    @property
    def footer(self):
        return Footer(self.device, translation_supported=True)

    @property
    def partners_and_sponsors(self):
        return PartnersAndSponsors(self.device)

    @property
    def support_project(self):
        return SupportProject(self.device)

    def check_page_presence(self, fast_check=False):
        with allure.step('Wait page title'):
            self.actions.wait_page_title(self.translator.get_translation('main.page_title'))
        with allure.step('Check page url'):
            self.check_page_url()
        with allure.step('Check page header'):
            self.header.check_presence()
        with allure.step('Check head section'):
            self.check_presence_head_section()
        if fast_check:
            return
        with allure.step('Check Getting Started section'):
            self.check_presence_getting_started_section()
        with allure.step('Check presence Partners and Sponsors section'):
            self.partners_and_sponsors.check_presence_partners_and_sponsors_section()
        with allure.step('Check presence News section'):
            self.check_presence_news_section()
        with allure.step('Check presence Support Project section'):
            self.support_project.check_presence_partners_and_sponsors_section()
        with allure.step('Check presence Donate to Selenium section'):
            self.check_presence_donate_section()
        with allure.step('Check page footer'):
            self.footer.check_presence()

    def check_presence_head_section(self):
        self.actions.check_item_exists(self.locators.head_section)

    def check_presence_getting_started_section(self):
        with allure.step('Scroll to Getting Started section'):
            title = self.actions.check_item_exists(self.locators.getting_started_title)
            self.actions.scroll_to_element(title)

        with allure.step('Check presence section title'):
            self.actions.check_item_exists(self.locators.getting_started_title)

        with allure.step('Check presence Selenium WebDriver block'):
            webdriver_block = self.actions.check_item_exists(self.locators.getting_started_webdriver_block)
            image = self.actions.check_item_exists(self.locators.getting_started_block_image, webdriver_block)
            self.actions.verify_image(image, 'resources/images/main/getting_started/webdriver.png')
            title = self.actions.check_item_exists(self.locators.getting_started_block_title, webdriver_block)
            self.checks.verify_strings(self.actions.get_element_text(title),
                                       self.translator.get_translation('main.getting_started.webdriver.title'))
            description = self.actions.check_item_exists(self.locators.getting_started_block_description, webdriver_block)
            self.checks.verify_strings(self.actions.get_element_text(description),
                                       self.translator.get_translation('main.getting_started.webdriver.description'))
            link = self.actions.check_item_exists(self.locators.getting_started_block_link, webdriver_block)
            self.checks.verify_strings(self.actions.get_element_text(link).upper(),
                                       self.translator.get_translation('main.getting_started.webdriver.link'))

        with allure.step('Check presence Selenium IDE block'):
            ide_block = self.actions.check_item_exists(self.locators.getting_started_ide_block)
            image = self.actions.check_item_exists(self.locators.getting_started_block_image, ide_block)
            self.actions.verify_image(image, 'resources/images/main/getting_started/ide.png')
            title = self.actions.check_item_exists(self.locators.getting_started_block_title, ide_block)
            self.checks.verify_strings(self.actions.get_element_text(title),
                                       self.translator.get_translation('main.getting_started.ide.title'))
            description = self.actions.check_item_exists(self.locators.getting_started_block_description, ide_block)
            self.checks.verify_strings(self.actions.get_element_text(description),
                                       self.translator.get_translation('main.getting_started.ide.description'))
            link = self.actions.check_item_exists(self.locators.getting_started_block_link, ide_block)
            self.checks.verify_strings(self.actions.get_element_text(link).upper(),
                                       self.translator.get_translation('main.getting_started.ide.link'))

        with allure.step('Check presence Selenium Grid block'):
            grid_block = self.actions.check_item_exists(self.locators.getting_started_grid_block)
            image = self.actions.check_item_exists(self.locators.getting_started_block_image, grid_block)
            self.actions.verify_image(image, 'resources/images/main/getting_started/grid.png')
            title = self.actions.check_item_exists(self.locators.getting_started_block_title, grid_block)
            self.checks.verify_strings(self.actions.get_element_text(title),
                                       self.translator.get_translation('main.getting_started.grid.title'))
            description = self.actions.check_item_exists(self.locators.getting_started_block_description, grid_block)
            self.checks.verify_strings(self.actions.get_element_text(description),
                                       self.translator.get_translation('main.getting_started.grid.description'))
            link = self.actions.check_item_exists(self.locators.getting_started_block_link, grid_block)
            self.checks.verify_strings(self.actions.get_element_text(link).upper(),
                                       self.translator.get_translation('main.getting_started.grid.link'))

    def check_presence_news_section(self):
        with allure.step('Scroll to News section'):
            title = self.actions.check_item_exists(self.locators.news_section_title)
            self.actions.scroll_to_element(title)
        with allure.step('Check presence News section title'):
            self.actions.check_item_exists(self.locators.news_section_title)
        # Unblocking fix since news items are currently displayed only with English version of the site
        if self.device.locale == 'en':
            with allure.step('Validate News items'):
                self.validate_news_items_elements()
        with allure.step('Check presence News section More News link'):
            self.actions.check_item_exists(self.locators.news_section_more_news_link)

    def news_items_generator(self):
        news_items = self.actions.find_elements(self.locators.news_item)
        for item in news_items:
            result = {
                'title': self.actions.get_element_text(self.actions.find_sub_element(item, self.locators.news_item_title)),
                'date': self.actions.get_element_text(self.actions.find_sub_element(item, self.locators.news_item_date)),
                'author': self.actions.get_element_text(self.actions.find_sub_element(item, self.locators.news_item_author)),
                'author_link': self.actions.find_sub_element(item, self.locators.news_item_author_link),
                'description': self.actions.get_element_text(self.actions.find_sub_element(item, self.locators.news_item_description)),
                'read_more_link': self.actions.find_sub_element(item, self.locators.news_item_read_more_link)
            }
            yield result

    def validate_news_items_elements(self):
        for news_item in self.news_items_generator():
            title = news_item.get('title')
            date = news_item.get('date')
            author = news_item.get('author')
            author_link = news_item.get('author_link')
            description = news_item.get('description')
            read_more_link = news_item.get('read_more_link')

            with allure.step('Validate news item title'):
                self.checks.check_text_present(title)
            with allure.step('Validate news item date'):
                self.checks.validate_date_text(date)
            with allure.step('Validate news item author'):
                self.checks.validate_string_by_pattern(author, r'^By\s+.+?@\w+$')
            with allure.step('Validate news item author link'):
                self.checks.check_text_present(self.actions.get_element_attribute(author_link, 'href'))
            with allure.step('Validate news item description'):
                self.checks.check_text_present(description)
            with allure.step('Validate news item Read More link'):
                self.checks.check_text_present(self.actions.get_element_attribute(read_more_link, 'href'))

    def check_presence_donate_section(self):
        with allure.step('Scroll to Donate to Selenium section'):
            title = self.actions.check_item_exists(self.locators.donate_section_title)
            self.actions.scroll_to_element(title)
        with allure.step('Check presence Donate to Selenium title'):
            self.actions.check_item_exists(self.locators.donate_section_title)
        with allure.step('Check presence Donate to Selenium description'):
            self.actions.check_item_exists(self.locators.donate_section_description)
        with allure.step('Check presence Donate to Selenium description link'):
            self.actions.check_item_exists(self.locators.donate_section_description_link)
