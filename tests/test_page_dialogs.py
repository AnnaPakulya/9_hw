from pages.demoqa import DemoQa
from pages.elemets_page import ElementsPage
from pages.modal_dialogs import ModalPage
import time

def test_modal_elements (browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    modal_page = ModalPage(browser)

    modal_page.visit()
    assert modal_page.links.check_count_elements(count=5)

# def test_navigation_modal(browser):
#     demo_qa_page = DemoQa(browser)
#     elements_page = ElementsPage(browser)
#     modal_page = ModalPage(browser)
#
#     modal_page.visit()
#     modal_page.refresh()
#
#     modal_page.hdr_element.click()
#     time.sleep(3)
#     browser.back()
#     browser.set_window_size(900, 400)
#     browser.forward()
#     assert demo_qa_page.equal_url()
#     assert demo_qa_page.icon.visible()

