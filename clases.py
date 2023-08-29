from abc import ABC, abstractmethod


class Vehiculo(ABC):
    identificador = 0

    def __init__(self, rendimiento, marca, *args, energia:int=120, **kwargs) -> None:
        self.rendimiento: int = rendimiento
        self.marca: str = marca
        self._energia: int = energia
        self.identificador: int = Vehiculo.identificador
        Vehiculo.identificador += 1

    @abstractmethod
    def recorrer(self, kilometros) -> None:
        pass

# Retorna la cantidad de kilometros que puede recorrer el vehiculo con la energia actual
    @property
    def autonomia(self) -> float:
        return int(self._energia * self.rendimiento)

    @property
    def energia(self) -> int:
        return self._energia

    @energia.setter
    def energia(self, consumo_energia) -> None:
        if consumo_energia > self._energia:
            self._energia = 0
        else:
            self._energia -= consumo_energia


class AutoBencina(Vehiculo):
    def __init__(self, *args,bencina_favorita: int, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bencina_favorita = bencina_favorita

    def recorrer(self, kilometros: int) -> str:
        km = min(self.autonomia, kilometros)
        gasto = int(km/self.rendimiento)
        self.energia = gasto
        return f"Anduve por {km}Km y gasté {gasto}L de bencina"

class AutoElectrico(Vehiculo):
    def __init__(self, vida_util_bateria: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vida_util_bateria = vida_util_bateria

    def recorrer(self, kilometros: int) -> str:
        km = min(self.autonomia, kilometros)
        gasto = int(km/self.rendimiento)
        self.energia = gasto
        return f"Anduve por {km}Km y gasté {gasto}W de energía eléctrica"


class Camioneta(AutoBencina):
    def __init__(self, capacidad_maleta: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.capacidad_maleta = capacidad_maleta


class FaitHibrido(AutoBencina, AutoElectrico):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, vida_util_bateria = 5, **kwargs)

    def recorrer(self, kilometros: int) -> str:
        return AutoBencina.recorrer(self, kilometros / 2) + AutoElectrico.recorrer(self, kilometros / 2)


class Telsa(AutoElectrico):
    def recorrer(self, kilometros: int) -> str:
        recorrido = super().recorrer(kilometros)
        return recorrido + "de forma inteligente"
