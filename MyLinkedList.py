from Element import Element


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, e):
        curr = self.head
        if curr is None:
            print("List is empty")
            return
        while True:
            if curr.data == e:
                return curr.data
            else:
                if curr.nextE is None:
                    print("Value you wish to find is not present")
                    return
                curr = curr.nextE

    def delete(self, e):
        curr = self.head
        if curr is None:
            print("List is empty")
            return
        while True:
            if curr.data == e:
                if self.head.nextE is None:

                    if self.head == curr:
                        self.head = curr.nextE
                        curr = None
                        self.size = self.size - 1
                        return
                    else:
                        prev.nextE = curr.nextE
                        if self.tail == curr:
                            self.tail = curr.nextE
                        curr = None
                        self.size = self.size - 1
                        return
                else:
                    self.head = None
                    self.tail = None
                    curr = None
                    self.size = self.size - 1
                    return
            else:
                if curr.nextE is None:
                    print("Value you wish to delete is not present")
                    return
                prev = curr
                curr = curr.nextE

    def append(self, e, func=None):
        new_element = Element(e)
        curr_element = self.head
        tmp = True
        if func is None or func == ">=":
            while tmp:
                if self.head is not None:
                    if e < curr_element.data:
                        if curr_element.nextE is None:
                            curr_element.nextE = new_element
                            self.tail = new_element
                            self.size = self.size + 1
                            tmp = False
                        else:
                            prev_element = curr_element
                            curr_element = curr_element.nextE
                    elif e >= curr_element.data:
                        element_holder = curr_element
                        curr_element = new_element
                        curr_element.nextE = element_holder
                        if self.head == element_holder:
                            self.head = curr_element
                        else:
                            prev_element.nextE = curr_element
                        self.size = self.size + 1
                        tmp = False
                else:
                    self.head = new_element
                    self.tail = new_element
                    self.size = self.size + 1
                    tmp = False
        elif func == "<=":
            while tmp:
                if self.head is not None:
                    if e > curr_element.data:
                        if curr_element.nextE is None:
                            curr_element.nextE = new_element
                            self.tail = new_element
                            self.size = self.size + 1
                            tmp = False
                        else:
                            prev_element = curr_element
                            curr_element = curr_element.nextE
                    elif e <= curr_element.data:
                        element_holder = curr_element
                        curr_element = new_element
                        curr_element.nextE = element_holder
                        if self.head == element_holder:
                            self.head = curr_element
                        else:
                            prev_element.nextE = curr_element
                        self.size = self.size + 1
                        tmp = False
                else:
                    self.head = new_element
                    self.tail = new_element
                    self.size = self.size + 1
                    tmp = False

    def __str__(self):
        tmp = "["
        curr_elem = self.head
        while curr_elem is not None:
            tmp = tmp + str(curr_elem.data) + ","
            curr_elem = curr_elem.nextE
        if tmp != "[":
            tmp = tmp[:-1] + "]"
        else:
            tmp = tmp + "]"
        return str(tmp)
