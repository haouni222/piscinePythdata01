def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    """ catch diff de len des lists + si taille = 0 pour
    eviter la division par 0 puis applique formule du bmi"""
    if len(height) != len(weight):
        print("The length of height and weight must be the same !")
        exit(1)
    bmi = []
    i = 0
    one = isinstance(height, list)
    two = isinstance(weight, list)
    if one is False or two is False:
        print("Height and weight must be lists !")
        exit(1)
    while i < len(height):
        if height[i] == 0:
            print("Height cannot be 0 !")
            exit(1)
        one = isinstance(height[i], int)
        two = isinstance(height[i], float)
        tree = isinstance(weight[i], int)
        four = isinstance(weight[i], float)
        if one is False and two is False or tree is False and four is False:
            print("Height and weight must be integers or floats !")
            exit(1)
        bmi.append(weight[i] / (height[i] ** 2))
        i += 1
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Compare chaque bmi avec la limite
    et retourne une liste de booleens"""
    i = 0
    ret = []
    one = isinstance(bmi, list)
    two = isinstance(limit, int)
    if one is False or two is False:
        print("BMI must be a list and limit an integer !")
        exit(1)
    while i < len(bmi):
        if bmi[i] > limit:
            ret.append(True)
        else:
            ret.append(False)
        i += 1
    return ret
