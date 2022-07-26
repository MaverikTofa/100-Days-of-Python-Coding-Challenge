from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {game.score}/{game.question_number}")
