print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')
print("Welcome To The Tip Calculator😊!")
a=float(input("What Was The Total Bill💵? $") )
b=float(input("What Percentage Tip Would You Like To Give💰? (10, 12, 15)?  "))
c=int(input("How Many People To Split The Bill👥? "))
total_tip=a+(a*(b/100))
total_bill=round(total_tip/c,2)
print(f"Each Person Should Pay: ${total_bill}❤️")
