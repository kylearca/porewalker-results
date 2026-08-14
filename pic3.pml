space rgb
bg_color white
hide everything, all
select axis, resi 0 & b > 0
show cartoon
show spheres, axis
run final_slice.py
color green, all
color blue, b>8
color orange, b>4 & b<5
color red, axis
show spheres, axis
show lines, axis
reset
turn z, 90
hide everything, !axis
show surface, !final
zoom complete = 1
ray 600, 600
png out1
hide surface, b>5 | b<4
ray 600, 600
png out1-pore
hide everything, !axis
turn y, 180
show surface, final
zoom complete = 1
ray 600, 600
png out2
hide surface, b>5 | b<4
ray 600, 600
png out2-pore
hide everything, !axis
turn y, 90
zoom complete = 1
show surface, finaly
ray 600, 600
png out3
hide surface, b>5 | b<4
ray 600, 600
png out3-pore
hide everything, !axis
turn y, 180
zoom complete = 1
show surface, !finaly
ray 600, 600
png out4
hide surface, b>5 | b<4
ray 600, 600
png out4-pore
quit
