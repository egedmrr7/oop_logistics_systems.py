class Route:
    def __init__(self, start_hub, end_hub):
        self.start_hub = start_hub
        self.end_hub = end_hub

    def calculate_distance(self):
        return self.start_hub.distance_to(self.end_hub)
