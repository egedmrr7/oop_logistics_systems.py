classDiagram

    class Package {
        -package_id: str
        -origin: str
        -destination: str
        -weight: float
        -priority: int
        -status: str
        +update_status()
    }

    class Hub {
        -hub_id: str
        -name: str
        -x: float
        -y: float
        +distance_to(other_hub)
    }

    class Route {
        -start_hub: Hub
        -end_hub: Hub
        +calculate_distance()
    }

    class DeliverySystem {
        -packages: dict
        -hubs: dict
        +register_package()
        +track_package()
        +search_package()
        +sort_packages()
    }

    DeliverySystem --> Package : manages
    DeliverySystem --> Hub : manages
    Route --> Hub : connects
