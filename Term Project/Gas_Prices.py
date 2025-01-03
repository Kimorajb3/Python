from datetime import datetime


fn = 'GasPrices.txt'


def average(GPdictionary):
    yearAverage={}

    for date in GPdictionary:
        if date.year in yearAverage:
            yearAverage[date.year].append(float(GPdictionary[date]))
        else:
            yearAverage[date.year] =[float(GPdictionary[date])]

    for yr in yearAverage:
        rates=yearAverage[yr]
        print("{}, yearly average was ${:.3f} per gallon".format(yr, sum(rates)/len(rates)))


def monthAverage(GPdictionary):
    monAverage={}
    for date in GPdictionary:
        mo_yr = date.strftime('%m-%Y')
        print(mo_yr)
        if mo_yr in monAverage:
            monAverage[mo_yr].append(float(GPdictionary[date]))
        else:
            monAverage[mo_yr]=[float(GPdictionary[date])]
    for mo in monAverage:
        rates=monAverage[mo]
        print("{}: monthly average was ${:.3f} per gallon".format(mo, sum(rates)/len(rates)))


def read(fn):
    Pdictionary = {}
    with open(fn, 'r') as f:
        details = f.readlines()
        for line in details:
            time, total = line.strip('\n').split(":")
            Pdictionary[datetime.strptime(time, '%m-%d-%Y')] = total
    return Pdictionary


def high_to_low(GPdictionary):
    yrCharge={}
    for date in GPdictionary:
        if date.year in yrCharge:
            yrCharge[date.year].append(float(GPdictionary[date]))
        else:
            yrCharge[date.year] =[float(GPdictionary[date])]
    for yr in yrCharge:
        rates=yrCharge[yr]
        print("{}, highest price: {} and lowest: {}".format(yr, max(yrCharge[yr]),min(yrCharge[yr])))


def get_rate(y):
    return y[1]


def sortedRate(GPdictionary,down,fn):

    sortedRates=sorted(GPdictionary.items(), key=get_rate, reverse=down)
    with open(fn,'w') as f:
        f.write("Date\t\tPrice\n")
        for date, rate in sortedRates:
            f.write("{}\t{}\n".format(date.strftime('%d-%m-%Y'),rate))
if __name__ == '__main__':
    gasFee = read(fn)
    average(gasFee)
    monthAverage(gasFee)
    high_to_low(gasFee)
    sortedRate(gasFee, down=False, fn='low_to_high.txt')
    sortedRate(gasFee, down=True,fn='high_to_low.txt')
