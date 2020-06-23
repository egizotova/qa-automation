для разбора строки лога используется библиотека https://pypi.org/project/apache-log-parser/
перед запуском скрипта установить библиотеку
    pip install apache-log-parser

запуск сркпипта
     python parse_logs.py -f access.logs -o stat.json
      -f access.logs - файл с access логами
      -o stat.json -  файл куда сохранить результат
      по умолчанию -f = access.logs -o = result.json
        