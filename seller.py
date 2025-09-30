from .company import Company

class Seller:
    def __init__(self, company: Company):
        self.company = company

    def respond(self, offer: float, session) -> str:
        fair_low = self.company.ideal_price * 0.9
        fair_high = self.company.ideal_price * 1.1

        if offer < fair_low * 0.8:
            session.success = False
            return f"Your ${offer:.1f}B offer is insulting. {self.company.name} walks away!"

        if offer > fair_high:
            session.deal_price = offer
            session.success = True
            return f"We’ll gladly accept ${offer:.1f}B. (You overpaid badly!)"

        if fair_low <= offer <= fair_high:
            session.deal_price = offer
            session.success = True
            return f"Hmm… ${offer:.1f}B is within range. We can make this deal."

        return f"Your ${offer:.1f}B offer is too low given our {self.company.growth_rate}% growth. Try again."
