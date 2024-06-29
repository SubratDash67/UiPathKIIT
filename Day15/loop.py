class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def detectCycle(head):
    if not head or not head.next:
        return None
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def createLinkedList(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if pos != -1:
        current.next = cycle_node
    return head


def getUserInput():
    values = list(
        map(int, input("Enter the linked list values separated by spaces: ").split())
    )
    pos = int(input("Enter the position where the cycle begins (-1 for no cycle): "))
    return values, pos


def main():
    values, pos = getUserInput()
    head = createLinkedList(values, pos)

    cycle_start = detectCycle(head)
    if cycle_start:
        print(f"Cycle detected at node with value: {cycle_start.value}")
    else:
        print("No cycle detected")


if __name__ == "__main__":
    main()
