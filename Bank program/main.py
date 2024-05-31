# Python Banking Program

def show_balance():
  print("*********************")
  print(f"Your balance is Ksh{balance}")
  print("*********************")

def deposit():
  print("*********************")
  amount = float(input("Enter an amount to be deposited: "))
  print("*********************")


  if amount < 0:
    print("*********************")
    print("That is not a valid amount")
    print("*********************")
    return 0

  else:
    return amount  

def withdraw():
  print("*********************")
  amount = float(input("Enter amount to be Withdraw:"))
  print("*********************")

  if amount > balance:
    print("*********************")
    print("You have insufficient funds")
    print("*********************")

  elif amount < 0:
    print("*********************")
    print("Amount must be greater than 0")
    print("*********************")
    return 0

  else:
    return amount
  
def main():  
    balance = 0
    is_running = True

    while is_running:
      print("*********************")
      print("Banking Program")
      print("*********************")
      print("1.Show balance")
      print("2.Deposit")
      print("3.Withdraw")
      print("4.Exit")
      print("*********************")

      choice = input("Enter your option (1-4)")

      if choice == '1':
        show_balance()
      elif choice == '2':
        balance += deposit()
      elif choice == '3':
        balance -= withdraw()
      elif choice == '4':
        is_running = False
      else:
        print("*********************")
        print("The choice is not a valid one")  
        print("*********************")  
print("*********************")
print("Thank you for Banking with us")
print("*********************")

  
if __name__== '__main__':
  main()