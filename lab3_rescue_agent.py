from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
import asyncio
import random

class IdleState(State):
    async def run(self):
        print("\n[STATE] IDLE - Monitoring for disaster events...")
        await asyncio.sleep(4)

        severity = random.randint(0, 10)

        if severity >= 7:
            print(f"[EVENT] High severity detected ({severity})")
            self.agent.current_severity = severity
            self.set_next_state("RESPONDING")
        else:
            print(f"[INFO] Severity low ({severity}). Remaining IDLE.")
            self.set_next_state("IDLE")


class RespondingState(State):
    async def run(self):
        print(f"[STATE] RESPONDING - Handling severity {self.agent.current_severity}")
        await asyncio.sleep(5)

        print("[ACTION] Rescue operation executed successfully.")
        self.set_next_state("COMPLETED")


class CompletedState(State):
    async def run(self):
        print("[STATE] COMPLETED - Mission logged. Resetting.")
        await asyncio.sleep(3)
        self.set_next_state("IDLE")


class RescueAgent(Agent):
    async def setup(self):
        print("🚒 RescueAgent initialized.")

        self.current_severity = None

        fsm = FSMBehaviour()

        fsm.add_state(name="IDLE", state=IdleState(), initial=True)
        fsm.add_state(name="RESPONDING", state=RespondingState())
        fsm.add_state(name="COMPLETED", state=CompletedState())

        fsm.add_transition("IDLE", "RESPONDING")
        fsm.add_transition("IDLE", "IDLE")
        fsm.add_transition("RESPONDING", "COMPLETED")
        fsm.add_transition("COMPLETED", "IDLE")

        self.add_behaviour(fsm)


if __name__ == "__main__":
    agent = RescueAgent(
        "max_rescue_agent@xmpp.jp",
        "xdedse"
    )

    asyncio.run(agent.start())