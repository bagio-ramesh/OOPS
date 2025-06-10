def smart_sub(num1,num2):
    return abs(num1-num2)

assert smart_sub(100,80)==20,"invalid put.."
assert smart_sub(80,100)==20,"invalid..."
assert smart_sub(100,50)==50,"invalid parameter order...."

# print(smart_sub(100,80))
# print(smart_sub(80,100))