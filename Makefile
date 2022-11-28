ALL := collisions.txt collisions.pdf

.PHONY: all clean


all: $(ALL)

clean:
	@rm -f $(ALL)


collisions.txt:
	@./run-collide.py -o $@

collisions.pdf: plot-collisions.gp collisions.txt
	@gnuplot							\
		-e 'OUT_FILE="$@"'				\
		-e 'IN_FILE="$(word 2, $^)"'	\
		$(word 1, $^)
