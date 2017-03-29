def verify_percents(function):
    def wrapper(deposit,percents):
        print("ok")
        if percents<0:
            percents=0
        if percents > 30:
            percents=30

        res = function(deposit,percents)
        return res
    return wrapper

@verify_percents
def percents(deposit, percents):
    return deposit+deposit*percents/100

result = percents(100,50)
print(result)

