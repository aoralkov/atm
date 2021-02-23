from atm import ATM

def main():
  myATM = ATM(qty100=20, qty50=20, qty20=20, qty5=20)
  print(myATM)
  while True:
    try:
      req = int(input("Enter requested amount of money: "))
    except (EOFError, KeyboardInterrupt):
      print("Exit")
      break
    except ValueError:
      print("Error. Enter number.")
      continue
    if req > myATM.get_total_sum():
      print("Not enough money")
      continue
    if (req % 5) != 0:
      print("Requested amount of money must be divisable by 5")
      continue
    myATM.money_output(req)
    if myATM.get_total_sum() == 0:
      print("ATM is empty")
      break
  

if __name__ == "__main__":
  main()