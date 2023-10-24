student_details = {}
questions = ["What state is SQI Dugbe located",
            "How many days of the week does SQI run classes",
            "The following include python language EXPECT"]
options = ["a. Ogun\n b. Lagos\n c. Oyo\n",
    "a. 4\n b.3\n c. 5\n",
    "a. Braces\n b. List\n c. Carousels"]

answers = ["c", "a", "c"]
    

for i in range(2):#for loop interating twice for 2 students
    student_name = input("Enter your name ")
    score = 0
    for i in range(len(questions)):#interate through the questions
        print(questions[i])
        print(options[i])
        user_ans = input("Enter your answer ").lower()
        if user_ans == answers[i]:#To check if users score the right answers
            print("Correct")
            score += 10
        else:
            print("Wrong")
    print(score)
    # student_details[student_name] = score
    student_details.update({student_name:score})

print(student_details)
print(f"The student with the highest score is {max(student_details)} and the student score is {student_details[max(student_details)]}")