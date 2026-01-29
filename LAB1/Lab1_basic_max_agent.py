from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio

class HelloBehaviour(CyclicBehaviour):
    async def run(self):
        print(f"Hello! I am running as {self.agent.jid}")
        await asyncio.sleep(5)


class BasicAgent(Agent):
    async def setup(self):
        print("Basic Agent Started Successfully")
        self.add_behaviour(HelloBehaviour())


if __name__ == "__main__":
    agent = BasicAgent(
        "maxwell_agent@xmpp.jp",   
        "xdedse"           
    )


asyncio.run(agent.start())


