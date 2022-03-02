from cpf_cnpj import CpfCnpj

cpf1 = CpfCnpj("70095189807", "cpf")
#print(cpf1)
cnpj1 = "35379838000112"

documento = CpfCnpj(cnpj1, "cnpj")
print(documento,"\n",cpf1)