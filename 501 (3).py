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

user_stats = {
    "legs_played": 0,
    "total_darts": 0,
    "three_dart_scores": [], 
    "checkout_attempts": 0,
    "successful_checkouts": 0,
    "highest_checkout": 0,
    "doubles_attempted": 0,
    "doubles_hit": 0,  
}

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
def get_checkout_success_rate(score):
    if 130 <= score <= 170:
        return "~10–25%"
    elif 90 <= score <= 129:
        return "~35–50%"
    elif 60 <= score <= 89:
        return "~50–70%"
    elif 40 <= score <= 59:
        return "~60–80%"
    elif 2 <= score <= 39:
        return "~60–90%"
    else:
        return "N/A"

def pick_luke_average():
    weights = [r["percent"] for r in luke_average_ranges]
    chosen_range = random.choices(luke_average_ranges, weights=weights, k=1)[0]
    return random.uniform(*chosen_range["range"])

luke_average = pick_luke_average()

def luke_turn_score(luke_score):
    
    possible_scores = [score for score in valid_scores if 0 < score <= luke_score]
    close_scores = [score for score in possible_scores if abs(score - luke_average) <= 10]
    if close_scores:
        return random.choice(close_scores)
    elif possible_scores:
        return random.choice(possible_scores)
    else:
        return 0

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

        darts_this_turn = 3  
        user_stats["total_darts"] += darts_this_turn
        user_stats["three_dart_scores"].append(user_turn)

        if user_score in double_finishes and user_score < 50:
            user_stats["doubles_attempted"] += 1

       
        if user_score - user_turn == 0:
            user_stats["checkout_attempts"] += 1
            while True:
                last_dart_input = input("What was the value of your final (winning) double? (e.g., 40 for double top): ")
                if last_dart_input.lower() == "undo":
                    print("Undoing last input. Please re-enter your final dart score.")
                    continue
                try:
                    last_dart = int(last_dart_input)
                    if last_dart in double_finishes:
                        user_stats["successful_checkouts"] += 1
                        if user_score > user_stats["highest_checkout"]:
                            user_stats["highest_checkout"] = user_score
                        if last_dart < 50:
                            user_stats["doubles_hit"] += 1
                        
                        while True:
                            darts_at_double = input("How many darts did you throw at the double? (1-3): ")
                            if darts_at_double.lower() == "undo":
                                print("Undoing last input. Please re-enter your final dart score.")
                                break  
                            try:
                                darts_at_double_int = int(darts_at_double)
                                if 1 <= darts_at_double_int <= 3:

                                    user_score = 0
                                    print(f"{name} wins with a double finish!")
                                    break  
                                else:
                                    print("Please enter a number between 1 and 3.")
                            except ValueError:
                                print("Please enter a number between 1 and 3, or 'undo'.")
                        if user_score == 0:
                            break  
                    else:
                        print("You must finish on a double! Bust!")
                        user_score = previous_score
                        current_player = "Luke Littler"
                        break
                except ValueError:
                    print("Please enter a valid number for the double.")
            else:
                print("You must finish on a double! Bust!")
                user_score = previous_score
                current_player = "Luke Littler"
                break
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
                luke_turn = luke_turn_score(luke_score)
                print(f"Luke scores: {luke_turn}")
                luke_score -= luke_turn
        else:
            luke_turn = luke_turn_score(luke_score)
            print(f"Luke scores: {luke_turn}")
            luke_score -= luke_turn

        if luke_score < 2:
            print("Luke busts! Score resets to previous value.")
            luke_score = previous_luke_score
        elif luke_score == 0:
            print("Luke Littler wins!")
            break

        current_player = name

user_stats["legs_played"] += 1

stats_filename = f"{name}_darts_stats.txt"
with open(stats_filename, "w") as f:
    for key, value in user_stats.items():
        f.write(f"{key}: {value}\n")

print(f"Stats saved to {stats_filename}")

