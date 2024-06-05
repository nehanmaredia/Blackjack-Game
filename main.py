import random

VALUES = {
    "A": 1,
    "K": 10,
    "Q": 10,
    "J": 10,
}

def deal_card(deck):
    return deck.pop(random.randrange(len(deck)))

def hand_value(hand):
    value = sum(VALUES.get(card, card) for card in hand)
    aces = hand.count("A")
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def dealer_hand_str(dealer_hand):
    if len(dealer_hand) == 2:
        return str(dealer_hand[0])
    else:
        return f"{dealer_hand[0]}, {dealer_hand[1]}"

def play_game():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10] * 4 + ["A", "K", "Q", "J"] * 4
    random.shuffle(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    while True:
        print(f"\nDealer's hand: {dealer_hand_str(dealer_hand)} and X")
        print(f"Your hand: {', '.join(map(str, player_hand))} (Value: {hand_value(player_hand)})")

        if hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            return

        choice = input("(1) Stay or (2) Hit? ").strip()
        if choice == "1":
            break
        elif choice == "2":
            player_hand.append(deal_card(deck))
            if hand_value(player_hand) > 21:
                print(f"Your hand: {', '.join(map(str, player_hand))} (Value: {hand_value(player_hand)})")
                print("Bust! Dealer wins!")
                return

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    print(f"\nDealer's hand: {', '.join(map(str, dealer_hand))} (Value: {hand_value(dealer_hand)})")
    print(f"Your hand: {', '.join(map(str, player_hand))} (Value: {hand_value(player_hand)})")

    if hand_value(dealer_hand) > 21:
        print("Dealer busts! You win!")
    elif hand_value(player_hand) > hand_value(dealer_hand):
        print("You win!")
    else:
        print("Dealer wins!")

while True:
    play_game()
    play_again = input("Play again? (y/n) ").lower()
    if play_again != "y":
        break
