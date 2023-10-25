"""
Abigail Boggs
amboggs@dmacc.edu
Last edited: 10/25/2023
Invoice Class Assignment
"""


class Invoice:

    """Invoice class"""
    def __init__(self, invoice_id, customer_id, address, last_name, first_name, phone_number, items_with_price={}):
        # step 1, get init running, look at previous assignments for empty dictionary
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")
        invoice_id_characters = set("1234567890")
        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
             raise ValueError
        if not phone_number_characters.issuperset(phone_number):
             raise ValueError
        if not customer_id_characters.issuperset(str(customer_id)):
            raise ValueError
        if not invoice_id_characters.issuperset(str(customer_id)):
            raise ValueError
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        if items_with_price == '':
            self.items_with_price = {}
        else:
            self.items_with_price = items_with_price

    def __str__(self):
        return (self.invoice_id + ": " + self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: "
                + self.phone_number + " Address: " + self.address + " Items: " + self.items_with_price)

    def __repr__(self):
        return'Invoice({},{},{},{},{},{},{})'.format(self.customer_id, self.customer_id, self.last_name,
                                                     self.first_name, self.phone_number, self.address,
                                                     self.items_with_price)

    def add_item(self, items_with_price):
        # step 2, figure out how to take a dictionary in and update the object's dictionary
        self.items_with_price.update(items_with_price)

    def create_invoice(self):
        total = 0
        tax = 0
        for k, v in self.items_with_price.items():
            print(f"{k}.....${v}")
            total = total + v
        tax = total * .06
        total = total + tax

        tax = "${:,.2f}".format(tax)
        total = "${:,.2f}".format(total)

        print(f"Tax..... {tax}")
        print(f"Total..... {total}")


# Driver code
if __name__ == '__main__':
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()

# output should look like this
'''
iPad.....$799.99
Surface.....$799.99
Tax..... $108.00
Total...... $1907.98
'''