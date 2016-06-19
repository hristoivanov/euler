import time
start=time.time()


def get_aux(num, aux, nom, den):
    """
    sqrt(23) = 
    4 + sqrt(23) - 4 =                  A0 = 4, nom = 1, den = -4
    4 + 1 /                             
          1 /
            sqrt)23) - 4 = 
    4 + 1 /
          1 /
            1 + ((sqrt(23) - 3) / 7))     A1 = 1, nom = 7, den = -3
    Returns the next element of the infinite continued fraction of sqrt(num).
    Parameters:
        num - The number whose square root we are calculating.
        aux - The first element of this continued fraction
                (The whole number od the square root).
        nom - The nominator left from the previos element.
        den - The denominator left from the previos element.
    Returns:
        nom - The nominator left.
        den - The denominator left.
        the_num - The element of the infinite continued fraction.
    """
    nomm=nom
    denn=den
    den=(num-(denn)**2)/nomm
    nom=(-aux+(aux-denn)%den)
    the_num=((aux-denn)/den)
    return nom, den, the_num

def getContinuedFractionValue(elementsList):
    """
    Symplifies a continued Frtaction: A0 + (1/A1 + (1/A2 + (1/A3 + ...)))
    Parameters:
        elementsList - [An, ...., A2, A1, A0]
    """
    nom = 1
    den = elementsList[0]
    for num in elementsList[1:-1]:
        aux_hold = den
        den = (den * num) + nom
        nom = aux_hold
    return elementsList[-1] * den + nom, den

def aux(D):
    """
    Returns the minimal solution in x for x^2 - D*y^2 = 1
    x^2 - D*y^2 = 1
        x = sqrt(1 + D * y^2)
        x ~= sqrt(D) * sqr(y^2)
        x ~= sqrt(D) * y
        sqrt(D) ~= x/y;
    """
    curr=0
    while True:
        if (curr+1)**2 > D:
            break
        curr+=1

    toople = (1, -curr)
    continuedFractionElements=[curr]
    while True:
        nom, den, the_num = get_aux(D, curr, toople[0], toople[1]);
        toople = (den, nom) 
        continuedFractionElements = [the_num] + continuedFractionElements

        d_nom, d_den = getContinuedFractionValue(continuedFractionElements)

        if d_nom**2 - D*d_den**2 == 1:
            return d_nom

dList = []
for D in range(2,1001):
    if (D**.5).is_integer():
        continue
    dList += [(D,aux(D))]

the_ans= sorted(dList, key=lambda tup: tup[1])[-1][0]
print 'Answer: '+`the_ans`+' Time: '+`time.time()-start`
