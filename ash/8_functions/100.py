#
# * 100. Making A Function Return Multiple Values

def circle(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area, circumference

a,c = circle(10)

print(f"Area of the circle is {a}. Circumference of circle is..  {c}")