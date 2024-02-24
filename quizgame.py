#quiz game in python

#new game function
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)

        print()
        guess = input("Enter (A, B, C or D) : ")
        guess = guess.upper()
        guesses.append(guess)


        correct_guesses += check_answer(questions.get(key), guess)
        print()
        question_num += 1

    display_score(correct_guesses, guesses)


#check answer function
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


#display score function
def display_score(correct_guesses, guesses):

    print("--------------------")
    print("RESULTS ")
    print("--------------------")

    print("Answers : ", end = "")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    print("Guesses : ", end = "")
    for i in guesses:
        print(i, end = " ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print()
    print("Your score is : " +str(score)+"%")
    print()


#play again function
def play_again():
    
    response = input("Do you want to play again ? (yes or no) : ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


#all quiz questions
questions = {
    "What is the output of the following code snippet ?\nx = 5\ny = 2\nresult = x ** y\nprint(result)\n" : "C",
    "Which of the following statements is true about Python ?" : "D",
    "What is the purpose of the range() function in Python ?" : "A",
    "In Python, which of the following data types is mutable ?" : "C",
    "What will the following code print ?\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[2:4])\n" : "A"
}


#options for all question
options = [["A. 7", "B. 10", "C. 25", "D. 8"],
           ["A. Python is a statically typed language", "B. Python is a low-level programming language", "C. Python code must be compiled before execution", "D. Python is an interpreted language"],
           ["A. To generate a list of numbers within a specified range", "B. To randomly shuffle a list of elements", "C. To return the length of a given sequence", "D. To check if a value exists in a dictionary"],
           ["A. Tuple", "B. String", "C. List", "D. Set"],
           ["A. [3, 4]", "B. [1, 2]", "C. [2, 3]", "D. [4, 5]"]]


new_game()

while play_again():
    new_game()

print()
print("Game Over!")
print("Byeeeeeeeeeeee!")
print("\n\n")

