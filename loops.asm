section	.text
	global _start       ;must be declared for using gcc
_start:     ;tell linker entry point
    
    mov eax, 0x5
    push eax
 
	
Helloworld:
	mov	edx, len    ;message length
	mov	ecx, msg    ;message to write
	mov	ebx, 1	    ;file descriptor (stdout)
	mov	eax, 4	    ;system call number (sys_write)
	int	0x80        ;call kernel

    pop eax
    dec eax
    push eax
    jnz Helloworld


	mov	eax, 1	    ;system call number (sys_exit)
	int	0x80        ;call kernel

section	.data

msg	db	'Hello, world!',0xa	;our dear string
len	equ	$ - msg			;length of our dear string
