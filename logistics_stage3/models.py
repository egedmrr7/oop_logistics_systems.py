class Package:
    def __init__(self, package_id, origin, destination, priority, weight, volume, status="Pending"):
        self.package_id = package_id
        self.origin = origin
        self.destination = destination
        self.priority = int(priority)  # Sayısal karşılaştırma için int yapıyoruz
        self.weight = weight           # Kg bilgisi
        self.volume = volume           # Boyut bilgisi
        self.status = status

    # Bu metod paketlerin priority (öncelik) değerine göre 
    # büyükten küçüğe otomatik sıralanmasını sağlar
    def __repr__(self):
        return f"Package({self.package_id}, Priority: {self.priority}, {self.weight}kg)"

class Hub:
    def __init__(self, hub_id, name):
        self.hub_id = hub_id
        self.name = name
