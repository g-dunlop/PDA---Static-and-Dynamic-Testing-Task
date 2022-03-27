import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardGame1 = CardGame()
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 5)
        self.card3 = Card("Clubs", 10)
        self.cards = [self.card1, self.card2, self.card3]

    def test_can_check_for_ace(self):
        self.assertEqual(True, self.cardGame1.check_for_ace(self.card1))

    def test_can_find_highest_card(self):
        self.assertEqual(self.card2, self.cardGame1.highest_card(self.card1, self.card2))

    def test_total_cards(self):
        self.assertEqual("You have a total of 16", self.cardGame1.cards_total(self.cards))

