#
# * 101. The enumerate Function

errands = ['go to gym', 'grab lunch', 'get promoted at work', 'sleep']

print(enumerate(errands))


for index, errand in enumerate(errands):
    print(f"{errand} is number {index} on my list of things to do today!")

print('-'*50)

for index, errand in enumerate(errands):
    print(f"{errand} is number {index+1} on my list of things to do today!")

print('-'*50)
                        # ! começa o index do 100
for index, errand in enumerate(errands, 100):
    print(f"{errand} is number {index} on my list of things to do today!")