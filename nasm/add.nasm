; Faz a soma de RAM[0] com RAM[1]

 leaw $1,%A         ; carrega a constant 1 em %A
 movw (%A),%D       ; move o valor da RAM[%A] para %D 
 leaw $0,%A         ; carrega a constant 0 em %A
 addw (%A), %D, %D  ; faz RAM[%A] + %D e salva em %D
 leaw $2, %A        ; carrega a constant 2 em %A
 movw %D, (%A)      ; copia o valor de %D para RAM[%A]
