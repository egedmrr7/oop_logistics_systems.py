# logistics_system.py
# Stage 1: Core Architecture


from datetime import datetime

class Package:
    def __init__(self, package_id, origin, destination, weight):
        self.package_id = package_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = "CREATED"   # CREATED – IN_TRANSIT – DELIVERED
        self.assigned_courier = None

    def __str__(self):
        return f"Package({self.package_id}, {self.origin} -> {self.destination}, {self.weight}kg)"


class Courier:
    def __init__(self, courier_id, name, vehicle_type):
        self.courier_id = courier_id
        self.name = name
        self.vehicle_type = vehicle_type
        self.current_location = None
        self.current_route = None

    def __str__(self):
        return f"Courier({self.name}, Vehicle: {self.vehicle_type})"


class Route:
    def __init__(self, route_id):
        self.route_id = route_id
        self.stops = []   # ["Hub A", "Customer X", ...]
        self.assigned_packages = []

    def add_stop(self, stop):
        self.stops.append(stop)

    def add_package(self,package):
        self.assigned_packages.append(package)

    def __str__(self):
        return f"Route({self.route_id}, Stops: {self.stops})"


class Hub:
    def __init__(self, hub_id, name, location):
        self.hub_id = hub_id
        self.name = name
        self.location = location
        self.stored_packages = []

    def accept_package(self, package):
        self.stored_packages.append(package)

    def __str__(self):
        return f"Hub({self.name}, {self.location})"


class DeliverySystem:
    def __init__(self):
        self.packages = {}
        self.couriers = {}
        self.hubs = {}
        self.routes = {}

    # --- Package operations ---
    def create_package(self, package_id, origin, destination, weight):
        pkg = Package(package_id, origin, destination, weight)
        self.packages[package_id] = pkg
        return pkg

    # --- Courier operations ---
    def register_courier(self, courier_id, name, vehicle_type):
        courier = Courier(courier_id, name, vehicle_type)
        self.couriers[courier_id] = courier
        return courier

    # --- Hub operations ---
    def register_hub(self, hub_id, name, location):
        hub = Hub(hub_id, name, location)
        self.hubs[hub_id] = hub
        return hub

    # --- Route operations ---
    def create_route(self, route_id):
        route = Route(route_id)
        self.routes[route_id] = route
        return route

    # Simple route assignment
    def assign_package_to_courier(self, package_id, courier_id):
        pkg = self.packages.get(package_id)
        courier = self.couriers.get(courier_id)

        if pkg and courier:
            pkg.assigned_courier = courier_id
            return True
        return False


if __name__ == "__main__":

    system = DeliverySystem()

    # Hub ekleme
    hub1 = system.register_hub("H1", "Merkez Hub", "Istanbul")

    # Paket oluşturma
    p1 = system.create_package("P001", "Istanbul", "Bursa", 5.2)
    hub1.accept_package(p1)

    # Kurye ekleme
    c1 = system.register_courier("C1", "Ahmet","Car")

    # Rota oluşturma
    r1 = system.create_route("R1")
    r1.add_stop("Istanbul Hub")
    r1.add_stop("Bursa Delivery Point")
    r1.add_package(p1)

    # Atama
    system.assign_package_to_courier("P001", "C1")

    # Konsol çıktısı
    print("=== SYSTEM STATE ===")
    print(p1)
    print(c1)
    print(r1)
    print(hub1)
