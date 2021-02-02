export interface Node<T> {
    value: T
    next: Node<T> | undefined
}

export class LinkedList<T> {
    _head: Node<T>
    constructor() {
        this._head = {
            value: <T><unknown>undefined,
            next: undefined
        }
    }

    insert(value: T): void {
        const tail = this.tail()
        tail.next = { value, next: undefined }
    }

    erase(index: number): void {
        let left = this._head
        for (let i = 0; i < index; i++) {
            if (left.next)
                left = left.next
            else
                throw new Error('Out of index')
        }

        left.next = undefined
    }

    at(index: number): T | undefined { // 0 <= index < size
        let node = this._head
        for (let i = 0; i <= index; i++) {
            if (node.next)
                node = node.next
            else
                throw new Error('Out of index') // TODO
        }

        if (node && node != this._head)
            return node.value
        else
            return undefined
    }

    head(): T | undefined {
        return this.at(0)
    }

    size(): number {
        let count = 0
        let node = this._head
        while (node.next) {
            count += 1
            node = node.next
        }

        return count
    }

    find(predicate: (value: T) => boolean): number {
        let node = this._head
        let index = 0
        while (node.next) {
            if (predicate(node.next.value)) {
                return index
            } else {
                index += 1
                node = node.next
            }
        }

        return -1
    }

    private tail() {
        let node = this._head
        while (node.next)
            node = node.next

        return node
    }
}