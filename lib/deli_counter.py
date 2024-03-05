katz_deli = ["Logan", "Avi", "Spencer"]

def line(arr):
    if not arr:
        print("The line is currently empty.")
    else:
        new_arr = []
        for index, customer in enumerate(arr, start=1):
            new_arr.append(f' {index}. {customer}')
        arr_str = ''.join(new_arr)
        print(f'The line is currently:{arr_str}')
            

line(katz_deli)
        
def take_a_number(arr,string):
    arr.append(string)
    index = arr.index(string) + 1
    print(f"Welcome, {string}. You are number {index} in line.")
    
def now_serving(arr):
    if arr:
        customer_serving = arr[0]
        print(f"Currently serving {customer_serving}.")
        arr.pop(0)
    else:
        print("There is nobody waiting to be served!")
    