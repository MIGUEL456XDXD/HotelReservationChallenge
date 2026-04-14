from dataclasses import dataclass, field
from datetime import date
# Importamos las utilidades del módulo indicado
from app.services.util import generate_unique_id, guest_not_found_error


@dataclass
class Guest:
    REGULAR = "regular"
    VIP = "vip"

    name: str
    email: str
    type_: str = REGULAR

    def __str__(self):
        return f"Guest {self.name} ({self.email}) of type {self.type_}"


@dataclass
class Reservation:
    # Atributos obligatorios en el constructor
    guest_name: str
    description: str
    check_in: date
    check_out: date

    # id es opcional en el constructor, usa default_factory para el valor por defecto
    id: str = field(default_factory=generate_unique_id)

    # guests no se inicializa en el constructor (init=False) y es una lista vacía
    guests: list[Guest] = field(default_factory=list, init=False)

    def add_guest(self, name: str, email: str, type_: str = Guest.REGULAR):
        # Crea el objeto Guest y lo agrega a la lista interna
        nuevo_huesped = Guest(name=name, email=email, type_=type_)
        self.guests.append(nuevo_huesped)

    def delete_guest(self, guest_index: int):
        # Verifica si el índice existe en la lista
        if 0 <= guest_index < len(self.guests):
            self.guests.pop(guest_index)
        else:
            # Si el índice no es válido, llama a la función de error
            guest_not_found_error()

    def __len__(self):
        # Calcula la diferencia de días entre las fechas
        diferencia = self.check_out - self.check_in
        return diferencia.days

    def __str__(self):
        # Retorna el formato de texto multilínea solicitado
        return (f"ID: {self.id}\n"
                f"Guest: {self.guest_name}\n"
                f"Description: {self.description}\n"
                f"Dates: {self.check_in} - {self.check_out}")