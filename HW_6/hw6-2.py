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


# def find_store_or_product(id, price_dict, num_dict):
#     if id in price_dict:
#         return price_dict[id]

      # if the key is not in price_dict and the key is string like "ZZ", this would crush the script
#     elif int(id) in num_dict:
#         return num_dict[int(id)]
#     else:
#         # return "BAD!!"
#         raise KeyError()

def find_store_or_product(id, price_dict, num_dict):
    # check if the price_dict first, if exists -> return
    if id in price_dict:
        return price_dict[id]
    else:
        # try to transform into int, if is "ZZ" (not in price_dict and not convertible to int) -> Keyerror
        try:
            int_id = int(id)
        except ValueError:
            raise KeyError(f"ID {id} is not valid for num_dict and not found in price_dict.")

        # if not, means it's convertible to int and check if is in the num_dict with int key
        if int_id in num_dict:
            return num_dict[int_id]
        else:
            # if id is int and not in the num_dict -> Keyerror still.
            raise KeyError(f"ID {int_id} not found in num_dict.")



def main():
    input_file = input()
    _ = input()
    # TYPE = input()

    store_rev, product_sales_cnt = construct_dict(input_file)
    print(store_rev, product_sales_cnt)

    try:
        result = find_store_or_product('4', store_rev , product_sales_cnt)
        print(result)
    except KeyError as e:
        print("BAD!!")


if __name__ == '__main__':
    main()
