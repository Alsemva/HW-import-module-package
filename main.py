from application.salary import calculate_salary
from application.db.people import get_employee
from datetime import date
from colorama import Fore, Style
from dirty_main import *


def current_date():
    cur_date = date.today()
    return print(Fore.GREEN + f'Current date: {cur_date}\n' + Style.RESET_ALL)


def main():
    calculate_salary()
    get_employee()
    current_date()
    function_1()
    function_2()
    function_3()


if __name__ == '__main__':
    main()
