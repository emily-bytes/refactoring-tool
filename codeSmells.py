class Tests: 
    def clone():
        z, t = 10, 10
        for i in range(1, z + 1):
            if i == 1:
                print(f"{z}, ", end="")      

    def exact_clone():
        z, t = 10, 10
        for i in range(1, z + 1):
            if i == 1:
                print(f"{z}, ", end="")     

    def renamed_clone():
        z, t = 10, 10
        for i in range(1, z + 1):
            if i == 1:
                print(f"{z}, ", end="")     
        
    def gapped_clone():
        n, t = 10, 10
        for i in range(1, n + 1):
            if i == 1:
                print(f"{n}, ", end="")    
                
    def method(n):
        return n 
    
    def is_long_method1():
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

    def is_long_method2():
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
            if n == 2: n
        return 0
    
    def not_long_parameter_list(n=0, t=5):
        y = n + t
        return y    
    
    def long_parameter_list(n, t, y, z):
        return n + t + y + z

    def not_long_method(n):
        n = 3
        for i in range(1, n + 1):
            if i == 1:
                print(f"{n}, ", end="")
        return 0
    
