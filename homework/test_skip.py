"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('width, height', [(1080, 720), (900, 300)])
def test_github_desktop_scip(width, height):
    browser.open('https://github.com/')
    if width == 900:
        pytest.skip('тут тест для пк')
    browser.driver.set_window_size(width, height)
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('width, height', [(1080, 720), (900, 300)])
def test_github_desktop_scip(width, height):
    browser.open('https://github.com/')
    if width == 1080:
        pytest.skip('тут тест для мобилок')
    browser.driver.set_window_size(height, width)
    browser.element(".Button-content").click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
