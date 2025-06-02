from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Folha de Atividade - Modelagem de Dados Relacional", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.chapter_title("Contexto da Atividade")
pdf.chapter_body(
    "Imagine que você está desenvolvendo o banco de dados relacional para um sistema de reservas de hotel. "
    "O sistema deve atender às seguintes regras de negócio:\n\n"
    "1. Um hóspede pode fazer uma ou várias reservas.\n"
    "2. Cada reserva corresponde a apenas um quarto e é feita para um intervalo de datas (check-in e check-out).\n"
    "3. Cada quarto pertence a uma categoria (simples, duplo, suíte, etc.).\n"
    "4. O hotel possui diversos quartos.\n"
    "5. Cada hóspede deve ter um nome, CPF e telefone registrados.\n"
    "6. O sistema precisa permitir a análise de histórico de reservas por hóspede."
)

pdf.chapter_title("Instruções")
pdf.chapter_body(
    "Trabalho em grupo. Utilize caderno ou folhas de papel para rascunho e desenvolvimento. "
    "Recomenda-se o uso de ferramenta digital de modelagem (como Draw.io ou dbdiagram.io).\n"
    "Tempo estimado: 40 minutos.\n\n"
    "Passo 1: Identificação de Entidades e Atributos (10 min)\n"
    "- Liste as entidades principais do sistema (mínimo de 4).\n"
    "- Identifique os atributos essenciais de cada entidade.\n"
    "- Indique a chave primária de cada entidade.\n\n"
    "Passo 2: Definição de Relacionamentos (10 min)\n"
    "- Defina os relacionamentos entre as entidades.\n"
    "- Indique a cardinalidade (1:1, 1:N, N:M) e chaves estrangeiras.\n\n"
    "Passo 3: Aplicação de Normalização (10 min)\n"
    "- Modele as tabelas até a 3ª forma normal.\n"
    "- Justifique cada normalização realizada.\n\n"
    "Passo 4: Esboço do Modelo (10 min)\n"
    "- Faça um esboço do modelo relacional.\n"
    "- Represente entidades, atributos e relacionamentos."
)

pdf.chapter_title("Discussão Final (5 minutos)")
pdf.chapter_body(
    "Responda às perguntas abaixo com seu grupo:\n"
    "- Quais decisões foram mais difíceis no processo de modelagem?\n"
    "- Algum relacionamento foi difícil de representar?\n"
    "- Como a normalização melhorou a estrutura do seu modelo?"
)

pdf.chapter_title("Materiais Necessários")
pdf.chapter_body(
    "- Caderno ou folhas de rascunho\n"
    "- Caneta ou lápis\n"
    "- Computador com acesso a ferramentas de modelagem (opcional)"
)

pdf.output("Folha_de_Atividade_Modelagem_Dados.pdf")
