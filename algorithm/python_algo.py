def calculate_nbrs_of_periods(frequency:str, everyXfrequency:float) -> float:
    coef_frequency:int = 24
    if (frequency == "hours"):
        coef_frequency = 24
    # elif (frequency == "day"): // a check
    #     coef_frequency = 365
    # elif (frequency == "minutes"): // a check
    #     coef_frequency = 1
    nbrs_of_periods:float = 365 * (coef_frequency / everyXfrequency)
    return (nbrs_of_periods)

def calculate_gross_rewards(nbrs_of_periods:float, gasCost:float, APR:float, initialInvestment:float) -> float:
    # all_gasCost:float = gasCost * nbrs_of_periods
    # APY:float = (1 + ((APR / 100) / nbrs_of_periods)) ** nbrs_of_periods - 1
    # net_rewards:float = APY * initialInvestment
    # gross_rewards = net_rewards - all_gasCost
    # return (gross_rewards)
    return ((((1 + ((APR / 100) / nbrs_of_periods)) ** nbrs_of_periods - 1) * initialInvestment) - (gasCost * nbrs_of_periods)) # ou alors faut voir le calcul de test.js.. idk ptdr

def calculate_optimum_compound_days(frequency:str, gasCost:float, APR:float, initialInvestment:float):
    optimumCompoundDays:float = 0.1
    gross_rewards:float = -99999999
    continueWhile:bool = True
    EveryXfrequency:float = 0

    while (optimumCompoundDays < 10000 and continueWhile):
        nbrs_of_periods:float = calculate_nbrs_of_periods(frequency, optimumCompoundDays)
        EveryXfrequency:float = calculate_gross_rewards(nbrs_of_periods, gasCost, APR, initialInvestment)
        if (EveryXfrequency > 0):
            if (EveryXfrequency > gross_rewards):
                gross_rewards = EveryXfrequency
            else:
                continueWhile = False
        optimumCompoundDays += 0.01
    return (optimumCompoundDays)


frequency:str = "hours"
gasCost:float = 0.1
APR:float = 368
initialInvestment:float = 840
print("frequency:", frequency)
print("gasCost:", gasCost)
print("APR:", APR)
print("initialInvestment:", initialInvestment)
print("\n")

optimumCompoundDays:float = calculate_optimum_compound_days(frequency, gasCost, APR, initialInvestment)
print(round(optimumCompoundDays, 2), frequency)

optimum_nbrs_of_periods:float = calculate_nbrs_of_periods(frequency, optimumCompoundDays)
optimum_grossRewards:float = calculate_gross_rewards(optimum_nbrs_of_periods, gasCost, APR, initialInvestment)
print(round(optimum_grossRewards, 2), "$")
