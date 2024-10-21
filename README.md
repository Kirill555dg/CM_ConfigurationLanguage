# Описание

Этот проект представляет собой инструмент для парсинга учебного конфигурационного языка, который преобразует его в XML-формат. 
В конфигурационном языке поддерживаются константы, массивы, словари и числа. 
Константы могут быть объявлены в начале файла и использоваться в других местах через механизм подстановки. 
Скрипт также обрабатывает ошибки: синтаксические, многократное объявление констант и использование неопределённых констант.

# Установка

Для начала, убедитесь, что у вас установлен Python (версия 3.9 или выше). Затем выполните следующие шаги:
1. ```bash
   git clone https://github.com/Kirill555dg/CM_ConfigurationLanguageParser.git
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

Проект установлен.

# Запуск скрипта

Скрипт принимает текст конфигурационного файла через стандартный ввод и выводит XML в стандартный вывод.

Пример запуска:
```bash
python script.py < input.txt > output.xml
```
Здесь:
- **input.txt** — файл с конфигурационными данными на вашем языке.
- **output.xml** — файл, в который будет записан результат в формате XML.

Также можно запустить скрипт с вводом данных напрямую через консоль:
```bash
python script.py
```
После этого вы можете ввести конфигурацию вручную. Для завершения ввода нажмите ```Ctrl+D``` (Linux/macOS) или ```Ctrl+Z``` (Windows).
# Примеры входных и выходных данных

### Пример 1: Простая конфигурация
**Входные данные:**
```ECL
var base 100
var arr [1,2,3]
cool {
   nums : [54, 13, 12];
   count : |base|;
   users : {
       kerrodar : |arr|;
       mystery : 123
   }
}
```
**Выходные данные (XML):**
```xml
<?xml version="1.0" ?>
<cool>
    <nums type="array">
        <element type="int">54</element>
        <element type="int">13</element>
        <element type="int">12</element>
    </nums>
    <count type="int">100</count>
    <users type="dict">
        <kerrodar type="array">
            <element type="int">1</element>
            <element type="int">2</element>
            <element type="int">3</element>
        </kerrodar>
        <mystery type="int">123</mystery>
    </users>
</cool>
```


### Пример 2: Настройка базы данных
**Входные данные:**
```ECL
var max_conn 100
var timeout 30
database {
    database : {
        host : 19216801;
        port : 5432;
        max_connections : |max_conn|;
        connection_timeout : |timeout|
    }
}
```
**Выходные данные (XML):**
```xml
<?xml version="1.0" ?>
<database>
    <database type="dict">
        <host type="int">19216801</host>
        <port type="int">5432</port>
        <max_connections type="int">100</max_connections>
        <connection_timeout type="int">30</connection_timeout>
    </database>
</database>
```


### Пример 3: Конфигурация веб-приложения
**Входные данные:**
```ECL
var max_threads 8
web_config {
    webserver : {
        hostname : 127001;
        port : 8080;
        threads : |max_threads|;
        routes : {
            home : 1;
            login : 2;
            logout : 3
        }
    }
}
```
**Выходные данные (XML):**
```xml
<?xml version="1.0" ?>
<web_config>
    <webserver type="dict">
        <hostname type="int">127001</hostname>
        <port type="int">8080</port>
        <threads type="int">8</threads>
        <routes type="dict">
            <home type="int">1</home>
            <login type="int">2</login>
            <logout type="int">3</logout>
        </routes>
    </webserver>
</web_config>
```


### Пример 4: Конфигурация системы мониторинга
**Входные данные:**
```ECL
var interval 15
var retention 365
monitoring_config {
    monitoring : {
        interval : |interval|;
        retention_days : |retention|;
        services : [1, 2, 3, 4]
    }
}
```
**Выходные данные (XML):**
```xml
<?xml version="1.0" ?>
<monitoring_config>
    <monitoring type="dict">
        <interval type="int">15</interval>
        <retention_days type="int">365</retention_days>
        <services type="array">
            <element type="int">1</element>
            <element type="int">2</element>
            <element type="int">3</element>
            <element type="int">4</element>
        </services>
    </monitoring>
</monitoring_config>
```

# Тесты

Для всех методов были написаны тесты, в результате удалось добиться покрытия в 94%.
Перед запуском тестов, нужно перейти в директорию, где находится файл test_script.py

Шаги запуска тестов:
1. Установить библиотеку pytest:
   ```shell
   pip install pytest
   ```
2. Установить библиотеку coverage:
   ```shell
   pip install coverage
   ```
3. Для запуска тестирования необходимо запустить следующий скрипт:
   ```shell
   pytest -v
   ```
4. Для генерации отчета о покрытии тестами необходимо выполнить команду:
   ```shell
   coverage run --branch -m pytest test_script.py
   ```
5. Просмотр результатов покрытия:
   ```shell
   coverage report
   ```

## Прохождение тестов:
![image](https://github.com/user-attachments/assets/0a9dfd4c-f815-4e96-87dc-dc1ba4a647cc)


## Процент покрытия:
![image](https://github.com/user-attachments/assets/f23f8a46-ec6b-487f-bc8b-7f67c1525c7e)
