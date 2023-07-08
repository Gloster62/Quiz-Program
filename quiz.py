#a dictinoary thath stores questions and answers
#have a variable that tracks the score of the player
#loop through the dictionary using the key values
# display each question to the user and allow them to answer
#tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question":"What is the capital of Portugal",
        "answer":"Lisbon"
    },
    "question2": {
        "question":"What is the capital of Austria",
        "answer":"Wien"
    },
    "question3": {
        "question":"What is the capital of Germany",
        "answer":"Berlin"
    },
    "question4": {
        "question":"What is the capital of England",
        "answer":"London"
    },
    "question5": {
        "question":"What is the capital of Spain",
        "answer":"Madrid"
    }    
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print("Your score is " + str(score) + "\n")
    else:
        print("Wrong")
        print("The answer is :" + value['answer'])
        print("Your score is " + str(score) + "\n")

print("You got" + str(score) + "out of 5 questions correctly")
print("Your percentage is " + str(int(score/5 * 100)) + "%")