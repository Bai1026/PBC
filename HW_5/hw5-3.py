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


# Main Function
def main():
    n = int(input().strip('\n'))
    pos_list = ['good', 'best', 'awesome', 'excellent', 'wonderful']
    neg_list = ['bad', 'worst', 'stupid', 'shame']
    results = []

    for _ in range(n):
        sentence = input().strip('\n')

        # get the positive and negeative num in each sentence
        pos_count, neg_count = word_detection(sentence, pos_list, neg_list)
        sentence_score = pos_count - neg_count

        results.append(sentence_score)

    print(",".join(map(str, results)))


if __name__ == "__main__":
    main()

'''
2
The weather today IS wonderful , but the traffic IS the worstttt.
I think this new movie IS AWeSOME, but the actors are stupid.
'''

'''
7
Despite the bad weather, we had a wwwonderful time at the beach.
The movie was awesome, but the seats were quite uncomfortable.
I thought the new cafe was overrated; the food was good but NOT excellent.
This has been the worst day of my life; everything that could go wrong did.
My Laptop Is The Best Purchase I've Made. wONderful PerforMANCE!
I will found the book quite STUPID, with a plot that madenosense.
Winning the award was an- "Awesome " experience ,truly the best-feeling.
'''