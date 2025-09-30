class Company:
    def __init__(self, name: str, revenue: float, growth_rate: float, market_cap: float, ideal_price: float):
        self.name = name
        self.revenue = revenue
        self.growth_rate = growth_rate
        self.market_cap = market_cap
        self.ideal_price = ideal_price  # hidden fair value

