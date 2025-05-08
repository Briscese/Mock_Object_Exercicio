from src.custom_stack_class import CustomStack, StackEmptyException

class NumberAscOrder:

    def sort(self, stack: CustomStack):
        if stack.is_empty():
            raise StackEmptyException("Pilha vazia, nao pode ser ordenada")
        
        temp_list = []

        while not stack.is_empty():
            temp_list.append(stack.pop())

        return sorted(temp_list)
