# 🫀 CardioIA - Fase 2: Diagnóstico Automatizado com IA

## Integrantes
- Michelle Cavalari rm564557

---

## Descrição do Projeto

Este projeto foi desenvolvido como parte da Fase 2 do CardioIA, cujo objetivo é simular um sistema de diagnóstico automatizado utilizando técnicas de Inteligência Artificial.

A proposta consiste em analisar descrições textuais de sintomas relatados por pacientes, identificar padrões e sugerir possíveis diagnósticos, além de classificar o nível de risco de cada caso.

O sistema simula, de forma simplificada, o funcionamento de tecnologias utilizadas em triagens clínicas modernas, aproximando o desenvolvimento acadêmico de aplicações reais na área da saúde.

---

##  Objetivos

- Interpretar frases contendo sintomas de pacientes
- Identificar sintomas relevantes utilizando um mapa de conhecimento
- Sugerir possíveis diagnósticos automaticamente
- Classificar o risco como "alto risco" ou "baixo risco"
- Aplicar técnicas de Processamento de Linguagem Natural (NLP)
- Refletir sobre vieses e governança de dados em IA

---
## 🗂️ Estrutura do Projeto

```bash
cardioia-fase2-diagnostico-automatizado/
│
├── data/
│   ├── frases_sintomas.txt
│   ├── mapa_conhecimento.csv
│   └── frases_risco.csv
│
├── src/
│   ├── parte1_diagnostico.py
│   └── parte2_classificador.py
│
├── README.md
└
```
---


##  Parte 1 – Extração de Sintomas e Diagnóstico

Nesta etapa, foi desenvolvido um sistema baseado em regras que:

1. Lê frases simulando relatos de pacientes
2. Identifica sintomas presentes no texto
3. Consulta um mapa de conhecimento em formato CSV
4. Sugere um diagnóstico com base nas associações

### Exemplo de funcionamento:

Entrada: "Tenho dor no peito e suor excessivo"

Saída: Sintomas identificados: dor no peito, suor excessivo
Diagnóstico sugerido: Infarto


Essa abordagem simula um sistema inicial de apoio à decisão médica baseado em reconhecimento de padrões simples.

---

##  Parte 2 – Classificação de Risco com IA

Nesta etapa, foi implementado um modelo de Machine Learning para classificar frases como:

- Alto risco
- Baixo risco

###  Etapas realizadas:

- Criação de base de dados rotulada (`frases_risco.csv`)
- Vetorização de texto utilizando TF-IDF
- Treinamento de modelo com Regressão Logística
- Avaliação do modelo com métricas de desempenho

---

##  Resultados do Modelo

- **Acurácia:** 0.67

### Relatório de Classificação:

precision recall f1-score support

alto risco 0.67 0.67 0.67 3
baixo risco 0.67 0.67 0.67 3

accuracy 0.67 6

###  Matriz de Confusão:
[[2 1]
[1 2]]


###  Testes com novas frases:

- estou com dor no peito e suor intenso -> alto risco
- tenho apenas um leve cansaço hoje -> baixo risco
- estou com falta de ar e tontura -> alto risco
- sinto um pequeno incômodo muscular -> baixo risco


---

## Vieses e Governança de Dados

A base de dados utilizada neste projeto é pequena e simulada, o que pode gerar limitações no desempenho do modelo.

Em aplicações reais na área da saúde, é fundamental considerar:

- Uso de bases de dados amplas e diversas
- Revisão por especialistas médicos
- Tratamento ético dos dados
- Transparência nas decisões da IA

Isso evidencia a importância da governança de dados no desenvolvimento de sistemas inteligentes.

---

##  Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Regressão Logística

---

##  Como Executar o Projeto

###  Instalar dependências:

pip install pandas scikit-learn

---

###  Executar Parte 1:
python src/parte1_diagnostico.py
###  Executar Parte 2:
python src/parte2_classificador.py


---

##  Vídeo de Demonstração

🔗 Link do vídeo (não listado no YouTube):  
*https://youtu.be/TVisHaDAAz0*

---

##  Observação Importante

Este projeto possui finalidade educacional e não substitui avaliação médica profissional.

---

##  Conclusão

O projeto demonstrou como técnicas simples de Inteligência Artificial podem ser aplicadas na análise de dados clínicos, simulando sistemas de apoio ao diagnóstico.

Através do uso de NLP e modelos de classificação, foi possível identificar padrões em textos e classificar riscos, evidenciando o potencial da IA na área da saúde, bem como a importância da responsabilidade no uso dessas tecnologias.



