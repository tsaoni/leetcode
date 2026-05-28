I ?= 

OBJECTS = test.o 

all: test 

test: $(OBJECTS)
	g++ $< -o $@ 

test.o: $(I).cpp 
	g++ -std=c++11 -c $< -o $@ 

clean: 
	rm -rf *.o test