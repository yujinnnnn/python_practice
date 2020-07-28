def multi_mx(a1,a2):
    result = []
    result = array(a1) * array(a2)
    result[0][1],result[1][0] = result[1][0],result[0][1]
    return result

if __name__ == '__main__':
    arr1 = [[1,2],[1,2]]
    arr2 = [[3,4],[5,6]]
    print(multi_mx(arr1,arr2))