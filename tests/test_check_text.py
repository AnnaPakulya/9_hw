from selenium.webdriver.support.expected_conditions import element_to_be_selected

from pages.demoqa import DemoQa
from pages.elemets_page import ElementsPage

def test_check_text_dq(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()

    assert str(demo_qa_page.ftr_element.get_text()) == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

def test_check_text_elp(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.btn_element.click()
    assert elements_page.equal_url()

    assert str(elements_page.cntr_element.get_text()) == "Please select an item from left to start practice."

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbook.exist()
