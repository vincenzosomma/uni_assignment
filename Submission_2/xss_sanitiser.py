#########################
#                       #
#     XSS sanitiser     #
#                       #
#   by Vincenzo Somma   #
#########################


# function that sanitise the user input
def sanitise_input(input_string):

  # denylist containing some of the common sources used to exploit XSS vulnerabilities
  denylist = [
'<script>', '<scr', '</script>', 'javascript&colon', 'onerror', 'alert(', 'document.', 
'.cookies', 'javascript:', 'onload(', 'vbscript:', 'expression', 'eval', '<', 
'onreadystatechange', 'xss:expression', '</>', 'String.fromCharCode(', 'src=', 
'atob(', '.URL', 'documentURI', 'location.', '.href', '.search', 'location.*', 
'window.', '.referrer', '(element', '.innerHTML', 'setTimeout', 'setInterval', 
'execscript', '.fromCharCod', '</scr', 'prompt(', '<x', 'contenteditable', 'onfocus',
'oninput', 'ondrag', 'ondblclick', 'oncut', 'oncontextmenu', 'oncopy', 'onblur', 'onchange',
'onmouse', '<brute', 'formaction', 'element.', '.write', '.hash', '.pathname', 'data:',
'bypassSecurityTrustAs*', '.textContent', '.encode(', '\\', 'url(', 'livescript:', 
'ondragend', 'onkey', 'onbefor', '&#', '%0', 'onafterprint', 'onafterscriptexecute',
'onanimationcancel', 'onanimationend', 'onanimationiteration', 'onanimationstart', 
'onauxclick', 'onbeforecopy', 'onbeforecut', 'onbeforeinput', 'onbeforeprint', 
'onbeforescriptexecute', 'onbeforeunload', 'onbegin', 'onbounce', 'oncanplay', 
'oncanplaythrough', 'onclick', 'onclose', 'oncuechange', 'ondragenter', 'ondragleave',
'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onend', 'onended', 'onfinish',
'onfocusin', 'onfocusout', 'onfullscreenchange', 'onhashchange', 'oninvalid', 'onkeydown',
'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadend', 'onloadstart',
'onmessage', 'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover',
'onmouseup', 'onmousewheel', 'onmozfullscreenchange', 'onpagehide', 'onpageshow', 'onpaste', 'onpause',
'onplay', 'onplaying', 'onpointerdown', 'onpointerenter', 'onpointerleave', 'onpointermove', 'onpointerout',
'onpointerover', 'onpointerrawupdate', 'onpointerup', 'onpopstate', 'onprogress', 'onratechange', 'onrepeat',
'onreset', 'onresize', 'onscroll', 'onsearch', 'onseeked', 'onseeking', 'onselect', 'onselectionchange',
'onselectstart', 'onshow', 'onstart', 'onsubmit', 'ontimeupdate', 'ontoggle', 'ontouchend',
'ontouchmove', 'ontouchstart', 'ontransitioncancel', 'ontransitionend', 'ontransitionrun',
'ontransitionstart', 'onunhandledrejection', 'onunload', 'onvolumechange', 'onwebkitanimationend',
'onwebkitanimationiteration', 'onwebkitanimationstart', 'onwebkittransitionend', 'onwheel'
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

 #if the sanitise_input function doesn't find any match
  if count == 0 :
  # Output user input if doesn't if it is safe
    print("Your output is:\n", user_input) 
  else:
  # Output the count of user input that may contain XSS similarities
    print("Your sanitised input:\n", sanitised_input ,"\nWe found" , count , "XSS common similarities in your input") 
   
   # asks the user if wants to continue
  loop = input("Type 'Y' to continue or 'N' to stop: ")

# Ends the program
else:
    print("The program is no longer running...")