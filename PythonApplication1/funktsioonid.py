# задаём имя файла, в который будем сохранять контакты
faili_nimi = "kontaktid.txt"

# функция для чтения контактов из файла
def loe_failist():
    kontaktid = []  # создаём пустой список для хранения всех контактов
    try:
        with open(faili_nimi, "r", encoding="utf-8") as f:  # открываем файл в режиме чтения
            for rida in f:  # проходимся по каждой строке в файле
                osad = rida.strip().split(";")  # удаляем лишние пробелы и разбиваем строку по разделителю ";"
                if len(osad) == 3:  # проверяем, что в строке 3 элемента (имя, телефон, email)
                    kontaktid.append({"nimi": osad[0], "telefon": osad[1], "email": osad[2]})  # добавляем как словарь
    except FileNotFoundError:
        open(faili_nimi, "w", encoding="utf-8").close()  # если файл не найден, создаём пустой файл
    return kontaktid  # возвращаем список контактов

# функция для записи всех контактов в файл
def kirjuta_failisse(kontaktid):
    with open(faili_nimi, "w", encoding="utf-8") as f:  # открываем файл в режиме перезаписи
        for k in kontaktid:  # проходимся по каждому контакту в списке
            # записываем в строку имя, телефон и email через ";"
            f.write(f"{k['nimi']};{k['telefon']};{k['email']}\n")

# функция для добавления нового контакта
def lisa_kontakt(nimi, telefon, email):
    kontaktid = loe_failist()  # читаем текущие контакты
    kontaktid.append({"nimi": nimi, "telefon": telefon, "email": email})  # добавляем новый контакт
    kirjuta_failisse(kontaktid)  # сохраняем изменения в файл

# функция для отображения всех контактов
def kuva_kontaktid():
    kontaktid = loe_failist()  # читаем контакты из файла
    if kontaktid:  # если список не пустой
        for k in kontaktid:  # выводим каждый контакт построчно
            print(f"{k['nimi']} | {k['telefon']} | {k['email']}")
    else:
        print("📭 Kontaktid puuduvad.")  # если контактов нет — выводим сообщение

# функция для поиска контакта по имени
def otsi_kontakti(nimi):
    kontaktid = loe_failist()  # читаем все контакты
    tulemused = [k for k in kontaktid if k['nimi'].lower() == nimi.lower()]  # ищем совпадения без учёта регистра
    return tulemused  # возвращаем найденные контакты (может быть 0 или больше)

# функция для удаления контакта по имени
def kustuta_kontakt(nimi):
    kontaktid = loe_failist()  # читаем все контакты
    uus_list = [k for k in kontaktid if k['nimi'].lower() != nimi.lower()]  # убираем те, чьё имя совпадает
    kirjuta_failisse(uus_list)  # сохраняем обновлённый список в файл

# функция для изменения данных у существующего контакта
def muuda_kontakti(vana_nimi, uus_nimi, uus_telefon, uus_email):
    kontaktid = loe_failist()  # читаем все контакты
    for k in kontaktid:
        if k['nimi'].lower() == vana_nimi.lower():  # ищем контакт по старому имени
            k['nimi'] = uus_nimi  # заменяем имя
            k['telefon'] = uus_telefon  # заменяем телефон
            k['email'] = uus_email  # заменяем email
    kirjuta_failisse(kontaktid)  # сохраняем изменения в файл

# функция для сортировки списка контактов по имени, телефону или email'у
def sorteeri_kontaktid(kriteerium):
    kontaktid = loe_failist()  # читаем все контакты
    if kriteerium in ["nimi", "telefon", "email"]:  # проверяем, что сортируем по допустимому полю
        kontaktid.sort(key=lambda x: x[kriteerium].lower())  # сортируем по нужному ключу (регистр не учитываем)
    return kontaktid  # возвращаем отсортированный список

