if '#' jump 46
if 'a' jump 6
if 'b' jump 9
if '#' jump 12
rejeita
read
X <- 'X'
jump 2
read
X <- 'Y'
jump 2
read
X <- symbol
if 'X' jump 21
if 'Y' jump 31
if 'x' jump 41
if 'y' jump 41
if '#' jump 44
if 'a' jump 47
if 'b' jump 47
read
X <- 'x'
if '#' jump 27
read
X <- symbol
jump 23
read
X <- 'a'
X <- symbol
jump 14
read
X <- 'y'
if '#' jump 37
read
X <- symbol
jump 33
read
X <- 'b'
X <- symbol
jump 14
read
X <- symbol
jump 14
read
X <- symbol
aceita
if '#' jump 51
read
X <- symbol
jump 47
read
X <- symbol
if 'x' jump 59
if 'y' jump 62
if '#' jump 65
read
X <- symbol
jump 53
read
X <- 'a'
jump 53
read
X <- 'b'
jump 53
read
X <- symbol
jump 46