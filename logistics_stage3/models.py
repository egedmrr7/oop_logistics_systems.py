class Package:
    def __init__(self, pid, origin, destination, priority, status="CREATED"):
        self.id = pid
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.status = status


class Hub:
    def __init__(self, name):
        self.name = name
        self.connections = {}  # hub_name -> distance


class Route:
    def __init__(self, path, total_distance):
        self.path = path
        self.total_distance = total_distance
