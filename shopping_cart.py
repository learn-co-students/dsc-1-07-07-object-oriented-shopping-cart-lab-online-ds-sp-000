class ShoppingCart:
    def __init__(self, emp_disc=None):
        self.total = 0
        self.items = []
        self.employee_discount = emp_disc
        
    def add_item(self, name=None, price=None, quantity=1):
        self.items.append({"name":name, "price":price, "quantity": quantity})
        self.total += price * quantity
        return self.total

    def mean_item_price(self):
        return (self.total) / (sum(i['quantity'] for i in self.items))
    
    def median_item_price(self):
        price_list = []
        for i in self.items:
            n=i['quantity']
            x=i['price']
            for i in range(n):
                price_list.append(x)
        from statistics import median
        return median(price_list)
    
    def apply_discount(self):
        if self.employee_discount:
            return self.total - (self.total*self.employee_discount*0.01)
        else:
            return "Sorry you don't have a discount"
        
    def item_names(self):
        names_list= []
        for i in self.items:
            n=i['quantity']
            x=i['name']
            for i in range(n):
                names_list.append(x)
        return names_list
       
    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']    