def computepay(hours, rate):
    print("In compute pay", hours, rate)

#Ask for user input
sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
#covert into flaots
hoursf = float(sh)
ratef = float(sr)

computepay(sh,sr)
if hoursf <=40:
    pay = hoursf * ratef
    print('Total Pay:', pay)
if hoursf > 40:
    pay = ratef * 40 + ratef * 1.5 * (hoursf - 40)
    print('Total Pay:', pay)













#rint("Pay:", pay)
