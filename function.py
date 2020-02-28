# 在參數名前面的 * 表示 args 是一個可變參數
def add (* args):
    total = 0
    for val in args:
        total += val
    return total

print(add());
print(add(1,2,3,4,5));