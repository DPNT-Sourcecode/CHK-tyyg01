from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("!") == -1
        assert checkout_solution.checkout("AAAABBC") == 245
        assert checkout_solution.checkout("AABBD") == 160

        assert checkout_solution.checkout("AAAAABBD") == 260
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("AAAEEBA") == 260

