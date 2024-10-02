import random

class Card:
    """يمثل ورقة لعب"""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    """يمثل مجموعة الأوراق"""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    def __init__(self):
        self.cards = [Card(value, suit) for suit in Deck.suits for value in Deck.values]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    """يمثل اللاعب"""
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def take_card(self, card):
        self.hand.append(card)

    def play_card(self):
        return self.hand.pop(0)  # في هذا النموذج البسيط، اللاعب يلعب أول ورقة

class BasraGame:
    """يمثل اللعبة نفسها"""
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.players = [Player(player1_name), Player(player2_name)]
        self.table = []
        self.deal_initial_cards()

    def deal_initial_cards(self):
        """توزيع الأوراق على اللاعبين والطاولة"""
        for _ in range(4):
            for player in self.players:
                player.take_card(self.deck.deal_card())
        for _ in range(4):
            self.table.append(self.deck.deal_card())

    def play_round(self):
        """إجراء جولة واحدة من اللعبة"""
        for player in self.players:
            print(f"\n{player.name}'s turn")
            print(f"Table cards: {[str(card) for card in self.table]}")
            played_card = player.play_card()
            print(f"{player.name} played {played_card}")

            # محاولة التقاط الأوراق
            for card in self.table:
                if card.value == played_card.value:
                    print(f"{player.name} captured {card}")
                    self.table.remove(card)
                    player.score += 1
                    break
            else:
                self.table.append(played_card)

    def check_winner(self):
        """تحديد الفائز بالنقاط"""
        if not self.deck.cards and all(len(player.hand) == 0 for player in self.players):
            if self.players[0].score > self.players[1].score:
                return self.players[0].name
            elif self.players[0].score < self.players[1].score:
                return self.players[1].name
            else:
                return "Draw"
        return None

    def play_game(self):
        """اللعب حتى انتهاء الأوراق"""
        while self.check_winner() is None:
            self.play_round()
        winner = self.check_winner()
        print(f"\nThe winner is {winner}!")

# بدء اللعبة
game = BasraGame("Player 1", "Player 2")
game.play_game()