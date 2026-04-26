import pytest

from framework.api.base.service_factory import Service

pytest_plugins = ['plugins.config', 'plugins.allure_api']


@pytest.fixture(scope='function')
def resource(request, config):
    yield Service(config)
