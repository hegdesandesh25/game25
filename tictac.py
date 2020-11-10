print("\nChoose any numbers from keyboard and it will get inserted \n")
#print("1 \t 2 \t 3 \n4 \t 5 \t 6 \n7 \t 8 \t 9\n\n")
dict={"1": '',"2": '',"3":'',
	  "4":'',"5":'',"6":'',
	  "7":'',"8":'',"9":''}
flag=0
#print("This is how the board looks like now")
def printdict(dict):
	#print(dict)
	j=0
	for i in dict.values():
		print("\t"+i +"\t"+ "|"+"\t", end="")
		j=j+1
		if(j%3==0):
			print("\n")
			print("--------------------------------------------------------")

def detuser(value):
	if(value == "X"):
		print("User1 has won \n")
	else:
		print("User2 has won \n")
		

def verifyTicTac(dict):
	det=1
	print("det:",det)
	if((dict["2"]==dict["1"]==dict["3"]=="X") | (dict["2"]==dict["1"]==dict["3"]=="0")):
		detuser(dict["1"])
		det=0
	elif((dict["1"]==dict["5"]==dict["9"] =="X")| (dict["1"]==dict["5"]==dict["9"]=="0")):
		detuser(dict["1"])
		det=0
	elif((dict["1"]==dict["4"]==dict["7"]=="X")| (dict["1"]==dict["4"]==dict["7"]=="0")):
		detuser(dict["1"])
		det=0
	elif((dict["4"]==dict["5"]==dict["6"]=="X")| (dict["4"]==dict["5"]==dict["6"]=="0")):
		detuser(dict["4"])
		det=0
	elif((dict["7"]==dict["8"]==dict["9"]=="X")| (dict["7"]==dict["8"]==dict["9"]=="0")):
		detuser(dict["7"])
		det=0
	elif((dict["7"]==dict["5"]==dict["3"]=="X")| (dict["7"]==dict["5"]==dict["3"]=="0")):
		detuser(dict["7"])
		det=0
	elif((dict["3"]==dict["6"]==dict["9"]=="X")| (dict["3"]==dict["6"]==dict["9"]=="0")):
		detuser(dict["7"])
		det=0
	elif((dict["2"]==dict["5"]==dict["8"]=="X")| (dict["2"]==dict["5"]==dict["8"]=="0")):
		detuser(dict["2"])
		det=0
	return det


entered=[]
for i in range(1,10):

	if(flag==0):
		print("User 1 - please enter position:")
		x=input()
		dict[x]="X"
	if(flag == 1):
		print("User 2 - please enter position:")
		x=input()
		dict[x]="0"
	
	value=verifyTicTac(dict)
	printdict(dict)
	if(value==0):
		break
	if(flag==0):
		flag=1
		continue
	if(flag==1):
		flag=0
		continue
	
	

#print(test)