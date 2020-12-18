def bubbleSort(lst):
    i = 0
    while True:
        if lst[i] > lst[i+1]:
            temp = lst[i+1]
            lst[i+1] = lst[i]
            lst[i] = temp
            i = 0
        else:
            i += 1
            if i == len(lst)-1:
                return lst

def binarySearch(lst, number):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low + high)//2
        if lst[mid] == number:
            return "Student is enrolled"
        elif number < lst[mid]:
            high = mid-1
        elif number > lst[mid]:
            low = mid+1
    return "Student is not enrolled"
def main():
    students = [1906, 1993, 2419, 2089, 4865, 2186, 3950, 1816, 2321, 3092,
                3457, 4410, 2157, 3197, 4717, 1539, 3940, 3928, 4881, 3270]
    sorted = bubbleSort(students)
    print(sorted)
    while True:
        if digits == -1:
            break
        digits = int(input("Enter the four digit S.N: "))
        print(binarySearch(sorted, digits))
        
main()
