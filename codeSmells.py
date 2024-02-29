class Tests: 
    def not_long_method(n):
        n = 3
        for i in range(1, n + 1):
            if i == 1:
                print(f"{n}, ", end="")
        return 0
    
    def method(n):
        return n 
    
    def is_long_method():
        n, t = 10, 10

        for i in range(1, n + 1):
            if i == 1:
                print(f"{n}, ", end="")

        for i in range(1, t + 1):
            if t == 1:
                print(f"{t}, ", end="")

        for i in range(1, n + 1):
            if i == 1:
                print(f"{n}, ", end="")

        for i in range(1, t + 1):
            if t == 1:
                print(f"{t}, ", end="")    
        for i in range(1, n + 1):
            if i == 1:
                print(f"{n}, ", end="")

        for i in range(1, t + 1):
            if t == 1:
                print(f"{t}, ", end="")
        return 0
    
    def not_long_parameter_list(n=0, t=5):
        y = n + t
        return y    
    
    def long_parameter_list(n, t, y, z):
        return n + t + y + z