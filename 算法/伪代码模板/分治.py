# -*- coding: utf-8 -*-


def divide_conquer(problem,param1,param2,...):
    if problem is None:
        print_result
        return
    data = prepare_data(problem)
    subproblems = split_problem(problem,data)

    subresult1 = self.divide_conquer(subproblems[0],p1,...)
    subresult2 = self.divide_conquer(subproblems[1],p1,...)
    subresult3 = self.divide_conquer(subproblems[2],p1,...)
    subresult4 = self.divide_conquer(subproblems[3],p1,...)
    ...

    result = process_result(subresult1,subresult2,subresult3,subresult4,...)