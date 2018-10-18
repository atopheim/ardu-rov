BUILDROOTDIR := .
TARGETDIR := ./executables
CC := $(BUILDROOTDIR)/g++ 

all:
	$(CC) -std=c++11 *.cpp `pkg-config --libs --cflags opencv` -o fresh.out

clean:
	rm rf *.o *~ core .depend .*.cmd *.ko *.mod.c .tmp_versions

