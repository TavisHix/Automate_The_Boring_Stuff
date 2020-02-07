# Write code that takes in a list of arguments and
# prints the ou separated by a comma and a space with
# and placed before the last item

def commaC(arr):
    lim = len(arr)
    string = ""
    if lim == 0:
        string = "This array is empty"
        return string
    for i in range(lim):
        if i == lim - 1:
            string = string + "and " + arr[i]
            return string
        string = string + arr[i] + ", "


arr = []
print(commaC(arr))
