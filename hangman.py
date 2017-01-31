answer = list(input("What's the answer?"))
clue = str(input("What's the clue?"))
answer_list = [["_ ", char] if char != " " else [" ", ''] for char in answer]
max_misses = int(input("Number of misses allowed? Generally five."))
miss_list = []
i = 0
def update():
    global i
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
    print("Clue: " + clue)
    feedback = ''.join(x[0] for x in answer_list)
    print("\"" + feedback.rstrip(' ') + "\"")
    print(str(i) + " out of maximum {}".format(str(max_misses)) + " missed.")
    print("Wrong guesses: {}".format(miss_list))
    if '_' not in feedback:
        i = max_misses + 1
update()
while i <= max_misses:
    guess = str(input("Guess a letter"))
    for item in answer_list:
            assert isinstance(item, list)
            if guess == item[1]:
                item[0] = " " + guess + " "
    if guess not in answer:
        i += 1
        miss_list.append(guess)
    update()
if i == max_misses:
    print("RIP you")
elif i == max_misses + 1:
    print("Good shit")
