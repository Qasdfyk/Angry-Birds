ftest: fractiontest.o fraction.o
	g++ -Wall -Wextra -Wpedantic -g fractiontest.o fraction.o -o ftest

fractiontest.o: fractiontest.cpp fraction.h
	g++ -Wall -Wextra -Wpedantic -g -c fractiontest.cpp -o fractiontest.o

fraction.o: fraction.cpp fraction.h
	g++ -Wall -Wextra -Wpedantic -g -c fraction.cpp -o fraction.o

clean: 
	rm ftest *.o

