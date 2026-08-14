from pymol import cmd

model = cmd.get_model("all")

cmd.spectrum("b", selection="all")

cmd.do("select final, none")
tmp1 = 0
tmp2 = 0
countx = 0

for a in model.atom:
	if re.search("Y", a.chain):
		tmp1 = a.coord[1]
		tmp2 = a.coord[2]
		countx = countx + 1


for a in model.atom:
	if a.coord[2] > tmp2:
		tmp = a.index
		s = 'select test, index ' + repr(tmp)
		cmd.do(s)
		cmd.do("select final, test | final")

cmd.do("select finaly, none")
cmd.do("select test, none")
tmp1 = 0
tmp2 = 0
	
for a in model.atom:
	if a.coord[1] > tmp1:
		tmp = a.index
		s = 'select test, index ' + repr(tmp)
		cmd.do(s)
		cmd.do("select finaly, test | finaly")

tmp0 = 0
i = 0
centre_array = [0] * (countx * 100) 

# for a in model.atom:
# 	if re.search("Y", a.chain):
# 		tmp0 = a.coord[0]
# 		tmp_id = a.index
# 		centre_array[i] = tmp_id
# 		i = i + 1
# 		s3 = 'select '+repr(tmp_id)+', none'
# 		cmd.do(s3)
# 		for b in model.atom:
# 			if b.coord[0] <= tmp0 + 2 and b.coord[0] >= tmp0 - 2 and b.chain != "Y":
# 				tmp = b.index
# 				s = 'select test, index ' + repr(tmp)
# 				cmd.do(s)
# 				s2 = 'select '+ repr(tmp_id) +', test | ' + repr(tmp_id)
# 				cmd.do(s2)