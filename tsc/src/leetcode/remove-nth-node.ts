/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let length = 0
    let node = head
    while (node !== null) {
        length += 1
        node = node.next
    }
    
    if (length > 1) {
        const delIndex = length - n
        if (delIndex > 0) {
            node = head
            for (let i = 1; i < delIndex; i++) {
                node = node.next
            }
            
            // now the node is pointing to the before node of the node that is to be deleted
            node.next = node.next.next
            
            return head
        } else { // removing the first node of the linked list
            return head.next
        }
    } else {
        return null
    }
};