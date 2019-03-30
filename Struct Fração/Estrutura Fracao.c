#include <stdio.h>
#include <stdlib.h>

typedef struct{
        int den, num;
    } Fracao;

void reduz(Fracao a);
void exibefracao(Fracao a);
void somafracao(Fracao a, Fracao b);
void multiplica(Fracao a, Fracao b);
void subtrai(Fracao a, Fracao b);

int main()
{
    int i;
    Fracao a, b;

    printf("Fracao A (n/n):\n");
    scanf("%d/%d", &a.num, &a.den);
    printf("Fracao B (n/n):\n");
    scanf("%d/%d", &b.num, &b.den);

    somafracao(a, b);
    multiplica(a, b);
    subtrai(a, b);

    system("pause");
    return 0;
}
void reduz(Fracao a){
    int m = a.num, n = a.den;
    int resto = m % n;

    if (m == n){
        resto = m;
    }
    else{
        while(resto != 0){
        m = n;
        n = resto;
        resto = m % n;
        }
    }

    if(resto != 0){
            a.num = a.num/resto;
            a.den = a.den/resto;
        }

    exibefracao(a);
}

void exibefracao(Fracao a){
    printf("\n%d/%d\n", a.num, a.den);
}

void somafracao(Fracao a, Fracao b){
    int soma = 0;

    if (a.den == b.den){
        soma = a.num + b.num;
        a.num = soma;
        reduz(a);
    }
    else{
        soma = ((a.num*b.den) + (a.den*b.num));
        a.num = soma;
        a.den = a.den*b.den;
        reduz(a);
    }
}

void multiplica(Fracao a, Fracao b){
    a.num = a.num*b.num;
    a.den = a.den*b.den;
    reduz(a);
}

void subtrai(Fracao a, Fracao b){
     int soma = 0;

    if (a.den == b.den){
        soma = a.num - b.num;
        a.num = soma;
        reduz(a);
    }
    else{
        soma = ((a.num*b.den) - (a.den*b.num));
        a.num = soma;
        a.den = a.den*b.den;
        reduz(a);
    }
}
