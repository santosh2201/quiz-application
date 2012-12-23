import os
import sys  
from PyQt4 import QtGui, QtCore	
from functools import partial

class SurveyWindow(QtGui.QWidget):	
    parent = None	
    def __init__(self, id, title,width,height):
        self.app = QtGui.QApplication(sys.argv)
        super(SurveyWindow, self).__init__() 
        self.id = id
        self.text = title
        self.width = width
        self.height = height
    def center(self):
        qr = self.frameGeometry()                                   # Getting current window frame of my desktop
        cp = QtGui.QDesktopWidget().availableGeometry().center()    # Getting center point of my Desktop wiondow
        qr.moveCenter(cp)                                           # moving the center of the window to the cp
        self.move(qr.topLeft())
	
class Canvas(object):	
    window = None	
    def __init__(self, id, title,width,height):
        self.window = SurveyWindow(id, title,width,height)
    def show(self):                                      # Finalizing the Grid for Display
	######   setting the geometry for the window
	self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)
        self.window.center()                                               # Aligning to the center
        self.window.setWindowTitle(self.window.text)
        self.window.show()
        sys.exit(self.window.app.exec_())
    def add(self,widget):
        widgetName = type(widget)
        
	if(widgetName==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = QtGui.QCheckBox(widget.title, self.window)
            widget.controller.setChecked(widget.value)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
        elif(widgetName==Button or isinstance(widget,Button)):
            widget.controller = QtGui.QPushButton(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
            if(widget.callbackMethod is not None):
                widget.controller.clicked.connect(widget.callbackMethod)
	###
	elif(widgetName==Password or isinstance(widget,Password)):
	    widget.controller = QtGui.QLineEdit(self.window)
	    widget.controller.setEchoMode(2)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)

	elif(widgetName==Slider or isinstance(widget,Slider)):
	    widget.controller = QtGui.QSlider(QtCore.Qt.Horizontal,self.window)
	    widget.controller.setFocusPolicy(QtCore.Qt.NoFocus)
	    widget.controller.setMinimum(widget.start)
	    widget.controller.setMaximum(widget.end)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(widgetName==SpinBox or isinstance(widget,SpinBox)):
	    widget.controller = QtGui.QSpinBox(self.window)
	    widget.controller.setMinimum(widget.start)
	    widget.controller.setMaximum(widget.end)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(widgetName==Label or isinstance(widget,Label)):
	    widget.controller = QtGui.QLabel(widget.text,self.window)
	    widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	
	elif(widgetName==TextLine or isinstance(widget,TextLine)):
	    widget.controller = QtGui.QLineEdit(self.window)
	    #widget.controller.setEchoMode(2)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	###
	elif(widgetName==TextArea or isinstance(widget,TextArea)):
            widget.controller = QtGui.QTextEdit(widget.text,self.window)
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)

        elif(widgetName==RadioGroup or isinstance(widget,RadioGroup)):	
            widget.groupBox = QtGui.QGroupBox("", self.window)
            widget.controller = []
            radio_controller = QtGui.QRadioButton(widget.labels[0], widget.groupBox)
            widget.groupBox.move(widget.positions_X[0], widget.positions_Y[0])
            radio_controller.resize(widget.width, widget.height)
            radio_controller.move(0, 0)
            widget.controller.append(radio_controller)
	
            for i in range(1,len(widget.labels)):
                radio_controller = QtGui.QRadioButton(widget.labels[i], widget.groupBox)
                radio_controller.resize(widget.width, widget.height)
                radio_controller.move(widget.positions_X[i]-widget.positions_X[0], widget.positions_Y[i]-widget.positions_Y[0])
                widget.controller.append(radio_controller)
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].setChecked(True)
	
        elif(widgetName==ValueList or isinstance(widget,ValueList)):
            widget.controller = QtGui.QComboBox(self.window)
            widget.controller.addItem(widget.value)
            for i in range(0,len(widget.choices)):
                widget.controller.addItem(widget.choices[i])
            widget.controller.resize(widget.width, widget.height)    
            widget.controller.move(widget.position_X, widget.position_Y)
	

####

class Password(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):
	
        #self.text = text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

    def getText(self):
		
        if(self.controller == None):
	    return ''
	else:	
	    return self.controller.text()

    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.setText(text)
	
        return True
    

class Slider(object):

    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):
	
        #self.text = text
	self.start=start
	self.end=end
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
    def getValue(self):
	
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.value()
   
class SpinBox(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,start,end,X,Y,width,height):
	
        #self.text = text
	self.start=start
	self.end=end
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
    
    def getValue(self):
	
	if(self.controller == None):
	    return ''
	else:	
	    return self.controller.value()


class Label(object):

    controller = None
	
    callback = None
	
    def __init__(self,text,X,Y,width,height):
	

	self.text=text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height


class TextLine(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,X,Y,width,height):
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
    def getText(self):

	if(self.controller == None):
            return ''
	else:
	    return self.controller.text()

    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.setText(text)
	
        return True
    	
    def clear(self):
	
        self.controller.setText("")
	
        return True
	
    

####
class TextArea(object):
	
    controller = None
	
    callback = None
	
    def __init__(self,text,X,Y,width,height):
	
        self.text = text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height
	
	
    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.setText(text)
	
        return True
	
	
    def appendText(self,text):
	
        if(self.controller == None):
	
            self.text = self.text+text
	
        else:
	
            self.text = self.controller.toPlainText() + text
	
            self.controller.setText(self.text)
	
        return True              
	
	
    def clear(self):
	
        self.controller.setText("")
	
        return True
	
	
	
	
class Button(object):
	
    controller = None
	
    callbackMethod = None
	
    def __init__(self,text,X,Y,width,height):
	
        self.text = text
	
        self.position_X = X
	
        self.position_Y = Y
	
        self.width = width
	
        self.height = height

    def clickListener(self,method):
	
        if(self.controller == None):
	
            self.callbackMethod = method
	
        else:
	
            self.controller.clicked.connect(method)
	
        return True
	
    #### shubham
    

    ###### end
	
class CheckBox(object):
	
        controller = None
	
        value = False
	
        def __init__(self,title,X,Y,width,height):
	
                self.title = title
	
                self.position_X = X
	
                self.position_Y = Y
	
                self.width = width
	
                self.height = height
	
	
        def setValue(self,value):
	
                if(self.controller == None):
	
                    self.value = value
	
                else:
	
                    self.controller.setChecked(value)
	
	
        def getValue(self):
	
                if(self.controller == None):
	
                    return self.value
	
                else:
	
                    return self.controller.isChecked()
	
	
class RadioGroup(object):
	
        controller = None
	
        selected_pos = None
	
	
        def __init__(self,width,height):
	
            self.labels = []
	
            self.positions_X = []
	
            self.positions_Y = []
	
            self.width = width
	
            self.height = height
	
	
        def addRadioButton(self,label,X,Y):
	
            self.labels.append(label)
	
            self.positions_X.append(X)
	
            self.positions_Y.append(Y)
	
            return True
	
	
        def getValue(self):
	
                for i in range(len(self.controller)):
	
                    if(self.controller[i].isChecked()):
	
                        return self.labels[i]
	
                return None
	
	
        def setButtonTrue(self,pos):
	
            if(self.controller == None):
	
                self.selected_pos = pos
	
            else:
	
                button_controller = self.controller[pos]
	
                button_controller.setChecked(True)
	
	
''' WIDGETS: ValueList '''
	
	
class ValueList(object):
	
        controller = None
	
        def __init__(self,choices,X,Y,width,height,value=""):
	
            self.choices = choices
	
            self.position_X = X
	
            self.position_Y = Y
	
            self.width = width
	
            self.height = height
	
            self.value = value
	
	
        def getValue(self):
	
            if(self.controller == None):
	
                return self.value
	
            else:
	
                return self.choices[self.controller.currentIndex() - 1]
	

if __name__ == '__main__':
	
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
	
        textarea.setText("Created by qtGUI Author\n")
	
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
	
    Frame = Canvas(1, 'Survey ' ,810,800)
	
    
	
    
	
    #Dropdown valuelist
	
    cities = ['General Knowledge','Maths','' ]
	
    valuelist = ValueList(cities,80,30,200,20,"Choose Subject")
    #relist = ValueList(restaurants,140,10,150,20,"<Select restaurant>")
	
    Frame.add(valuelist)

	

	
    
	
    #radioGroup1
	
    rb1 = RadioGroup(100,50)
	
    rb1.addRadioButton("TRUE",475,210)
	
    rb1.addRadioButton("FALSE",575,210)
	
	
    rb1.setButtonTrue(0)
	
    Frame.add(rb1)
    
    rb2 = RadioGroup(100,50)
    rb2.addRadioButton("Easy",10,220)
    rb2.addRadioButton("Moderate",10,240)
    rb2.addRadioButton("Difficult",10,260)
    rb2.setButtonTrue(0)
    Frame.add(rb2)
    #TextArea
    textarea = TextArea("\n Question appears here!!",460,10,300,200)
    Frame.add(textarea)
    textarea1 = TextArea("\nYour Review!!\n\n",460,450,300,200)
    Frame.add(textarea1)
    #Creating Buttons
    submitBtn = Button("Start Quiz!",235,80,150,60)
    aboutBtn = Button("About",260,230,120,30)
    nextbtn = Button("Next Question",515,280,160,40)
    submit = Button("Submit Review",515,685,160,40)
    Frame.add(submit)
    submit.clickListener(review)
    nextbtn.clickListener(nextbuttonclick)
    Frame.add(nextbtn)
    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)
    ## password
    label3=Label(' Difficulty Level',0,55,490,30)
    label4=Label(' Select the topics you want to add on',10,340,300,30)
    Frame.add(label4)
    checkbox1 = CheckBox("History",10,375,225,15)
    checkbox2 = CheckBox("Philosophy",160,375,225,15)
    checkbox3 = CheckBox("Geography",310,375,225,15)
    Frame.add(checkbox1)
    Frame.add(checkbox2)
    Frame.add(checkbox3)
    Frame.add(label3) 
    label6 = Label("Please enter username and password",10,450,250,30)
    Frame.add(label6)
    pas=Password(100,540,150,30)
    Frame.add(pas)
    sli=Slider(0,25,20,100,150,30) 
    Frame.add(sli)
    spin=SpinBox(0,10,10,610,150,30) 
    Frame.add(spin)   
    label=Label('How was the Quiz ?',10,210,150,25)
    Frame.add(label)   
    label1=Label(' Select the Subject whose Quiz you want to take : ',0,0,490,30)
    Frame.add(label1)
    label9 = Label('Number of questions you would like to have in next quiz',10,580,500,30)
    Frame.add(label9)
    label7 = Label('Username',10,490,100,30)
    Frame.add(label7)      
    label8 = Label('Password',10,540,100,30)
    Frame.add(label8)
    text=TextLine(100,490,150,30)
    Frame.add(text)
    #Adding buttons to Frame
#    Frame.add(aboutBtn)
    Frame.add(submitBtn)
    Frame.show()
    
