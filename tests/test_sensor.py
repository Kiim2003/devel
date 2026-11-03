import pytest
from hwtest.simulator import SimulatedDevice


def test_voltage_in_range(device):
    assert 4.75 <= device.read_voltage() <= 5.25


def test_read_requires_connection():
    dev = SimulatedDevice()
    with pytest.raises(RuntimeError):
        dev.read_voltage()
