from State import State

qlparen = State('QLPAREN')
qlbraces = State('QLBRACES')
qrparen = State('QRPAREN')
qnumber = State('QNUMBER')
qlessequal = State('QLESSEQUAL')
qgreaterequal = State('QGREATERQUAL')
qequal = State('QEQUAL')
qdifferent = State('QDIFFERENT')

qo = State('QO')  # Estado padrão, ou seja, quando não for definido um estado, sera utilizado ele

q0 = State('Q0')
q1 = State('Q1')
q2 = State('Q2')
q3 = State('Q3')
q4 = State('Q4')
q5 = State('Q5')
q6 = State('Q6')
q7 = State('Q7')
q8 = State('Q8')
q9 = State('Q9')
q10 = State('Q10')
q11 = State('Q11')
q12 = State('Q12')
q13 = State('Q13')
q14 = State('Q14')
q15 = State('Q15')
q16 = State('Q16')
q17 = State('Q17')
q18 = State('Q18')
q19 = State('Q19')
q20 = State('Q20')
q21 = State('Q21')
q22 = State('Q22')
q23 = State('Q23')
q24 = State('Q24')
q25 = State('Q25')
q26 = State('Q26')
q27 = State('Q27')
q28 = State('Q28')
q29 = State('Q29')
q30 = State('Q30')

qo.addTransition(' ', q0, 'ID\n')
qo.addTransition('(', qlparen, 'ID\n')
qo.addTransition(')', qrparen, 'ID\n')
qo.addTransition(',', q0, 'ID\nCOMMA\n')
qo.addTransition(';', q0, 'ID\nSEMICOLON\n')

q0.addTransition('e', q1, '')  # ELSE
q0.addTransition('i', q2, '')  # INT/IF
q0.addTransition('r', q3, '')  # RETURN
q0.addTransition('v', q4, '')  # VOID
q0.addTransition('w', q5, '')  # WHILE
q0.addTransition('f', q24, '')  # FLOAT/FOR
q0.addTransition(' ', q0, '')
q0.addTransition('\n', q0, '')
q0.addTransition('+', q0, 'PLUS\n')
q0.addTransition('-', q0, 'MINUS\n')
q0.addTransition('-', q0, 'MINUS\n')
q0.addTransition('*', q0, 'TIMES\n')
q0.addTransition('/', q0, 'DIVIDE\n')
q0.addTransition('(', q0, 'LPAREN\n')
q0.addTransition(')', q0, 'RPAREN\n')
q0.addTransition('[', q0, 'LBRACKETS\n')
q0.addTransition(']', q0, 'RBRACKETS\n')
q0.addTransition('{', q0, 'LBRACES\n')
q0.addTransition('}', q0, 'RBRACES\n')
q0.addTransition(';', q0, 'SEMICOLON\n')
q0.addTransition(',', q0, 'COMMA\n')
q0.addTransition('=', qequal, '')
q0.addTransition('<', qlessequal, '')
q0.addTransition('>', qgreaterequal, '')
q0.addTransition('!', qdifferent, '')
for i in range(0, 10):
    q0.addTransition(str(i), qnumber, '')

# ---------- ELSE ---------- #

q1.addTransition('l', q6, '')  # ELSE - consumindo o L
q1.addTransition(' ', q0, 'ID\n')
q1.addTransition(',', q0, 'ID\nCOMMA\n')
q1.addTransition('(', qlparen, 'ID\n')

q6.addTransition('s', q7, '')  # ELSE - consumindo o S
q6.addTransition(' ', q0, 'ID\n')
q6.addTransition(',', q0, 'ID\nCOMMA\n')
q6.addTransition('(', qlparen, 'ID\n')

q7.addTransition('e', q8, '')  # ELSE - consumindo o último E
q7.addTransition(',', q0, 'ID\nCOMMA\n')
q7.addTransition(' ', q0, 'ID\n')
q7.addTransition('(', qlparen, 'ID\n')

q8.addTransition('{', q0, 'ELSE\nLBRACES\n')
q8.addTransition(' ', q0, 'ELSE\n')
q8.addTransition('\n', q0, 'ELSE\n')

# ---------- INT/IF ---------- #

q2.addTransition('n', q9, '')  # INT - consumindo o N
q2.addTransition('f', q11, '')  # IF - consumindo o F
q2.addTransition(' ', q0, 'ID\n')
q2.addTransition(',', q0, 'ID\nCOMMA\n')

# ---------- INT ---------- #

q9.addTransition('t', q10, '')  # INT - consumindo o T
q9.addTransition(' ', q0, 'ID\n')
q9.addTransition(',', q0, 'ID\nCOMMA\n')

q10.addTransition(' ', q0, 'INT\n')

# ---------- IF ---------- #

q11.addTransition(' ', q0, 'IF\n')
q11.addTransition('(', qlparen, 'IF\n')

# ---------- RETURN ---------- #

q3.addTransition('e', q19, '')  # RETURN - consumindo o E
q3.addTransition(' ', q0, 'ID\n')
q3.addTransition(',', q0, 'ID\nCOMMA\n')

q19.addTransition('t', q20, '')  # RETURN - consumindo o T
q19.addTransition(' ', q0, 'ID\n')
q19.addTransition(',', q0, 'ID\nCOMMA\n')

q20.addTransition('u', q21, '')  # RETURN - consumindo o U
q20.addTransition(' ', q0, 'ID\n')
q20.addTransition(',', q0, 'ID\nCOMMA\n')

q21.addTransition('r', q22, '')  # RETURN - consumindo o R
q21.addTransition(' ', q0, 'ID\n')
q21.addTransition(',', q0, 'ID\nCOMMA\n')

q22.addTransition('n', q23, '')  # RETURN - consumindo o N
q22.addTransition(' ', q0, 'ID\n')
q22.addTransition(',', q0, 'ID\nCOMMA\n')

q23.addTransition(' ', q0, 'RETURN\n')
q23.addTransition('(', qlparen, 'RETURN\n')

# ---------- VOID ---------- #

q4.addTransition('o', q12, '')  # VOID - consumindo o O
q4.addTransition(' ', q0, 'ID\n')
q4.addTransition(',', q0, 'ID\nCOMMA\n')

q12.addTransition('i', q13, '')  # VOID - consumindo o I
q12.addTransition(' ', q0, 'ID\n')
q12.addTransition(',', q0, 'ID\nCOMMA\n')

q13.addTransition('d', q14, '')  # VOID - consumindo o D
q13.addTransition(' ', q0, 'ID\n')
q13.addTransition(',', q0, 'ID\nCOMMA\n')

q14.addTransition(' ', q0, 'VOID\n')
q14.addTransition(')', qrparen, 'VOID\n')

# ---------- WHILE ---------- #

q5.addTransition('h', q15, '')  # WHILE - consumindo o H
q5.addTransition(' ', q0, 'ID\n')
q5.addTransition(',', q0, 'ID\nCOMMA\n')

q15.addTransition('i', q16, '')  # WHILE - consumindo o I
q15.addTransition(' ', q0, 'ID\n')
q15.addTransition(',', q0, 'ID\nCOMMA\n')

q16.addTransition('l', q17, '')  # WHILE - consumindo o L
q16.addTransition(' ', q0, 'ID\n')
q16.addTransition(',', q0, 'ID\nCOMMA\n')

q17.addTransition('e', q18, '')  # WHILE - consumindo o E
q17.addTransition(' ', q0, 'ID\n')
q17.addTransition(',', q0, 'ID\nCOMMA\n')

q18.addTransition(' ', q0, 'WHILE\n')
q18.addTransition('(', qlparen, 'WHILE\n')

# ---------- FLOAT ---------- #

q24.addTransition('l', q25, '')  # FLOAT - consumindo o L
q24.addTransition('o', q29, '')  # FOR - consumindo o O
q24.addTransition(' ', q0, 'ID\n')
q24.addTransition(',', q0, 'ID\nCOMMA\n')

q25.addTransition('o', q26, '')  # FLOAT - consumindo o O
q25.addTransition(' ', q0, 'ID\n')
q25.addTransition(',', q0, 'ID\nCOMMA\n')

q26.addTransition('a', q27, '')  # FLOAT - consumindo o A
q26.addTransition(' ', q0, 'ID\n')
q26.addTransition(',', q0, 'ID\nCOMMA\n')

q27.addTransition('t', q28, '')  # FLOAT - consumindo o T
q27.addTransition(' ', q0, 'ID\n')
q27.addTransition(',', q0, 'ID\nCOMMA\n')

q28.addTransition(' ', q0, 'FLOAT\n')

# ---------- FOR ---------- #

q29.addTransition('r', q30, '')  # FOR - consumindo o R
q29.addTransition(' ', q0, 'ID\n')
q29.addTransition(',', q0, 'ID\nCOMMA\n')

q30.addTransition(' ', q0, 'FOR\n')
q30.addTransition('(', qlparen, 'FOR\n')


qlparen.addTransition('a', qo, 'LPAREN\n')
qlparen.addTransition('b', qo, 'LPAREN\n')
qlparen.addTransition('c', qo, 'LPAREN\n')
qlparen.addTransition('d', qo, 'LPAREN\n')
qlparen.addTransition('e', qo, 'LPAREN\n')
qlparen.addTransition('f', q24, 'LPAREN\n')  # FLOAT
qlparen.addTransition('g', qo, 'LPAREN\n')
qlparen.addTransition('h', qo, 'LPAREN\n')
qlparen.addTransition('i', q2, 'LPAREN\n')  # INT/IF
qlparen.addTransition('j', qo, 'LPAREN\n')
qlparen.addTransition('k', qo, 'LPAREN\n')
qlparen.addTransition('l', qo, 'LPAREN\n')
qlparen.addTransition('m', qo, 'LPAREN\n')
qlparen.addTransition('n', qo, 'LPAREN\n')
qlparen.addTransition('o', qo, 'LPAREN\n')
qlparen.addTransition('p', qo, 'LPAREN\n')
qlparen.addTransition('q', qo, 'LPAREN\n')
qlparen.addTransition('r', qo, 'LPAREN\n')
qlparen.addTransition('s', qo, 'LPAREN\n')
qlparen.addTransition('t', qo, 'LPAREN\n')
qlparen.addTransition('u', qo, 'LPAREN\n')
qlparen.addTransition('v', q4, 'LPAREN\n')  # VOID
qlparen.addTransition('w', qo, 'LPAREN\n')
qlparen.addTransition('x', qo, 'LPAREN\n')
qlparen.addTransition('y', qo, 'LPAREN\n')
qlparen.addTransition('z', qo, 'LPAREN\n')
qlparen.addTransition(' ', q0, 'LPAREN\n')
qlparen.addTransition('+', q0, 'LPAREN\n')
qlparen.addTransition('-', q0, 'LPAREN\n')
qlparen.addTransition('*', q0, 'LPAREN\n')
qlparen.addTransition('/', q0, 'LPAREN\n')
qlparen.addTransition('(', q0, 'LPAREN\n')
qlparen.addTransition(')', q0, 'LPAREN\n')
qlparen.addTransition('[', q0, 'LPAREN\n')
qlparen.addTransition(']', q0, 'LPAREN\n')
qlparen.addTransition('{', q0, 'LPAREN\n')
qlparen.addTransition('}', q0, 'LPAREN\n')
qlparen.addTransition(';', q0, 'LPAREN\n')
qlparen.addTransition(',', q0, 'LPAREN\n')
for i in range(0, 10):
    qlparen.addTransition(str(i), qnumber, 'LPAREN\n')

qlbraces.addTransition('a', qo, 'LBRACES\n')
qlbraces.addTransition('b', qo, 'LBRACES\n')
qlbraces.addTransition('c', qo, 'LBRACES\n')
qlbraces.addTransition('d', qo, 'LBRACES\n')
qlbraces.addTransition('e', qo, 'LBRACES\n')
qlbraces.addTransition('f', qo, 'LBRACES\n')
qlbraces.addTransition('g', qo, 'LBRACES\n')
qlbraces.addTransition('h', qo, 'LBRACES\n')
qlbraces.addTransition('i', qo, 'LBRACES\n')
qlbraces.addTransition('j', qo, 'LBRACES\n')
qlbraces.addTransition('k', qo, 'LBRACES\n')
qlbraces.addTransition('l', qo, 'LBRACES\n')
qlbraces.addTransition('m', qo, 'LBRACES\n')
qlbraces.addTransition('n', qo, 'LBRACES\n')
qlbraces.addTransition('o', qo, 'LBRACES\n')
qlbraces.addTransition('p', qo, 'LBRACES\n')
qlbraces.addTransition('q', qo, 'LBRACES\n')
qlbraces.addTransition('r', qo, 'LBRACES\n')
qlbraces.addTransition('s', qo, 'LBRACES\n')
qlbraces.addTransition('t', qo, 'LBRACES\n')
qlbraces.addTransition('u', qo, 'LBRACES\n')
qlbraces.addTransition('v', qo, 'LBRACES\n')
qlbraces.addTransition('w', qo, 'LBRACES\n')
qlbraces.addTransition('x', qo, 'LBRACES\n')
qlbraces.addTransition('y', qo, 'LBRACES\n')
qlbraces.addTransition('z', qo, 'LBRACES\n')
qlbraces.addTransition(' ', q0, 'LBRACES\n')
qlbraces.addTransition('+', q0, 'LBRACES\n')
qlbraces.addTransition('-', q0, 'LBRACES\n')
qlbraces.addTransition('*', q0, 'LBRACES\n')
qlbraces.addTransition('/', q0, 'LBRACES\n')
qlbraces.addTransition('(', q0, 'LBRACES\n')
qlbraces.addTransition(')', q0, 'LBRACES\n')
qlbraces.addTransition('[', q0, 'LBRACES\n')
qlbraces.addTransition(']', q0, 'LBRACES\n')
qlbraces.addTransition('{', q0, 'LBRACES\n')
qlbraces.addTransition('}', q0, 'LBRACES\n')
qlbraces.addTransition(';', q0, 'LBRACES\n')
qlbraces.addTransition(',', q0, 'LBRACES\n')

qrparen.addTransition('a', qo, 'RPAREN\n')
qrparen.addTransition('b', qo, 'RPAREN\n')
qrparen.addTransition('c', qo, 'RPAREN\n')
qrparen.addTransition('d', qo, 'RPAREN\n')
qrparen.addTransition('e', qo, 'RPAREN\n')
qrparen.addTransition('f', qo, 'RPAREN\n')
qrparen.addTransition('g', qo, 'RPAREN\n')
qrparen.addTransition('h', qo, 'RPAREN\n')
qrparen.addTransition('i', qo, 'RPAREN\n')
qrparen.addTransition('j', qo, 'RPAREN\n')
qrparen.addTransition('k', qo, 'RPAREN\n')
qrparen.addTransition('l', qo, 'RPAREN\n')
qrparen.addTransition('m', qo, 'RPAREN\n')
qrparen.addTransition('n', qo, 'RPAREN\n')
qrparen.addTransition('o', qo, 'RPAREN\n')
qrparen.addTransition('p', qo, 'RPAREN\n')
qrparen.addTransition('q', qo, 'RPAREN\n')
qrparen.addTransition('r', qo, 'RPAREN\n')
qrparen.addTransition('s', qo, 'RPAREN\n')
qrparen.addTransition('t', qo, 'RPAREN\n')
qrparen.addTransition('u', qo, 'RPAREN\n')
qrparen.addTransition('v', qo, 'RPAREN\n')
qrparen.addTransition('w', qo, 'RPAREN\n')
qrparen.addTransition('x', qo, 'RPAREN\n')
qrparen.addTransition('y', qo, 'RPAREN\n')
qrparen.addTransition('z', qo, 'RPAREN\n')
qrparen.addTransition(' ', q0, 'RPAREN\n')
qrparen.addTransition('+', q0, 'RPAREN\n')
qrparen.addTransition('-', q0, 'RPAREN\n')
qrparen.addTransition('*', q0, 'RPAREN\n')
qrparen.addTransition('/', q0, 'RPAREN\n')
qrparen.addTransition('(', q0, 'RPAREN\n')
qrparen.addTransition(')', q0, 'RPAREN\n')
qrparen.addTransition('[', q0, 'RPAREN\n')
qrparen.addTransition(']', q0, 'RPAREN\n')
qrparen.addTransition('{', q0, 'RPAREN\nLBRACES\n')  # Será que era melhor criar uma estado para fazer isso?
qrparen.addTransition('}', q0, 'RPAREN\n')
qrparen.addTransition(';', q0, 'RPAREN\nSEMICOLON\n')
qrparen.addTransition(',', q0, 'RPAREN\n')

for i in range(0, 10):
    qnumber.addTransition(str(i), qnumber, '')
qnumber.addTransition('.', qnumber, '')
qnumber.addTransition(' ', q0, 'NUMBER\n')
qnumber.addTransition(',', q0, 'NUMBER\nCOMMA\n')
qnumber.addTransition(')', q0, 'NUMBER\nRPAREN\n')
qnumber.addTransition(';', q0, 'NUMBER\nSEMICOLON\n')

qlessequal.addTransition(' ', q0, 'LESS\n')
qlessequal.addTransition('=', q0, 'LESS_EQUAL\n')

qgreaterequal.addTransition(' ', q0, 'GREATER\n')
qgreaterequal.addTransition('=', q0, 'GREATER_EQUAL\n')

qequal.addTransition(' ', q0, 'ATTRIBUTION\n')
qequal.addTransition('=', q0, 'EQUALS\n')

qdifferent.addTransition('=', q0, 'DIFFERENT\n')
