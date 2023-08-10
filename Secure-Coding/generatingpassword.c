#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Function to generate a random character from the given character set
char random_character(const char *charset) {
    int charset_length = strlen(charset);
    int random_index = rand() % charset_length;
    return charset[random_index];
}

int main() {
    srand(time(NULL)); // Seed the random number generator with the current time

    const char lowercase[] = "abcdefghijklmnopqrstuvwxyz";
    const char uppercase[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const char special_chars[] = "!@#$%^&*()";
    const char digits[] = "0123456789";

    int password_length;
    printf("Enter the length of the password: ");
    scanf("%d", &password_length);

    // Make sure the password length is at least 8
    if (password_length < 8) {
        printf("Password length should be at least 8 characters.\n");
        return 1;
    }

    // Build the character set for generating the password
    char charset[100];
    strcpy(charset, lowercase);
    strcat(charset, uppercase);
    strcat(charset, special_chars);
    strcat(charset, digits);

    printf("Generated password: ");
    for (int i = 0; i < password_length; i++) {
        putchar(random_character(charset));
    }
    printf("\n");

    return 0;
}

