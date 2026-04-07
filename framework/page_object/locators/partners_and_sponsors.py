from framework.page_object.base.base_locator import BaseLocator


class PartnersAndSponsorsLocators(BaseLocator):
    @property
    def development_partners_title(self):
        title = self.translator.get_translation('partners_and_sponsors.development_partners_title')
        return self.new_locator(
            chrome_xpath=f'//h2[@id="dev-partners" and .="{title}"]',
            description=f'Title "{title}"'
        )

    @property
    def sponsors_title(self):
        title = self.translator.get_translation('partners_and_sponsors.sponsors_title')
        return self.new_locator(
            chrome_xpath=f'//h2[@id="selenium-level" and .="{title}"]',
            description=f'Title "{title}"'
        )

    @property
    def browserstack_link(self):
        return self.new_locator(
            chrome_xpath='//a[preceding::h2[@id="dev-partners"] and following::h2[@id="selenium-level"] and .//img[@title="BrowserStack"]]',
            description='Dev partners BrowserStack link'
        )

    @property
    def saucelabs_link(self):
        return self.new_locator(
            chrome_xpath='//a[preceding::h2[@id="dev-partners"] and following::h2[@id="selenium-level"] and .//img[@title="Sauce Labs"]]',
            description='Dev partners Sauce Labs link'
        )

    @property
    def testmu_link(self):
        return self.new_locator(
            chrome_xpath='//a[preceding::h2[@id="dev-partners"] and following::h2[@id="selenium-level"] and .//img[@title="TestMu AI (formerly LambdaTest)"]]',
            description='Dev partners TestMu AI link'
        )

    @property
    def bright_data_link(self):
        return self.new_locator(
            chrome_xpath='//a[preceding::h2[@id="selenium-level"] and .//img[@title="Bright Data"]]',
            description='Sponsors Sauce Labs link'
        )

    @property
    def applitools_link(self):
        return self.new_locator(
            chrome_xpath='//a[preceding::h2[@id="selenium-level"] and .//img[@title="Applitools"]]',
            description='Sponsors Applitools link'
        )

    @property
    def thordata_link(self):
        return self.new_locator(
            chrome_xpath='//a[preceding::h2[@id="selenium-level"] and .//img[@title="Thordata"]]',
            description='Sponsors Thordata link'
        )

    @property
    def link_image(self):
        return self.new_locator(
            chrome_xpath='.//img',
            description='Partners and sponsors link image'
        )
