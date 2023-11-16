from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("E") == -1
        assert checkout_solution.checkout("AAAABBC") == 245
        assert checkout_solution.checkout("AABBD") == 160
