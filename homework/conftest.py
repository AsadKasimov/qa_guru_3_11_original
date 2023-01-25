import pytest
from selene.support.shared import browser


@pytest.fixture(params=['desktop', 'mobile'], scope='session')
def test_github_param(request):

    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_width = 1080
    elif request.param == 'mobile':
        browser.config.window_width = 920
        browser.config.window_width = 300
