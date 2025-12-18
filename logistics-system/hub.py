import math

class Hub:
    def __init__(self, hub_id, name, x, y):
        self.hub_id = hub_id
        self.name = name
        self.x = x
        self.y = y

    def distance_to(self, other_hub):
        return math.sqrt((self.x - other_hub.x) ** 2 + (self.y - other_hub.y) ** 2)
