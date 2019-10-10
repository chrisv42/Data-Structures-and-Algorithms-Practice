def binarySearch(arr: list):
    if not arr: return None
    if len(arr) == 1: return arr[0]
    if len(arr) == 2: return max(arr[-1],arr[0])
    mid = len(arr)//2
    if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
        return arr[mid]
    if arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
        self.binarySearch(arr[:mid+1])
    if arr[mid] < arr[mid+1] and arr[mid] > arr[mid-1]:
        self.binarySearch(arr[mid:])

a = [-2,-1,1,2,1,-1]

print(binarySearch(a))
