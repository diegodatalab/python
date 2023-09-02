# 
# * 99. Calling a function in other function


def area(radius, pi=3.14): # //, po):
    result = pi*radius*radius
    return result


def cost(circle_area, cost_per_sqm):
    total_cost = circle_area*cost_per_sqm
    return total_cost


print(cost(area(10,3.15), 2))