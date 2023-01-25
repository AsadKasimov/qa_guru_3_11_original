"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('test_github_param', ['desktop'], indirect=True)
def test_github_desktop(test_github_param):
    browser.open('https://github.com/')
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('test_github_param', ['mobile'], indirect=True)
def test_github_mobile(test_github_param):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))