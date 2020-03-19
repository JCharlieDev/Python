from Question import Question

questionPrompts = [
    "What color are apples?: \n(a)Red\Green\n(b)Purple\n(c)Orange\n\n",
    "What color are bananas?: \n(a)Red\Green\n(b)Yellow\n(c)Blue\n\n",
    "What color are strawberries?: \n(a)Red\n(b)Purple\n(c)White\n\n"
]

questions = [
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "b"),
    Question(questionPrompts[2], "a")
]

def RunTest(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)

        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

RunTest(questions)