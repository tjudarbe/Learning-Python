str = 'X-DSPAM-Confidence:0.8475 '
index = str.find(':') #18
print(index)
end = str.find(' ', index)#25
print(end)
number = str[index+1 : end]
final = float(number)
print(final)
