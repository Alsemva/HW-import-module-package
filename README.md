# Домашнее задание к лекции 1.«Import. Module. Package»
1. Разработать структуру программы "Бухгалтерия".
 * main.py;
 * application/salary.py;
 * application/db/people.py;<br>
    main.py - основной модуль для запуска программы.<br>
В модуле salary.py функция calculate_salary.<br>
В модуле people.py функция get_employees.
2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.

```Python
if __name__ == '__main__':
```
**Сами функции реализовать не надо.** Достаточно добавить туда какой-либо вывод.
3. Познакомиться с модулем [datetime](https://pythonworld.ru/moduli/modul-datetime.html). При вызове
4. Найти интересный для себя пакет на [pypi](https://pypi.org/) и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.

*5. Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции (необязательное задание)
```Python
from package.module import *
```
