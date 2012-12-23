import gtk



class Canvas:
    def __init__(self, id, title,width,height):
        self.window = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title(title)
        self.window.set_size_request(width,height)
        # Create a Fixed Container
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.show()


    def show(self):
        self.window.show()
        gtk.main()
        return

    def add(self,widget):
        widget_type = type(widget)  
        print widget_type     
        if(widget_type==Button):
            widget.controller = gtk.Button(widget.text)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
                
        elif(widget_type==TextArea):
            widget.controller = gtk.TextView(widget.buffer)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            if(widget.callbackMethod != None ):
                widget.controller.connect('clicked',widget.callbackMethod)
        elif(widget_type==TextLine):
      widget.controller = gtk.Entry()
            widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()

        elif(widget_type==CheckBox):
            widget.controller = gtk.CheckButton(widget.title)
            widget.controller.set_size_request(widget.width,widget.height)
            self.fixed.put(widget.controller, widget.position_X, widget.position_Y)            
            widget.controller.show()
            widget.controller.set_active(widget.value)
	####
	elif(widget_type==Password):
	    widget.controller = gtk.Entry()
	    widget.controller.set_visibility(0)
            widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()

	elif(widget_type==Slider):
	    widget.controller = gtk.HScale()
	    widget.controller.set_range(widget.start, widget.end)
	    widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()
            
	
	elif(widget_type==SpinBox):
	    widget.controller = gtk.SpinButton()
	    widget.controller.set_range(widget.start,widget.end)
	    widget.controller.set_increments(1, 1)
	    widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()
            
	elif(widget_type==Label):
	    widget.controller = gtk.Label(widget.text)
	    widget.controller.set_size_request(widget.width,widget.height)
	    self.fixed.put(widget.controller, widget.position_X, widget.position_Y)
	    widget.controller.show()
	
	###
            
        elif(widget_type==RadioGroup):
            widget.controller = []
            radio_controller = gtk.RadioButton(None, widget.labels[0])
            radio_controller.set_size_request(widget.width,widget.height)
            self.fixed.put(radio_controller,widget.position_X[0], widget.position_Y[0])
            radio_controller.show()
            widget.controller.append(radio_controller)
            for i in range(1,len(widget.labels)):
                radio_controller = gtk.RadioButton(widget.controller[0], widget.labels[i])
                radio_controller.set_size_request(widget.width,widget.height)
                self.fixed.put(radio_controller,widget.position_X[i], widget.position_Y[i])
                radio_controller.show()
                widget.controller.append(radio_controller)
            
            if(widget.selected_pos != None):
                widget.controller[widget.selected_pos].set_active(True)
            
        elif(widget_type==ValueList):
            widget.controller = gtk.OptionMenu()
            widget.controller.set_size_request(widget.width,widget.height)
            menu = gtk.Menu()
            for name in widget.choices:
                item = gtk.MenuItem(name)
                item.show()
                menu.append(item)
                print "gis"
            widget.controller.set_menu(menu)
            widget.controller.show()
            self.fixed.put(widget.controller,widget.position_X, widget.position_Y)
            

class Button(gtk.Button):
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
            self.controller.connect("clicked", method)
        return True
    
class TextArea(gtk.TextView):
    controller = None
    callbackMethod = None
    buffer = gtk.TextBuffer()
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height

    def setText(self,text):
        self.buffer.set_text(text)
        return True

    def appendText(self,text):
        self.buffer.insert(self.buffer.get_end_iter(),text)
        return True              

    def clear(self):
        self.buffer.set_text("")
        return True
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
	    return self.controller.get_text()

    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.set_text(text)
	
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
	    return self.controller.get_value()
   
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
	    return self.controller.get_value()


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
	    return self.controller.get_text()

    def setText(self,text):
	
        if(self.controller == None):
	
            self.text = text
	
        else:
	
            self.controller.set_text(text)
	
        return True
    	
    def clear(self):
	
        self.controller.set_text("")
	
        return True
	
    

####

class CheckBox(gtk.CheckButton):
    controller = None
    value = False
    def __init__(self,title,X,Y,width,height):
        self.title = title
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
    
    def setValue(self,value):   #True or False for checked
        if(value != True or value != False):
            return
        if(self.controller == None):
            self.value = value
        else:
            self.controller.set_active(value)

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            return self.controller.get_active()


class RadioGroup(gtk.RadioButton):
    GroupController = None
    controller = None
    selected_pos = None
    def __init__(self,width,height):
        self.labels = []
        self.position_X = []
        self.position_Y = []
        self.width = width
        self.height = height
        self.GroupController = None

    def addRadioButton(self,label,X,Y):
        self.labels.append(label)
        self.position_X.append(X)
        self.position_Y.append(Y)
        return True

    def getValue(self):
        for i in range(len(self.controller)):
            if(self.controller[i].get_active()):
                return self.labels[i]
        return "None"

    def setButtonTrue(self,pos):
        if(self.controller == None):
            self.selected_pos = pos
        else:
            button_controller = self.controller[pos]
            button_controller.set_active(True)

class ValueList(gtk.OptionMenu):
    controller = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.title = ""
        self.position_X = X
        self.position_Y = Y
        self.width = width
        self.height = height
        self.value = value
        temp = [value]
        for i in range(len(choices)):
            temp.append(choices[i])
        self.choices = temp

    def getValue(self):
        if(self.controller == None):
            return self.value
        else:
            IntValue = self.controller.get_history()
            if(IntValue < 0):
                return None
            return self.choices[IntValue]
            
if __name__ == "__main__":            
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
	
    
	
        textarea.appendText("_______________________\n"+report+"\n\n")
	
        return True 
	
    
	
    def AboutButtonClick(event=None):
	
        textarea.setText("Created by qtGUI Author :\n")
	
        return True
	
    
	
    
	
    
	
    #Constructor Frame
	
    Frame = Canvas(1, 'qtGUI |' ,800,500)
	
    
	
    
	
    #Dropdown valuelist
	
    cities = ['New Delhi', 'London', 'Ropar', 'Ludhiana', 'Chandigrah', 'Rome', 'Jaipur' ]
    restaurants = ['Mc Donalds','Pind Baluchi', 'KFC' , 'CCD']
	
    valuelist = ValueList(cities,10,10,130,30,"   Select city")
    relist = ValueList(restaurants,160,10,180,30,"   Select restaurant")
	
    Frame.add(valuelist)
    Frame.add(relist)
	
    
	
    #checkboxs
	
    checkbox1 = CheckBox("Pizza",10,45,215,15)
	
    checkbox2 = CheckBox("cheese tomato",10,65,235,15)
    checkbox3 = CheckBox("Chicken Tikka Butter Masala",10,85,235,15)
    checkbox4 = CheckBox("Chana Masala",10,105,235,15)
	
    checkbox1.setValue(True)
    #dishes  = Label('Dishes you like:',10,20,210,15)
    #Frame.add(dishes)
    Frame.add(checkbox1)
	
    Frame.add(checkbox2)
    Frame.add(checkbox3)
    Frame.add(checkbox4)
	
    
	
    #radioGroup1
	
    rb1 = RadioGroup(80,50)
	
    rb1.addRadioButton("Nice",10,130)
	
    rb1.addRadioButton("Good",90,130)
	
    rb1.addRadioButton("Great",170,130)
	
    rb1.setButtonTrue(2)
	
    Frame.add(rb1)
    #radioGroup2
    rb2 = RadioGroup(150,50)
    rb2.addRadioButton("Like to visit again!",10,170)
    rb2.addRadioButton("Not for me!",170,170)
    rb2.setButtonTrue(0)
    Frame.add(rb2)
    #TextArea
    textarea = TextArea("\n Click submit button to see output here!!",480,10,280,400)
    Frame.add(textarea)
    #Creating Buttons
    submitBtn = Button("Submit",130,460,120,30)
    aboutBtn = Button("About",260,460,120,30)
    #Callback methods on buttons click
    submitBtn.clickListener(SubmitButtonClick)
    aboutBtn.clickListener(AboutButtonClick)
    #Adding buttons to Frame
    Frame.add(aboutBtn)
    Frame.add(submitBtn)
    Frame.show()
            
            
