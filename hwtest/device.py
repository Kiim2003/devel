from abc import ABC, abstractmethod


class Device(ABC):
    """Giao diện chung: simulator và thiết bị thật đều phải tuân theo."""

    @abstractmethod
    def connect(self) -> None: ...

    @abstractmethod
    def disconnect(self) -> None: ...

    @abstractmethod
    def read_voltage(self) -> float:
        """Điện áp nguồn, đơn vị Volt."""

    @abstractmethod
    def read_temperature(self) -> float:
        """Nhiệt độ, đơn vị độ C."""
