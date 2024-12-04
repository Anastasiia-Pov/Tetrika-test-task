from bs4 import BeautifulSoup
import requests
import csv
import re


def count_animals(url, domain="https://ru.wikipedia.org"):
    # результирующий словарь
    result = dict()

    while url:
        res = requests.get(url=url)
        soup = BeautifulSoup(res.text, 'lxml')

        # считаем животных на текущей web-странице
        columns = soup.find('div', class_='mw-category mw-category-columns')
        if not columns:
            break
        columns = columns.find_all('div', class_='mw-category-group')
        for column in columns:
            animals = column.find('ul').find_all('li')
            # список/списки животных по буквам
            animals_list = list(map(lambda x: x.get_text(), animals))
            # первая буква первого животного в списке
            letter = animals_list[0][0]
            if re.match('[А-Я]', letter):
                result[letter] = result.get(letter, 0) + len(animals_list)
            else:
                break
        # ищем следующую ссылку
        link = soup.find('a', string='Следующая страница')
        if link:
            url = domain + link['href']
        else:
            break
    return result

def write_result(result, filename):
    with open(filename, 'w+', newline='') as file:
        writer = csv.writer(file)
        for key, value in result.items():
            writer.writerow([key, value])


# запускаем функцию count_animals() для парсинга страниц
url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
animals_count = count_animals(url)
# записываем результат парсинга в файл beasts.csv
write_result(animals_count, filename='beasts.csv')


