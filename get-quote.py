import random
def primary():
<<<<<<< HEAD
	print("Keep it logically awesome.")
	f = open("quotes.txt")
	quotes = f.readlines()
	f.close()
	last = len(quotes)-1
	rnd = rand.randint(0,last)
	print(quotes[13])
=======
   print("Keep it logically awesome.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()

  print(quotes[0])
>>>>>>> cdb21920a748655e125160915d60c358670dadd4

if __name__== "__main__":
	primary()
