from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        # R1
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("!") == -1
        assert checkout_solution.checkout("AAAABBC") == 245
        assert checkout_solution.checkout("AABBD") == 160

        # R2
        assert checkout_solution.checkout("AAAAABBD") == 260
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("AAAEEBA") == 260

        # R3
        assert checkout_solution.checkout("FFFFFFF") == 50

        # R4
        assert checkout_solution.checkout("HHHHHHKKO") == 185
        assert checkout_solution.checkout("NNNNMMPPPPP") == 375
        assert checkout_solution.checkout("QQQQRRRST") == 270
        assert checkout_solution.checkout("UUUUVVVV") == 300

        # R5
        assert checkout_solution.checkout("ZZXS") == 66
        assert checkout_solution.checkout("ZSTXXYA") == 140
        assert checkout_solution.checkout("SSSZ") == 65










