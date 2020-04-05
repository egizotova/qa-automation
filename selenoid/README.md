Изначальная установка selenoid локально

1. Описане тут
    https://aerokube.com/cm/latest/
2. в cmd выполняем
    curl -s https://aerokube.com/cm/bash | bash && ./cm selenoid start --vnc
3. selenoid скачается и стартует на локальной машине
4. проверяем что он появился в докере выполянем в cmd
    docker ps
    будет запущен контейнер
    CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS              PORTS                    NAMES
    134809e1dbb3        aerokube/selenoid:latest   "/usr/bin/selenoid -…"   13 minutes ago      Up 13 minutes       0.0.0.0:4444->4444/tcp   selenoid
5. проверяем в браузере что запустился
    http://localhost:4444/status
    откроется страница с текскои примерно таким
       {"total":5,"used":0,"queued":0,"pending":0,"browsers":{"chrome":{"79.0":{},"80.0":{}},"opera":{"66.0":{},"67.0":{}}}}

Перезапуск контейнера

1. Ищем процесс в докере 
    docker ps
    копируем CONTAINER ID (см п 4 по установке)
2. убиваем контейнер
    docker kill 134809e1dbb3
3. удаляем контейнер selenoid
    docker rm selenoid
4. запускаем конейнер
    ./cm selenoid start --vnc --args "-limit=10"
5. запускаем конейнер для веб
    ./cm selenoid-ui start
6. проверяем что он запустился в веб
    http://localhost:8080/#/
7. обязательно в браузере после рестарта дергаем http://localhost:4444/status
    
добваляем определенную версию в браузере

1. версии ищем тут
2. добавляем в докер образ 
    docker pull selenoid/chrome:56.0
3. добавляем его в .aerocube/selenoid/browsers.json
 
    

  
    


 