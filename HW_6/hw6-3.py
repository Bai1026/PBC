'''do not use the enumerate in this HW =='''

# This function is for cleaning the useless or messy punctuation
def clean_word(word):
    punctuation = ".,:;?!'\"-"
    # Replace each punctuation with space since if replace by nothing some error would occur.
    for p in punctuation:
        word = str(word).replace(p, " ")
    return word


# This function is to count the number of positive and negative word in each sentence
def word_detection(sentence, pos_list, neg_list):
    pos_count = 0
    neg_count = 0

    words = sentence.lower().split()
    words = clean_word(words)

    # after cleaning, the words become string, so remove the '[' and ']'
    words = words.replace('[', "")
    words = words.replace(']', "")

    # here the words is the list contain all the correct words.
    words = words.split(" ")

    pos_count = sum(word in pos_list for word in words)
    neg_count = sum(word in neg_list for word in words)
    return pos_count, neg_count


# get all the input first
def get_input_string():
    sentence_list = []
    n = int(input().strip('\n'))
    for _ in range(n):
        sentence_list.append(input().strip('\n'))
    LABEL = [int(x) for x in input().split(',')]
    return n, sentence_list, LABEL


def get_common_dict(input_list, compare_list, ALPHA_BETA):
    common_dict = {}
    # go through the ALPHA_BETA list in order
    for idx, tmp_list in enumerate(compare_list):
        count = 0
        for i in range(len(input_list)):
            if input_list[i] == tmp_list[i]:
                count += 1
        common_dict[tuple(ALPHA_BETA[idx])] = count
        print(tuple(ALPHA_BETA[idx]))

    max_value = max(common_dict.values())

    max_common_dict = {key: value for key, value in common_dict.items() if value == max_value}

    return max_common_dict


# Main Function
def main():
    n, sentence_list, LABEL = get_input_string()

    POS_LIST = ['good', 'best', 'awesome', 'excellent', 'wonderful']
    NEG_LIST = ['bad', 'worst', 'stupid', 'shame']
    ALPHA_BETA = [[1,1], [1,2], [1,3], [2,1], [2,3], [3,1], [3,2]]
    predict_list = []

    # go through the APHPA_BETA list in order
    for hyper_parameter in ALPHA_BETA:
        results = []
        print(hyper_parameter)
        for i in range(n):
            sentence = sentence_list[i]

            alpha = hyper_parameter[0]
            beta = hyper_parameter[1]
            # get the positive and negeative num in each sentence
            pos_count, neg_count = word_detection(sentence, POS_LIST, NEG_LIST)

            # from the formula, and the CONST list -> we get each scores in every round and store in the result_list
            sentence_score = alpha * pos_count - beta * neg_count

            if sentence_score >= 0:
                results.append(1)
            else:
                results.append(0)

        predict_list.append(results)

    # print(LABEL)
    # print(",".join(map(str, results)))
    # print(predict_list)
    max_common_dict = get_common_dict(LABEL, predict_list, ALPHA_BETA)
    print(max_common_dict)

    alpha = list(max_common_dict.keys())[0][0]
    beta = list(max_common_dict.keys())[0][1]
    value = list(max_common_dict.values())[0]

    print(alpha, beta, value, sep=',')


if __name__ == "__main__":
    main()


'''
7
The food was good AND excellent. However, the service was bad!
The movie was awesome; the experience was wonderful.
The instructor tried his best, but the course IS still the worst.
I cannot tell whether the food iS good Or bad. But the waiter IS stupid. 
The lapTOP isss the BeSt ! Wonderful performance! Awesome!
This book makes no sense; I feel shame that the authors are NTUalumni. 
Winning the award was an "terrific " experience ,truly the best-feeling.
1,1,0,0,1,0,1
'''

'''
7
The food was good AND excellent. However, the service was bad!
The movie was awesome; the experience was wonderful.
The instructor tried his best, but the course IS still the worst.
I cannot tell whether the food iS good Or bad. But the waiter IS stupid. 
The lapTOP isss the BeSt ! Wonderful performance! Awesome!
This book makes no sense; I feel shame that the authors are NTUalumni. 
Winning the award was an "terrific " experience ,truly the best-feeling.
1,1,0,0,1,0,1
'''