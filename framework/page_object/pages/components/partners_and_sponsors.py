import allure

from framework.page_object.base.base_page import BasePage
from framework.page_object.locators.partners_and_sponsors import \
    PartnersAndSponsorsLocators


class PartnersAndSponsors(BasePage):
    @property
    def locators(self):
        return PartnersAndSponsorsLocators(self.device)

    def check_presence_partners_and_sponsors_section(self):
        with allure.step('Scroll to partners and sponsors section'):
            title = self.actions.check_item_exists(self.locators.development_partners_title)
            self.actions.scroll_to_element(title)

        with allure.step('Check presence Development Partners title'):
            self.actions.check_item_exists(self.locators.development_partners_title)

        with allure.step('Check presence Development Partners links and images'):
            link = self.actions.check_item_exists(self.locators.browserstack_link)
            image = self.actions.find_sub_element(link, self.locators.link_image)
            self.actions.verify_image(image, 'resources/images/partners_and_sponsors/browserstack.png')

            link = self.actions.check_item_exists(self.locators.saucelabs_link)
            image = self.actions.find_sub_element(link, self.locators.link_image)
            self.actions.verify_image(image, 'resources/images/partners_and_sponsors/saucelabs.png')

            link = self.actions.check_item_exists(self.locators.testmu_link)
            image = self.actions.find_sub_element(link, self.locators.link_image)
            self.actions.verify_image(image, 'resources/images/partners_and_sponsors/testmu-ai.png')

        with allure.step('Check presence Sponsors title'):
            self.actions.check_item_exists(self.locators.sponsors_title)

        with allure.step('Check presence Selenium Level Sponsors links and images'):
            link = self.actions.check_item_exists(self.locators.bright_data_link)
            image = self.actions.find_sub_element(link, self.locators.link_image)
            self.actions.verify_image(image, 'resources/images/partners_and_sponsors/bright-data.png')

            link = self.actions.check_item_exists(self.locators.applitools_link)
            image = self.actions.find_sub_element(link, self.locators.link_image)
            self.actions.verify_image(image, 'resources/images/partners_and_sponsors/applitools.png')

            link = self.actions.check_item_exists(self.locators.thordata_link)
            image = self.actions.find_sub_element(link, self.locators.link_image)
            self.actions.verify_image(image, 'resources/images/partners_and_sponsors/thordata.png')
