# Crawling
Projeto de TCC.

## Mensagens de ocorrência
Mensagens que cada recomendação pode retornar em uma ocorrência compiladas em um arquivo CSV (data/messages.csv) com quatro colunas: `recommendation`, `code_feedback`, `code_message` e `message`. Sendo:

- `recommendation` - número da recomendação [1-50]
- `code_feedback` - código do tipo, ela pode ser:
    - 0 - Erro
    - 1 - Ok
    - 2 - Alerta
- `code_message` - código da mensagem [0-️]
- `message` - texto da mensagem