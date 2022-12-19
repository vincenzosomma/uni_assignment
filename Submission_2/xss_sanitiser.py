#########################
#                       #
#  Simple xss sanitiser #
#                       #
#   by Vincenzo Somma   #
#########################


# function that sanitise the user input
def sanitise_input(input_string):

  # denylist containing some of the common sources used to exploit XSS vulnerabilities
  denylist = [
  "<script>", "<scr","</script>", "javascript&colon", "onerror", "alert(", "document.",
  ".cookies", "javascript:", "onload(", "vbscript:", "expression", "eval", "&lt;",
  "onreadystatechange", "xss:expression", "</>", "String.fromCharCode(88,83,83)", 
  "src=","atob(", ".URL", "documentURI", "location.", ".href", ".search", "location.*", 
  "window.", ".referrer", "(element", ".innerHTML", "setTimeout", "setInterval",  "execScript", 
  ".fromCharCod", "</scr", "prompt(", "<x", "contenteditable", "onfocus", "oninput", "ondrag", 
  "ondblclick", "oncut", "oncontextmenu", "oncopy", "onblur", "onchange", "onmouseup", "<brute", 
  "<brute", "formaction", "element.", "setInterval", ".write", ".hash", ".pathname"
   ]

  # transforming the words in the list in lowercase
  for i in range(len(denylist)):
    denylist[i] = denylist[i].lower() 

# XSS similarity counter
  count = 0
  # Iterates through each word in the denylist and checks if it appears in the input_string. 
  # If it does, it increments a counter and removes the word from the input_string.
  for word in denylist:
    if word in input_string:
        count += 1
        input_string = input_string.replace(word, "")


# The function returns the sanitised input_string, 
# the count of denied words found in the input_string.
  return input_string, count

# initialisation loop
# The loop continues until the user types 'N' to stop

loop = 'Y'
while loop.upper() == 'Y':
  # prompts the user for input and transforms the input in lower case
  user_input = input("Enter you input:\n")
  user_input = user_input.lower()
  # passes the user's input to the sanitise_input function
  sanitised_input, count = sanitise_input(user_input)

  
  # Output user input sanitised
  print("Your output is:\n", sanitised_input)  
  # Output the count of user input that may contain XSS similarity
  print("We found" , count , "XSS similarity in your inout") 
   
   # asks the user if wants to continue
  loop = input("Type 'Y' to continue or 'N' to stop: ")

# Ends the program
else:
    print("The program is no longer running...")


