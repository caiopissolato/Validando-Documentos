from cpf_cnpj import Documento

cpf  = Documento.cria_documento("70095189807")
cnpj = Documento.cria_documento("35379838000112")

print(cnpj,"\n",cpf)