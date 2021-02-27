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

 function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    if (l1 === null && l2 !== null)
        return l2
    
    else if (l1 !== null && l2 === null)
        return l1
    
    else if (l1 === null && l2 === null)
        return null
    
    else if (l1 !== null && l2 !== null && l1.val > l2.val)
        return mergeTwoLists(l2, l1)
    
    // l1는 l2보다 반드시 시작하는 값이 더 작고, l1, l2 는 null이 아님
    let l1_curr = l1
    let l2_curr = l2
    while (l1_curr.next !== null && l2_curr !== null) {
        if (l1_curr.next.val <= l2_curr.val) {
            l1_curr = l1_curr.next
        } else { // 중간에 삽입해야함
            const l1_next = l1_curr.next
            const l2_next = l2_curr.next
            l1_curr.next = l2_curr
            l2_curr.next = l1_next
            
            l1_curr = l1_curr.next
            l2_curr = l2_next
        }
    }
    
    if (l2_curr !== null) {
        let tail = l1_curr
        while (tail.next !== null)
            tail = tail.next
        
        tail.next = l2_curr
    }
    
    return l1
};