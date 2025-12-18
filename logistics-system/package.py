class Package:
    def __init__(self, package_id, origin, destination, weight, priority=1):
        self.package_id = package_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.priority = priority
        self.status = "REGISTERED"  # REGISTERED, IN_TRANSIT, DELIVERED

    def update_status(self, new_status):
        self.status = new_status
