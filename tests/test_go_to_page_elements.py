from pages.demoqa import DemoQa
from pages.elemets_page import ElementsPage

def test_go_to_page_elements (browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    # demo_qa_page.click_on_the_icon()
    # assert demo_qa_page.exist_icon()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_element.click()
    assert elements_page.equal_url()