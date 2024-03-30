#5

def count_herbs() -> None:
    herbs = {}
    with open("magical.csv", 'r', encoding="utf-8") as f:
        arr = []
        h = f.readline()
        for i in f:
            data = i.replace("\n", '').split(",")
            for j in range(2, len(data)):
                if data[j] not in herbs.keys():
                    herbs[data[j]] = 1
                else:
                    herbs[data[j]] += 1
        mus = [[key, value] for key, value in herbs.items()]
        mus.sort(key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(f"{mus[i][0]} - {mus[i][1]}")


if __name__ == '__main__':
    count_herbs()
