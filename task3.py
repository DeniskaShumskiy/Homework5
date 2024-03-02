def count_it(sequence):
    # Создаём словарь
    my_dict = {int(item): sequence.count(item) for item in sequence}
    # Сортируем словарь
    sorted_my_dict = sorted(my_dict.items(), key=lambda element: element[1])

    # Возвращаем последние 3 элемента списка, т. е. кортежи с самыми большими значениями
    return dict(sorted_my_dict[-3:])

print(count_it("12312345"))