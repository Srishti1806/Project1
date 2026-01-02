# test_product_program.py

from product import calculate_final_price, classify_product

# Test final price calculation
def test_final_price_no_discount():
    price = 10000
    discount = 0
    assert calculate_final_price(price, discount) == 10000

def test_final_price_with_discount():
    price = 8000
    discount = 10
    assert calculate_final_price(price, discount) == 7200

def test_final_price_full_discount():
    price = 5000
    discount = 100
    assert calculate_final_price(price, discount) == 0

# Test product classification
def test_classification_premium():
    final_price = 15000
    assert classify_product(final_price) == "Premium"

def test_classification_standard():
    final_price = 7000
    assert classify_product(final_price) == "Standard"

def test_classification_budget():
    final_price = 3000
    assert classify_product(final_price) == "Budget"
def test_classification_economy():
    final_price = 1500
    assert classify_product(final_price) == "Economy"
