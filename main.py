import gtk
import sys
#import gtkapi
#import assignment4a as anygui1






#**********************************************************************************
#This is our main function

def Main():
    sampleProgram()
    
    
def sampleProgram():

    print " Enter Your Choice:  "
    print " 1 pyGTk GUI"
    print " 2 wXPYTHON GUI"
    print " 3 pyQt GUI"
    print " 4 tKINTER "
    print " 5 Exit "

    loop = 0
    #ensure whether a valid number is given
    while(loop == 0):           
        
        try:
            x = int(raw_input())
            loop = 1
        except ValueError:
            print 'Enter a valid number please'
            loop = 0
    
    #call PyGTk GUI output
    if x == 1:
        import pygtk as anygui
        

    #call FLTK GUI output
    elif x == 2:
        #pyFLTK_P2009CS1011.pyFLTK()
        import wxpython as anygui
        
    #call pyQT GUI output
    elif x == 3:
        #pyQT_P2009CS1027.PyQt()
        import pyqt as anygui
        
    #call tkinter GUI output
    elif x == 4:
       # tkinter_P2009CS1001.tkinter()
       import tkinter as anygui
       
    elif x == 5:
        print "bye"
        
    #exit
    else:
        print "Not a desired Number"

    #print "Exiting...."

    if x!=1 and x!=2 and x!=3 and x!=4:

        sys.exit(0)   

    #Functions bind to button events
  
    def SubmitButtonClick(event=None):
	
        report = " You are giving your review of the following dishes of "+ relist.getValue() +' in ' +valuelist.getValue()+".\n"
	
        if(checkbox1.getValue()):
	
            report = report + " Pizza\n"
	

    
	
        if(checkbox2.getValue()):
	
            report = report + " Cheese tomato\n"

        if(checkbox3.getValue()):
	
            report = report + " Chicken Tikka Butter Masala\n"
		
        if(checkbox4.getValue()):
	
            report = report + " Chana Masala\n"
	    
	
        report = report + " You felt food was---> "+rb1.getValue()+".\n"
        
        if(rb2.getValue()=='Not for me!'):
            report =report + "You would not revisit the Restaurant. \n"
        else:
            report =report + "You would love to have a visit again. \n"
	
    
	textarea.appendText(report+"\n" + " Slider value " + str(sli.getValue())+" SpinBox value  " + str(spin.getValue())+" \n")
        #textarea.appendText("_______________________\n"+report+"\n\n")
	
        return True 
	
    
	
    def AboutButtonClick(event=None):
	
        textarea.setText("Created by qtGUI Author :\n")
	
        return True
	
    Frame = anygui.Canvas(1, 'Quiz Application ' ,810,800)	
    global i,j		
    #Functions bind to button events
	
    def SubmitButtonClick(event=None):
	
        if(valuelist.getValue()=='Maths'):
		#print "hi"
		#label2=Label('Hindi',60,400,150,30)	    
    		textarea.setText('')
		global i 
		i = 1
		global j 
		j = 0
        

		textarea.setText(" You are taking a Maths test")
	

        if(valuelist.getValue()=='General Knowledge'):
		#print "hi"
		#label2=Label('Hindi',60,400,150,30)	    
    		textarea.setText('')
		global i 
		i = 2
		global j
		j = 0
        

		textarea.setText(" You are taking a General Knowledge test") 
		    
		


        return True 
	
    def nextbuttonclick(event = None):
        global i
	global j
	if i == 1:
		if j == 0:
	
			textarea.setText("QUESTION 1 : \n101 is a prime number ?")
			j = j+1
			
		elif j== 1:
			textarea.setText("QUESTION 2 : \n729 is divisible by 9 ?")
			j = j + 1	
			
		elif j == 2:
			textarea.setText("YOUR ANSWERS HAVE BEEN SUBMITTED\n\n PLEASE FILL THE FEEDBACK BELOW")
			

	if i == 2:
		if j == 0:	
			textarea.setText("QUESTION 1 : \nDolphins sleep with one eye open ?")
			j = j+1
		elif j== 1:
			textarea.setText("QUESTION 2 : \nSun is the largest star ?")
			j = j + 1	
		elif j == 2:
			textarea.setText("YOUR ANSWERS HAVE BEEN SUBMITTED\n\n PLEASE FILL THE FEEDBACK BELOW")
	
	
    def AboutButtonClick(event=None):
	
        textarea.setText("Created by  Author\n")
	
        return True

    def review(event = None):
	report = "\n\n"+text.getText() + ",\n you selected " + rb2.getValue() + " as the difficulty level \n\n You would like to add "
        
        if(checkbox1.getValue()):
	
            report = report + " History "
	
      
    
	
        if(checkbox2.getValue()):
	
            report = report + " Philosophy "

	
        if(checkbox3.getValue()):
	
            report = report + " Geography "

        

	
    
	report = report + " subjects in the future\n\n"
        r = str(spin.getValue())
 	report = report + "You also selected " + r + " as the number of questions in future quizes\n"

	
    
	
        textarea1.appendText(report)
	
	#textarea.appendText(sli.getValue())

        return True 
	
    
	
    
	
    
	
    
	
    #Constructor Frame
	
    
	
    
	
    
	
    #Dropdown valuelist
	
    cities = ['General Knowledge','Maths','' ]
	
    valuelist = anygui.ValueList(cities,90,30,200,20,"Choose Subject")
    #relist = ValueList(restaurants,140,10,150,20,"<Select restaurant>")
	
    Frame.add(valuelist)

	

	
    
	
    #radioGroup1
	
    rb1 = anygui.RadioGroup(100,50)
	
    rb1.addRadioButton("TRUE",515,210)
	
    rb1.addRadioButton("FALSE",625,210)
	
	
    rb1.setButtonTrue(0)
	
    Frame.add(rb1)
    
    rb2 = anygui.RadioGroup(100,50)
    rb2.addRadioButton("Easy",20,220)
    rb2.addRadioButton("Moderate",30,260)
    rb2.addRadioButton("Difficult",30,300)
    rb2.setButtonTrue(0)
    Frame.add(rb2)
    #TextArea
    textarea = anygui.TextArea("\n Question appears here!!",500,10,300,200)
    Frame.add(textarea)
    textarea1 = anygui.TextArea("\nYour Review!!\n\n",500,450,300,200)
    Frame.add(textarea1)
    #Creating Buttons
    submitBtn = anygui.Button("Start Quiz!",245,180,150,60)
    aboutBtn = anygui.Button("About",260,230,120,30)
    nextbtn = anygui.Button("Next Question",515,280,160,40)
    submit = anygui.Button("Submit Review",515,685,160,40)
    Frame.add(submit)
    submit.clickListener(review)
    nextbtn.clickListener(nextbuttonclick)
    Frame.add(nextbtn)
    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)
    ## password
    label3=anygui.Label(' Difficulty Level',10,75,490,30)
    label4=anygui.Label(' Select the topics you want to add on',10,340,300,30)
    Frame.add(label4)
    checkbox1 = anygui.CheckBox("History",20,375,225,15)
    checkbox2 = anygui.CheckBox("Philosophy",180,375,225,15)
    checkbox3 = anygui.CheckBox("Geography",330,375,225,15)
    Frame.add(checkbox1)
    Frame.add(checkbox2)
    Frame.add(checkbox3)
    Frame.add(label3) 
    label6 = anygui.Label("Please enter username and password",10,450,250,30)
    Frame.add(label6)
    pas=anygui.Password(100,540,150,30)
    Frame.add(pas)
    sli=anygui.Slider(0,25,100,100,150,30) 
    Frame.add(sli)
    spin=anygui.SpinBox(0,10,30,610,150,30) 
    Frame.add(spin)   
    label=anygui.Label('How was the Quiz ?',10,210,150,25)
    Frame.add(label)   
    label1=anygui.Label(' Select the Subject whose Quiz you want to take : ',0,0,490,30)
    Frame.add(label1)
    label9 = anygui.Label('Number of questions you would like to have in next quiz',0,580,500,30)
    Frame.add(label9)
    label7 = anygui.Label('Username',10,490,100,30)
    Frame.add(label7)      
    label8 = anygui.Label('Password',10,540,100,30)
    Frame.add(label8)
    text=anygui.TextLine(100,490,150,30)
    Frame.add(text)
    #Adding buttons to Frame
#    Frame.add(aboutBtn)
    Frame.add(submitBtn)
    Frame.show()

	
    
	
    
	
  
    
        
if __name__ == '__main__':
        Main()        


