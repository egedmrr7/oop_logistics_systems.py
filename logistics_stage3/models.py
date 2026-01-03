class Package:
    def __init__(self, package_id, origin, destination, priority, status="Pending"):
        self.package_id = package_id
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.status = status


class Hub:
    def __init__(self, hub_id, name):
        self.hub_id = hub_id
        self.name = name

