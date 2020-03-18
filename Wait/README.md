запустить pylint в Terminal
pylint Wait/test_waits_product_page.py

в conftest:
    default="https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41",

в проверках значений изменить 
    basket = browser.find_element_by_id(ProductPage.basket).text
    assert basket == " "