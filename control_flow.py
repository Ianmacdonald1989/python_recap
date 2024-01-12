# if statements 
# if 3 > 4:
#     print("correct result")
# elif 0 > 1:
#     print("some other result")
# elif 0 == 0 and 5 > 1:
#     print("some other result")
#     if len([1,2,3]) > 2:
#         print("list is long enough")
# else:
#     print("incorrect result")   

# while loop
# counter = 0 
# while counter <= 10:
#     print(counter)
#     counter +=1 
#     if counter == 5:
#         print("counter is 5 ")
# print("while loop is finished") 


#for loop 
# test_list = {1:2, 3:4, 5:6}
# for k,v in test_list.items():
#     print(k)
#     print(v)

#truthy and falsey (only empty, string without letters or 0 are falsey)
# if "H": 
#     print("truthy")
# else:
#     print("falsey")

#excersice 

excercise_list = [1,2,3,4,5]
excercise_counter = 0
for x in excercise_list:
    if x == 2:
        print("the value is 2")
    else: 
        print("the value is not 2")
while excercise_counter<=6:
        print("last item")
        excercise_counter +=1
