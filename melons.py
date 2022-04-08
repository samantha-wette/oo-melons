"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base call that other Melon Orders inherit from"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""
        
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type
    
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        if self.species == "Christmas Melon":
            base_price = base_price*1.5
            total = (1 + self.tax) * self.qty * base_price

        elif self.order_type == "international" and self.qty < 10:
            total = total + 3

        return round(total, 2)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes."""

        super().__init__(species, qty, 'domestic', .08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize international melon order attributes."""
        super().__init__(species, qty, 'international', 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
    
        return self.country_code

