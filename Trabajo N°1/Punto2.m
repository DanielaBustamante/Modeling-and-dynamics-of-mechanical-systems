clear clc 

syms x y z

disp('Sean las siguientes matrices:') 

A=[0,4,-7,5;4,0,-1,0;6,4,-6,8;-2,2,6,9]

B=[2,4,-7,5;4,0,-1,0;6,4,-6,8;-2,-4,7,-5]

C=[2,4,-7,0;4,3,-1,0;6,4,-6,0;-2,2,6,0]

% ¿Qué condición se debe dar para que en una matriz exista el determinante? 
% Para que una matriz cuadrada tenga determinante, se requiere que la matriz sea no singular, es decir, que su determinante sea diferente de cero.
disp('Obtener el determinante de cada matriz')

disp('El determinante de A es:')
det(A)

disp('El determinante de B es:') 
det(B)

disp('El determinante de C es:') 
det(C)

% Con el resultado obtenido, ¿Es posible obtener la matriz inversa?  
% Si es distinto de 0 podemos calcular la matriz inversa

disp('Calculamos la inversa de A:')
inv(A)

disp('La inversa de B y C no se pueden hacer debido a que el resultado de su matriz da 0')

% b) Si no es posible, ¿qué habría que modificar para que sea posible? Si es así modificarlo. Justificar.  
% ara hacer que una matriz sea invertible, debemos modificarla para que tenga un determinante distinto de cero. Esto se puede lograr agregando o eliminando filas o columnas según sea necesario.

% c) Calcular la traspuesta y la inversa de cada matriz.   

% Dejando la ultima fila toda positiva:
B_nueva=[2,4,-7,5;4,0,-1,0;6,4,-6,8;2,4,7,5]
disp('La traspuesta de la nueva matriz B es')
transpose(B_nueva)
disp('La inversa de la nueva matriz B es')
inv(B_nueva)

% Cambiando la columna de ceros por 1:
C_nueva=[2,4,-7,1;4,3,-1,1;6,4,-6,1;-2,2,6,1]
disp('La tranpuesta de la nueva matriz C es')
transpose(C_nueva)
disp('La inversa de la nueva matriz C es')
inv(C_nueva)

% d) Obtener los siguientes vectores fila de cada matriz:   

% d1=[diagonal principal]  
disp('La diagonal principal de A es')
diag(A)
disp('La diagonal principal de B_nueva es')
diag(B_nueva)
disp('La diagonal principal de C_nueva es')
diag(C_nueva)

% d2=[fila 3]  
disp('La fila 3 de A es')
A(3,:)
disp('La fila 3 de B_nueva es')
B_nueva(3,:)
disp('La fila 3 de C_nueva es')
C_nueva(3,:)

% d3=[columna 3]  
disp('La columna 3 de A es')
A(:,3)
disp('La columna 3 de B_nueva es')
B_nueva(:,3)
disp('La columna 3 de B_nueva es')
C_nueva(:,3)

% e) Obtener las siguientes matrices de cada matriz:   

% e1=[filas 1 y 2 x columnas 2 y 3]  
disp('Las filas 1 y 2: de cada matriz')
A_filas1y2 = vertcat(A(1,:), A(2,:))
B_nueva_filas1y2 = vertcat(B_nueva(1,:), B_nueva(2,:))
C_nueva_filas1y2 = vertcat(C_nueva(1,:), C_nueva(2,:))
disp('Las columnas 2 y 3 de cada matriz:')
A_columnas2y3 = horzcat(A(:,2), A(:,3))
B_nueva_columnas2y3 = horzcat(B_nueva(:,2), B_nueva(:,3))
C_nueva_columnas2y3 = horzcat(C_nueva(:,2), C_nueva(:,3))
disp('Las matrices obtenidas de multiplicar las filas 1 y 2 por columnas 2 y 3:')
Matriz1=A_filas1y2*A_columnas2y3
Matriz2=B_nueva_filas1y2*B_nueva_columnas2y3
Matriz3=C_nueva_filas1y2*C_nueva_columnas2y3

% e2=[filas 3 y 4 x columnas 2 y 3] 
disp('Las filas 3 y 4: de cada matriz')
A_filas3y4 = vertcat(A(3,:), A(4,:))
B_nueva_filas3y4 = vertcat(B_nueva(3,:), B_nueva(4,:))
C_nueva_filas3y4 = vertcat(C_nueva(3,:), C_nueva(4,:))
disp('Las matrices obtenidas de multiplicar las filas 1 y 2 por columnas 2 y 3:')
Matriz4=A_filas3y4*A_columnas2y3
Matriz5=B_nueva_filas3y4*B_nueva_columnas2y3
Matriz6=C_nueva_filas3y4*C_nueva_columnas2y3

% e3=[columnas 1 y 4 x filas 3 y 4 ] 
disp('Las columnas 3 y 4 de cada matriz:')
A_columnas1y4 = horzcat(A(:,1), A(:,4))
B_nueva_columnas1y4 = horzcat(B_nueva(:,1), B_nueva(:,4))
C_nueva_columnas1y4 = horzcat(C_nueva(:,1), C_nueva(:,4))
disp('Las filas 3 y 4: de cada matriz')
A_filas3y4 = vertcat(A(3,:), A(4,:))
B_nueva_filas3y4 = vertcat(B_nueva(3,:), B_nueva(4,:))
C_nueva_filas3y4 = vertcat(C_nueva(3,:), C_nueva(4,:))
disp('Las matrices obtenidas de multiplicar las filas 1 y 2 por columnas 2 y 3:')
Matriz7=A_filas3y4*A_columnas1y4
Matriz8=B_nueva_filas3y4*B_nueva_columnas1y4
Matriz9=C_nueva_filas3y4*C_nueva_columnas1y4
