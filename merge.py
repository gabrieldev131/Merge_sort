# Merge_sort
#Aplication of merge sort in python for my home work of my college
# coding: utf-8
import pickle

def MergeSort(l,lm):
	if len(lm) > 1:
		meio = len(lm) // 2
		lEsq = lm[:meio]
		lDir = lm[meio:]
		
		MergeSort(l,lEsq)
		MergeSort(l,lDir)
		
		Merge(l,lm, lEsq, lDir)
		
def Merge(l,lm,lEsq, lDir):
  i = 0
  j = 0
  k = 0
  
  while i < len(lEsq) and j < len(lDir):
    if compara_dicionario(l,lEsq[i],lDir[j]):
      lm[k] = lEsq[i]
      i += 1
    else:
      lm[k] = lDir[j]
      j += 1
    k += 1
    
  while i < len(lEsq):
    lm[k] = lEsq[i]
    i += 1
    k += 1 
    
  while j < len(lDir):
    lm[k] = lDir[j]
    j += 1
    k += 1 

def lista_ordenada(l, lm):
  dicionario_novo = {}
  MergeSort(l,lm)
  for chave in lm:
    dicionario_novo[chave] = l[chave]
  return dicionario_novo

def compara_dicionario(l,chave1,chave2):
    nome1, (ano1, periodo1), (nota1_1, nota1_2, nota1_3, extra1), faltas1 = l[chave1]
    nome2, (ano2, periodo2), (nota2_1, nota2_2, nota2_3, extra2), faltas2 = l[chave2]
    if faltas1 == 0:
      extra1+=2
    if faltas2 == 0:
      extra2+=2
    nota_final_ordenacao1 = nota1_1 + nota1_2 + nota1_3 + extra1
    nota_final_ordenacao2 = nota2_1 + nota2_2 + nota2_3 + extra2
    # (a) Ordenar pelo semestre letivo (do mais recente para o mais antigo)
    if (ano1,periodo1)>(ano2, periodo2): return True
    elif (ano1,periodo1)<(ano2, periodo2): return False
    # (b) Em caso de empate, ordenar pela nota final (da maior para a menor)
    elif nota_final_ordenacao1<100 or nota_final_ordenacao2<100:
      if nota_final_ordenacao1 < nota_final_ordenacao2: return False
      elif nota_final_ordenacao1 > nota_final_ordenacao2: return True
    # (c) Em caso de novo empate, ordenar em ordem alfabética do nome
    elif nome1 < nome2: return True
    elif nome1 > nome2: return False
    # (d) Em caso de novo empate, ordenar em ordem crescente de matrícula
    elif chave1<chave2: return True
    else: return False
  
def ordenada(l,lm):
  k = len(lm)
  for i in range(k-1):
    if compara_dicionario(l,lm[i],lm[i+1]) == False: 
      return False  
  return True
  
def abre_arquivo():  
  #função de abrir o arquivo pickle que vamos usar. ele será colocado aqui
  with open('entrada1000000.bin', mode='rb') as file:
    objeto = pickle.load(file)
  return objeto

def lista_matricula(l):
  #função que pega a matricula
  lm = []
  for matricula in l:
    lm.append(matricula)   
  return lm  

def formatado(l):
  #coloquei essas variaveis pq tava dando problema, ai declarei pra resolver
  lista_formatada = []
  p = 0
  nota = 0
  for i in l:
    nome, (ano, periodo), (nota1, nota2, nota3, extra), faltas = l[i]
    if faltas == 0:
      p = 2 
    else:
      p = 0
    #if e else classico pra ver se estrapolou os 100 pontos
    nota = nota1+ nota2+ nota3+ extra+ p
    if nota>100:
      nota = 100
    #é aqui que faço a lista e formato ela. o ^ significa xor (ou exclusivo)
    if p == 0 ^ (extra == 0 and p == 0):   
      lista_formatada.append((f'{ano}/{periodo} {i} {nome} - {nota} ({nota1}+{nota2}+{nota3} +{extra}E = {nota1+ nota2+ nota3+ extra+ p})'))
    elif extra == 0 ^ (p == 0 and extra == 0):
      lista_formatada.append((f'{ano}/{periodo} {i} {nome} - {nota} ({nota1}+{nota2}+{nota3} +{p}P = {nota1+ nota2+ nota3+ extra+ p})'))
    elif p == 0 and extra == 0:
      lista_formatada.append((f'{ano}/{periodo} {i} {nome} - {nota} ({nota1}+{nota2}+{nota3} = {nota1+ nota2+ nota3})'))
    else:
      lista_formatada.append((f'{ano}/{periodo} {i} {nome} - {nota} ({nota1}+{nota2}+{nota3} +{extra}E +{p}P = {nota1+ nota2+ nota3+ extra+ p})')) 
      
  return lista_formatada

#procedimento de criação de arquivo
def saida(a):  
  with open("saida.txt",mode="w", encoding="utf-8") as dados:
    for dado in a:
      dados.write(str(dado)+'\n')
  dados.close()

def main():
  
  l = abre_arquivo()
  lm = lista_matricula(l)
  a = lista_ordenada(l, lm)
  b = formatado(a)
  #c = ordenada(a,lm)
  saida(b)
  return 0
if __name__ == "__main__":
  main()
