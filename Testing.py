from Main import *

# Define some reusable data
ebook1 = Ebook("Python Programming", "Author1", "Publisher1", date(2021, 1, 1), 50.0)
ebook2 = Ebook("Data Science", "Author2", "Publisher2", date(2022, 2, 1), 70.0)
customer1 = Customer(1, "John Doe", "john@example.com", "Gold")

# Test Cases

def test_add_modify_remove_ebook():
    catalog = Catalog()
    # Add e-book
    catalog.add_ebook(ebook1)
    assert len(catalog.ebooks) == 1
    print("E-book added:", catalog.ebooks[0].title)

    # Modify e-book
    catalog.modify_ebook(0, ebook2)
    assert catalog.ebooks[0].title == "Data Science"
    print("E-book modified to:", catalog.ebooks[0].title)

    # Remove e-book
    catalog.remove_ebook(0)
    assert len(catalog.ebooks) == 0
    print("E-book removed successfully")


def test_add_modify_remove_customer():
    # Adding customer
    customer_db = []
    customer_db.append(customer1)
    assert len(customer_db) == 1
    print("Customer added:", customer_db[0].name)

    # Modifying customer
    customer_db[0].name = "Jane Doe"
    assert customer_db[0].name == "Jane Doe"
    print("Customer modified to:", customer_db[0].name)

    # Removing customer
    customer_db.pop(0)
    assert len(customer_db) == 0
    print("Customer removed successfully")


def test_add_ebook_to_cart():
    cart = ShoppingCart()
    # Add e-books to cart
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    assert len(cart.items) == 2
    print("E-books in cart:", [item.title for item in cart.items])

    # Calculate total
    total = cart.calculate_total()
    assert total == 120.0  # 50 + 70
    print("Total cart value:", total)


def test_apply_discount():
    cart = ShoppingCart()
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    total = cart.calculate_total()

    # Apply a 10% discount for a loyalty program member
    discount = Discount("Loyalty", 10)
    discounted_total = discount.apply_discount(total)
    assert discounted_total == 108.0  # 120 - 10%
    print("Total after applying discount:", discounted_total)


def test_generate_invoice():
    cart = ShoppingCart()
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    subtotal = cart.calculate_total()

    # Apply multiple discounts
    discount1 = Discount("Loyalty", 10)
    discount2 = Discount("Bulk Purchase", 5)
    discounts = [discount1, discount2]

    # Generate invoice
    invoice = Invoice(subtotal, discounts)
    total_with_vat = invoice.calculate_total_with_discounts_and_vat()
    assert round(total_with_vat, 2) == 116.64  # 120 - 15% discount + 8% VAT
    print("Total with discounts and VAT:", total_with_vat)


# Run all tests
if __name__ == "__main__":
    print("Running tests...")
    test_add_modify_remove_ebook()
    test_add_modify_remove_customer()
    test_add_ebook_to_cart()
    test_apply_discount()
    test_generate_invoice()
    print("All tests passed!")
