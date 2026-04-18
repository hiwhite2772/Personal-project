#Dinh nghia node cua linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Giai thuan cong 2 linked list
class Solution(object):
    def add_two_numbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next

#Ham tien ich tao linked list tu ds
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next    

#Ham tien ich in linked list
def print_linked_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))

#Test
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

sol = Solution()
result = sol.add_two_numbers(l1, l2)
print("Ket qua cong hai so:")
print_linked_list(result)