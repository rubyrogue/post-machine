; Sobrescreve o primeiro elemento por 'b' e anda uma posição à esquerda

read
X <- 'b'
if '#' jump 9
read
X <- symbol
jump 5
read
X <- symbol
X <- '_'
if '#' jump 16
read 
X <- symbol
jump 12
read
X <- symbol
aceita