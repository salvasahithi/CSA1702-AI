#include <stdio.h>
#include <string.h>
#include <ctype.h>
void generateKeyMatrix(char key[], char keyMatrix[5][5]) {
    char*alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    int i, j, len, k = 0, flag = 0;
    len = strlen(key);
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            if (k < len) {
                keyMatrix[i][j] = toupper(key[k++]);
            } else {
                while (strchr(keyMatrix[0], alpha[flag])) {
                    flag++;
                }
                keyMatrix[i][j] = alpha[flag++];
            }
        }
    }
}
void encrypt(char plaintext[], char keyMatrix[5][5]) {
    int i, j, row1, col1, row2, col2;
    char ciphertext[strlen(plaintext)];
    for (i = 0; i < strlen(plaintext); i += 2) {
        if (plaintext[i] == plaintext[i + 1]) {
            plaintext[i + 1] = 'X';
        }
        for (j = 0; j < 5; j++) {
            if (strchr(keyMatrix[j], plaintext[i])) {
                row1 = j;
                col1 = strchr(keyMatrix[j], plaintext[i]) - keyMatrix[j];
            }
            if (strchr(keyMatrix[j], plaintext[i + 1])) {
                row2 = j;
                col2 = strchr(keyMatrix[j], plaintext[i + 1]) - keyMatrix[j];
            }
        }
        if (row1 == row2) {
            col1 = (col1 + 1) % 5;
            col2 = (col2 + 1) % 5;
        } else if (col1 == col2) {
            row1 = (row1 + 1) % 5;
            row2 = (row2 + 1) % 5;
        } else {
            int temp = col1;
            col1 = col2;
            col2 = temp;
        }
        ciphertext[i] = keyMatrix[row1][col1];
        ciphertext[i + 1] = keyMatrix[row2][col2];
    }
    printf("Encrypted Text: %s\n", ciphertext);
}
int main() {
    char key[100], plaintext[100], keyMatrix[5][5];
    printf("Enter the key: ");
    scanf("%s", key);
    printf("Enter the plaintext: ");
    scanf("%s", plaintext);
    generateKeyMatrix(key, keyMatrix);
    encrypt(plaintext, keyMatrix);
}
