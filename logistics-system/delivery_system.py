from package import Package

class DeliverySystem:
    def __init__(self):
        self.packages = {}

    # Package registration
    def register_package(self, package_id, origin, destination, weight, priority=1):
        package = Package(package_id, origin, destination, weight, priority)
        self.packages[package_id] = package
        return package

    # Tracking by ID
    def track_package(self, package_id):
        return self.packages.get(package_id)

    # Search package
    def search_package(self, package_id):
        return self.packages.get(package_id)

    # Sorting algorithms
    def sort_packages(self, by="priority"):
        if by == "priority":
            return sorted(self.packages.values(), key=lambda p: p.priority)
        elif by == "weight":
            return sorted(self.packages.values(), key=lambda p: p.weight)
        elif by == "destination":
            return sorted(self.packages.values(), key=lambda p: p.destination)
        else:
            return list(self.packages.values())
