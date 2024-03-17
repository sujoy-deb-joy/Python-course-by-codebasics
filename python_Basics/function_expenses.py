def find_total_expenses(expenses):
    """
    This function takes expenses list as an input
    and return a total sum of that list
    :param expenses:  list of input expenses
    :return: total expense
    """
    total = 0
    for expense in expenses:
        total += expense
    return total

expenses_sergey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

expeses_sergey = find_total_expenses(expenses_sergey)
expeses_sundar = find_total_expenses(expenses_sundar)

