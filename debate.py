from typing import List, Optional
from .message import Message
from .seller import Seller
from .evaluation import Evaluation
from .company import Company

class DebateSession:
    def __init__(self, buyer: str, target: Company, max_rounds: int = 5):
        self.buyer = buyer
        self.target = target
        self.seller = Seller(target)
        self.transcript: List[Message] = []
        self.round = 1
        self.max_rounds = max_rounds
        self.deal_price: Optional[float] = None
        self.success: bool = False
        self.score: int = 0

    def add_message(self, speaker: str, text: str):
        self.transcript.append(Message(speaker, text))

    def negotiate(self, offer: float):
        self.add_message("intern", f"Offer: ${offer:.1f}B")
        reply = self.seller.respond(offer, self)
        self.add_message("seller", reply)
        print(f"Seller: {reply}")
        self.round += 1

    def finalize(self):
        result = Evaluation.evaluate(self)
        print("\n--- Outcome ---")
        print(result)
        print(f"Final Score: {self.score}/100")
        print("\nTranscript:")
        for msg in self.transcript:
            print(f"{msg.speaker.title()}: {msg.text}")
