import random

def get_game_data():
    return [
        {
            "name": "The Legend of Zelda: Breath of the Wild",
            "hint": "An open-world action-adventure game set in a fantasy world."
        },
        {
            "name": "Minecraft",
            "hint": "A sandbox game that allows players to build and explore a blocky world."
        },
        {
            "name": "Among Us",
            "hint": "A multiplayer game where players work together to find an imposter."
        },
        {
            "name": "Dark Souls",
            "hint": "An action RPG known for its challenging gameplay and deep lore."
        },
        {
            "name": "Stardew Valley",
            "hint": "A farming simulation game that lets you build and manage your own farm."
        }
    ]

def play_game():
    games = get_game_data()
    selected_game = random.choice(games)

    print("Welcome to the Video Game Guessing Game!")
    print("Guess the video game based on the hint provided.\n")

    print(f"Hint: {selected_game['hint']}\n")

    attempts = 3  # Number of attempts the player has

    while attempts > 0:
        guess = input("Your guess: ").strip()

        if guess.lower() == selected_game['name'].lower():
            print("Congratulations! You guessed it right!")
            break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempt(s) left.\n")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct answer was: {selected_game['name']}")

if __name__ == "__main__":
    play_game()
