"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""


from collections import namedtuple


campaigns = set()
period_ = 4
profit = [None] * period_
total_profit = 0
company = namedtuple('company', ['Name', 'quarters', 'Profit'])

company_number = int(input('Какое количество предприятиий будет? Введите целое число:\n'))

for i in range(1, company_number+1):
    company_name = input(f'Введите название компаниии {i} :\n')
    profit_ = 0

    for j in range(period_):
        profit[j] = float(input(f'Введите прибыль компании за {j+1}-й квартал, млрд. :\n'))
        profit_ += profit[j]

    comp = company(Name=company_name, quarters=tuple(profit), Profit=profit_)
    campaigns.add(comp)
    total_profit += profit_

average = total_profit / company_number
print(f'Средняя прибыль по компаниям = {average} млрд.')

for i in campaigns:
    if i.Profit > average:
        print(f'Компании с прибылью больше средней "{i.Name}" заработала {i.Profit} млрд.')
    else:
        print(f'Компании с прибылью меньше средней "{i.Name}" заработала {i.Profit} млрд.')
