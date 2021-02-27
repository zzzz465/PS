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

 function reverseList(head: ListNode | null): ListNode | null {
    if (head === null)
        return null
    
    let before = null
    let curr = head
    let newHead = null
    while (curr !== null) {
        const next = curr.next
        curr.next = before
        
        if (next === null) {
            // last element
            newHead = curr
        }
        before = curr
        curr = next
    }
    
    return newHead
};