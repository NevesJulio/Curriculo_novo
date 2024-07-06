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
    ["Formação Acadêmica","Engenharia Biomédica - UFRN -\n 7º período (Previsão de Conclusão: 2025).","Bacharelado em Ciência e Tecnologia\n- UFRN - Conclusão: 2021."],
    ["Cursos", "Curso de python - Udemy - Conclusão: 2022.", "Curso de API - Udemy - Conclusão: 2022."]
]
content2 = [
    ["Áreas de interesse", "Tenho o objetivo de me aprofundar mais\nem conhecimentos práticos nas áreas de\nEletrônica, assim como em programação,\nprincipalmente em python e C++."]
    
]
content3 = [
    ["Experiência","Monitoria - UFRN -\nCálculo III - 2022.2.\nFísica Experimental II - 2023.1/2023.2.\nEletricidade Aplicada - 2024.1.","Auxílio aos alunos em suas dúvidas e\ndificuldades nas disciplinas.","Auxílio dos alunos em atividades de eletrônica,\ncircuitos e microcontroladores.","Iniciação Científica - Instituto Santos Drumond -\nAuxílio no desenvolvimento de projeto de\npesquisa voltados para a área de robótica e\nprogramação."],
    ["Habilidades Técnicas","Python, C++, C#, HTML, CSS.","Eletrônica e Microcontroladores."],
    ["Idiomas","Inglês Fluente."]
]



posicao_ret = 250
posicao0 = [20,altura_A4-20]
posicao1 = [20,altura_A4-220]
posicao3 = [260, altura_A4-50]
posicao4 = [40,altura_A4-150]
posicao4_copia = [280, altura_A4-140]




#Cor do fundo
cnv.setFillColorRGB(0.9, 0.9, 0.9)
cnv.rect(0,0,largura_A4,altura_A4, fill=True, stroke = 0)

#Cor do retangulo
cnv.setFillColorRGB(115/255, 69/255, 85/255)
cnv.setStrokeColorRGB(0.2, 0.5, 0.8)
cnv.rect(0,0,posicao_ret,altura_A4, fill=True, stroke = 0)




def Exibir_Ponto(content, posicao, tamanho):
    
    for j in range(len(content)):
        for i in range(len(content[j])):
            posicao[1] = posicao[1]-15
            cnv.setFillColorRGB(0, 0, 0)
            if i == 0:
                cnv.setFont("Helvetica-Bold", tamanho+5)
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
                    cnv.setFont("Helvetica", tamanho)
                    cnv.drawString(posicao[0], posicao[1], content[j][i][k])
                    posicao[1] = posicao[1] - 15
        posicao[1] = posicao[1] - 30
        


def Exibir_Sem(content, posicao):
    
    for j in range(len(content)):
        for i in range(len(content[j])):
            posicao[1] = posicao[1]-25
            cnv.setFillColorRGB(0, 0, 0)
            if i == 0:
                cnv.setFont("Helvetica-Bold", 16)
                cnv.drawString(posicao[0], posicao[1], content[j][i])
                cnv.setStrokeColorRGB(1, 1, 1)
                cnv.line(posicao[0], posicao[1]-5,posicao[0]+200, posicao[1]-5)
                #posicao[1] = posicao[1]-15
            else:
                content[j][i] = content[j][i].split("\n")
                print(len(content[j][i]))
                for k in range(len(content[j][i])):
                    cnv.setFillColorRGB(0, 0, 0)
                    cnv.setFont("Helvetica", 12)
                    cnv.drawString(posicao[0], posicao[1], content[j][i][k])
                    posicao[1] = posicao[1] - 15
        posicao[1] = posicao[1] - 30
        #cnv.setStrokeColorRGB(1, 1, 1)
        #cnv.line(posicao[0], posicao[1],posicao[0]+200, posicao[1] )

#Nome
splitar = Name.split("\n")
cnv.setFont("Helvetica-Bold", 25)
cnv.setFillColorRGB(0, 0, 0)
cnv.drawString(posicao0[0]+260,posicao0[1]-50, splitar[0])
cnv.setFillColorRGB(115/255, 69/255, 85/255)
cnv.drawString(posicao0[0]+260,posicao0[1]-80, splitar[1])

#Declaração
cnv.setFont("Helvetica-Bold", 7)
cnv.setFillColorRGB(0, 0, 0)
cnv.drawString(posicao0[0]+235,posicao0[1]-815, "*Este documento foi gerado por meio de um código Python desenvolvido por Júlio Cesar Neves.")

#Exibir conteúdo
Exibir_Ponto(content1, posicao1, 11)
Exibir_Sem(content2, posicao1)
Exibir_Ponto(content3, posicao4_copia, 14)
cnv.setFillColorRGB(0.9, 0.9, 0.9)
cnv.circle(posicao0[0]+30, posicao0[1]-30,75, fill = 1, stroke = 0)
cnv.drawImage(fr"C:\Users\Julio\Desktop\CoisasCesar\Minhas fotos\OIG.png", posicao0[0]+30, posicao0[1]-170,150, 150, mask = 'auto')
cnv.drawImage(fr"C:\Users\Julio\Desktop\Programacao\Currículo\icones\perfil.png", posicao0[0]-20, posicao0[1]-177,206, 156, mask = 'auto')

#Contatos
for i in range(len(contact_info[0])):
    print(i)
    cnv.setFillColorRGB(0, 0, 0)
    cnv.setFont("Helvetica-Bold", 12)
    cnv.drawString(posicao4[0], posicao1[1]-130-20*i, contact_info[0][i])
    cnv.drawImage(rf"C:\Users\Julio\Desktop\Programacao\Currículo\icones\img{i}.png",posicao4[0]-25, posicao1[1]-135-20*i, 15, 15, mask = 'auto')



cnv.save()




