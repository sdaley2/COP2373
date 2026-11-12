import random

class Deck:
    """Create and manage a deck of cards."""

    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        """Deal one card from the deck."""

        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")

        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)

        return new_card

    def new_hand(self):
        """Move cards in play to the discard list."""

        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

def display_hand(hand, ranks, suits):
    """Display each card in poker hand."""

    for i in range(len(hand)):
        card = hand[i]
        rank = card % 13
        suit = card // 13

        print(f"{i + 1}. {ranks[rank]} of {suits[suit]}")

def draw_cards(deck, hand, selections):
    """Replace the selected cards with new cards."""

    for position in selections:
        index = position - 1

        if 0 <= index < 5:
            hand[index] = deck.deal()

def main():
    """Run the five-card poker draw program."""

    ranks = [
        "2", "3", "4", "5", "6", "7", "8",
        "9", "10", "J", "Q", "K", "A"
    ]

    suits = ["hearts", "clubs", "diamonds", "spades"]

    deck = Deck(52)

    # Deal the original five-card hand.
    hand = []

    for i in range(5):
        hand.append(deck.deal())

    print("Your Poker Hand:")
    display_hand(hand, ranks, suits)

    # Ask which cards the user want to replace.
    user_input = input(
        "\nEnter card numbers to replace, separated by commas "
        "(example: 1, 3, 5):"
    )

    selections = []

    for number in user_input.split(","):
        number = number.strip()

        if number.isdigit():
            selections.append(int(number))

    # Replace the selected cards.
    draw_cards(deck, hand, selections)

    print("\nYour New Poker Hand:")
    display_hand(hand, ranks, suits)

    deck.new_hand()

if __name__ == "__main__":
    main()