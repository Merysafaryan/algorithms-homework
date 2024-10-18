#check point 
#Quick sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

sample_list = [3, 6, 8, 10, 1, 2, 9]
sorted_list = quick_sort(sample_list)
print(sorted_list)

# Creating a list
my_list = [10, 20, 30, 40, 50]
my_list.append(60)
my_list.insert(1, 15) 
my_list.remove(30)
popped_element = my_list.pop()
length_of_list = len(my_list)
my_list.sort()
my_list.reverse()
index_of_element = my_list.index(20)
count_of_element = my_list.count(40)
print(my_list)
