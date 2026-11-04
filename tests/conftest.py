import pytest
from hwtest.simulator import SimulatedDevice


@pytest.fixture
def device():
    dev = SimulatedDevice()
    dev.connect()
    yield dev
    dev.disconnect()
