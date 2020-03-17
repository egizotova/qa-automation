Opencart (архитектура):

- локаторы (селекторы) по странично
-- главная страница https://demo.opencart.com/
-- страница товара https://demo.opencart.com/index.php?route=product/product&product_id=40
-- страница каталога https://demo.opencart.com/index.php?route=product/category&path=33
-- страница логина админа https://demo.opencart.com/admin/index.php?route=common/login
-- страница результатов поиска https://demo.opencart.com/index.php?route=product/search&search=iphone

- поиск элементов 
- функции поиска элементов
На каждый экран по одному тесту, которые просто проверяют наличие элементов.
Т.е. открывается экран и последовательно вызываются функции поиска УНИКАЛЬНЫХ элементов,
 минимум по 5 на каждой странице.