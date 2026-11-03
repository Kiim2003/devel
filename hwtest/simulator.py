from hwtest.device import Device


class SimulatedDevice(Device):
    def __init__(self, voltage=5.0, temperature=35.0):
        self._voltage = voltage
        self._temperature = temperature
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def read_voltage(self):
        self._require_connected()
        return self._voltage

    def read_temperature(self):
        self._require_connected()
        return self._temperature

    def _require_connected(self):
        if not self.connected:
            raise RuntimeError("Device is not connected")
