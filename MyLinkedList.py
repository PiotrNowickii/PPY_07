from Element import Element


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, e, func=None):
        new_element = Element(e)
        curr_element = self.head
        tmp = True
        if func is None:
            while tmp:
                if self.head is not None:
                    if e >= curr_element.data:
                        if curr_element.nextE is None:
                            curr_element.nextE = new_element
                            self.size = self.size + 1
                            tmp = False
                        else:
                            curr_element = curr_element.nextE
                    elif e < curr_element.data:
                        element_holder = curr_element
                        curr_element = new_element
                        new_element.nextE = element_holder

                        self.size = self.size + 1
                        tmp = False
                else:
                    self.head = new_element
                    self.size = self.size + 1
                    tmp = False

    def __str__(self):
        tmp = "["
        curr_elem = self.head
        while curr_elem is not None:
            tmp = tmp + str(curr_elem.data) + ","
            curr_elem = curr_elem.nextE
        tmp = tmp[:-1] + "]"
        return str(tmp)
