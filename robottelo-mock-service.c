#include <robottelo-mock-service.h>

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>


int main(int argc, char** argv) {
    char buff[100];
    time_t now = time (0);
    strftime (buff, 100, "%Y-%m-%d %H:%M:%S.000", localtime (&now));
    printf("robottelo mock service started at: %s\n", buff);
    fflush(NULL);

    if (write_to_file() != 0) {
        fprintf(stderr, "%s", "An error occured during the file creation!\n");
        return(EXIT_FAILURE);
    };

    for(;;) {
        sleep(5);
    };
    return (EXIT_SUCCESS);
}

