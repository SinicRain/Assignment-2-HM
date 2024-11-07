from datetime import date

class Ebook:
    def __init__(self, title, author, publisher, publication_date, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.price = price


class Customer:
    def __init__(self, customer_id, name, email, membership_status):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.membership_status = membership_status


class Catalog:
    def __init__(self):
        self.ebooks = []

    def add_ebook(self, ebook):
        self.ebooks.append(ebook)

    def modify_ebook(self, index, new_ebook):
        if 0 <= index < len(self.ebooks):
            self.ebooks[index] = new_ebook

    def remove_ebook(self, index):
        if 0 <= index < len(self.ebooks):
            self.ebooks.pop(index)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, ebook):
        self.items.append(ebook)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)

    def calculate_total(self):
        return sum(item.price for item in self.items)


class Discount:
    def __init__(self, discount_type, discount_value):
        self.discount_type = discount_type
        self.discount_value = discount_value

    def apply_discount(self, amount):
        return amount - (amount * self.discount_value / 100)


class Invoice:
    VAT_RATE = 0.08  # 8% VAT

    def __init__(self, subtotal, discounts):
        self.subtotal = subtotal
        self.discounts = discounts
        self.total = 0

    def calculate_total_with_discounts_and_vat(self):
        discounted_total = self.subtotal
        for discount in self.discounts:
            discounted_total = discount.apply_discount(discounted_total)
        self.total = discounted_total + (discounted_total * self.VAT_RATE)
        return self.total
