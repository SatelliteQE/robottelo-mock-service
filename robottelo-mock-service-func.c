#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <robottelo-mock-service.h>

int write_to_file() {
    char *cmd = "rpm -q robottelo-mock-service --queryformat='%{version}'";    
    
    char buf[BUFSIZE];
    FILE *fp;

    if ((fp = popen(cmd, "r")) == NULL) {
        printf("Error opening pipe!\n");
        return -1;
    }

    while (fgets(buf, BUFSIZE, fp) != NULL) {
        struct stat st = {0};

        if (stat("/var/log/robottelo-mock-service", &st) == -1) {
            mkdir("/var/log/robottelo-mock-service", 0700);
        }
        printf("robottelo-mock-service version %s", buf);
        FILE *fo;
        fo = fopen("/var/log/robottelo-mock-service/service.log", "w");
        fprintf(fo, "%s", buf);
        fclose(fo);
    }

    if (pclose(fp)) {
        printf("Command not found or exited with error status\n");
        return -1;
    }

    return 0;
}
