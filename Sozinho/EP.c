#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    int n, pilhas, i;
    int vetor[52] = {100};

    scanf("%d", &n);    // Número de Cartas
    pilhas = n;        // Inicialmente num cartas == pilhas

    for (i = 0; i < n; i++)
        scanf("%d", &vetor[i]);

    for (i = 1; i <= n; i++)
    {
        if (i == n)
            break;
        if (pilhas == 1)
            break;
        if (vetor[i] != 0 && vetor[i] <= vetor[i-1])  // 'i-1' para não ir após o 'N'
        {
            //vetor[i] = 0;
            pilhas -= 1;
        }
    }

    printf("%d\n", pilhas);
    return 0;
}
