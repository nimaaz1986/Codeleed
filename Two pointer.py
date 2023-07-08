def find_pair_with_sum(arr, target)
left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]


 if current_sum == target:
    return (arr[left], arr[right])

elif
