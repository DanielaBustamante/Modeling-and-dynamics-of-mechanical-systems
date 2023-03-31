% Resolver los siguientes sistemas de forma matricial:
% Si no es posible resolver alguno de ellos, mencionar por qué. Justificar. 
% Efectuar un cambio en algún coeficiente para salvar esto y calcular. 
% Justificar el cambio. 

disp('4.*X.^2-7.*X.^3+5.*X.^4=2; 4.*X.^1-1.*X.^3=-5; 6.*X.^1+4.*X.^2-6.*X.^3+8.*X.^4=1; -2.*X.^1+2.*X.^2+6.*X.^3+9.*X.^4=9;')
% Armamos la matriz de los coeficientes
A=[0,4,-7,5;4,0,-1,0;6,4,-6,8;-2,2,6,9]
% Armamos el vector
A_vector=[2;-5;1;9]
disp('Calculamos el determinante de la matriz de los coeficientes')
Det=det(A)
disp('Calculamos la inversa')
%Como es distinto de 0 podemos calcular la matriz inversa
Ai=inv(A)
disp('Solucion del sistema')
%Calculo la solucion del sistema como Ai*B
Sol=Ai*A_vector

disp('2.*X.^1+4.*X.^2-7.*X.^3+5.*X.^4=8; 4.*X.^1-1.*X.^3=3; 6.*X.^1+4.*X.^2-6.*X.^3+8.*X.^4=-4; -2.*X.^1-4.*X.^2+7.*X.^3-5.*X.^4=-7')
B=[2,4,-7,5;4,0,-1,0;6,4,-6,8;-2,-4,7,-5]
% Armamos el vector
B_vector=[8;3;-4;-7]
disp('Calculamos el determinante de la matriz de los coeficientes')
Det=det(B)
disp('Calculamos la inversa')
%Como es distinto de 0 podemos calcular la matriz inversa
Bi=inv(B)
disp('Solucion del sistema')
%Calculo la solucion del sistema como Ai*B
Sol=Bi*B_vector