inject.so: inject.c
	gcc -std=c99 -Wall -shared $(CFLAGS) -g -fPIC -Wl,--no-as-needed -ldl inject.c -o  inject.so

.PHONY: clean

clean:
	rm -f *.o *.so inject.so.*

test: inject.so
	./run_tests.sh
