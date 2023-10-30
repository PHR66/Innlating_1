"""Innlating 1"""
try:
	s=int(input("Skriva eitt fimm siffrað positivt heiltal:"))
except:
	print('Error')
else:

	if s < 10000:
		print('Skriva eitt positiv fimmsifrað heiltal')
	else:
		s = str(s)
		for i in s.split():
			j = '   '.join(i)
			#print('   '.join(i))
			print(s + ' >> ' + j)


#s=input("Skriva eitt fimm siffrað positivt heiltal:")
#if s.isdigit()==True and len(s)==5:
	#print(s)
#	for i in s.split():
#		j = '   '.join(i)
		#print('   '.join(i))
#		print(s + ' >> ' + j)
#else: 
#	print("Talið skal vera positvt og fimm siffur")



