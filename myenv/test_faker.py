
import pytest
from faker import Faker

#importing faker 
fake = Faker()


@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_fake(input_value):
    try:
        assert input_value % fake.random_number(1, 10) == 0
    except AssertionError as e:
        raise e

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


#python -m pytest myenv\test_faker.py