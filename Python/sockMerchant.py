def sockMerchant(n, ar):
    numpairs = 0
    counted =[]
    for sock in ar:
        if sock not in counted:
            qty = ar.count(sock)
            counted.append(sock)
            numpairs += qty // 2
    return numpairs