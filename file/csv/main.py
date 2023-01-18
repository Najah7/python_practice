import csv

# NOTE:windowの場合は改行が\r\nになり２行改行されるので、newline引数を指定したがいい


def main():

    print_message('書き込み')

    with open('test.csv', 'w', newline='') as csv_f:
        field_names = ['Name', 'Number']
        writer = csv.DictWriter(csv_f, fieldnames=field_names)
        writer.writeheader()

        names = ['taro', 'jiro', 'saburou']

        for i in range(3):
            writer.writerow({'Number': i, 'Name': names[i]})

    print_message('読み込み')

    with open('test.csv', 'r', newline='') as csv_f:
        reader = csv.DictReader(csv_f)
        for row in reader:
            print(row['Number'], row['Name'])


def print_message(message):
    print(f'===={message}====')


if __name__ == '__main__':
    main()
