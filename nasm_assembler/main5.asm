section .text
	global _start

segment .bss
	res resb 4

section _data
	; overridden constant 
	; 返最近利私秋知売買
	; 返最近利私秋知売買和出口
	%assign total 50
	message db 'hello linux'
	; Multiple initializations
	stars times 20 db '#'
	; This directive is also overridden and case sensitive.
	%define PTR [EBP+4]
	oneconst equ 10
	count dw 0


_start:
	mov edx, 11
	mov ecx, message
	mov eax, 4
	mov ebx, 1
	int 0x80

	mov eax, 4
	mov ebx, 1
	mov ecx, count
	mov edx, 3
	int 0x80




	mov eax, [count]
	sub eax, '0'

	mov [res], eax


  ; Считываем и сохраняем пользовательский ввод

	mov eax, 1
	int 0x80



