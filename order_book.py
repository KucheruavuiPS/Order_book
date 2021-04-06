class OrderBook:
    """Representing of market order book"""
    def __init__(self):
        self.bid_list = []
        self.ask_list = []
        self.last_order_id = 0
        self.bid_count = len(self.bid_list)
        self.ask_count = len(self.ask_list)

    def add_new_order(self, type: bool, price: float, quantity: int):
        """
        Creating and adding new order in OrderBook
        :param type: order type, True - Bid, False - Ask
        :param price: order price
        :param quantity: quantities of order
        """
        self.last_order_id += 1
        new_order = Order(type, price, quantity, self.last_order_id)
        self.bid_list.append(new_order) if new_order.type else self.ask_list.append(new_order)

    def delete_order_by_id(self, order_id: int):
        """
        Deleting order by order ID
        :param order_id: id of order
        """
        all_orders = [self.ask_list, self.bid_list]
        for array in all_orders:
            for order in array:
                if order.id == order_id:
                    array.remove(order)
        print(f"Order - {order_id} deleted successfully")

    def get_order_by_id(self, order_id: int):
        """
        Getting order entities by order ID
        :param order_id: id of order
        :return: Order
        """
        all_orders = [self.ask_list, self.bid_list]
        for array in all_orders:
            for order in array:
                if order.id == order_id:
                    return order

    @property
    def spread(self):
        """
        Calculating current spread
        :return: float
        """
        return self.ask - self.bid

    @property
    def bid(self):
        """
        Calculating highest bid price
        :return:
        """
        if len(self.bid_list) == 0:
            print('There is no one buy orders')
        else:
            max_bid = self.bid_list[0].price
            for order in self.bid_list:  # Searching highest price
                if order.price > max_bid:
                    max_bid = order.price
            return max_bid

    @property
    def ask(self):
        """
        Calculating lowest ask price
        :return: float
        """
        if len(self.ask_list) == 0:
            print('There is no one sell orders')
        else:
            min_ask = self.ask_list[0].price
            for order in self.ask_list:  # Searching lowest price
                if order.price < min_ask:
                    min_ask = order.price
            return min_ask

    def get_market_data_snapshot(self):
        """
        Creating dict with all ask & bid prices and quantities
        :return: dict
        """
        snapshot = {"asks": [], "bids": []}
        orders_list = [self.ask_list, self.bid_list]
        for orders in orders_list:  # Getting ask and bid lists
            result_dict = {}
            for order in orders:
                if order.price in result_dict:  # Adding new price
                    result_dict[order.price] += order.quantity  # If already exist
                else:
                    result_dict[order.price] = order.quantity  # If not exist
            if orders_list.index(orders):  # Checking the type of orders
                snapshot["bids"].append(result_dict)
            else:
                snapshot["asks"].append(result_dict)
        return snapshot


class Order:
    """Represents the market order entity"""
    def __init__(self, type: bool, price: float, quantity: int, order_id: int):
        """
        :param type: True - Bid, False - Ask
        :param price: order price
        :param quantity: order quantity
        :param order_id: id of order
        """
        self.type = type
        self.price = price
        self.quantity = quantity
        self.id = order_id

    def __str__(self):
        bid_or_ask = 'Bid' if self.type else 'Ask'
        return f"Type: {bid_or_ask}\n" \
               f"Price: {self.price}\n" \
               f"Quantity: {self.quantity}\n" \
               f"ID: {self.id}"


if __name__ == '__main__':
    order_book = OrderBook()
    new_orders = [(True, 36.32, 15), (True, 44.22, 28), (True, 58.43, 5), (True, 21.98, 15), (False, 65.87, 55),
                  (False, 72.95, 30), (False, 200.23, 36), (False, 83.65, 50)]
    for o in new_orders:  # Adding new orders in order book
        order_book.add_new_order(o[0], o[1], o[2])
    print(order_book.ask)  # Calculating lowest ask price
    print(order_book.bid)  # Calculating highest bid price
    print(order_book.get_market_data_snapshot())  # Getting market data snapshot
    print(order_book.get_order_by_id(3))  # Getting order from order book by ID
    order_book.delete_order_by_id(3)  # Deleting order from order book by ID

