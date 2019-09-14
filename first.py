#!/usr/bin/env python3

class Elem:
	def __init__(self,val=None,link=None):
		self.value=val
		self.next=link
		
class NumList:
	def __init__(self,first=None,count=0):
		self.first=first
		self.count=count
		
	def elem_info(self,k):
		if (k<self.count):
			search=self.first
			if (k>0):
				for i in range(0,k):
					search=search.next
			print("Value: ")
			return search.value
		else:
			print("Error: no element on this position")
		return '-'
			
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
			
		
	def elem_delete(self,k):
		if (k==0) and (self.count>1):
			self.first=self.first.next
			self.count-=1
		elif (k==0) and (self.count==1):
			self.firs=None
			self.count-=1
		elif (k>0) and (k<self.count):
			behind=self.first
			after=self.first
			for i in range(1,k):
				behind=behind.next
			after=behind.next.next
			behind.next=after
			self.count-=1	
		elif (k==self.count):
			search=self.first
			for i in range(2,self.count):
				search=search.next 
			search.next=None
			self.count-=1	
		else:
			print("Error: no element on this position")

	def list_print(self):
		print("")
		search=self.first
		print("There are {} numerals:".format(self.count))
		for i in range(0,self.count):
			print("{}".format(search.value))
			search=search.next
		
def fun(a):
	List=NumList()
	while a!=0:
		m=a%10
		List.elem_putpos(m,0)
		a=a//10
	return List
	
newlist=fun(int(input("Insert the number: ")))
newlist.list_print()
i=0
while i==0:
	print("")
	print('Choose something: "q" - to quit; "d" to delete an element; "p" to put an element; "f" to find an element; "i" to see the list:')
	c=input(">>")
	if c=='d':
		k=int(input("Choose the position: "))
		newlist.elem_delete(k)
	elif c=='p':
		k=int(input("Choose the position: "))
		a=int(input("Insert the value: "))
		newlist.elem_putpos(a,k)
	elif c=='f':
		k=int(input("Choose the position: "))
		print(newlist.elem_info(k))
	elif c=='i':
		newlist.list_print()
	else:
		break
		

		
		
				
	
			
