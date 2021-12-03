#include <stdio.h>
#include <stdlib.h>
#include "string.h"

#define LINE_LENGTH 12


void parse_line(int8_t *counters, const char *line) {
    for (int i = 0; i < LINE_LENGTH; i++) {
        if (line[i] == '1') {
            counters[i]++;
            continue;
        }
        counters[i]--;
    }
}

int get_gamma_rate(const int8_t *counters) {
    int result = 0;
    for (int i = 0; i < LINE_LENGTH; ++i) {
        if (counters[i] > 0) {
            result |= 1;
        } else {
            result |= 0;
        }
        result = result << 1;
    }
    result = result >> 1;
    return result;
}

int get_epsilon_rate(const int8_t *counters) {
    int result = 0;
    for (int i = 0; i < LINE_LENGTH; ++i) {
        if (counters[i] > 0) {
            result |= 0;
        } else {
            result |= 1;
        }
        result = result << 1;
    }
    result = result >> 1;
    return result;
}

void print_counters(const int8_t *counters) {
    printf("Counters: [");
    for (int i = 0; i < LINE_LENGTH - 1; ++i) {
        printf("%d, ", counters[i]);
    }
    printf("%d]\n", counters[LINE_LENGTH - 1]);
}

int main() {
    FILE *input = fopen("../input.txt", "r");
    if (!input) {
        exit(EXIT_FAILURE);
    }
    char *line = NULL;
    size_t len = 0;
    int8_t *counters = calloc(LINE_LENGTH, sizeof(int8_t));
    while (getline(&line, &len, input) != EOF) {
        line[strcspn(line, "\n\r")] = 0;
        parse_line(counters, line);
    }
    print_counters(counters);
    int gamma_rate = get_gamma_rate(counters);
    int epsilon_rate = get_epsilon_rate(counters);
    printf("gamma_rate: %d\nepsilon_rate: %d\nresult: %d", gamma_rate, epsilon_rate, gamma_rate * epsilon_rate);
    fclose(input);
    if (line) {
        free(line);
    }
    free(counters);
    exit(EXIT_SUCCESS);
}
