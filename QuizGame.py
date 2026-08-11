Questions = [
{
“question”: “1. What is the capital of India?”,
“answer”: “Delhi”
},
{
“question”: “2. Which programming language are you learning?”,
“answer”: “Python”
},
{
“question”: “3. What is 10 + 5?”,
“answer”: “15”
},
{
“question”: “4. Which keyword is used to define a function in Python?”,
“answer”: “def”
},
{
“question”: “5. What is the output of print(2 * 5)?”,
“answer”: “10”
}
]

Score = 0

Print(“===== Welcome to Quiz Game =====\n”)

For q in questions:
Print(q[“question”])
User_answer = input(“Your Answer: “)

If user_answer.strip().lower() == q[“answer”].lower():
Print(“Correct!\n”)
Score += 1
Else:
Print(“Wrong! Correct Answer:”, q[“answer”], “\n”)

Print(“===== Quiz Finished =====”)
Print(“Your Score:”, score, “/”, len(questions))

Percentage = (score / len(questions)) * 100
Print(“Percentage:”, percentage, “%”)
