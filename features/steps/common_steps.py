import time

from behave import step, then

from framework.page_object.base.base_page import BasePage
from framework.page_object.base.page_factory import Page


def get_page_by_name(page_factory: Page, page_name: str):
    page_names_map = {
        'Main': 'main_page',
        'About Selenium': 'about_selenium_page',
        'Structure and Governance': 'structure_and_governance_page',
        'Events': 'events_page',
        'Ecosystem': 'ecosystem_page',
        'History': 'history_page',
        'Get Involved': 'get_involved_page',
        'Sponsors': 'sponsors_page',
        'Sponsor Us': 'sponsor_us_page',
        'Downloads': 'downloads_page',
        'Documentation': 'documentation_page',
        'Projects': 'projects_page',
        'Support': 'support_page',
        'Blog': 'blog_page'
    }
    property_name = page_names_map.get(page_name)
    if not property_name:
        raise ValueError(f"Unknown page name: {page_name}")
    return getattr(page_factory, property_name)


@step('{page_name} page is opened')
def step_open_page(context, page_name):
    page = get_page_by_name(context.page, page_name)
    page.open_page()


@then('{page_name} page is fully displayed')
def check_page_presence(context, page_name):
    page = get_page_by_name(context.page, page_name)
    page.check_page_presence(fast_check=False)


@then('{page_name} page is displayed')
def check_page_presence(context, page_name):
    page = get_page_by_name(context.page, page_name)
    page.check_page_presence(fast_check=True)


@then('Page title is "{title}"')
def wait_page_title(context, title):
    page = BasePage(context.device)
    page.actions.wait_page_title(title)


@step('Wait {key} seconds')
def wait(context, key):
    time.sleep(int(key))
