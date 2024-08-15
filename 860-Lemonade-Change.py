class Solution(object):
    def lemonadeChange(self, bills):
        cash = []
        billNum = 0
        while bills : 
            if bills[billNum] == 5 : 
                cash.append(5)
            elif bills[billNum] == 10 : 
                if 5 in cash : 
                    cash.pop(cash.index(5))
                    cash.append(10)
                else : 
                    return False 
            else : 
                if 5 in cash and 10 in cash: 
                    cash.pop(cash.index(5))
                    cash.pop(cash.index(10))
                    cash.append(20)
                elif cash.count(5) >= 3 : 
                    cash.pop(cash.index(5))
                    cash.pop(cash.index(5))
                    cash.pop(cash.index(5))
                    cash.append(20)
                else : 
                    return False 
            bills.pop(billNum)
        return True
            