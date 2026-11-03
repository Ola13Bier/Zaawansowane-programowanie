# funkcja zwracająca cenę po uwzględnieniu zniżki
def Calculate_discount(price: float, discount: float) -> float:
    if discount > 1 or discount < 0:
        return ValueError.__name__
    else:
        return price - (price * discount)
