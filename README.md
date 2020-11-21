# IA
Diogo C. Volpato e Matheus H. Piana
Em primeira instância baixamos packs das imagens, e pros 
algoritmos que não encontramos packs prontos baixamos as 
imagens manualmente;

As imagens foram divididas entre positivas e negativas, 
criado o arquivo .txt das imagens negativas e um para as 
positivas a IA foi treinada por cada imagem a reconhecer o 
objeto em questão.

Criado um vetor que compara as imagens negativas e positivas 
criando amostras para o treinamento da IA.

Treinamento da IA mostrando a ela todas as imagens originais 
para que ela gere arquivos .xml, sendo um deles ferente a 
cada estágio e aos parâmetros.

Foram usados: urllib, numpy, cv2, importado comandos para a 
comunicação direta com o so, listas para a leitura das 
imagens nos arquivos .txt, comandos básicos do cv2 para trocar a cor da imagem para cinza 
facilitando a leitura da imagem pelo sistema, usados os comandos para renomear todas as imagens para o mesmo 
alterando apenas o número final para diferenciar as mesmas. 

PS: interessante destacar que encontramos um problema com a 
"sujeira" fazendo que o detector das armas detectasse mais de 
um objeto na mesma imagem, com algumas pesquisas conseguimos 
entender o problema.
