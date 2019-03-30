/*
1.Defina um registro empregado para guardar os dados (nome, sobrenome, data de
nascimento, RG, data de admissão, salário) de um empregado de sua empresa.
Defina um vetor de empregados para armazenar todos os empregados de sua
empresa.
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct empregado
{
    char nome[20], sobrenome[20];
    char data_nasc[11], data_adm[11], rg[11];
    int salario;
} Empregado;

int main(void)
{
    int i;
    Empregado emp[2];

    for (i = 0; i < 2; i++)
    {
        printf("Empregado %d\nNome:", i+1);
        fgets(emp[i].nome, sizeof(emp[i].nome), stdin);
        fflush(stdin);
        printf("Sobrenome:");
        fgets(emp[i].sobrenome, sizeof(emp[i].sobrenome), stdin);
        fflush(stdin);
        printf("Data de Nascimento:");
        fgets(emp[i].data_nasc, sizeof(emp[i].data_nasc), stdin);
        fflush(stdin);
        printf("RG:");
        fgets(emp[i].rg, sizeof(emp[i].rg), stdin);
        fflush(stdin);
        printf("Data de Admissao:");
        fgets(emp[i].data_adm, sizeof(emp[i].data_adm), stdin);
        fflush(stdin);
        printf("Salario:");
        scanf("%d", &emp[i].salario);
        fflush(stdin);
        printf("\n");
    }

    printf("------EMPREGADOS------\n");

    for (i = 0; i < 2; i++)
    {
        printf("Empregado %d\n", i+1);
        printf("Nome: %s", emp[i].nome);
        printf("Sobrenome: %s", emp[i].sobrenome);
        printf("Data de Nascimento: %s\n", emp[i].data_nasc);
        printf("RG: %s", emp[i].rg);
        printf("Data de Admissao: %s\n", emp[i].data_adm);
        printf("Salario: %d\n", emp[i].salario);
        printf("\n");
    }

    system("pause");
    return 0;
}
