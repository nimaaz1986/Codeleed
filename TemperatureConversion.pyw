# Name: Nima Azadikhah
# Date: April 19th, 2022
# App name: Temperature Conversion
# Description: convert the temperature to the other scale and display the result rounded to 1 decimal place


from tkinter import *           # imports everything * from tkinter mudole
from tkinter.ttk import *       # Modernize the look of GUI
from tkinter import messagebox  # Need for the pop-ups


#constant

CELSIUS = "Convert to Celsius"
FAHRENHEIR = "Convert to Fahrenheit"
COEFFICIENT1 = 32
COEFFICIENT2 = 5/9
COEFFICIENT3 = 9/5


#Functions
def convert_click():
    """
    Executed when the convert button is clicked
    * Dispaly a result fron conversion celsius to Fahrenheit 
    * Display an error if a question is left unanswe the user input in the Entry textbox is empty, or not a numeric,red
    * Resert the form
    
    """
    temperature = input_text.get() # gets the temperature from the Entry
    

    # Try to convert to  a  float number
    try:
        temperature = float(temperature)
        numeric = True
    except:
        numeric = False    
    # Error in case not numeric 
    if not numeric:
        messagebox.showerror(title="Error", message="Please enter the valid temperature")
          
    # We got a valid number
    else:
        if select_converter.get() == CELSIUS:
            # Conversion of fahrenheit temperature to celsius
        
            result = ((temperature - COEFFICIENT1) * COEFFICIENT2)
            # Display the reulit in celsius
            out_text.set(f"{result:.1f}")

        if select_converter.get() == FAHRENHEIR:
            # Conversion of celsius temperature to fahrenheit
            result = ((temperature * COEFFICIENT3) + COEFFICIENT1)
            out_text.set(f"{result:.1f}")








def clear_click():
    """
    Executed when the user clicks the Clear button
    * Resets input and output to nothing
    """
    input_text.set(" ") # Reset value of Entry temperature
    out_text.set(" ") # Reset value of output conversion  
    select_converter.set(CELSIUS) # Reset value is from ℉ to ℃

def key_handler(event:Event):
    """
    Handles the key presses
    * Event means the key press
    """

    if event.keysym == "Escape" : # aka [Esc] key
        clear_click() 

    elif event.keysym == "Return": # [Enter] key
        convert_click()
 



window = Tk()                                         # Create a new window
window.title("Temperature Converter-Nima Azadikhah")  # Set the title
window.resizable(width=False, height=False)           # Window is not resizable
window.bind("<Key>", key_handler)                     # call a function whenever a key is pressed

#frame1
temperatureframe = LabelFrame(text= "Temperature Converter")
#  RadioButtons (for the temperature) 


#frame2
frame = Frame()
# Input Label

input_label = Label(frame, text=" temperature: ")
# Input Entry (aka textbox) for the user putting the temperature
input_text = Variable() # only for the wedgets
input_text.set(" ") # Defult value
input_entry = Entry(frame,width=60,textvariable=input_text) 


# Output Label

out_label = Label(frame, text="Conversion:  ")
out_text = Variable() # only for the wedgets
out_text.set("") # Defult value
out_entry = Entry(frame,width=60,state="readonly",cursor="no",textvariable=out_text)

select_converter = Variable() # Variable holding which button is checked
select_converter.set(CELSIUS) # when the program starts the Radio button of covert to Celsius is on
temperature1_radiobutton = Radiobutton(temperatureframe, text=CELSIUS, variable = select_converter, value=CELSIUS)
temperature2_radiobutton = Radiobutton(temperatureframe, text=FAHRENHEIR,variable = select_converter, value=FAHRENHEIR)

# Convert Button
convert_button = Button(frame,text = 'Convert', command=convert_click)

# Clear Button
clear_button = Button(frame,text = 'Clear',command=clear_click)

# Place widgets using pack()
temperatureframe.pack(padx=5,pady=5,fill="x")
temperature1_radiobutton.pack(anchor="w")      # Align the button to the left (west)
temperature2_radiobutton.pack(anchor="w")      # Align the button to the left (west)
#frame2
frame.pack(padx=10,pady=10)
input_label.pack(anchor="w")
input_entry.pack(pady=(0,10))                  # adding 0 padding at the top, and 10 at the bottom
out_label.pack(anchor="w")
out_entry.pack(pady=(0,10))                    # adding 0 padding at the top, and 10 at the bottom
# Button
clear_button.pack(side="left")
convert_button.pack(side="right")


window.mainloop() # Make the window visible


