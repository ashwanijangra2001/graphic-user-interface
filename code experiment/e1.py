import json

with open("question.json",'r')as file:
    content = file.read()

data = json.loads(content)
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["Alternative"]):
        print(index +1, '-', alternative)
    user_choice = int(input("a enter the answer;"))
    question["user_choice"] = user_choice

score = 0
for index,question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "correct answer"
    else:
        result = "wrong answer"
    message = f"question {index+1} is {result}"\
              f" ,you choose option {question['user_choice']}" \
              f" ,then correct answer is {question['correct_answer']}"
    print(message)
print(f"score is {score}/ {len(data)}")

