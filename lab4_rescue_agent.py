from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio


class ReceiveBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)

        if msg:
            performative = msg.get_metadata("performative")

            print("\n[RECEIVED MESSAGE]")
            print("Sender:", msg.sender)
            print("Performative:", performative)
            print("Content:", msg.body)

            if performative == "inform" and "CRITICAL_SEVERITY" in msg.body:
                severity = msg.body.split(":")[1]
                print(f"[ACTION] Initiating rescue for severity {severity}\n")
        else:
            print("[INFO] No new messages.")


class RescueAgent(Agent):
    async def setup(self):
        print("🚑 RescueAgent ready to receive messages.")
        self.add_behaviour(ReceiveBehaviour())

if __name__ == "__main__":
    agent = RescueAgent(
        "rescue_agent_max@xmpp.jp",
        "xdedse"
    )

asyncio.run(agent.start())