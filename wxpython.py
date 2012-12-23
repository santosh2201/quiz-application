#!/usr/bin/python
# Button and Text-Area
import wx
#import lab
#WindowFrame(1, 'Survey ' ,510,500)
#----------------------------------------------------------------------------#----------------------------------------------------------#
class Canvas(wx.Frame):
  controller = None
	def __init__(self,id, title,width,height):
		self.app = wx.App(False)
		wx.Frame.__init__(self, None, id, title, wx.DefaultPosition, wx.Size(width, height))
		self.panel = wx.Panel(self, -1)
	
	def center(self):
		self.Centre()	

	def show(self):
		self.Show(True)
		self.app.MainLoop()
				
		
	def add(self,widget,field=None):
		widget_type = type(widget)
	        if(widget_type==TextArea or isinstance(widget,TextArea)):
			widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_MULTILINE)
		elif(widget_type==Password or isinstance(widget,Password)):      
			widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=wx.TE_PASSWORD)
		elif(widget_type==TextLine or isinstance(widget,TextLine)):      
			widget.controller = wx.TextCtrl(self.panel, -1, widget.text,  widget.position, widget.size, style=0) 
		elif(widget_type==Slider or isinstance(widget,Slider)):
			widget.controller = wx.Slider(self.panel, -1, value = -1,minValue=widget.start,maxValue=widget.end,pos=widget.pos,size=widget.size)	
			#self,start,end,X,Y,width,height
		elif(widget_type==SpinBox or isinstance(widget,SpinBox)):
			widget.controller = wx.SpinButton(self.panel, -1,  widget.pos, widget.size)			
		elif(widget_type==Button or isinstance(widget,Button)):
        		widget.controller = wx.Button(self.panel, -1, widget.title,  widget.position, widget.size)
          		if(widget.callBackMethod is not None):
                		widget.controller.Bind(wx.EVT_BUTTON,widget.callBackMethod,id = widget.controller.GetId())
        	elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
          		widget.controller = wx.CheckBox(self.panel, -1, widget.title,  widget.position)
        	elif(widget_type==RadioGroup or isinstance(widget,RadioGroup)):
            		widget.controller = []
          		radio_controller = wx.RadioButton(self.panel, -1, widget.labels[0], widget.positions[0],widget.size,style=wx.RB_GROUP)
            		widget.controller.append(radio_controller)
            		for i in range(1,len(widget.labels)):
                		radio_controller = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i],widget.size)
                		widget.controller.append(radio_controller)
                        if(widget.selected_index != None):
                		widget.controller[widget.selected_index].SetValue(True)
		elif(widget_type==ValueList or isinstance(widget,ValueList)):
         		widget.controller = wx.ComboBox(self.panel, -1,widget.value,widget.position,widget.size,widget.choices,style=wx.CB_READONLY)
		elif(widget_type==Label or isinstance(widget,Label)):
			widget.controller = wx.StaticText(self.panel,-1,widget.name,widget.position,widget.size)

class Password(wx.TextCtrl):
	controller = None
	def __init__(self,X,Y,width,height):
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text=""
	def setText(self,text):
		self.controller.text = text		
	def appendText(self,text):
		self.controller.text = self.controller.text + text
	def clearText():
		self.controller.text = ""	
	def getText(self):
		return self.controller.GetValue()


class TextArea(wx.TextCtrl):
	controller = None
	def __init__(self,string,X,Y,width,height):
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text = string
	def setText(self,text):
        	if(self.controller == None):
        	    self.text = text
        	else:
        	    self.controller.SetValue(text)
        	return True
	def appendText(self,text):
	        if(self.controller == None):
	            self.text = self.controller.GetValue() + text
	        else:
	            self.controller.AppendText(text)
	        return True              

	def clearText():
		self.controller.text = ""	
	def getText(self):
		return self.controller.GetValue()

	#textarea.appendText(" password :  \n"+ pas.getText()+"_______________________\n"+report+"\n" + " Slider value " + str(sli.getValue())+" SpinBox value  " + str(spin.getValue())+" \n")

class TextLine(wx.TextCtrl):
	controller = None
	def __init__(self,X,Y,width,height):
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text=""
	def setText(self,text):
		self.controller.text = text		
	def appendText(self,text):
		self.controller.text = self.controller.text + text
	def clearText():
		self.controller.text = ""	
	def getText(self):
		return self.controller.GetValue()

class Slider(wx.Slider):
	controller = None
	callBackMethod = None
	def __init__(self,start,end,X,Y,width,height):
		self.start=start
		self.end=end
        	self.pos = (X,Y)
		self.size = (width,height)
	def getValue(self):
		if(self.controller == None):
			return ''
		else:	
	    		return self.controller.GetValue()


class Label(wx.StaticText):
	controller =  None
	def __init__(self,name, X,Y, width,height):
		self.position = (X,Y)
       		self.size = (width,height)
		self.name = name

class SpinBox(wx.SpinButton):
	controller = None
	callBackMethod = None
	def __init__(self,start,end,X,Y,width,height):
	
        	#self.text = text
		self.start=start
		self.end=end
        	self.pos = (X,Y)
        	self.size = (width,height)
    
    	def getValue(self):
		if(self.controller == None):
	       		return ''
		else:	
	    		return self.controller.GetValue()

class Button(wx.Button):
	controller = None
	callBackMethod = None	
	def __init__(self,string,X,Y,width,height):	
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.title = string

	def clickListener(self,method):
		self.callBackMethod = method

class CheckBox(wx.CheckBox):
	controller = None
	def __init__(self,string,X,Y,width=10,height=10):
		self.position = (X,Y)
		self.id = -1
		self.title = string

	def setValue(self,value):
        	#self.controller.SetValue(value)
                1
	def getValue(self):
		return self.controller.GetValue()              	

class RadioGroup(object):
	controller = None
   	selected_index = None
    
	def __init__(self,width,height):
	        self.labels = []
	        self.positions = []
	        self.size = wx.Size(width, height)

        def addRadioButton(self,label,X,Y):
	        self.labels.append(label)
	        self.positions.append((X,Y))
	        return True

	def getValue(self):
        	for i in range(len(self.controller)):
        	    if(self.controller[i].GetValue()):
        	        return self.labels[i]
        	return None

    	def setButtonTrue(self,index):
    	    if(self.controller == None):
    	        self.selected_index = index
    	    else:
    	        button_controller = self.controller[index]
    	        button_controller.SetValue(True)

class ValueList(wx.ComboBox):
    controller = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.choices = choices
        self.position = (X,Y)
        self.size = (width,-1)
        self.value = value

    def getValue(self):
            if(self.controller == None):
                return self.value
            else:
                return self.controller.GetValue()


if __name__ == "__main__":		     # This will only run if this very file is executed and not when it has been executed by importing
	#Functions bind to button events
	app = wx.App()
		
	def SubmitButtonClick(event=None):
	
	        report = " Your city is "+valuelist.getValue()+"\n"
	
	        if(checkbox1.getValue()):
		
	        	report = report + " you have read the code\n"
	
        	else:
	
            		report = report + " you have not read the code\n"
	
    
	
        	if(checkbox2.getValue()):
	
            		report = report + " you have read the documentation\n"
	
        	else:
	
            		report = report + " you have not read the documentation\n"
	
    
	
        	report = report + " you are "+rb1.getValue()+"\n"
	
        	report = report + " you need "+rb2.getValue()+"\n"
	
    
	
        	textarea.appendText(" password :  \n"+ pas.getText()+"_______________________\n"+report+"\n" + " Slider value " + str(sli.getValue())+" SpinBox value  " + str(spin.getValue())+" \n")
	
		#textarea.appendText(sli.getValue())

        	return True 
	
    
	
    	def AboutButtonClick(event=None):
	
        	textarea.setText("Created by qtGUI Author : Prateek Mukati\n")
	
        	return True
	
    	#Constructor Frame
	
    	Frame = Canvas(1, 'Survey ' ,510,500)
	
    
	
    
	
    	#Dropdown valuelist
	
    	cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]
	
    	valuelist = ValueList(cities,10,10,200,20,"<Select your city>")
	
    	Frame.add(valuelist)
	
    
	
    	#checkboxs
	
    	checkbox1 = CheckBox("I have read the code.",10,45,215,15)
	
    	checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
	
    	#checkbox1.setValue(True)
	
    	Frame.add(checkbox1)
	
    	Frame.add(checkbox2)
	
    
	
    	#radioGroup1
	
    	rb1 = RadioGroup(60,50)
	
    	rb1.addRadioButton("Nice",10,110)
	
    	rb1.addRadioButton("Good",70,110)
	
    	rb1.addRadioButton("Great",140,110)
	
    	rb1.setButtonTrue(2)
	
    	Frame.add(rb1)
    	#radioGroup2
    	rb2 = RadioGroup(100,50)
    	rb2.addRadioButton("Option #1",10,160)
    	rb2.addRadioButton("Option #2",110,160)
    	rb2.setButtonTrue(0)
    	Frame.add(rb2)
    	#TextArea
    	textarea = TextArea("\n Click submit button to see output here!!",250,10,250,200)
    	Frame.add(textarea)
    	#Creating Buttons
    	submitBtn = Button("Submit",130,230,120,30)
    	aboutBtn = Button("About",260,230,120,30)
    	#Callback methods on buttons click
    	submitBtn.clickListener(SubmitButtonClick)
    	aboutBtn.clickListener(AboutButtonClick)
    	## password
    	pas=Password(130,280,150,30)
    	Frame.add(pas)
    	sli=Slider(0,10,130,320,150,30) 
    	Frame.add(sli)
    	spin=SpinBox(0,10,130,360,150,30) 
    	Frame.add(spin)   
    	label=Label("happy",130,400,150,30)
    	Frame.add(label)   
    	text=TextLine(300,400,150,30)
	#def __init__(self,string,X,Y,width,height):
    	Frame.add(text)
    	#Adding buttons to Frame
    	Frame.add(aboutBtn)
    	Frame.add(submitBtn)
    	Frame.show()
	app.MainLoop()
