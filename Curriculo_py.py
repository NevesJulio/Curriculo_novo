from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from fpdf import FPDF


cnv = canvas.Canvas("MeuCurrículo.pdf")
largura_A4, altura_A4 = A4

# Dados pessoais
Name = "Júlio Cesar\nNeves Nascimento"
contact_info = [[
    "Rua Poços de Calda, 1875",
    "(81)995019156",
    "julio.neves.063@ufrn.edu.br",
    "https://github.com/NevesJulio"
]]


content1 = [
    ["Formação Acadêmica","Bacharelado em Engenharia Biomédica\n- UFRN - Previsão de Conclusão: 2026","Bacharelado em Ciência e Tecnologia\n- UFRN - Conclusão: 2021", "Curso de python - Udemy - Conclusão: 2022", "Curso de API - Udemy - Conclusão: 2022"],
    ["Experiência","Monitoria - UFRN -\nCálculo III - 2022.2\nFísica Experimental II - 2023.1/2023.2\nEletricidade Aplicada - 2024.1","Auxílio aos alunos em suas dúvidas e\ndificuldades nas disciplinas.","Preparação de materiais didáticos\ne suporte ao professor na correção de\nexercícios e provas.","Iniciação Científica - Instituto Santos Drumond -\nAuxílio no desenvolvimento de projeto de\npesquisa voltados para a área de robótica e\nprogramção"],
    ["Habilidades Técnicas","Python, C++, C#, HTML, CSS","Ferramentas de Desenvolvimento:\n[IDE's, plataformas de desenvolvimento, etc.]","Inglês: Fluente"]
]
content2 = [
    ["Áreas de interesse", "Tenho o objetivo de me aprofundar mais em conhecimentos\npráticos nas áreas de Eletrônica, assim como em programação,\nprincipalmente em python e C++"],
    [" "],
    [" "]
]


posicao_ret = 250
posicao0 = [20,altura_A4-20]
posicao1 = [20,altura_A4-100]
posicao3 = [260, altura_A4-50]


cnv.setFillColorRGB(0.2, 0.5, 0.8)
cnv.setStrokeColorRGB(0.2, 0.5, 0.8)
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
        

def Exibir_Ponto(content, posicao):
    
    for j in range(len(content)):
        for i in range(len(content[j])):
            posicao[1] = posicao[1]-15
            cnv.setFillColorRGB(0, 0, 0)
            if i == 0:
                cnv.setFont("Helvetica-Bold", 16)
                cnv.drawString(posicao[0], posicao[1], content[j][i])
                cnv.setStrokeColorRGB(1, 1, 1)
                cnv.line(posicao[0], posicao[1]-5,posicao[0]+200, posicao[1]-5)
                posicao[1] = posicao[1]-15
            else:
                cnv.setFillColorRGB(0, 0, 0)
                cnv.setStrokeColorRGB(0, 0, 0)
                cnv.circle(posicao[0]-10, posicao[1]+5, 2, fill=True)
                content[j][i] = content[j][i].split("\n")
                print(len(content[j][i]))
                for k in range(len(content[j][i])):
                    cnv.setFillColorRGB(0, 0, 0)
                    cnv.setFont("Helvetica", 11)
                    cnv.drawString(posicao[0], posicao[1], content[j][i][k])
                    posicao[1] = posicao[1] - 15
        posicao[1] = posicao[1] - 5
        


def Exibir_Sem(content, posicao):
    
    for j in range(len(content)):
        for i in range(len(content[j])):
            posicao[1] = posicao[1]-25
            cnv.setFillColorRGB(0, 0, 0)
            if i == 0:
                cnv.setFont("Helvetica-Bold", 12)
                cnv.drawString(posicao[0], posicao[1], content[j][i])
            else:
                content[j][i] = content[j][i].split("\n")
                print(len(content[j][i]))
                for k in range(len(content[j][i])):
                    cnv.setFillColorRGB(0, 0, 0)
                    cnv.setFont("Helvetica", 11)
                    cnv.drawString(posicao[0], posicao[1], content[j][i][k])
                    posicao[1] = posicao[1] - 15
        posicao[1] = posicao[1] - 30
        cnv.setStrokeColorRGB(1, 1, 1)
        cnv.line(posicao[0], posicao[1],posicao[0]+200, posicao[1] )


splitar = Name.split("\n")
for i in range(len(splitar)):
    cnv.setFillColorRGB(i, i, i)
    cnv.setFont("Helvetica-Bold", 20)
    cnv.drawString(posicao0[0],posicao0[1]-15-20*i, splitar[i])
cnv.setFillColorRGB(1, 1, 1)
cnv.roundRect(posicao0[0]-5,posicao0[1]-55, 230, 15, 10, stroke=0, fill=1)
cnv.setFillColorRGB(0, 0, 0)
cnv.setFont("Helvetica-Bold", 11)
cnv.drawString(posicao0[0],posicao0[1]-50, "Sétimo período de Engenharia Biomédica")



Exibir_Ponto(content1, posicao1)
Exibir_Sem(content2, posicao3)
#Exibir(contact_info, posicao3)

for i in range(len(contact_info[0])):
    print(i)
    cnv.setFillColorRGB(0, 0, 0)
    cnv.setFont("Helvetica-Bold", 12)
    cnv.drawString(posicao0[0]+350, posicao0[1]-723-20*i, contact_info[0][i])
    cnv.drawImage(rf"C:\Users\Julio\Desktop\Programacao\Currículo\icones\img{i}.png",posicao0[0]+325, posicao0[1]-730-19*i, 15, 15, mask = 'auto')



cnv.save()




