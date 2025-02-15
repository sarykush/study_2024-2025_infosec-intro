# само за себя говорит
def hex_to_bin(ints):
    scale = 16
    res = bin(int(ints, scale)).zfill(8) 
    return res

# xor для двух строк (должны быть одинаковой длины, чтобы получить полный ключ/шифротекст. в случае, если длины строк не совпадают, ту, что короче, необходимо повторить до соответствия длине второй строки)
def xor(a, b, n):
    ans = ""
    for i in range(n):
        if (a[i] == b[i]): 
            ans += "0"
        else: 
            ans += "1"
    return ans 
 
# main code
if __name__ == "__main__":
    a = hex_to_bin('d8f2e8f0ebe8f6202d20c2fb20c3e5f0eee92121d8f2')
    b = hex_to_bin('d120cdeee2fbec20c3eee4eeec2c20e4f0f3e7fcff21')

    n = len(a)
    c = xor(a, b, n)
    print(c)
