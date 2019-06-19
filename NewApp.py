Ferry_fare = 11
FFD_fare = 5.75
Vallejo_fare = 5
ECDN_BART = 4.55
Conc_BART = 5.95
PH_BART = 5.55
WO = 3.25


print("Welcome to the commute cost calculator")

# the following sets the method of transport and the number of days. Will change the first question later
# it is supposed to gather if going today but need boolean lessons

ferry_info = float(input("Times taking the ferry: "))
ferry_days = float(input("How many days: "))

fairfield_info = float(input("Times taking the bus from Fairfield: "))
fairfield_days = float(input("How many days: "))

vallejo_info = float(input("Times taking Vallejo bus: "))
vallejo_days = float(input("How many days: "))

ECDN_info = float(input("Times taking El Cerrito Del Norte BART"))
ECDN_days = float(input("How many days: "))

conc_info = float(input("Times taking Concord BART"))
conc_days = float(input("How many days: "))

PH_info = float(input("Pleasant Hill BART: "))
PH_days = float(input("How many days: "))

WO_info = float(input("Taken West Oakland"))
WO_days = float(input("How many days: "))

# now I will define the calculations for each set of transportation into a total to be
# used later in the final calculation


ferry_total = (ferry_info + ferry_days)
fairfield_total = (fairfield_info + fairfield_days)
vallejo_total = vallejo_info + vallejo_days
ECDN_total = ECDN_info + ECDN_days
conc_total = conc_info + conc_days
PH_total = PH_info + PH_days
WO_total = WO_info + WO_days


# this is just here for now until I can use it later maybe

numDays = int(input("Please enter the number of days you commuted: "))


cost = (((distance * numDays) / (mileage*0.4251)) * gasPrice)


