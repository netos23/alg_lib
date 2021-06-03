from rselect import rSelect

if __name__ == "__main__":
    print("Введите массив:")
    arr = list(map(int, input().split()))
    order_statistic = int(input("Введите номер порядковой статистика:\n"))

    print()
    print(rSelect(arr, order_statistic))
