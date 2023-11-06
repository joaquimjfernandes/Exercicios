"""2) Analise os algoritmos abaixo e diga o que será impresso na tela ao serem executados:
a) A<-10 - B<-20  == ler B, B<-5 == ler A,B
b) A<-30 - B<-20 - C<- A+B == ler C, B<- 10, ler B,C == C<-A+B, ler A,B,C
c) A<-10 - B<-20 - C<-A - B<-C - A<-B == ler A,B,C
d) A<-10 - B<-A+1 - A<-B+1 - B<-A+1 == ler A, A<-B+1 == ler A,B
e) A<-10 - B<-5 - C<-A+B - B<-20 - A<-10 == ler A,B,C
f) X<-1 - Y<-2 - Z<-Y-X ==ler Z, X<- 5 - Y<-X+Z == ler X,Y,Z"""

# Linha A
a = 10
b = 20
print(f'B: {b}')
b = 5
print(f'A: {a} <> B: {b}')
print('---'*10)

# Linha B
a = 30
b = 20
c = a+b
print(f'C: {c}')
b = 10
print(f'B: {b} <> C: {c}')
c = a+b
print(f'A: {a} <> B: {b} <> C:{c}')
print('---'*10)
