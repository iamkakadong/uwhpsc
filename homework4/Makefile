# $MYUWHPSC/homework4/Makefile

OBJECTS = quadrature.o test2.o
OBJECTS_OMP = quadrature_omp.o test2_omp.o
MODULES = quadrature.mod
MODULES_OMP = quadrature_omp.mod

FFLAGS = -g
OMPFLAGS = -fopenmp

.PHONY: test2 test2_omp clean

test2: test2.exe
	./test2.exe

test2_omp: test2_omp.exe
	./test2_omp.exe

test2.exe: $(MODULES) $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o test2.exe

test2_omp.exe: $(MODULES_OMP) $(OBJECTS_OMP)
	gfortran $(OMPFLAGS) $(OBJECTS_OMP) -o test2_omp.exe

%_omp.o: %_omp.f90
	gfortran $(OMPFLAGS) -c $<

%_omp.mod: %_omp.f90
	gfortran $(OMPFLAGS) -c $<

%.o: %.f90
	gfortran $(FFLAGS) -c $<

%.mod: %.f90
	gfortran $(FFLAGS) -c $<

clean:
	rm -f *.o *.exe *.mod