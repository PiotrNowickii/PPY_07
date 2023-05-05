import MyLinkedList

linked_list = MyLinkedList.MyLinkedList()
linked_list.append(4, "<=")
linked_list.append(19, "<=")
linked_list.append(7, "<=")
linked_list.append(2, "<=")


print(linked_list)
linked_list.delete(19)
linked_list.delete(8)
linked_list.delete(4)

print(linked_list)
print(linked_list.get(2))
print(linked_list)
linked_list.delete(2)
