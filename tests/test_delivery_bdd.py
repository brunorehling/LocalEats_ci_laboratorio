from pytest_bdd import scenarios
from tests.steps import test_delivery_steps  # noqa: F401,F403

scenarios("features/calc_delivery.feature")
