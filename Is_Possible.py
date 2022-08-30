

def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    while (sx < tx and sy < ty):
        if (ty > tx):
            ty %= tx;
        else:
            tx %= ty;
    if (sx > tx or sy > ty):
        return False;
    #又过了 while 又过了 if，说明 sx == tx 或者 sy == ty
    return (ty - sy) % sx == 0 if sx == tx else (tx - sx) % sy == 0;

# sx = 1, sy = 1, tx = 2, ty = 2
print(reachingPoints(1,1,6,2))
