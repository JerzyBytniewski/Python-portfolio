from Question import Question

question_prompts = [
    "Why can you do in Python?\n(a) Teach machines\n(b) Make a surgical intervention\n(c) Spagetthi\n\n",
    "Why it is a pleasure to programing in Python?\n(a) Because you are a snake raiser\n(b) Because its logo is a masterpiece of graphic design\n(c) Because it's a user friendly programing language\n\n",
    "In which commercial areas you can use Python?\n(a) In Data Analysis\n(b) In trafficking Encyclopedia Britannica\n(c) In gastronomy\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def quiz_it(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    if score >= 2:
        print("Congratulations! You obtained " + str(score) + "/" + str(len(questions)) + " points. You are a genuin pythonist!")
    if score < 2:
        print("You obtained " + str(score) + "/" + str(len(questions)) + " points. There is still hope for you, try again ;) !")

quiz_it(questions)

