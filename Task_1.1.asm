section .text
global _start

_start:
	mov ecx, prompt
	mov edx, prompt_len
	call printstring
	
	call getAnsware
	cmp al,'w'
	je f_woman
	cmp al,'m'
	je f_man
error:
	mov ecx,werror
	mov edx,error_len
	call printstring
	jmp done

f_man:
	mov ecx,man
	mov edx,man_len
	call printstring
	jmp done

f_woman:
	mov ecx,woman
	mov edx,woman_len
	call printstring
	jmp done	

done:
	mov ebx,0
	mov eax,1
	int 0x80

getAnsware:
	push ecx
	mov ebx,0
	mov eax,3
	int 0x80

	pop ecx
	mov al, [ecx]
	ret

printstring:
	mov ebx,1
	mov eax,4
	int 0x80
	ret

section .data
	prompt db "Male or Woman?",0xa,"Use man or woman",0xa
	prompt_len equ $-prompt
	man db "Hi Sir!!",0xa
	man_len equ $-man
	woman db "Hi Madam!!",0xa
	woman_len equ $-woman
	werror db "WRONG ANSWARE TRY AGAIN!!!", 0xa
	error_len equ $-werror
	
