from delivery_system import DeliverySystem
from hub import Hub
from route import Route

system = DeliverySystem()

# Hubs
hub1 = Hub("H1", "Istanbul", 0, 0)
hub2 = Hub("H2", "Ankara", 3, 4)

# Packages
system.register_package("P001", "Istanbul", "Ankara", 5, priority=1)
system.register_package("P002", "Istanbul", "Izmir", 2, priority=3)

# Route & distance calculation
route = Route(hub1, hub2)
print("Route distance:", route.calculate_distance())

# Sorting packages
sorted_packages = system.sort_packages(by="priority")
print("Sorted by priority:")
for p in sorted_packages:
    print(p.package_id, p.priority)

# Tracking
pkg = system.track_package("P001")
print("Tracking P001:", pkg.status)
