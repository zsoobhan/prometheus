from django.test import TestCase

import service


class TestServices(TestCase):

    def test_number_generator(self):
        limits = range(1, 10)
        for lim in limits:
            num = service._pick_random_number(lim)
            self.assertTrue(num <= lim)

    def test_generate_words(self):
        expected = ('one', 'five')
        result = service.generate_words(1, 5)
        self.assertEqual(result, expected)

    def test_generate_answer(self):
        question = "What is one + one?"
        answer = service.generate_answer(question)
        self.assertEqual(answer, 2)

    def test_generate_sum(self):
        res = service._generate_sum('one', 'three')
        expected = 4
        self.assertEqual(res, expected)
