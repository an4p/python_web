def verify_percents(min,max):
    def wrapper1(function):
        def wrapper2(deposit,percents):
            print("ok")
            if percents<min:
                percents=min
            if percents > max:
                percents=max

            res = function(deposit,percents)
            return res
        return wrapper2
    return wrapper1

@verify_percents(10,20)
def percents(deposit, percents):
    return deposit+deposit*percents/100

result = percents(100,50)
print(result)

