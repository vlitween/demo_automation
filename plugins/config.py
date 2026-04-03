import os
from json import JSONDecodeError

import pytest
from python_json_config import ConfigBuilder

CONFIG = None


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not config.option.env:
        raise pytest.UsageError('--env option is required')

    config_path = os.path.join(config.rootdir.strpath, 'config', f'{config.option.env}.json')
    if not os.path.exists(config_path):
        raise pytest.UsageError(f'No config file found at {config_path}')

    try:
        config.cfg = ConfigBuilder().parse_config(config_path)
    except JSONDecodeError as e:
        raise pytest.UsageError(f"Error parsing config file '{config.option.env}.json' ({e})")


def pytest_addoption(parser):
    group = parser.getgroup('config')
    group.addoption(
        '--env',
        action='store',
        dest='env',
        default='main',
        help='Environment to use config for'
    )


@pytest.fixture(autouse=True)
def config(request):
    return request.config.cfg
