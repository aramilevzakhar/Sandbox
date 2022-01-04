

section .text
    global _start 
_start: 
    loop: 
        mov rax, 4
    mov        rdi, 1
    add rsi, 1
    mov rdx, 1
    syscall
    cmp rsi,11
    jne loop
exit: 
    mov rax,60
    xor rdi,rdi
    syscall
