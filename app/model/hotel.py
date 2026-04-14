from dataclasses import dataclass

@dataclass
class Guest:
    REGULAR = "regular"
    VIP = "vip"


    name: str
    email: str

    type_: str = REGULAR

    def __str__(self):
        return f"Guest {self.name} ({self.email}) of type {self.type_}"