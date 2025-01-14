class Recursion:
    def add_list_elements(self, l):
        length = len(l)
        if length == 1:
            return l[0]
        return l[0] + self.add_list_elements(l[1:])
    def add_list_data(self, list_data):
        total = 0
        for element in list_data:
            if type(element) == type([]):
                total = total + self.add_list_data(element)
            else:
                total=total + element

        return total
    
    def get_factorial(self, num):
        if num<=1:
            return 1
        return num * self.get_factorial(num-1)
    def get_fibonachi(self, num):
        if num == 1 or num == 2:
            return 1
        return self.get_fibonachi(num-1) + self.get_fibonachi(num-2)
    
    def get_sum_digit(self, num):
        if num == 0:
            return 0
        return num % 10 + self.get_sum_digit(int(num/10))
    
    def sum_of_n_num(self, num):
        sum = 0
        if num == 0:
            return 0
        return num + self.sum_of_n_num(num-1) 
        

if __name__ == "__main__":
    obj = Recursion()
    # result = obj.add_list_elements([1,2,3,4])
    # result = obj.add_list_data([1, 2, [3, 4], [5, 6]])
    # result = obj.get_factorial(5)
    # result = obj.get_fibonachi(5)
    # result = obj.get_sum_digit(345)
    result = obj.sum_of_n_num(6)
    print(result)