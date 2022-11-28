set terminal pdfcairo enhanced font "Gill Sans, 16" linewidth 2 rounded dashed

set style line 80 lc rgb "#202020" lt 1 lw 0.5
# Border: 3 (X & Y axes)
set border 3 back ls 80

set style line 81 lc rgb "#808080" lt 1 lw 0.50 dt 3
set style line 82 lc rgb "#999999" lt 1 lw 0.10 dt 4

load 'Set1.plt'

set xtics border in scale 1,0.5 nomirror norotate autojustify
set ytics border in scale 1,0.5 nomirror norotate autojustify

set tics in

set xtics nomirror offset 0,0.2
set ytics nomirror offset 0.2,0

set grid xtics mxtics ytics mytics back ls 81, ls 82

set xtics font ',12'
set xlabel "Index" offset 0,0.5

set logscale y
set mytics 10
set ylabel "Access time (ms)" offset 2,0

# Pass the output file name via command-line arguments.
set output OUT_FILE
plot IN_FILE u 1:($2*1000) not w p ls 1 pt 6 ps 0.25
unset output
