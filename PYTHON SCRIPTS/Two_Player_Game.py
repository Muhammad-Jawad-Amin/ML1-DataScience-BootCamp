import random

dice_rolls = [1, 2, 3, 4, 5, 6]
coin_tosses = ["HEADS", "TAILS"]

player1_name = input("Player 1 Please Enter Your Name : ")
player2_name = input("Player 2 Please Enter Your Name : ")

players_scores = [0, 0]


def twoplayergame():
    while True:
        for player_no in range(2):
            print(f"\nPlayer {player_no+1} Turn :")
            dice_roll = random.choice(dice_rolls)
            coin_toss = random.choice(coin_tosses)

            print(f"Dice Roll Of Player {player_no+1} : {dice_roll}")
            print(f"Coin Toss Of Player {player_no+1} : {coin_toss}")

            if dice_roll % 2 != 0 and coin_toss == "HEADS":
                players_scores[player_no] += dice_roll * 5
            elif dice_roll % 2 == 0 and coin_toss == "HEADS":
                players_scores[player_no] += dice_roll * 2
            else:
                players_scores[player_no] += dice_roll * 1

            if players_scores[0] >= 100:
                print(f"{player1_name} is winner & his score is {players_scores[0]}.")
                return
            elif players_scores[1] >= 100:
                print(f"{player2_name} is winner & his score is {players_scores[1]}.")
                return

            print(
                f"Updated Score Of Player {player_no+1} : {players_scores[player_no]}"
            )

            input("Press Any Key To Continue For The Next Player Turn.")


if __name__ == "__main__":
    twoplayergame()
