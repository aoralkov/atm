from statistics import stdev

class ATM:
  def __init__(self, qty100=0, qty50=0, qty20=0, qty5=0):
    self.qty100 = qty100
    self.qty50 = qty50
    self.qty20 = qty20
    self.qty5 = qty5

  def get_total_sum(self):
    return (100 * self.qty100 +
      50 * self.qty50 +
      20 * self.qty20 +
      5 * self.qty5)

  def __str__(self):
    return f"""ATM Status:
    100$ - {self.qty100}
    50$ - {self.qty50}
    20$ - {self.qty20}
    5$ - {self.qty5}
Total sum - {self.get_total_sum()}"""

  def money_output(self, req):
    output_options = self.__find_output_options(req)
    print(output_options)
    if len(output_options) == 0:
      # print("Not enough money")
    else:
      best_option = self.__choose_best_option(output_options)
      # print(best_option)
      self.__give_money(best_option)
      print(self)
  
  def __give_money(self, best_option):
    self.qty100 -= best_option[0]
    self.qty50 -= best_option[1]
    self.qty20 -= best_option[2]
    self.qty5 -= best_option[3]

  def __choose_best_option(self, output_options):
    if len(output_options) == 1:
      return output_options[0]
    else:
      curr_avg = self.get_total_sum() / 4
      tmp = []
      for option in output_options:
        tmp.append( stdev([self.qty100 - option[0], self.qty50 - option[1],self.qty20 - option[2], self.qty5 - option[3]]) )
      return output_options[tmp.index(min(tmp))]

  def __find_output_options(self, req):
    res = []
    tmp_100 = int(req / 100)
    tmp_100 = self.qty100 if tmp_100 > self.qty100 else tmp_100
    while tmp_100 >= 0:
      tmp_50 = int( (req - 100 * tmp_100) / 50 )
      tmp_50 = self.qty50 if tmp_50 > self.qty50 else tmp_50
      while tmp_50 >= 0:
        tmp_20 = int( (req - 100 * tmp_100 - 50 * tmp_50) / 20)
        tmp_20 = self.qty20 if tmp_20 > self.qty20 else tmp_20
        while tmp_20 >= 0:
          tmp_5 = int( (req - 100 * tmp_100 - 50 * tmp_50 - 20 * tmp_20) / 5)
          if tmp_5 <= self.qty5:
            res.append([tmp_100, tmp_50, tmp_20, tmp_5])
          tmp_20 -= 1
        tmp_50 -= 1
      tmp_100 -= 1
    return res



  