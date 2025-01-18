# CMS 
**CMS** – консольное приложение для изменения ссылок в html-файлах для разных сайтах. 

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать.

2. Установить [Python](https://www.python.org/downloads/) версии 3.11 и выше. Рекомендуется добавить в PATH.

3. Открыть каталог со скриптом в консоли: можно воспользоваться командой cd или встроенными возможностями файлового менеджера.

4. Создать виртуальное окружение Python.

```
python -m venv .venv
```

5. Активировать вирутальное окружение.

#### Для Windows.
    
```shell
.venv\Scripts\activate.bat
```

#### Для Linux или MacOS.

```bash
source .venv/bin/activate
```

6. Установить зависимости скрипта.

```
pip install -r requirements.txt
```

7. Создать папку Config в корень репозитория. В неё добавить файл JSON для каждого сайта со структурой представленной ниже.

```JSON
{
    "name": "",
    "mount": "",
    "sites": {
        "Telegram": {
            "property": "class",
            "value": "btn telegram",
            "files": [
                ""
            ]
        }
    }
}
```

```JSON
"name": ""
```

Название сайта.

```JSON
"mount": ""
```

Общий путь к папке, где необходимо что-то изменить. Не указывать название файла!

```JSON
"sites": {}
```

Словарь, в котором описывается что и где необходимо поменять. Где ключ, название опознавателя для ссылки, которую нужно поменять.

```JSON
"property": "",
```

Тип атрибута, по которому происходит поиск ссылки. 

```JSON
"value": "", 
```

Название атрибута, по которому происходит поиск ссылки. 

```JSON
"files": [""]
```

Список путей к файлу/файлам html, в которых нужно поменять ссылки. В итоге, путь к файлу складывается из двух частей из значения ключа mount и значения/значений ключа files.

8. Запустить файл _main.py_.
```
python main.py
``` 

---
**_Copyright © Dub Irina. 2024-2025._**
