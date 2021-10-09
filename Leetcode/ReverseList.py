from typing import List
 
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:

        result = []

        while head:
            result.append(head.val)
            head = head.next
        
        return result[::-1]

if __name__ == "__main__":

    x_1 = ListNode(1)

    x_2 = ListNode(2)

    x_3 = ListNode(3)

    x_1.next = x_2

    x_2.next = x_3

    print(x_1.val,x_1.next.val,x_2.next.val)




    solution = Solution()

    print(solution.reversePrint(x_1))