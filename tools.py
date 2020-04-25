def htrgb(hex):
    hex = hex.strip('#')
    l = len(hex)
    scalar = 6//l
    if scalar == 0:
        raise ArithmeticError('Can\'t solve > 24-bit RGB values')
    elif scalar == 6:
        return (int(hex*2, 16),)*3
    return int(hex[:l//3]*scalar, 16), int(hex[l//3:2*l//3]*scalar, 16), int(hex[2*l//3:]*scalar, 16)

def htrgba(hex):
    hex = hex.strip('#')
    l = len(hex)
    scalar = 8//l
    if scalar == 0:
        raise ArithmeticError('Can\'t solve > 24-bit RGB values')
    elif scalar == 8:
        return (int(hex*2, 16),)*4
    return int(hex[:l//4]*scalar, 16), int(hex[l//4:2*l//4]*scalar, 16), int(hex[2*l//4:3*l//4]*scalar, 16), int(hex[3*l//4:]*scalar, 16)

if __name__ == "__main__":
    print(htrgba('#023f'))
