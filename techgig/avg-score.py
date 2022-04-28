def main():
    score = [0, 0, 0]
    names = []
    num = int(input("no of people:"))
    for i in range(num):
        sc = input("enter:").split()
        fc = sc[1:]

        f = 0
        for j in range(0, 3):
            score[f] += int(fc[j])
        f += 1

        names.append(sc[0])
    ask = input("avg:")
    index_name = names.index(ask)
    print(score[index_name] / 3)


main()
