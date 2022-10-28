;this is a comment


;Printing Hello World

global _start

section .text
;Print a text on the console
_start:
;######################################
; syscall - write(1, msg, len);
;######################################
    mov eax, 0x4  ;Syscall number for Write()
                    ; system call in the case we are writing on the screen
    mov ebx, 0x1 ;File Descriptor to write to
                  ; In this case: STDOUT is 1
    mov ecx, message ;message is the variable storing the data
    mov edx, 0xc ;The length of string to print it is the lenght of our message in exadecimal
                ;which is 12 characters    
    int 0x80 ; tell to the kernel to implenet this code
;######################################
; syscall - exit(0);
;######################################
    mov aex, 0x1 ;system call to exit() the program
    mov ebx, 0x0 ;The status code we want to provide.
    int 0x80 ;Poke kernel. This will end the program

section .data

 message: db "Hello World!", 0xa  
                                ;Declare a label "msg" which has
                                ; our string we want to print.
                                ; for reference: 0xa = "\n"

