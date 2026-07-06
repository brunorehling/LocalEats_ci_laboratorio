from pytest_bdd import scenarios
from tests.steps import test_discount_steps  # noqa: F401,F403

scenarios("features/calc_discount.feature")
