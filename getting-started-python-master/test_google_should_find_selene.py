from selene import browser
from selene import be, have

def test_one():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene was inspired by Selenide from Java world'))
