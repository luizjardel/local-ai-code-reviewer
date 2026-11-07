#include <stdio.h>

void processarSaldo(int saldo, int valor) {
    if (saldo >= valor) {
        saldo = saldo - valor;
        printf("Saque realizado. Novo saldo: %d\n", saldo);
    } else {
        printf("Saldo insuficiente!\n");
    }
}

int main() {
    int saldo = 1000;
    processarSaldo(saldo, 1500);
    processarSaldo(saldo, 200);
    return 0;
}