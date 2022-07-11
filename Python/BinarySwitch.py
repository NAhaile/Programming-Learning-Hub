#Written  by Natnael Haile

num = int(input("What is your number?"))

'''

I will preface that there is a mathematical way to find Binary representations of
decimal numbers, but for purposes of playing with switch statements, my approach 
conditionally. Here will be a little more brute force.

Starting from the right most bit

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512


'''

def dec_to_num(x):

	x = num

	if x == 0:
		return "0"
	elif x == 1:
		return "1"
	elif x == 2:
		return "10"
	elif x == 3:
		return "11"
	elif x == 4:
		return "100"
	elif x == 5:
		return "101"
	elif x == 6:
		return "110"
	elif x == 7:
		return "111"
	elif x == 8:
		return "1000"
	elif x == 9:
		return "1001"
	elif x == 10:
		return "1010"



print("")
print("your number is ", dec_to_num(num))

