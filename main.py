from simulation.company import Company
from simulation.debate import DebateSession   # or session if you renamed it

def run_acquisition():
    slack = Company(
        name="Slack",
        revenue=0.9,
        growth_rate=40,
        market_cap=17,
        ideal_price=27.7
    )

    session = DebateSession(buyer="Salesforce", target=slack)

    print(f"{session.buyer} is considering acquiring {slack.name}.")
    print(f"Financials: Revenue=${slack.revenue:.1f}B | Growth={slack.growth_rate}% | Market Cap=${slack.market_cap}B")
    print("=" * 50)

    while session.round <= session.max_rounds and not session.success:
        try:
            offer = float(input(f"[Round {session.round}] Intern offer (in $B): "))
        except ValueError:
            print("Please enter a numeric value.")
            continue

        session.negotiate(offer)

        if session.success:
            break

    session.finalize()


if __name__ == "__main__":
    run_acquisition()
