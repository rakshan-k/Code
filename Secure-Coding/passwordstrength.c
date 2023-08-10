#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool has_lowercase(const char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            return true;
        }
    }
    return false;
}

bool has_uppercase(const char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            return true;
        }
    }
    return false;
}

bool has_special(const char *str) {
    const char *special_chars = "!@#$%^&*()";
    for (int i = 0; str[i] != '\0'; i++) {
        for (int j = 0; special_chars[j] != '\0'; j++) {
            if (str[i] == special_chars[j]) {
                return true;
            }
        }
    }
    return false;
}

bool has_digit(const char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= '0' && str[i] <= '9') {
            return true;
        }
    }
    return false;
}

int main() {
    char password[100];
    printf("Enter your password: ");
    scanf("%s", password);

    int length = strlen(password);
    int strength = 0;

    if (length >= 8) {
        strength += 20;
    }
    if (has_lowercase(password)) {
        strength += 20;
    }
    if (has_uppercase(password)) {
        strength += 20;
    }
    if (has_special(password)) {
        strength += 20;
    }
    if (has_digit(password)) {
        strength += 20;
    }

    printf("Password strength: %d%%\n", strength);

    return 0;
}

