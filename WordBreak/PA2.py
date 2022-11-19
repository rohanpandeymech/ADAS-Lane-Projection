import timeit



targer_file_1='target1.txt'
wordbank_file_1='wordbank1.txt'

targer_file_2='target2.txt'
wordbank_file_2='wordbank2.txt'

targer_file_3='target3.txt'
wordbank_file_3='wordbank3.txt'

targer_file_4='target4.txt'
wordbank_file_4='wordbank4.txt'

targer_file_5='target5.txt'
wordbank_file_5='wordbank5.txt'

targer_file_6='target6.txt'
wordbank_file_6='wordbank6.txt'

targer_file_7='target7.txt'
wordbank_file_7='wordbank7.txt'

targer_file_8='target8.txt'
wordbank_file_8='wordbank8.txt'

targer_file_9='target9.txt'
wordbank_file_9='wordbank9.txt'

targer_file_10='target10.txt'
wordbank_file_10='wordbank10.txt'



def memoization(target, wordbank, memo):
    if target in memo:
        return memo[target]
    
    if not target:
        return [[]]
    solution=[]
    for i in wordbank:
        if target.startswith(i, 0):
            index=len(i)
            rest=target[index:]
            possible=memoization(rest,wordbank,memo)
            combinations=[[*way,i] for way in possible]
            if combinations:
                solution.extend(combinations)
    memo[target] = solution
    return solution

         



def testcase(targer_file,wordbank_file):
    #time running
    start = timeit.default_timer()
    
    #  read file 1
    with open(wordbank_file) as f:
        wordbank=[word for line in f for word in line.split()]

    # read file 2
    f = open(targer_file, "r")
    target=f.read()

    print("\n*********")
    print('Word Bank List :  ', wordbank)
    print("\n*********")
    print("Our Target is :  ", target)
    if not target:
        print(("Our Target is EMPTY !!"))
    print("\n*********")
    memo={}  # Initialize a dictionary 
    s=memoization(target, wordbank, memo)

    solution=[s[x] for x in range(len(s)) if not(s[x] in s[:x])]

    print('Total --- {}  --- ways Solutions, it is {} :'.format(len(solution),solution))
    stop = timeit.default_timer()
    print("\n*********")
    print('The Total Run Time: ', stop - start)
    print("*********")

if __name__ == "__main__":
    print('Test Case 1 : ')
    testcase(targer_file_1,wordbank_file_1)
    print('\n\n\n\nTest Case 2 : ')
    testcase(targer_file_2,wordbank_file_2)
    print('\n\n\n\nTest Case 3 : ')
    testcase(targer_file_3,wordbank_file_3)
    print('\n\n\n\nTest Case 4 : ')
    testcase(targer_file_4, wordbank_file_4)
    print('\n\n\n\nTest Case 5 : ')
    testcase(targer_file_5, wordbank_file_5)
    print('\n\n\n\nTest Case 6 : ')
    testcase(targer_file_6, wordbank_file_6)
    print('\n\n\n\nTest Case 7 : ')
    testcase(targer_file_7, wordbank_file_7)
    print('\n\n\n\nTest Case 8 : ')
    testcase(targer_file_8, wordbank_file_8)
    print('\n\n\n\nTest Case 9 : ')
    testcase(targer_file_9, wordbank_file_9)
    print('\n\n\n\nTest Case 10 : ')
    testcase(targer_file_10, wordbank_file_10)

