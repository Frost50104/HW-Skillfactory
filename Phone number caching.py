import redis

red = redis.Redis(
    host="redis-11118.c228.us-central1-1.gce.cloud.redislabs.com",
    port=11118,
    password="AzSGtOmQdoelmr0GSIyRj2Ec8XBZq2MY"
)

while True:


    command = input("1 - Записать номер "
                "\n2 - Показать номер"
                "\n3 - Удалить номер"
                "\n4 - Завершить программу"
                "\n"
                "\nВведите команду: ")

    if command == "1":
        name = input("Введите имя друга: ")
        number = input("Введите телефон друга: ")
        red.set(name, number)
        print("Номер успешно добавлен!\n")
    elif command == "2":
        name = input("Введите имя друга: ")
        print(red.get(name))
    elif command == "3":
        name = input("Введите имя друга: ")
        red.delete(name)
        print("Удаление выполнено успешно!\n")
    elif command == "4":
        break
