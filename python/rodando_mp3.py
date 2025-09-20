'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

'''Use playsound se: 
    Precisa apenas reproduzir um som simples e não se preocupa com funcionalidades avançadas.
    Quer uma solução rápida e sem dependências extras de módulos mais complexos. 

Use pygame se: 
    Está a desenvolver um jogo ou aplicação multimédia e precisa de mais controlo sobre o áudio, como parar a música, controlar o volume ou reproduzir vários efeitos sonoros simultaneamente.
    Precisa de uma solução robusta e com mais recursos, apesar de ser mais complexo para configurar e usar do que playsound.'''

from playsound import playsound
try:
# Toca o arquivo MP3. O caminho pode ser completo ou relativo à pasta do script.
    playsound("H:\tec_tec_tec\TreinoTreino\python\zittiibuoni2.wav") # Altere 'seu_arquivo.mp3' para o nome do seu arquivo
except Exception as e:
    print(f"Erro ao reproduzir o som: {e}")