#Tip Calculator
print('welcome to the tip calculator!')
print()

#Asking for the total bill
total = float(input('What is the total bill? $'))

#percentage tip to give
tip = int(input('What % do you want to tip? 10,12 or 15?'))

#Number of people to split the bill
peeps = int(input('How many people are splitting the bill? '))

#Simple tip calculation
calc_tip = (100+tip)/100

#Calculating the total amount together with the tip
total_amount = total * calc_tip

#Dividing the amount between the number of people
each_user = total_amount/peeps

#Rounding off to two decimal places
result = round(each_user,2)

#Similar method
result = "{:.2f}".format(each_user)

#Displaying the amount each person is going to pay
print(f'Each person is to pay ${result}')

#For more advance code, you can incorporate control flow to ensure the user is inputing the correct data.
