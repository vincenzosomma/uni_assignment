;############################################
;# This is a simple Assembly program        #
;# that requests user input  and elaborates #
;# the output based on the input given      #
;#                                          #
;#            by VINCENZO SOMMA             #
;############################################


section .text                           ; this section contains the program instructions
    
    global _start                       ; tells the kernel where the program begins

_start:                                 ; tell linker entry point

	mov ecx, prompt                     ; store the string 'prompt' in the ecx register
	mov edx, prompt_len                 ; store the string length 
	call printstring                    ; calls the function 'printstring' that contains the system calls to display the string on the screen
	
	call getAnsware                     ; call the function that contains the system calls to get the user input
	cmp al,'w'                          ; Condition: compare the value in the 8-bit "al" register, "if" corresponds to the value assigned 
	je f_woman                          ; "if the comparison is true, the program will jump and call the function f_woman
	cmp al,'m'                          ; Condition: compare the value in the 8-bit "al" register, "if" corresponds to the value assigned
	je f_man                            ; "if" the comparison is true, the program will jump and call the function f_man
    
    call error                          ; "else" the program will execute the error function as it is most likely that the user inserted the wrong answer

error:                                  

	mov ecx,w_error                     ; store the string 'w_error' in the ecx register
	mov edx,error_len                   ; store the string length 
	call printstring                    ; calls the function 'printstring' that contains the system calls to display the string on the screen
	jmp done                            ; calls the function 'done' that contain the system calls to display the string on the screen

f_man:

	mov ecx,man                         ; store the string 'w_error' in the ecx register
	mov edx,man_len                     ; store the string length
	call printstring                    ; calls the function 'printstring' that contains the system calls to display the string on the screen
	jmp done                            ; calls the function 'done' that contain the system calls to display the string on the screen


f_woman:

	mov ecx,woman                       ;########################################################################
	mov edx,woman_len                   ;#  same instructions as f_man functions but using the woman variable
	call printstring                    ;#
	jmp done	                    ;########################################################################   

done:

	mov ebx,0                           ; file descriptor 0 (stdin), standard input (for reading conventional input) (Opengroup.org, 2018)
	mov eax,1                           ; system call to exit() the program
	int 0x80                            ; Poke kernel. This will end the program (Linfo.org, 2022)

getAnsware:

	push ecx                            ; push the 
	mov ebx,0                           ; file descriptor 0 (stdin), standard input (for reading conventional input) (Opengroup.org, 2018)
	mov eax,3                           ; system call to read() the user input
	int 0x80                            ; Poke kernel. the program interrupt by a service performed by the kernel such as input/output


	pop ecx                                 
	mov al, [ecx]                       ; move in AL the first letter of the keyboard input
	ret                                 ; Return from Procedure, to resume the exeution flow ar the program incstructions

printstring:

	mov ebx,1                            ; file descriptor 1 (stdout) Standard output.  (Opengroup.org, 2018)
	mov eax,4                            ; Syscall for Write() on the screen
	int 0x80                             ; Poke kernel. the program interrupt by a service performed by the kernel such as input/output
	ret                                  ; Return from Procedure, to resume the exeution flow ar the program incstructions 

section .data			;This section cointains initialised data or constants
                                                                  ; stores the message into the variable prompt
	prompt db "Are you a Male or Woman?",0xa,"Type: m or w",0xa   ; 0Xa causes the next set of output to occur on the next line
	prompt_len equ $-prompt                                       ; automatically calculates the lenght of the messages
	
	man db "Hi Sir :) !!",0xa
	man_len equ $-man
	
	woman db "Hi Madam :) !!",0xa
	woman_len equ $-woman
	
	w_error db " :'(  WRONG ANSWER!!! TRY AGAIN :P !!!", 0xa
	error_len equ $-w_error
