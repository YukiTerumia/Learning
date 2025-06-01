import random
name = input("What is your name? ")
print("Welcome to darts 501,", name)

luke_average_ranges = [
    {"range": (87.0, 91.9), "percent": 0.02, "description": "very rare, poor day"},
    {"range": (92.0, 94.9), "percent": 0.10, "description": "below par"},
    {"range": (95.0, 97.9), "percent": 0.22, "description": "solid but beatable"},
    {"range": (98.0, 100.9), "percent": 0.25, "description": "very common range"},
    {"range": (101.0, 104.9), "percent": 0.21, "description": "strong performance"},
    {"range": (105.0, 109.9), "percent": 0.12, "description": "elite level"},
    {"range": (110.0, 114.9), "percent": 0.06, "description": "exceptional"},
    {"range": (115.0, 122.9), "percent": 0.02, "description": "career-best zone"}
]
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
    {"range": (0.0, 19.9), "percent": 0.02},
    {"range": (20.0, 29.9), "percent": 0.08},
    {"range": (30.0, 39.9), "percent": 0.20},
    {"range": (40.0, 49.9), "percent": 0.30},
    {"range": (50.0, 59.9), "percent": 0.25},
    {"range": (60.0, 69.9), "percent": 0.10},
    {"range": (70.0, 79.9), "percent": 0.04},
    {"range": (80.0, 99.9), "percent": 0.009},
    {"range": (100.0, 100.0), "percent": 0.001}
]

user_choice = input("Choose Heads or Tails: ")
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
        user_turn = int(input("Enter your score for this turn: "))
        user_score -= user_turn

        if user_score <= 0:
            print(f"{name} wins!")
            break

        current_player = "Luke Littler"  

    else:
        
        print(f"\nLuke Littler's score: {luke_score}")
        if luke_score <= 170 and can_checkout(luke_score):
            
            if random.random() < 0.4:
                print("Luke checks out and wins!")
                break
            else:
                print("Luke misses the checkout.")
                luke_turn = random.randint(60, min(180, luke_score - 1))
                print(f"Luke scores: {luke_turn}")
                luke_score -= luke_turn
        else:
            luke_turn = random.randint(60, min(180, luke_score - 1))
            print(f"Luke scores: {luke_turn}")
            luke_score -= luke_turn

        if luke_score <= 0:
            print("Luke Littler wins!")
            break

        current_player = name  
