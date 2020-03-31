
def main():
    values = [
        130,
        154,
        136,
        252,
        131,
        157,
        155,
        137,
        252,
        233,
        227,
        229,
        231
    ] 
    password = []
    for i in range(13):
        temp = chr(values[i] ^ 209)
        password.append(temp)
    print(password)
main()
