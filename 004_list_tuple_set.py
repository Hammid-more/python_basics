
string_list = ["apple", "banana", "cherry", "date", "fig"]

int_list = [5, 3, 8, 1, 9, 2]

list = string_list + int_list
print(list)

print(len(string_list))

print(string_list[0:-1])

print(int_list[1:4])

string_list.append('grape')
print(string_list)

string_list.insert(2,"orange")
print(string_list)

list_2 = [10, 11, 12]
int_list.extend(list_2)
print(int_list)

string_list.remove('banana')
print(string_list)

popped = int_list.pop()
print(popped)
print(int_list)

string_list.reverse()
print(string_list)

int_list.sort()
print(int_list)

int_list.sort(reverse=True)
print(string_list)


print(min(int_list))

print(max(int_list))

print(sum(int_list))

print(string_list.index('cherry'))

print("fig" in string_list)
 
for item in int_list:
    print(item)

for index, string_list in enumerate(string_list):
    print(index, string_list)


string_list_str = ', '.join(string_list)
print(string_list_str)


string_list_str = string_list_str.split('-')
print(string_list_str)

fruit_tuple = ("mango", "pineaple", "papaya", "guava")
fruit = fruit_tuple
print(fruit_tuple)
print(fruit)

print(fruit_tuple[0:3])

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}

print(set_1.intersection(set_2))

print(set_1.difference(set_2))

print(set_1.union(set_2))
