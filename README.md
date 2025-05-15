 # projeto-final-IA
 Projeto final do Bootcamp de Ciência de Dados e IA

 # 🧠 Projeto Final — Classificação de Defeitos em Chapas de Aço Inoxidável

Este repositório contém o projeto final desenvolvido por **Rosemeri Borges** no Bootcamp de Ciência de Dados e Inteligência Artificial do UNISENAI. O objetivo é aplicar técnicas de aprendizado de máquina para classificar automaticamente **falhas em chapas de aço inoxidável** com base em atributos extraídos de imagens industriais.

---

## 🎯 Objetivo

Criar um modelo de classificação multiclasse capaz de identificar automaticamente o tipo de falha em uma chapa, otimizando o controle de qualidade na indústria.

---


---

## 🔍 Etapas Desenvolvidas

- Análise exploratória dos dados (EDA)
- Tratamento de inconsistências e outliers
- Normalização e codificação
- Testes com diversos algoritmos:
  - Regressão Logística
  - KNN
  - Naïve Bayes com PCA
  - Decision Tree
  - Random Forest
  - XGBoost (modelo final)
  - LightGBM e CatBoost (suporte)
  - Avaliação com LazyPredict e AutoML

---

## 🏁 Resultado Final

O modelo **XGBoost** foi escolhido como o melhor classificador, com os seguintes resultados:

| Métrica                | Valor      |
|------------------------|------------|
| Acurácia Macro         | 0.899      |
| ROC-AUC Macro          | 0.913      |
| Submissão              | ✅ Válida via API
| Arquivo Submetido      | `predicoes_final.csv`

---

## 📤 Submissão via API

A submissão foi realizada com sucesso na plataforma do Bootcamp via API oficial:

- Autenticação com token
- Envio do CSV com `id` + probabilidades
- Código HTTP `200 OK` retornado com as métricas detalhadas

---

## 🧪 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/RoseBorges44/projeto-final-IA.git
   cd projeto-final-IA

---
   
👩‍💻 Autora

Rosemeri Borges
📧 rose.jbob@gmail.com
📘 Bootcamp de Ciência de Dados e IA — UNISENAI
