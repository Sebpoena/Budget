class Day:
	def __init__(self, name):
		self.name = name
		
	
	def setNeighbours(self, prev, next):
		self.prev = prev
		self.next = next
	
	
	def __repr__(self):
		return self.name
		
		
class Month:
	def __init__(self, name, length, num):
		self.name = name
		self.length = length 
		self.num = num
		
		
	def setDates(self, startDay):
		currentDay = startDay
		result = []
		for i in range(self.length):
			result.append((currentDay, i + 1))
			currentDay = currentDay.next
		return result
		
		
	def __repr__(self):
	 return self.name
	 
	 
class Year:
	def __init__(self, startDay):
		self.months = (January, February, March, April, May, June, July, August, September, October, November, December)
		self.startDay = startDay
		self.calendar = self.setCalendar()
		self.moneyCalendar = self.resetMoneyCalendar()
		
		
	def setCalendar(self):
		result = []
		result.append(January.setDates(self.startDay))
		for i in self.months[1::]:
			result.append(i.setDates(result[-1][-1][0].next))
		return result
		
		
	def resetMoneyCalendar(self):
		result = []
		for i in self.calendar:
			result.append([0 for x in i])
		return result
		
		
	def date(self, day, month):
		return (self.calendar[month-1][day-1][0], self.calendar[month-1][day-1][1], self.months[month-1])
		
		
	def dateSpan(self, date1, date2, month):
		result = []
		for i in self.calendar[month][date1-1:date2:]:
			result.append(self.date(i[1], month))
		return result
		
		
	def spent(self, amount, day, month):
		self.moneyCalendar[month-1][day-1] += amount
		return (self.date(day, month), self.moneyCalendar[month-1][day-1])
		
		
class Product:
	def __init__(self, purchased, price, year):
		#purchased is a date, formated: date, month
		self.purchased = purchased
		self.price = price
		self.year = year
		
		
	def used(self, date):
		#date is formatted in the same way as purchsed
		spread = self.year.dateSpan(self.purchased[0], date[0], date[1])
		spending = round(self.price/len(spread), 2)
		for i in spread:
			self.year.spent(spending, i[1], i[2].num)
		result = self.year.moneyCalendar[date[1]-1]
		return result
		
	
Monday = Day("Mon")
Tuesday = Day("Tue")
Wednesday = Day("Wed")
Thursday = Day("Thu")
Friday = Day("Fri")
Saturday = Day("Sat")
Sunday = Day("Sun")

Monday.setNeighbours(Sunday, Tuesday)
Tuesday.setNeighbours(Monday, Wednesday)
Wednesday.setNeighbours(Tuesday, Thursday)
Thursday.setNeighbours(Wednesday, Friday)
Friday.setNeighbours(Thursday, Saturday)
Saturday.setNeighbours(Friday, Sunday)
Sunday.setNeighbours(Saturday, Monday)

January = Month("Jan", 31, 1)
February = Month("Feb", 29, 2)
March = Month("Mar", 31, 3)
April = Month("Apr", 30, 4)
May = Month("May", 31, 5)
June = Month("Jun", 30, 6)
July = Month("Jul", 31, 7)
August = Month("Aug", 31, 8)
September = Month("Sep", 30, 9)
October = Month("Oct", 31, 10)
November = Month("Nov", 30, 11)
December = Month("Dec", 31, 12)

a = Year(Monday)	
	
print(a.date(14, 5))
print(a.dateSpan(14, 20, 5))

Spaghetti = Product((14, 4), 1.99, a)
Pesto = Product((14, 4), 1.79, a)
Cheese = Product((10, 4), 2.69, a)
Tomato = Product((16, 4), 1.59, a)
Aubergine = Product((8, 4), 1.98, a)

Spaghetti.used((18, 4))
Pesto.used((18, 4))
Cheese.used((21, 4))
Tomato.used((18, 4))
Aubergine.used((18, 4))

print(a.moneyCalendar[3])
