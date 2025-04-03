print("Создание инфо <3")
print("При поддержке @mifka_post")
print("Автор -> @Mifka174")
print("Вопросы можете задавать автору или в бота @mifka174_bot")

input("Нажмите Enter, чтобы создать себе инфо...")

while True:
    print("Выберите стиль инфо. Все стили в style.py")
    style = input("1 или 2: ")

    if style == "1":
        print("Хороший выбор")
        break
    elif style == "2":
        print("Coming soon...")
        print("Будет первым значит ;)")
        break
    else:
        print("Упс! Вы ввели некорректное число :[")

name_user = input("Напишите свое имя/ник -> ")
username_user = input("Напишите свой юзер в Telegram ЧЕРЕЗ @ -> ")
nazivat_user = input("Как тебя называть? Пример: Хилка, Хилкост, Hilka или Хилка/Хилкост/Hilka -> ")

def get_list_from_input(prompt):
    while True:
        try:
            count = int(input(prompt))
            break
        except ValueError:
            print("Упс! Вы не ввели число, введите число :-[")

    items = []
    for i in range(count):
        item = input(f"Введите название {i+1}-го: ")
        items.append(item)

    return items

apps = get_list_from_input("Сколько приложений/игр в инфо вы хотите? ")
accounts = get_list_from_input("Сколько аккаунтов в инфо вы хотите? ")
interests = get_list_from_input("Сколько интересов у тебя есть, которые ты бы хотел добавить в инфо?: ")
devices = get_list_from_input("Сколько устройств ты бы хотел видеть в инфо?: ")

input("Нажмите Enter, чтобы создать инфо...")

print(f" Info {name_user} ")
print(f"Владелец: {name_user} ({username_user})")
print(f"Называть: {nazivat_user}")

print("\nИгры и приложения:")
for app in apps:
    print(f" - {app}")

print("\nАккаунты:")
for account in accounts:
    print(f" - {account}")

print("\nИнтересы:")
for interest in interests:
    print(f" - {interest}")

print("\nУстройства:")
for device in devices:
    print(f" - {device}")

print("Созданно при помощи paddos")
print("Спасибо за использование <3 @mifka_post")
input("Тыкните Enter чтобы выйти")