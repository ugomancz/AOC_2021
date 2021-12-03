#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "string.h"

#define LINE_LENGTH 12
#define LINES_COUNT 1000


void parse_line(int *counters, const char *line) {
    for (int i = 0; i < LINE_LENGTH; i++) {
        if (line[i] == '1') {
            ++(counters[i]);
            continue;
        }
        --(counters[i]);
    }
}

void clear_counters(int *counters) {
    memset(counters, 0, LINE_LENGTH * sizeof(int));
}

void read_lines(FILE *input, char **lines) {
    char *line = NULL;
    size_t len = 0;
    int lines_counter = 0;
    while (getline(&line, &len, input) != EOF) {
        line[strcspn(line, "\n\r")] = 0;
        lines[lines_counter] = calloc(20, sizeof(char));
        memcpy(lines[lines_counter], line, LINE_LENGTH);
        ++lines_counter;
    }
    if (line) {
        free(line);
    }
}

void parse_lines(char *const *lines, int *counters, const bool *in) {
    for (int i = 0; i < LINES_COUNT; ++i) {
        if (in[i]) {
            parse_line(counters, lines[i]);
        }
    }
}

int lines_in(const bool *in) {
    int count = 0;
    for (int i = 0; i < LINES_COUNT; ++i) {
        if (in[i]) {
            ++count;
        }
    }
    return count;
}

int to_int(const char *number) {
    int result = 0;
    for (int i = 0; i < LINE_LENGTH; ++i) {
        if (number[i] == '1') {
            result |= 1;
            result = result << 1;
            continue;
        }
        result &= 0xffe;
        result = result << 1;
    }
    return (result >> 1);
}

const char *get_last_line(char **lines, const bool *in) {
    for (int i = 0; i < LINES_COUNT; ++i) {
        if (in[i]) {
            return lines[i];
        }
    }
    return NULL;
}

int find_oxygen(char **lines, int *counters) {
    bool *in = malloc(LINES_COUNT);
    memset(in, true, LINES_COUNT);
    parse_lines(lines, counters, in);
    int bit_position = 0;
    while (lines_in(in) > 1 && bit_position <= 12) {
        if (counters[bit_position] >= 0) { // keep values with '1'
            for (int i = 0; i < LINES_COUNT; ++i) {
                if (lines[i][bit_position] != '1') {
                    in[i] = false;
                }
            }
        } else { // keep values with '0'
            for (int i = 0; i < LINES_COUNT; ++i) {
                if (lines[i][bit_position] != '0') {
                    in[i] = false;
                }
            }
        }
        clear_counters(counters);
        parse_lines(lines, counters, in);
        ++bit_position;
    }
    const char *last_line = get_last_line(lines, in);
    free(in);
    clear_counters(counters);
    return to_int(last_line);
}

int find_co(char **lines, int *counters) {
    bool *in = malloc(LINES_COUNT);
    memset(in, true, LINES_COUNT);
    parse_lines(lines, counters, in);
    int bit_position = 0;
    while (lines_in(in) > 1 && bit_position <= 12) {
        if (counters[bit_position] >= 0) { // keep values with '0'
            for (int i = 0; i < LINES_COUNT; ++i) {
                if (lines[i][bit_position] != '0') {
                    in[i] = false;
                }
            }
        } else { // keep values with '1'
            for (int i = 0; i < LINES_COUNT; ++i) {
                if (lines[i][bit_position] != '1') {
                    in[i] = false;
                }
            }
        }
        clear_counters(counters);
        parse_lines(lines, counters, in);
        ++bit_position;
    }
    const char *last_line = get_last_line(lines, in);
    free(in);
    return to_int(last_line);
}

int main() {
    FILE *input = fopen("../input.txt", "r");
    if (!input) {
        exit(EXIT_FAILURE);
    }
    char **lines = calloc(LINES_COUNT, sizeof(char *));
    int *counters = calloc(LINE_LENGTH, sizeof(int));
    read_lines(input, lines);
    int oxygen_levels = find_oxygen(lines, counters);
    int co_levels = find_co(lines, counters);
    printf("oxygen lvl: %d\n", oxygen_levels);
    printf("co lvl: %d\n", co_levels);
    printf("result: %d\n", oxygen_levels * co_levels);

    fclose(input);
    free(counters);
    exit(EXIT_SUCCESS);
}
