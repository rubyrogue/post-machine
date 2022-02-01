; Aceita palíndromo do alfabeto [ab]

if '#' jump 49
if 'a' jump 8
if 'b' jump 28
if '#' jump 11
rejeita

; verifica se o último elemento também é 'a'
read
if # jump 49
if 'a' jump 15
if 'b' jump 22
if # jump 26
read
if # jump 19
X <- symbol
jump 12
read
X <- symbol
jump 3
read
X <- symbol
if # jump 7
jump 12
read
X <- symbol

; verifica se o último elemento também é 'b'
read
if # jump 49
if 'b' jump 35
if 'a' jump 42
if # jump 46
read
if # jump 39
X <- symbol
jump 32
read
X <- symbol
jump 3
read
X <- symbol
if # jump 7
jump 32
read
X <- symbol

aceita