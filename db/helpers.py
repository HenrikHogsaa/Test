

class YieldInput:

    def __init__(self, tenor_id, tenor, frequency, eff_yield, long_term_mean, first_coupon):
        self.tenor_id = tenor_id
        self.tenor = tenor
        self.frequency = frequency
        self.eff_yield = eff_yield
        self.long_term_mean = long_term_mean
        self.first_coupon = first_coupon

