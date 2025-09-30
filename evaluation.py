class Evaluation:
    @staticmethod
    def evaluate(session) -> str:
        if not session.success or session.deal_price is None:
            session.score = 0
            return "❌ No deal. You failed to close the acquisition."

        ideal = session.target.ideal_price

        if session.deal_price < ideal:
            discount = ideal - session.deal_price
            session.score = int(50 + discount * 10)
            return f"✅ Deal closed at ${session.deal_price:.1f}B (below fair ${ideal:.1f}B)! Excellent negotiation."
        elif session.deal_price <= ideal * 1.05:
            session.score = 40
            return f"✅ Deal closed at ${session.deal_price:.1f}B (fair value). Solid outcome."
        else:
            session.score = 10
            return f"✅ Deal closed at ${session.deal_price:.1f}B (above fair ${ideal:.1f}B). You overpaid."
