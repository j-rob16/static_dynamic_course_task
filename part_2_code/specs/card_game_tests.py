import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_if_card_is_ace(self):
        ace_card = Card('hearts', 1)
        king_card = Card('diamonds', 13)

        test_pass = CardGame.check_for_ace(self, ace_card)
        self.assertEqual(True, test_pass)

        test_fail = CardGame.check_for_ace(self, king_card)
        self.assertEqual(False, test_fail)

    def test_can_find_highest_card(self):
        ace_card = Card('hearts', 1)
        king_card = Card('diamonds', 13)

        highest_card = CardGame.highest_card(self, ace_card, king_card)
        self.assertEqual(king_card, highest_card)

    def test_can_find_total_card_value(self):
        ace_card = Card('hearts', 1)
        king_card = Card('diamonds', 13)
        cards = [ace_card, king_card]
        total_value = CardGame.cards_total(self, cards)
        self.assertEqual('You have a total of14', total_value)