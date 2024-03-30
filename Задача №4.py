#4

def count_of_classes() -> None:
    classes = {}
    with open("magical.csv", 'r', encoding="utf-8") as f:
        arr = []
        h = f.readline()
        for i in f:
            data = i.replace("\n", '').split(",")
            arr.append(data)
            name = data[0].split()
            tip = ' '.join([name[x] for x in range(1, len(name))])
            if tip in classes.keys():
                classes[tip].append(int(data[1]))
            else:
                classes[tip] = []
                classes[tip].append(int(data[1]))
        for key, value in classes.items():
            print(f"{len(value)} зелий класса {key}, общее количество зелий {sum(value)}")


if __name__ == '__main__':
    count_of_classes()
