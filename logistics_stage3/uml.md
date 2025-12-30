
---

# UML Diyagramı (uml.md)



```md
```mermaid
classDiagram
    class Package {
        +package_id
        +origin
        +destination
        +weight
        +priority
        +status
        +update_status()
    }

    class Hub {
        +hub_id
        +name
        +x
        +y
        +distance_to()
    }

    class Route {
        +start_hub
        +end_hub
        +calculate_distance()
    }

    class DeliverySystem {
        +packages
        +hubs
        +register_package()
        +track_package()
        +sort_packages()
        +generate_report()
    }

    class Database {
        +connect()
        +insert_package()
        +fetch_packages()
    }

    DeliverySystem --> Package
    DeliverySystem --> Hub
    DeliverySystem --> Route
    DeliverySystem --> Database
    Route --> Hub
