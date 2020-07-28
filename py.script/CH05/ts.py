def tuple_ss(ts):
    ts= ts[1:len(ts)-1].replace("},","}=").split("=")
    ts = sorted([x[1:len(x)-1].split(',')for x in ts],key=lambda x:len(x))
    result = [int(i)for i in ts[-1]]
    return result
if __name__=="__main__":
    ts = input("중복없는 튜플의 집합 형태 입력 >> ")
    print(tuple_ss(ts))