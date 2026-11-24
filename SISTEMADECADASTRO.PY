class Curso:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Disciplina(Curso):
    pass


class Professor:
    def __init__(self, nome, disciplina, curso):
        self.nome, self.disciplina, self.curso = nome, disciplina, curso

    def __str__(self):
        return f"{self.nome} | {self.disciplina} | {self.curso}"


class Aluno:
    def __init__(self, matricula, nome, curso, disciplina, media, situacao, aprovadas):
        self.dados = (
            f"[{matricula}] {nome} | {curso} | {disciplina} | "
            f"Média: {media:.1f} | {situacao} | "
            f"Aprovadas: {aprovadas} | Geral: {'Aprovado' if aprovadas >= 10 else 'Reprovado'}"
        )

    def __str__(self):
        return self.dados


class SistemaAcademico:
    def __init__(self):
        self.cursos, self.disciplinas, self.professores, self.alunos = [], [], [], []

    def cadastrar(self, tipo, *dados):
        lista = {
            "curso": self.cursos,
            "disciplina": self.disciplinas,
            "professor": self.professores,
        }[tipo]

        lista.append(Curso(dados[0]) if tipo == "curso" else
                     Disciplina(dados[0]) if tipo == "disciplina" else
                     Professor(*dados))

        print(f"{tipo.capitalize()} cadastrado!")

    def cadastrar_aluno(self, matricula, nome, curso, disciplina, n1, n2, aprovadas):
        media = (n1 + n2) / 2
        situacao = "Aprovado" if media >= 7 else "Reprovado"

        if 4 <= media < 7:
            media = (media + float(input("Nota da recuperação: "))) / 2
            situacao = "Aprovado" if media >= 5 else "Reprovado"

        aluno = Aluno(matricula, nome, curso, disciplina, media, situacao, aprovadas)
        self.alunos.append(aluno)
        print(aluno)

    # ==========================================
    # VISUALIZAÇÃO DOS DADOS
    # ==========================================

    def ver_dados(self):
        print("\n========== DADOS DO SISTEMA ==========")

        categorias = (
            ("CURSOS", self.cursos),
            ("DISCIPLINAS", self.disciplinas),
            ("PROFESSORES", self.professores),
            ("ALUNOS", self.alunos)
        )

        for titulo, lista in categorias:
            print(f"\n--- {titulo} ---")

            if lista:
                for numero, item in enumerate(lista, start=1):
                    print(f"{numero}. {item}")
            else:
                print("Nenhum cadastro realizado.")

        print("\n======================================")


# ==========================================
# CRIAÇÃO DO SISTEMA
# ==========================================

sistema = SistemaAcademico()


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:
    opcao = input(
        "\n1-Curso  2-Disciplina  3-Professor  "
        "4-Aluno  5-Ver dados  0-Sair: "
    )

    if opcao == "0":
        print("Sistema encerrado!")
        break

    elif opcao == "1":
        sistema.cadastrar("curso", input("Nome do curso: "))

    elif opcao == "2":
        sistema.cadastrar("disciplina", input("Nome da disciplina: "))

    elif opcao == "3":
        sistema.cadastrar(
            "professor",
            input("Nome: "),
            input("Disciplina: "),
            input("Curso: ")
        )

    elif opcao == "4":
        sistema.cadastrar_aluno(
            input("Matrícula: "),
            input("Nome: "),
            input("Curso: "),
            input("Disciplina: "),
            float(input("Nota 1: ")),
            float(input("Nota 2: ")),
            int(input("Matérias aprovadas: "))
        )

    elif opcao == "5":
        sistema.ver_dados()

    else:
        print("Opção inválida!")