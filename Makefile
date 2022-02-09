
DESTDIR?=

CC=gcc
CFLAGS=-I.

RMS=robottelo-mock-service

DEPS = robottelo-mock-service.h
OBJ = robottelo-mock-service.o robottelo-mock-service-func.o 

# Directories for installation
BINDIR	= $(DESTDIR)/usr/bin
# all dirs
DIRS		= $(BINDIR)

# INSTALL scripts 
INSTALL         = install -p --verbose
INSTALL_BIN     = $(INSTALL) -m 755
INSTALL_DIR     = $(INSTALL) -m 755 -d

all:: $(RMS)

$(DIRS):
	@$(INSTALL_DIR) $@

install:: all $(DIRS)
	$(INSTALL_BIN) $(RMS) $(BINDIR)/$(RMS)

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(RMS): $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f *.o *~ core
