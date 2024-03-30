#1

def count_of_potions() -> None:
    with open("magical.csv", 'r', encoding="utf-8") as f:
        arr = {}
        count = 0
        h = f.readline()
        for number in f:
            data = number.split(",")
            if data[1] == "-1":
                data[1] = "0"
            if data[0] == "Мощное Зелье":
                count += int(data[1])
            if not data[0] in arr.keys():
                arr[data[0]] = int(data[1])
            else:
                arr[data[0]] += int(data[1])

    with open("magicaPotions.txt", 'w', encoding="utf-8") as out:
        for key, value in arr.items():
            out.write(f"{key} в запасах еще есть - {value}\n")

    print('Данного зелья осталось - '+str(count))


if __name__ == '__main__':
    count_of_potions()
