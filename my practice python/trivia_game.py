# list of questions 
# store the answers 
# randomly pick questions 
# ask the questions 
# see if they are correct 
# keep track of the score
# tell the user their score


import random

trivia_questions = [
    {
        "question": "What is the capital city of Japan?",
        "options": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
        "answer": "Tokyo"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Osmium", "Ozone", "Oxide"],
        "answer": "Oxygen"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1945", "1939", "1918", "1950"],
        "answer": "1945"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Which language has the most native speakers in the world?",
        "options": ["English", "Mandarin Chinese", "Spanish", "Hindi"],
        "answer": "Mandarin Chinese"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Diamond", "Iron", "Graphite"],
        "answer": "Diamond"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Who discovered gravity when he saw an apple fall from a tree?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Isaac Newton"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["1", "2", "3", "5"],
        "answer": "2"
    },
    {
        "question": "In which country is the Great Pyramid of Giza located?",
        "options": ["Egypt", "Mexico", "Peru", "Iraq"],
        "answer": "Egypt"
    },
    {
        "question": "Which instrument has keys, pedals, and strings?",
        "options": ["Piano", "Violin", "Guitar", "Drum"],
        "answer": "Piano"
    },
    {
        "question": "Who was the first person to walk on the Moon?",
        "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
        "answer": "Neil Armstrong"
    },
    {
        "question": "Which animal is known as the 'Ship of the Desert'?",
        "options": ["Horse", "Camel", "Elephant", "Donkey"],
        "answer": "Camel"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "What is the chemical formula for water?",
        "options": ["H2O", "O2H", "HO2", "H3O"],
        "answer": "H2O"
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["France", "Germany", "Italy", "Canada"],
        "answer": "France"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["K2", "Mount Kilimanjaro", "Mount Everest", "Mount Fuji"],
        "answer": "Mount Everest"
    }
]

def python_trivia_game():
    question_list = random.sample(trivia_questions,5)
    
    score = 0
    
    for i,q in enumerate(question_list,1):
        print(f"\nQuestion {i}:{q["question"]}")
        for idx,option in enumerate(q["options"],1):
            print(f"{idx}.{option}")
            
            
        try:
            user_choice = int(input("Enter the option number:"))
            if q["options"][user_choice-1].lower() == q["answer"].lower():
                print("✅ Correct Answer")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was: {q['answer']}")
        except (ValueError,IndexError):
            print("⚠️ Invalid input! Skipping this question.")
            
            
    print("\n🎯 Game Ended!")
    print(f"Your final score : {score}/{len(question_list)}")
    if score == len(question_list):
        print("🏆 Perfect! You nailed every question!")
    elif score >= len(question_list) - 1:
        print("🔥 Almost perfect! Great job!")
    elif score >= len(question_list) // 2:
        print("👍 Nice! You did pretty well!")
    else:
        print("😅 Better luck next time — keep practicing!")
        
python_trivia_game()