from validate_docbr import CPF # validate_docbr baixando via pip

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida.")

    def format_cpf(self):
        fatia_um     = self.cpf[:3]
        fatia_dois   = self.cpf[3:6]
        fatia_tres   = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]

        return "{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)

    def __str__(self):
        return self.format_cpf()