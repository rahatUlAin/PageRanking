
import urllib.request
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from pymsgbox import *



while True:

	connection_successful = True
	wordData = {}
	userList=[]
	order=[]
	count=0
	choice=""
	dataUrls = [
	        'http://www.dawn.com/news/1308190/panamagate-hearing-disqualification-of-pm'
	        '-under-articles-62-and-63-not-possible-counsel-argues',
	        'http://www.dawn.com/news/1308162/pm-may-have-omitted-details-from-na-speech',
	        'http://www.dawn.com/news/1298572/pml-n-papers-purchase-of-london-flats-and-the-al-thani-connection',
	        'http://www.dawn.com/news/1308186/australia-beat-pakistan-by-92-runs-in-first-odi-at-brisbane',
	        'http://www.dawn.com/news/1308035/individual-performance-wont-help-pakistan-in-australia-odis',
	    ]
	keyWords = [
			"nawaz","nawaz sharif","pm","makhdoom ali khan","makhdoom khan","pakistan","na",
			"tehreek-i-insaf","panama paper","prime minister","islamabad","supreme court",
			"yousaf raza gillani","justice azmat saeed","justice","steel mills",
			"qatari letter","al-thani","london flats","pmln","panamagate","hussain nawaz","maryam nawaz",
			"mian muhanmmad sharief","odi","australia","maxwell","wade","sarfaraz","steve smith",
			"umar akmal","javed miandad","pcb","zaheer","misbah","cricket","australia",
			"asia","test series","world cup","captain","bangladesh","azhar ali"
		]
	def crawl(url):
		global choice
		try:
			html = urllib.request.urlopen(url).read()
			
			
		except Exception as e:
			global connection_successful
			connection_successful=False
			print('connection failed')
			choice=error()
			if choice=="Retry":
				return
			elif choice=="Cancel":
				quit()
		else:
			return html

			
			

		

	def prepareData(dataUrls):
		
		for url in dataUrls:
			#Get words from html

			print('Collecting data from:\n {0}\n'.format(url))
			html = crawl(url)
			if not (connection_successful):
				return
			try:
				soup = BeautifulSoup(html,"html.parser")
				# kill all script and style elements
				for useless_content in soup(['script', 'style']):
					# rip it out
					useless_content.extract() 

				# get text
				text = soup.get_text()
			except Exception as e:
				print(e)
				choice=error()
				textbox.delete(0.0,END)
				textbox.insert(0.0,e)
				if choice=="Retry":
					print("trying to connect to internet")
					prepareData()
				elif choice=="Cancel":
					exit()

				


			# break into lines and remove leading and trailing space on each
			lines = (line.strip() for line in text.splitlines())

			# break multi-headlines into a line each
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
			# drop blank lines
			text = '\n'.join(chunk for chunk in chunks if chunk)
			text=text.lower()
			print(text)
			'''
				making dataBase
			'''
			global wordData
			for word in keyWords:
				if not(word in  wordData):
					wordData[word]=[]
				print(word)
				wordData[word].append((url,(text.count(word))))



					
	def userInput():
		if (entry.get()!="") :
			query=(entry.get()).strip()
			query.lower()

		elif (box.get()!=""):
			query=box.get()
			
		else:
			return "NO Result Found"
		print("searching for ",query)

		userList = []
		count    = 0
		order    = []
		if "+" in query:
			try:
				while ("+" in query):

					index = (query.index("+")).lower()
					userList.append(wordData[(query[0:index].strip())])
					query = query[index+1:].strip()

			except:
				return('No result found')
			for j in range(len(userList[0])):
				count = 0
				for i in range(len(userList)):
					url01 = userList[i][j][0]
					count+= userList[i][j][1]
				order.append((url01,count))
			try:
				sorted(order,key=lambda x:x[1],reverse=True)
			except:
				return('No result found')




		elif query in keyWords:
			try:
				order = sorted(wordData[query],key=lambda x:x[1],reverse=True)
			except:
				choice=error()
				if choice=="Cancel":
					exit()
				return('Sorry there is no data for "{0}"'.format(query))

		for x in order:
			print(x[0],end="\n\n")
		box.set("")
		return order

	def quit():
		exit()
	def error():
		ans=confirm(text='Connection Error Appeared', title='', buttons=['Retry', 'Cancel'])


			
	def mainFuction():

		
		if not(connection_successful):
			print("Check connection and Try Again!(Y/N)")
			choice=error()
			
			textbox.delete(0.0,END)
			textbox.insert(0.0,e)
			if choice=="Retry":
				return
			elif choice=="Cancel":
				exit()
			
		

		
		result=userInput()
		for i in result:
			print(i,end="\n\n")
		userList=""
		try:
			for i in result:
				
				i=i[0]+"\t"+str(i[1])+"\n"
				userList+=i
		except:
			userList=result

		textbox.delete(0.0, END)
		textbox.insert(0.0, userList )
		
		
	prepareData(dataUrls)
	window=Tk()
	# View

		
	window.title("Dawn Search")
	window.configure(bg="#F5EEF8")
	
	window.attributes("-fullscreen", True)





			
			
	# ComboBox Ones
	box = ttk.Combobox(window, font=("Calibri",12), height="15",state="readonly", values=keyWords)
	box.grid(row=1, column=1, padx= 5, pady=7, sticky=E)

	frame1=Frame(window,bg="light grey")
	frame1.grid()
	label1=Label(frame1,text="D",font=("Helvetica", 32),bg="light grey",fg="blue")

	label2=Label(frame1,text="A",font=("Helvetica", 32),bg="light grey",fg="red")
			
	label3=Label(frame1,text="W",font=("Helvetica", 32),bg="light grey",fg="green")
			
	label4=Label(frame1,text="N",font=("Helvetica", 32),bg="light grey",fg="blue")
				
	label5=Label(frame1,text="E",font=("Helvetica", 32),bg="light grey",fg="green")
			
	label6=Label(frame1,text="W",font=("Helvetica", 32),bg="light grey",fg="red")
			
	label7=Label(frame1,text="S",font=("Helvetica", 32),bg="light grey",fg="blue")

	label8=Label(frame1,text="N",font=("Helvetica", 32),bg="light grey",fg="yellow")

	label1.pack(padx=5,pady=5,side="left")
	label2.pack(side="left")
	label3.pack(side="left")
	label4.pack(side="left")
	label8.pack(side="left")
	label5.pack(side="left")
	label6.pack(side="left")
	label7.pack(side="left")
	#controll

	entry=ttk.Entry(frame1,font=("Calibri",12),width=100)
	entry.pack(padx=5,pady=10,side="left")

	# Button that calls output function and gets result from it
	#controller
	findResult = ttk.Button(frame1, text="Search", command=mainFuction)
	findResult.pack(side=RIGHT, padx=5, pady=3)
	#OUTPUT
	textbox = Text(window,font=("Calibri",12), width=100, height=30, wrap=WORD)
	textbox.grid(row=3, columnspan=2,padx=4, pady=7)
		
	exitButton = Button(window, text = "Exit", bg = "#008080", fg = "blue",  font=("Helvetica", 32), command = quit)
	exitButton.grid(row=4,column=9,columnspan=1,)
		

	window.mainloop()
	




		