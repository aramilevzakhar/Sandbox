section .text
	global _start

section .data
name db 'Hello world'
choice DB 'y'
number1 DW 1232
number2 DW 12132
marks times 20 db '*'
msg1 db 'Hello, linux', 0xa, 0xd
len equ $ - msg1
SYS_EXIT  equ 1
SYS_WRITE equ 4
STDIN     equ 0
STDOUT    equ 1
%assign TOTAL 10





_start:
  mov eax, SYS_WRITE         
  mov ebx, STDOUT         
  mov ecx, msg1         
  mov edx, len 
  int 0x80

	mov edx, 20
	mov ecx, marks
	mov ebx, 2
	mov eax, 4
	int 0x80

  mov eax, SYS_WRITE         
  mov ebx, STDOUT         
  mov ecx, TOTAL
  mov edx, 5
  int 0x80

	;%assign TOTAL 20

  ;mov eax, SYS_WRITE         
  ;mov ebx, STDOUT         
  ;mov ecx, TOTAL
  ;mov edx, 80
  ;int 0x80




;	mov edx, 11
;	mov ecx, name
;	mov ecx, choice
;	mov ebx, 2			; файловый дескриптор (stdout)
;	mov eax, 4			; номер системного вызова (sys_write)
;	int 0x80

;	mov eax, 2
;	int 80h

;	mov edx, 32
;	mov ecx, number2
;	mov ebx, 2
;	mov eax, 4
;	int 80h

	mov eax, 1
	mov ebx, 0
	int 0x80







