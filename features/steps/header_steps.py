import time

from behave import then, when

from features.steps.common_steps import get_page_by_name


@then('{page_name} page header is displayed')
def check_presence_header(context, page_name):
    current_page = get_page_by_name(context.page, page_name)
    current_page.header.check_presence()


@when('Click header navigation button "{button_name}"')
def click_header_nav_button(context, button_name):
    button_map = {
        'About': 'about',
        'About Selenium': 'about_selenium',
        'Structure and Governance': 'structure_and_governance',
        'Events': 'events',
        'Ecosystem': 'ecosystem',
        'History': 'history',
        'Get Involved': 'get_involved',
        'Sponsors': 'sponsors',
        'Sponsor Us': 'sponsor_us',
        'Downloads': 'downloads',
        'Documentation': 'documentation',
        'Projects': 'projects',
        'Support': 'support',
        'Blog': 'blog'
    }
    suffix = button_map.get(button_name)
    if not suffix:
        raise ValueError(f'Button "{button_name}" not found in mapping.')
    target_method = f'click_{suffix}_button'
    header = context.page.header_component
    method = getattr(header, target_method, None)
    if callable(method):
        method()
        time.sleep(1)   # added slight delay for correct opening nav button pages
    else:
        raise AttributeError(f"Header component has no method named '{target_method}'")


@when('Click header logo')
def click_header_logo(context):
    header = context.page.header_component
    header.click_logo()


@then('About dropdown is displayed')
def check_presence_about_dropdown(context):
    header = context.page.header_component
    header.check_about_dropdown_buttons()
