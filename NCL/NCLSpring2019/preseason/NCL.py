def main():

    values = [130, 154, 136, 252, 131, 157, 155, 137, 252, 228, 226, 229, 230]
    newvalues = []
    for i in range(13):
        temp = chr(values[i] ^ 209)
        newvalues.append(temp)
    print(newvalues)

main()