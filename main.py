

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. J.K. Rowling", "D. Leo Tolstoy"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Great White Shark", "D. Giraffe"],
        "answer": "B"
    }
]

prize = [1000, 5000, 10000, 50000]
total_prize = 0

def kbc_game():
    print("Welcome to Kaun Banega Crorepati (KBC)!\n")
    
    for i, a in enumerate(questions):
        print(f"Question {i+1} for Rs. {prize[i]}:")
        print(a["question"])
        for option in a["options"]:
            print(option)
        
        answer = input("Enter your answer (A/B/C/D): ").upper()
        
        if answer == a["answer"]:
            total_prize = prize[i]
            print(f"Correct! You have won Rs. {total_prize}\n")
        else:
            print(f"Wrong answer! The correct answer was {a['answer']}.")
            print(f"You are leaving with Rs. {total_prize}")
            break
    else:
        print(f"Congratulations! You have won the maximum prize of Rs. {total_prize}")


kbc_game()
