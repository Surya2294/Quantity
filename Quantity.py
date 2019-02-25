for quant in range(50,0,-1):
    if quant>1:
        print(quant, "bottles of beer on the wall", quant, "bottle of beer")
        if quant > 2:
            suffix = str(quant) + "bottels of beer on the wall"
        else:
            suffix = "1 bottle of beer on the wall"
    elif quant == 1 :
        print("1 bottle of beer on the wall, 1 bottle of beer")
        suffix = "no more beer on the wall"
    print("take one down and pass it around ", suffix)
    print("--------")