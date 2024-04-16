# This function is for cleaning the useless or messy punctuation
def clean_word(word):
    punctuation = ".,:;?!\'\"-\\"
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


# get all the input first, and store in the sentence_list
def get_input_string():
    sentence_list = []
    n = int(input().strip('\n'))
    for _ in range(n):
        sentence_list.append(input().strip('\n'))
    LABEL = [int(x) for x in input().split(',')]
    return n, sentence_list, LABEL


def get_common_dict(input_list, compare_list, ALPHA_BETA):
    common_dict = {}
    # go through the ALPHA_BETA list in order, and since we can not use enumerate, use idx += 1 instead
    idx = 0
    for tmp_list in compare_list:
        # to count the number of the predictions and labels in common place
        count = 0
        for i in range(len(input_list)):
            if input_list[i] == tmp_list[i]:
                count += 1
        common_dict[tuple(ALPHA_BETA[idx])] = count
        idx += 1

    # find the maximum number of common dictionary.
    max_value = max(common_dict.values())

    # get the dictionary with the max. values
    max_common_dict = {key: value for key, value in common_dict.items() if value == max_value}

    return max_common_dict


n, sentence_list, LABEL = get_input_string()

POS_LIST = ['good', 'best', 'awesome', 'excellent', 'wonderful']
NEG_LIST = ['bad', 'worst', 'stupid', 'shame']

# define the alpha and beta like this would not occur the order issues.
ALPHA_BETA = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
predict_list = []

# go through the APHPA_BETA list in order
for hyper_parameter in ALPHA_BETA:
    results = []
    # print(hyper_parameter)
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

max_common_dict = get_common_dict(LABEL, predict_list, ALPHA_BETA)

# since the order we add into the max_common_dict is in order, just print the first set of the results.
alpha = list(max_common_dict.keys())[0][0]
beta = list(max_common_dict.keys())[0][1]
value = list(max_common_dict.values())[0]

print(alpha, beta, value, sep=',')