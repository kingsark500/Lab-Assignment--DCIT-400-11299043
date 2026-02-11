from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from spade.message import Message
import random
import asyncio

class SensorBehaviour(PeriodicBehaviour):
    async def run(self):
        severity = random.randint(0, 10)

        print(f"[SENSOR] Current severity level: {severity}")

        if severity >= 7:
            print("[ALERT] Critical disaster detected. Sending INFORM message.")

            msg = Message(to="rescue403@xmpp.jp")
            msg.set_metadata("performative", "inform")
            msg.body = f"CRITICAL_SEVERITY:{severity}"

            await self.send(msg)
            print("[SENSOR] INFORM message sent.\n")


class SensorAgent(Agent):
    async def setup(self):
        print("📡 SensorAgent initialized.")
        self.add_behaviour(SensorBehaviour(period=5))


if __name__ == "__main__":
    agent = SensorAgent(
        "max_sensor_agent@xmpp.jp",
        "xdedse"
    )

asyncio.run(agent.start())