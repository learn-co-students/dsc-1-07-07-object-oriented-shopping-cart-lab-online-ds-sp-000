class ShoppingCart:
    # write your code here
    
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            item_dict = {'name': name, 'price': price, 'quantity': quantity}
            self.items.append(item_dict)
            self.total += price 
        return round(self.total,2)
    def mean_item_price(self):
        num_items = len(self.items)
        total = self.total
        mean = total/num_items
        return mean
            

    def median_item_price(self):
        prices = [item["price"] for item in self.items]
        num_items = len(self.items)
        if (num_items%2==0):
            mid_one = int(len/2)
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        else:
            mid = int(num_items/2)
            return prices[mid]

            
    def apply_discount(self):
        if self.employee_discount != None:
            self.total = self.total*(100-self.employee_discount)/100
            return self.total
        else:
            print('Sorry, there is no discount to apply to your cart :(')

    def void_last_item(self):
        removed_item = self.items.pop()
        self.total = self.total - removed_item['price']
        return self.items