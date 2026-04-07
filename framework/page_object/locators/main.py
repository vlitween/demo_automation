from framework.page_object.base.base_locator import BaseLocator


class MainPageLocators(BaseLocator):
    @property
    def head_section(self):
        header_1 = self.translator.get_translation('main.head_section.header_1')
        header_2 = self.translator.get_translation('main.head_section.header_2')
        description_1 = self.translator.get_translation('main.head_section.description_1')
        description_2 = self.translator.get_translation('main.head_section.description_2')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::header][1 and .//h1[.="{header_1}"] and .//p[.="{header_2}"] and .//p[.="{description_1}"] and .//p[.="{description_2}"]]',
            description=f'Header "{header_1} {header_2} {description_1} {description_2}"'
        )

    @property
    def getting_started_title(self):
        title = self.translator.get_translation('main.getting_started.title')
        return self.new_locator(
            chrome_xpath=f'//h2[.="{title}"]',
            description=f'Title "{title}"'
        )

    @property
    def getting_started_webdriver_block(self):
        title = self.translator.get_translation('main.getting_started.title')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::h2[.="{title}"]][1]//div[contains(@class, "card ") and .//h4[contains(@class, "selenium-webdriver")]]',
            description='Getting Started WebDriver block'
        )

    @property
    def getting_started_ide_block(self):
        title = self.translator.get_translation('main.getting_started.title')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::h2[.="{title}"]][1]//div[contains(@class, "card ") and .//h4[contains(@class, "selenium-ide")]]',
            description='Getting Started IDE block'
        )

    @property
    def getting_started_grid_block(self):
        title = self.translator.get_translation('main.getting_started.title')
        return self.new_locator(
            chrome_xpath=f'//section[preceding::h2[.="{title}"]][1]//div[contains(@class, "card ") and .//h4[contains(@class, "selenium-grid")]]',
            description='Getting Started Grid block'
        )

    @property
    def getting_started_block_image(self):
        return self.new_locator(
            chrome_xpath='.//span[contains(@class, "selenium-logo")]//*[local-name()="svg"]',
            description='Getting Started block image'
        )

    @property
    def getting_started_block_title(self):
        return self.new_locator(
            chrome_xpath='.//h4[text()]',
            description='Getting Started block title'
        )

    @property
    def getting_started_block_description(self):
        return self.new_locator(
            chrome_xpath='.//p[text()]',
            description=f'Getting Started block title'
        )

    @property
    def getting_started_block_link(self):
        return self.new_locator(
            chrome_xpath='.//a',
            description='Getting Started block link'
        )

    @property
    def news_section_title(self):
        title = self.translator.get_translation('main.news.title')
        return self.new_locator(
            chrome_xpath=f'//h2[.="{title}"]',
            description=f'News section title "{title}"'
        )

    @property
    def news_item(self):
        return self.new_locator(
            chrome_xpath='//div[contains(@class, "row") and contains(@class, "pb-4")]',
            description='News section item'
        )

    @property
    def news_item_title(self):
        return self.new_locator(
            chrome_xpath='.//h4[contains(@class, "card-title")]',
            description='News item title'
        )

    @property
    def news_item_date(self):
        return self.new_locator(
            chrome_xpath='.//p[contains(@class, "card-text") and contains(@class, "mb-1")]',
            description='News item date'
        )

    @property
    def news_item_author(self):
        return self.new_locator(
            chrome_xpath='.//p[contains(@class, "card-text") and .//a]',
            description='News item author'
        )

    @property
    def news_item_author_link(self):
        return self.new_locator(
            chrome_xpath='.//p[contains(@class, "card-text")]//a',
            description='News item author link'
        )

    @property
    def news_item_description(self):
        return self.new_locator(
            chrome_xpath='.//div[contains(@class, "card-body")]//p[contains(@class, "card-text")]',
            description='News item description'
        )

    @property
    def news_item_read_more_link(self):
        text = self.translator.get_translation('main.news.read_more_link')
        return self.new_locator(
            chrome_xpath=f'.//div[contains(@class, "card-body")]//a[normalize-space()="{text}"]',
            description=f'News item link "{text}"'
        )

    @property
    def news_section_more_news_link(self):
        text = self.translator.get_translation('main.news.more_news_link')
        return self.new_locator(
            chrome_xpath=f'//a[normalize-space()="{text}"]',
            description=f'News section link "{text}"'
        )

    @property
    def donate_section_title(self):
        title = self.translator.get_translation('main.donate.title')
        return self.new_locator(
            chrome_xpath=f'//h2[.="{title}"]',
            description=f'Donate section title "{title}"'
        )

    @property
    def donate_section_description(self):
        description = self.translator.get_translation('main.donate.description')
        return self.new_locator(
            chrome_xpath=f'//h3[normalize-space()="{description}"]',
            description=f'Donate section description "{description}"'
        )

    @property
    def donate_section_description_link(self):
        link_text = self.translator.get_translation('main.donate.description_link')
        return self.new_locator(
            chrome_xpath=f'//h3//a[normalize-space()="{link_text}"]',
            description=f'Donate section description link "{link_text}"'
        )
