from funktsioonid import *  # импортируем все функции из файла funktsioonid.py

 # бесконечный цикл — программа будет работать, пока пользователь не выберет "välju"
print("\n TELEFONIRAAMAT")  # заголовок меню
print("1 - Lisa kontakt")      # пункт меню для добавления
print("2 - Kuva kõik kontaktid")  # показать все
print("3 - Otsi kontakti nime järgi")  # поиск по имени
print("4 - Kustuta kontakt")  # удалить по имени
print("5 - Muuda kontakti")  # изменить данные
print("6 - Sorteeri kontaktid")  # сортировка
print("0 - Välju")  # выход из программы

valik = input("Vali tegevus: ")  # запрашиваем у пользователя выбор

if valik == "1":
        nimi = input("Sisesta nimi: ")  # запрашиваем имя
        telefon = input("Sisesta telefon: ")  # запрашиваем телефон
        email = input("Sisesta e-post: ")  # запрашиваем email
        lisa_kontakt(nimi, telefon, email)  # добавляем контакт
        print("Kontakt lisatud!")

elif valik == "2":
        kuva_kontaktid()  # выводим все контакты

elif valik == "3":
        nimi = input("Sisesta otsitava nimi: ")  # запрашиваем имя
        tulemused = otsi_kontakti(nimi)  # ищем контакт(ы)
        if tulemused:
            for k in tulemused:
                print(f"{k['nimi']} | {k['telefon']} | {k['email']}")  # выводим найденные
        else:
            print("Kontakti ei leitud.")  # если не найдено

elif valik == "4":
        nimi = input("Sisesta kustutatava nimi: ")  # запрашиваем имя для удаления
        kustuta_kontakt(nimi)
        print("Kontakt kustutatud!")

elif valik == "5":
        vana_nimi = input("Sisesta kontakti vana nimi: ")  # указываем, кого редактировать
        uus_nimi = input("Uus nimi: ")  # новое имя
        uus_telefon = input("Uus telefon: ")  # новый телефон
        uus_email = input("Uus e-post: ")  # новый email
        muuda_kontakti(vana_nimi, uus_nimi, uus_telefon, uus_email)
        print("Kontakt muudetud!")

elif valik == "6":
        kriteerium = input("Sorteeri mille järgi (nimi / telefon / email): ").lower()
        kontaktid = sorteeri_kontaktid(kriteerium)
        for k in kontaktid:
            print(f"{k['nimi']} | {k['telefon']} | {k['email']}")  # выводим отсортированный список

elif valik == "0":
        print("Head aega!")
        # выходим из цикла и завершаем программу

else:
        print("Vale valik, proovi uuesti!")  # обработка некорректного ввода


