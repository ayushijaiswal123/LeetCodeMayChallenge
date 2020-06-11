class StockSpanner:

#     def __init__(self):
#         self.storage = [] 
#         # self.storage = {}
#         self.size = 0
#         minimum = 0
#         maximum = 0

#     def next(self, price: int) -> int:
#         # Inital Case
#         if self.size == 0:
#             self.storage.append(price)
#             self.minimum = price
#             self.maximum = price
#             self.size += 1
#             return 1
#         # All Rest of the Cases
#         self.storage.append(price)
#         self.size += 1
#         self.minimum = min(self.minimum, price)
#         self.maximum = max(self.maximum, price)
#         if price >= self.minimum and price >= self.maximum:
#             print("Not executing Loop")
#             return self.size
#         count = 1
#         print("Loop will run")
#         for i in range(self.size-2,-1,-1):
#             if self.storage[i] > price:
#                 return count
#             count += 1
#         return count
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
