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


def find_store_or_product(id, price_dict, num_dict):
    try:
        if id in price_dict:
            return price_dict[id]
        elif id in num_dict:
            return num_dict[id]
    except KeyError as e:
        print("BAD!!")

def main():
    input_file = input()
    _ = input()
    # TYPE = input()

    price_dict, num_dict = construct_dict(input_file)
    print(price_dict, num_dict)

    output = find_store_or_product('PB', price_dict, num_dict)
    print(output)


if __name__ == '__main__':
    main()

