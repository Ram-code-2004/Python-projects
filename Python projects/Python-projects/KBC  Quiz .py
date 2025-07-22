# KBC Quiz Game
# This is a simple implementation of a quiz game similar to "Kaun Banega Crorep
questions = [
    ["What is the capital of France?",
     ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
     3],
    ["Which planet is known as the Red Planet?",
     ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
     2],
    ["Who wrote 'Romeo and Juliet'?",
     ["a) Charles Dickens", "b) Mark Twain", "c) William Shakespeare", "d) Jane Austen"],
     3],
    ["What is the largest mammal on Earth?",
     ["a) Elephant", "b) Blue whale", "c) Giraffe", "d) Great white shark"],
     2],
    ["Which gas do plants use for photosynthesis?",
     ["a) Oxygen", "b) Carbon dioxide", "c) Nitrogen", "d) Hydrogen"],
     2],
    ["How many continents are there on Earth?",
     ["a) 5", "b) 6", "c) 7", "d) 8"],
     3],
    ["What is the chemical symbol for gold?",
     ["a) Ag", "b) Au", "c) Pb", "d) Fe"],
     2],
    ["Which is the longest river in the world?",
     ["a) Amazon", "b) Nile", "c) Yangtze", "d) Mississippi"],
     2],
    ["What is the hardest natural substance on Earth?",
     ["a) Gold", "b) Diamond", "c) Iron", "d) Quartz"],
     2],
    ["Who painted the Mona Lisa?",
     ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Michelangelo"],
     3],
    ["Which element is most abundant in Earth's atmosphere?",
     ["a) Oxygen", "b) Nitrogen", "c) Carbon dioxide", "d) Hydrogen"],
     2],
    ["How many bones are there in the adult human body?",
     ["a) 200", "b) 206", "c) 212", "d) 218"],
     2],
    ["Who developed the theory of relativity?",
     ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Nikola Tesla"],
     2],
    ["Which ocean is the largest?",
     ["a) Atlantic Ocean", "b) Indian Ocean", "c) Pacific Ocean", "d) Arctic Ocean"],
     3],
    ["Which language has the most native speakers?",
     ["a) English", "b) Spanish", "c) Mandarin Chinese", "d) Hindi"],
     3]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(question[0])
    for opt in question[1]:
        print(opt)
    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    if reply == 0:
        money = levels[i-1] if i > 0 else 0
        break
    if reply == question[2]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")