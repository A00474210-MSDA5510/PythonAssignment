def Stack(stack_list: list, operation: str, element=None):
    if operation == "add":
        stack_list = [element] + stack_list
        return stack_list
    elif operation == "remove":
        stack_list.pop(0)
        return stack_list
    else:
        raise Exception("invalid arguement")


def Queue(queue_list: list, operation: str, element=None):
    if operation == "add":
        queue_list.append(element)
        return queue_list
    elif operation == "remove":
        queue_list.pop(0)
        return queue_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    random_list = [1, 2, 3, 4, 5]
    random_list = Stack(random_list, "remove")
    print(random_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
