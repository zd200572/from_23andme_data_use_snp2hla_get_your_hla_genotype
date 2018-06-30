########get##result##from##SNP2HLA####################


def get_sample_id(fin):
	with open(fin) as f:
		HLA_type = {}
		hla_id = {}
		i = 0
		for line in f:
			if i == 1:
				#print(line)
				#break
				j = 2
				#print(len(line.strip().split(' ')))
				for j in range(2, len(line.strip().split(' '))):
					#print(j)
					sample_id = line.strip().split(' ')[j]
					#print(sample_id)
					HLA_type[sample_id] = []
					hla_id[sample_id] = j
			i += 1
		#print(hla_id)
	return HLA_type, hla_id


def get_HLA_typing_result(fin, HLA_type, hla_id):
	#print(hla_id)
	new_dict = {v:k for k,v in hla_id.items()} 
	fout = open('HLA-result.txt', 'w')
	i = 0
	j = 0
	for j in hla_id.values(): #range(2, len(HLA_type)):
		with open(fin) as f:
			if j in hla_id.values():
				print(j, new_dict[j])
				#break
				fout.write(str(new_dict.get(j)) + '\t' + '\n')
			#print(j)
			#HLA_allele = []
			for line in f:
				''' if i == 1: #print(line) #break #print(len(line.strip().split(' '))) for j in range(2, len(line.strip().split(' '))): sample_id = line.strip().split(' ')[j] #print(sample_id) HLA_type[sample_id] = [] hla_id[sample_id] = j '''
				sub_line = line.strip().split(' ')
				#if i <= 16:
				#	print(sub_line[1])
				#break
				#print(j)
				if 'HLA' in sub_line[1] and sub_line[j - 1] == 'P':
					#print(sub_line[1])
					fout.write('\t' + sub_line[1] + '\n')
					#HLA_type[hla_id.get(j)].append(sub_line[1])
				if 'HLA' in sub_line[1] and sub_line[j] == 'P':
					fout.write('\t' + sub_line[1] + '\n')
					#print(sub_line[1])
					#HLA_type[hla_id.get(j)].append(sub_line[1])
					print(hla_id.get(j), HLA_allele)
				i += 1
			#HLA_type[hla_id.get(j)] = HLA_allele
		
					#break
							
					
			#j += 1
			fout.write('\n')
			print(HLA_type)
	fout.close()



