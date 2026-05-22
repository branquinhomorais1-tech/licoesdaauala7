import nltk
from nltk.tokenize import word_tokenize

# Garante o download do recurso de tokenização necessário para o NLTK
nltk.download('punkt')

# Mensagem recebida do cliente
feedback_cliente = "O suporte técnico resolveu meu problema muito rápido! Excelente atendimento."

# Realizando a tokenização do texto (separando em palavras e pontuações)
palavras_tokenizadas = word_tokenize(feedback_cliente)

# Exibindo o resultado final
print(palavras_tokenizadas)
#------------------------------------------------
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Garante o download do recurso de tokenização
nltk.download('punkt')

# Texto de exemplo (Avaliações consolidadas)
avaliacoes = "O produto é bom. O produto é barato. O atendimento também foi bom."

# 1. Normalização (colocar tudo em minúsculo para não duplicar "O" e "o") e Tokenização
palavras = word_tokenize(avaliacoes.lower())

# 2. Contagem de frequência com o FreqDist do NLTK
frequencia = FreqDist(palavras)

# Exibindo as 3 palavras mais comuns
print("Palavras mais comuns:", frequencia.most_common(3))

# Exibindo a contagem de uma palavra específica
print("Frequência da palavra 'produto':", frequencia['produto'])
#---------------------------------------------------------
import nltk
from nltk.tokenize import word_tokenize

# Garante o download do recurso de tokenização
nltk.download('punkt')

# Mensagem de exemplo que veio do cliente
mensagem_cliente = "O sistema apresentou um erro crítico e o acesso ficou péssimo."

# 1. Tokenização e normalização para minúsculo
palavras = word_tokenize(mensagem_cliente.lower())

# 2. Definição da nossa lista de gatilhos negativos (Blacklist)
palavras_negativas = ["ruim", "péssimo", "erro", "falha", "atraso"]

# 3. Verificação usando interseção de conjuntos (set) para ver se há correspondência
# Isso verifica se alguma palavra da mensagem está na nossa lista negativa
contem_negativa = any(palavra in palavras_negativas for palavra in palavras)

# 4. Regra condicional para tomada de decisão
if contem_negativa:
    print("STATUS: 🚨 ALERTA CRÍTICO - Priorizar suporte imediatamente!")
else:
    print("STATUS: ✅ Normal - Fila de atendimento padrão.")
    #---------------------------------------------
    import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Garante o download do recurso de tokenização e do corpus de stopwords
nltk.download('punkt')
nltk.download('stopwords')

# 1. Definindo a lista de stopwords oficiais em português do NLTK
stopwords_pt = set(stopwords.words('portuguese'))

# Mensagem original do cliente
mensagem = "O suporte foi excelente para o meu problema, mas a espera foi longa."

# 2. Tokenização e normalização
palavras = word_tokenize(mensagem.lower())

# 3. Filtragem: Mantém na lista apenas as palavras que NÃO são stopwords e que não são pontuações
palavras_filtradas = [p for p in palavras if p not in stopwords_pt and p.isalnum()]

# Exibindo o antes e o depois
print("Antes da filtragem (Original):")
print(palavras)

print("\nDepois da filtragem (Sem Stopwords):")
print(palavras_filtradas)
