#include <stdio.h>
#include <stdint.h> // Untuk uint32_t

// Definisi func2: menambahkan 3 ke param
uint32_t func2(uint32_t x) {
    return x + 3;
}

// Definisi func1 sesuai loop yang kamu kasih
uint32_t func1(uint32_t param_1) {
    uint32_t local_14;
    uint32_t local_4 = 0;

    for (local_14 = param_1; local_14 != 0; local_14 = local_14 >> 1) {
        if ((local_14 & 1) != 0) {
            local_4 = func2(local_4);
        }
    }

    return local_4;
}

int main() {
    uint32_t input;
    printf("Masukkan angka (uint32): ");
    scanf("%u", &input);

    uint32_t result = func1(input);
    printf("Hasil func1(%u) = %u\n", input, result);

    return 0;
}

