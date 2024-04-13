def construct_dict(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    info = []
    for line in lines:
        info.append(line.strip())

    price_dict = {}
    num_dict = {}
    
    # omit the first row
    for item in info[1:]:
        tmp_list = item.split(',')
        store = tmp_list[0]
        goods = int(tmp_list[2])
        num = int(tmp_list[3])
        price = int(tmp_list[4])

        total_price = num * price
        if store in price_dict:
            price_dict[store] += total_price
        else:
            price_dict[store] = total_price

        if f'{goods}' in num_dict:
            num_dict[f'{goods}'] += 1
        else:
            num_dict[f'{goods}'] = 1
    return price_dict, num_dict

def output_function(price_dict, num_dict, TYPE):
    if TYPE == 'S':
        sorted_stores = sorted(price_dict.items(), key=lambda x: (-x[1], len(x[0]), x[0]))

        top_stores = sorted_stores[:3]

        for store, revenue in top_stores:
            print(f"{store},{revenue}")

    elif TYPE == 'P':
        sorted_products = sorted(num_dict.items(), key=lambda x: (-x[1], int(x[0])))

        for i in range(min(3, len(sorted_products))):
            print(sorted_products[i][0], sorted_products[i][1], sep=',')

    else:
        print('ERROR input')


def main():
    input_file = input()
    _ = input()
    TYPE = input()

    price_dict, num_dict = construct_dict(input_file)
    output_function(price_dict, num_dict, TYPE)


if __name__ == '__main__':
    main()
