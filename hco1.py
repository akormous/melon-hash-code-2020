def createCatalog(book_scores,ids):
	catalog = []
	z = len(ids)
	while len(catalog)<z:
		mx = -1
		for i in ids:
			if book_scores[int(i)]>mx:
				mx=book_scores[int(i)]
				mx_id = i
		catalog.append(mx_id)
		ids.remove(mx_id)

	return catalog


def getChoiceFactor(ids,scores,tdays,sdays,max_shipment):
	s = 0
	for i in ids:
		s = s + scores[int(i)]
	avg = s/len(ids)
	q = tdays-int(sdays)-(len(ids)/int(max_shipment))
	return avg+(q*2)




class library():
	def __init__(self,books,su_days,max_books,scores,bl,all_days,count):
		self.lib_id = count
		self.num_books = int(books)
		self.signup_days = int(su_days)
		self.max_shipment = int(max_books)
		self.book_ids = createCatalog(scores,bl)
		#print(self.signup_days,self.max_shipment,all_days)
		self.choice_factor = getChoiceFactor(self.book_ids,scores,all_days,self.signup_days,self.max_shipment)
		#print(self.choice_factor)


def allFlags(flag_books):
	for i in flag_books:
		if i == 0:
			return False
	return True


def main():
	# Reading the file
	fin = open('c_incunabula.txt','r')
	inp = fin.readline()
	inp = inp.rstrip()
	inp = inp.split(' ')

	# Get total number of books, libraries and days
	all_books = int(inp[0])
	all_libraries = int(inp[1])
	all_days = int(inp[2])

	# Get score for each book
	inp = fin.readline()
	inp = inp.rstrip()
	inp = inp.split(' ')
	book_scores = []
	for i in inp:
		book_scores.append(int(i))

	#print(book_scores)



	# Create a flag thing to indicate if a book is scanned or not
	flag_books = []
	for j in range(all_books):
		flag_books.append(0)

	#print(flag_books)

	# Create a list of objects of library class
	libraries = []
	count = 0
	z = all_libraries
	# Read each library data
	while z>0:
		inp = fin.readline()
		inp = inp.split(' ')
		nl = inp[0]
		tl = inp[1]
		mj = inp[2]
		inp = fin.readline()
		inp = inp.rstrip()
		inp = inp.split(' ')
		bl = inp[:]
		libraries.append(library(nl,tl,mj,book_scores,bl,all_days,count))
		z = z-1
		count = count + 1

	libraries.sort(key=lambda x:x.choice_factor)
	selected_libs = []
	selected_books = []
	cur_lib = len(libraries)-1
	lib_count=0
	rem_days = all_days

	while rem_days>0:
		rem_days = rem_days - libraries[cur_lib].signup_days
		q = rem_days
		yp=0
		
		sel_ids = []
		books_selected = 0
		#len(libraries[cur_lib].book_ids)/libraries[cur_lib].max_shipment
		for i in libraries[cur_lib].book_ids:
			if flag_books[int(i)]==0:
				sel_ids.append(i)
				yp=1
				flag_books[int(i)]=1
				books_selected=books_selected+1
		if yp==1:
			lib_count = lib_count+1
			selected_libs.append(libraries[cur_lib].lib_id)
			selected_books.append(sel_ids)
		cur_lib = cur_lib-1

	#print(lib_count)
	#print(selected_books)
	#print(selected_libs)


	fout = open('c_output.txt','w')
	fout.write(str(lib_count))
	
	
	for z in range(len(selected_libs)):
		fout.write('\n')
		str1 = ''
		fout.write(str(selected_libs[z])+' '+str(len(selected_books[z])))
		fout.write('\n')
		for i in selected_books[z]:
			str1 = str1 + str(i) + ' '
		fout.write(str1)
		

	fout.close()
	fin.close()
	
if __name__ == '__main__':
	main()


