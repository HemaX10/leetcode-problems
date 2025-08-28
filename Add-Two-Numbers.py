# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        firstNumber = ""
        secondNumber = ""
        num1 = l1
        num2 = l2
        while(num1.next != None) : 
            num = str(num1.val)
            firstNumber += num
            num1 = num1.next
        firstNumber += str(num1.val)

        while(num2.next != None) : 
            num = str(num2.val)
            secondNumber += num
            num2 = num2.next
        secondNumber += str(num2.val)

        revresedN1 = "".join(reversed(firstNumber))
        reversedN2 = "".join(reversed(secondNumber))

        addedNumber = int(revresedN1) + int(reversedN2)

        strAddedNumber = str(addedNumber)
        lengthNumber = len(strAddedNumber) -1
        head = ListNode(int(strAddedNumber[lengthNumber]))
        current = head
        for num in range(lengthNumber ,0,-1) : 
            current.next = ListNode(int(strAddedNumber[num-1]))
            current = current.next 
        return head
        