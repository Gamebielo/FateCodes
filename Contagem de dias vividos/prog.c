#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int dia;
    int mes;
    int ano;
} dma;

int main(int argc, char const *argv[])
{
    dma a;

    a.dia = atoi(argv[1]);
    a.mes = atoi(argv[2]) * 30;   // 30 dias em um mês
    a.ano = atoi(argv[3]) * 360;  // 360 dias em um mês

    int diaAtual, mesAtual, anoAtual, totalDias;

    diaAtual = atoi(argv[4]);
    mesAtual = atoi(argv[5]) * 30;
    anoAtual = atoi(argv[6]) * 360;

    totalDias = (diaAtual + mesAtual + anoAtual) - (a.dia + a.mes + a.ano);

    printf("Total de dias vividos: %d\n\n", totalDias);

    system("pause");
    return 0;
}
