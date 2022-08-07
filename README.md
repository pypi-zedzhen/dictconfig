# dictconfig
Базовый класс для представлени конфигураций в виде словаря.\
[GitHub](https://github.com/pypi-zedzhen/dictconfig)

## Установка
> pip install dictconfig --index-url=pypi.zedzhen.ru

## Использование
### BaseDictConfig(filename, func_read, func_write)
Объект BaseDictConfig ведёт себя как словарь.
#### filename
путь до файла в виде строки
#### func_read 
Вызываемый объект, первый параметр путь до файла.\
При успешном прочтении должна возвращать словарь.\
Иначе должна вызывать ошибку error.ReadError (иные ошибки не будут подавлены)
#### func_write
Вызываемый объект, первый параметр путь до файла, второй словарь.\
Если запись не удалась, должна вызывать ошибку error.WriteError (иные ошибки не будут подавлены)

### .read()
Перечитывает конфигурацию.\
Возвращает успешность операции.
### .save()
Сохраняет конфигурацию.\
Возвращает успешность операции.