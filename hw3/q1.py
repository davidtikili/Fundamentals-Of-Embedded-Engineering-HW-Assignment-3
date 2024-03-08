def mk_wd(balance):
  
    bal = [balance]
    def remove(amount):
        if amount <= bal[0]:
            bal[0] -= amount
            return bal[0]
        else:
            return "Insufficient Funds"

    return remove


rem = mk_wd(100)  
print(rem(10))  
print(rem(20))  
print(rem(100)) 
