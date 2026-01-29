import random

class DisasterEnvironment:
    def sense(self):
        """
        Simulate sensing the disaster environment.
        Returns random severity levels from 0 to 10.
        """
        return {
            "flood_level": random.randint(0, 10),
            "fire_intensity": random.randint(0, 10),
            "earthquake_severity": random.randint(0, 10)
        }