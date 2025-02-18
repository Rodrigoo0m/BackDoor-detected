# Backdoor Detection Tool

## Descrição

A ferramenta de detecção de backdoors para sistemas operacionais permite a análise em tempo real de processos suspeitos, conexões de rede, persistência e integridade de arquivos, monitoramento de comportamento de usuários, e muito mais. O objetivo é identificar atividades maliciosas em sistemas comprometidos.

## Funcionalidades

- **Monitoramento de Processos**: Detecta processos suspeitos em execução.
- **Escaneamento de Rede**: Analisa as conexões de rede para possíveis atividades maliciosas.
- **Verificação de Persistência**: Detecta técnicas usadas por backdoors para persistir após reinicializações.
- **Monitoramento de Integridade de Arquivos**: Garante que arquivos críticos não sejam alterados.
- **Monitoramento de Atividade de Usuários**: Registra o comportamento de usuários no sistema.
- **Integração com Discord**: Envia alertas para um canal Discord quando atividades suspeitas são detectadas.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `psutil`
  - `requests`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/backdoor_detector.git

2. Navegue até ao diretório do projeto:
   ```bash
    cd backdoor_detector

3. Instale as dependências necessárias:
   ```bash
    pip install -r requirements.txt

## Uso
Para rodar a ferramenta e iniciar a detecção, basta executar o script main.py:
   ```bash
    python main.py

## Contribuição

Contribuições são bem-vindas! Se você tem alguma sugestão ou encontrou um erro, sinta-se à vontade para abrir um issue ou fazer um pull request.
