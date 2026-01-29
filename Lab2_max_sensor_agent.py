from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
import datetime
import asyncio
from environment import DisasterEnvironment


class SensorBehaviour(PeriodicBehaviour):
    async def run(self):
        percepts = self.env.sense()
        timestamp = datetime.datetime.now()

        print(f"[{timestamp}] Sensor readings: {percepts}")

        for event, value in percepts.items():
            if value >= 7:
                print(f"⚠️ ALERT: High {event} detected (severity={value})")


class SensorAgent(Agent):
    async def setup(self):
        print("SensorAgent started successfully.")
        self.env = DisasterEnvironment()

        behaviour = SensorBehaviour(period=5)
        behaviour.env = self.env
        self.add_behaviour(behaviour)


if __name__ == "__main__":
    agent = SensorAgent(
        "max_sensor_agent@xmpp.jp",   # 👈 replace with YOUR JID
        "xdedse"        # 👈 replace with YOUR password
    )

    asyncio.run(agent.start())
