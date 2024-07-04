from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from fpdf import FPDF


cnv = canvas.Canvas("MeuCurrículo.pdf")
largura_A4, altura_A4 = A4

content1 = [
    ["Formação Acadêmica","Bacharelado em Engenharia Biomédica \n - UFRN - Previsão de Conclusão: 2026","Bacharelado em Ciência e Tecnologia \n - UFRN - Conclusão: 2021"],
    ["Experiência","Monitor - UFRN - [Período das Monitorias]","Auxílio aos alunos em suas dúvidas e \n dificuldades nas disciplinas.","Preparação de materiais didáticos \n e suporte ao professor na correção de \n exercícios e provas.","Contribuição para o desenvolvimento de \n projetos acadêmicos relacionados às \n disciplinas."],
    ["Habilidades Técnicas","Python, C++, C#, HTML, CSS","Ferramentas de Desenvolvimento: \n [IDE's, plataformas de desenvolvimento, etc.]","Bancos de Dados: [SQL, NoSQL, etc.]"]
]


posicao_ret = 250
posicao1 = [0,altura_A4-100]


cnv.setFillColorRGB(0.2, 0.5, 0.8)
cnv.rect(0,0,posicao_ret,altura_A4, fill=True)





#for j in range(len(content)):
    
#   for i in range(len(content[j])):
#       posicao[1] = posicao[1]-25
#       cnv.setFillColorRGB(0, 0, 0)
#       if i == 0:
#           cnv.setFont("Helvetica-Bold", 12)
#           cnv.drawString(10, posicao[1], content[j][i])
#       else:
#           cnv.setFillColorRGB(0, 0, 0)
#           cnv.circle(10, posicao[1]+5, 2, fill=True)
#           content[j][i] = content[j][i].split("\n")
#           print(len(content[j][i]))
#           for k in range(len(content[j][i])):
#               cnv.setFillColorRGB(1, 1, 1)
#               cnv.setFont("Helvetica", 11)
#               cnv.drawString(20, posicao[1], content[j][i][k])
#               posicao[1] = posicao[1] - 15
#   posicao[1] = posicao[1] - 50
        

def Exibir(content, posicao):
    
    for j in range(len(content)):
        
        for i in range(len(content[j])):
            posicao[1] = posicao[1]-25
            cnv.setFillColorRGB(0, 0, 0)
            if i == 0:
                cnv.setFont("Helvetica-Bold", 12)
                cnv.drawString(10, posicao[1], content[j][i])
            else:
                cnv.setFillColorRGB(0, 0, 0)
                cnv.circle(10, posicao[1]+5, 2, fill=True)
                content[j][i] = content[j][i].split("\n")
                print(len(content[j][i]))
                for k in range(len(content[j][i])):
                    cnv.setFillColorRGB(1, 1, 1)
                    cnv.setFont("Helvetica", 11)
                    cnv.drawString(20, posicao[1], content[j][i][k])
                    posicao[1] = posicao[1] - 15
        posicao[1] = posicao[1] - 50



Exibir(content1, posicao1)


class Section:
    def __init__(self, title, content, position):
        self.title = title
        self.content = content
        self.position = position


    def printar(self):
        cnv.setFillColorRGB(0.2, 0.5, 0.8)
        cnv.rect(self.position[0],self.position[1],posicao_ret,posicao_ret, fill=True)
        for i in range(len(self.content[self.title])):
            cnv.setFillColorRGB(0, 0, 0)
            cnv.drawString(self.position[0],self.position[1]-10*i,self.content[self.title][i])
        
        




cnv.save()




# Dados pessoais
name = "Júlio Cesar Neves Nascimento"
contact_info = [
    "Rua Poços de Calda, 1875",
    "81995019156",
    "julio.neves.063@ufrn.edu.br",
    "https://github.com/NevesJulio"
]

# Seções do currículo




