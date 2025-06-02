import random

singles = list(range(1, 21))
doubles = [2 * i for i in range(1, 21)]
triples = [3 * i for i in range(1, 21)]
bulls = [25, 50]

all_dart_scores = singles + doubles + triples + bulls

valid_scores = set()

for d1 in all_dart_scores:
    for d2 in all_dart_scores:
        for d3 in all_dart_scores:
            total = d1 + d2 + d3
            valid_scores.add(total)

valid_scores.add(0)

valid_scores = sorted(valid_scores)

name = input("What is your name? ")
print("Welcome to darts 501,", name)

luke_average_ranges = [
    {"range": (87.0, 91.9), "percent": 0.02,},
    {"range": (92.0, 94.9), "percent": 0.10,},
    {"range": (95.0, 97.9), "percent": 0.22,},
    {"range": (98.0, 100.9), "percent": 0.25,},
    {"range": (101.0, 104.9), "percent": 0.21,},
    {"range": (105.0, 109.9), "percent": 0.12,},
    {"range": (110.0, 114.9), "percent": 0.06,},
    {"range": (115.0, 122.9), "percent": 0.02,}
]
double_finishes = [2 * i for i in range(1, 21)] + [50]

def can_checkout(score):
    possible_checkouts = [
        170, 167, 164, 161, 160, 158, 157, 156, 155, 154, 153, 152, 151, 150,
        149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136,
        135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 122,
        121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108,
        107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93,
        92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76,
        75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 58,
        57, 56, 55, 54, 53, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30,
        28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2
    ]
    return score in possible_checkouts
luke_checkout_ranges = [
    {"range": (2.0, 39.0), "percent": random.uniform(0.60, 0.90)},
    {"range": (40.0, 59.0), "percent": random.uniform(0.60, 0.80)},
    {"range": (60.0, 89.0), "percent": random.uniform(0.50, 0.70)},
    {"range": (90.0, 130.0), "percent": random.uniform(0.35, 0.50)},
    {"range": (130.0, 170.0), "percent": random.uniform(0.10, 0.25)}
]

while True:
    user_choice = input("Choose Heads or Tails: ").capitalize()
    if user_choice in ["Heads", "Tails"]:
        break
    print("Please enter 'Heads' or 'Tails'.")
result = random.choice(["Heads", "Tails"])
print("The coin landed on:", result)

if user_choice.capitalize() == result:
    print(f"{name} wins the throw!")
    thrower = name
else:
    print("The opponent wins the throw!")
    thrower = "Luke Littler"

print("The first throw goes to:", thrower)

user_score = 501
luke_score = 501
current_player = thrower 

while user_score > 0 and luke_score > 0:
    if current_player == name:
        print(f"\n{name}'s score: {user_score}")
        previous_score = user_score  

        while True:
            try:
                user_turn = int(input("Enter your score for this turn: "))
                if user_turn in valid_scores and user_turn <= user_score:
                    break
                else:
                    print("Invalid score. Enter a realistic darts score that doesn't bust.")
            except ValueError:
                print("Please enter a number.")

        if user_score - user_turn == 0:
            try:
                last_dart = int(input("What was your final dart (score)?"))
                if last_dart in double_finishes:
                    user_score = 0
                    print(f"{name} wins with a double finish!")
                    break
                else:
                    print("You must finish on a double! Bust!")
                    user_score = previous_score
                    current_player = "Luke Littler"
                    continue
            except ValueError:
                print("Invalid input. Bust!")
                user_score = previous_score
                current_player = "Luke Littler"
                continue
        else:
            user_score -= user_turn

            if user_score < 0:
                print("Bust! Your score resets to previous value.")
                user_score = previous_score

        current_player = "Luke Littler"

    else:
        print(f"\nLuke Littler's score: {luke_score}")
        previous_luke_score = luke_score  

        if luke_score <= 170 and can_checkout(luke_score):
            if luke_score in double_finishes and random.random() < 0.4:
                print("Luke checks out with a double finish and wins!")
                break
            else:
                print("Luke misses the double finish or fails to checkout.")
                possible_scores = [score for score in valid_scores if 0 < score <= luke_score]
                luke_turn = random.choice(possible_scores) if possible_scores else 0
                print(f"Luke scores: {luke_turn}")
                luke_score -= luke_turn
        else:
            possible_scores = [score for score in valid_scores if 0 < score <= luke_score]
            luke_turn = random.choice(possible_scores) if possible_scores else 0
            print(f"Luke scores: {luke_turn}")
            luke_score -= luke_turn

        if luke_score < 0:
            print("Luke busts! Score resets to previous value.")
            luke_score = previous_luke_score
        elif luke_score == 0:
            print("Luke Littler wins!")
            break

        current_player = name
