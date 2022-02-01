; Programa que aceita somente a palavra "aabb"

if 'a' jump 5
rejeita
read 
X <- symbol
if 'a' jump 9
jump 4
read
X <- symbol
if 'b' jump 13
jump 4
read
X <- symbol
if 'b' jump 17
jump 4
read
X <- symbol
if # jump 21
jump 4
read

X <- symbol
aceita