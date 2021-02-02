export class Stack<T> {
    array = [] as T[]

    push(val: T): void {
        this.array.push(val)
    }

    pop(): T | undefined {
        if (this.array.length > 0)
            return this.array.pop()
        else
            throw new Error()
    }

    get size() {
        return this.array.length
    }
}

export class Queue<T> {
    in_stack = new Stack<T>()
    out_stack = new Stack<T>()

    push(val: T): void {
        this.in_stack.push(val)
    }

    pop(): T | undefined {
        if (this.out_stack.size == 0)
            while (this.in_stack.size > 0)
                this.out_stack.push(this.in_stack.pop()!)

        return this.out_stack.pop()
    }
}