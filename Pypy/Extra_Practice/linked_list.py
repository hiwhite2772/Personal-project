class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
class Solution:
    def lien_ket(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 != None and list2 != None:
            if list1.value <= list2.value:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
        if list1 != None:
            tail.next = list1

        else:
            tail.next = list2

        return dummy.next

node4 = ListNode(7)
node4 = ListNode(5, node5)
node3 = ListNode(4, node4)
node2 = ListNode(3, node3)
list1 = ListNode(1, node2)

node4 = ListNode(6)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
list2 = ListNode(1, node2)

res = Solution().lien_ket(list1, list2)

while res != None:
    print(res.value, end=" ")
    res = res.next