#!/usr/bin/env python3

class Elem:
	def __init__(self,val=None,link=None):
		self.value=val
		self.next=link
		
class NumList:
	def __init__(self,first=None,count=0):
		self.first=first
		self.count=count
		
	def elem_putpos(self, val=0, k=0):
		if k<=self.count:
			if self.count > 0:
				if k==0:
					newelem=self.first
					self.first=Elem(val)
					self.first.next=newelem
				elif k==self.count:
					search=self.first
					for i in range(1,k):
						search=search.next
					search.next=Elem(val)
				else:
					search=self.first
					for i in range(1,k):
						search=search.next
					newelem=search.next
					search.next=Elem(val)
					search=search.next
					search.next=newelem		
			else:
				self.first=Elem(val)	
			self.count+=1
		else:
			print("Error! Change the position")
			
	def list_print(self):
		print("")
		search=self.first
		print("There are {} numerals:".format(self.count))
		for i in range(0,self.count):
			print("{}".format(search.value))
			search=search.next
			
def fun(a):
	List=NumList()
	k=0
	while a!=0:
		m=a%10
		List.elem_putpos(m,k)
		a=a//10
		k+=1
	return List
	
def summ(a,b):
	num=0
	if a.count==b.count:
		length=a.count
	else:
		if a.count<b.count:
			length=a.count
			search=b.first
			maxl=b.count
		else:
			length=b.count
			search=a.first
			maxl=a.count
		for i in range(0,length):
			search=search.next
		for i in range(length,maxl):
			num+=search.value*(10**i)
			if i!=maxl-1:
				search=search.next	
			
	e1=a.first
	e2=b.first
	i=0
	for	i in range(0,length):	
		num+=(10**i)*(e1.value+e2.value)
		e1=e1.next
		e2=e2.next
	return fun(num)
	
newlist1=fun(int(input("Insert the first number: ")))
newlist1.list_print()

newlist2=fun(int(input("Insert the second number: ")))
newlist2.list_print()

print("")
summ(newlist1,newlist2).list_print()



