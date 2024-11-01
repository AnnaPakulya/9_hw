import time

from pages.demoqa import DemoQa

def test_navigation (browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(3)
    browser.set_window_size(1000, 1000)
    time.sleep(3)