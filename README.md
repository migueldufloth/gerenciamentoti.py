# Gerenciamento de Equipamentos de TI

Este projeto é uma aplicação simples para **gerenciamento de equipamentos de TI** utilizando arquitetura cliente-servidor.

## Arquitetura

- **Client-Server**:
  - O cliente envia solicitações ao servidor central.
  - O servidor processa as requisições e retorna respostas ao cliente.
  - Comunicação baseada em sockets.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Bibliotecas padrão**:
  - `socket`: Para comunicação entre cliente e servidor.
  - `threading`: Para permitir conexões simultâneas no servidor.

## Funcionalidades

1. **Adicionar Equipamentos**  
   Registre um novo equipamento no servidor.
2. **Consultar Equipamentos**  
   Consulte informações sobre um equipamento específico pelo seu ID.

## Como o Protocolo Funciona

O protocolo utiliza mensagens em formato de texto simples. A estrutura das mensagens trocadas é:

### Comandos Implementados

1. **Adicionar Equipamento (`A`)**  
   - Estrutura da mensagem enviada pelo cliente:  
     ```
     A-<ID>-<NOME>-<TIPO>
     ```
     - `<ID>`: Número único do equipamento.
     - `<NOME>`: Nome do equipamento.
     - `<TIPO>`: Tipo ou categoria do equipamento.

   - Respostas do servidor:  
     - `OK-Adicionado com sucesso!`: Equipamento registrado.  
     - `ERRO-Dados inválidos!`: Falha na validação.

2. **Consultar Equipamento (`C`)**  
   - Estrutura da mensagem enviada pelo cliente:  
     ```
     C-<ID>
     ```
     - `<ID>`: Número único do equipamento a ser consultado.

   - Respostas do servidor:  
     - `R-<ID>-<NOME>-<TIPO>`: Equipamento encontrado.  
     - `NE-Não encontrado`: Equipamento não encontrado.  
     - `ERRO-Dados inválidos!`: Mensagem malformada.

3. **Comando Não Reconhecido (`NR`)**  
   - Enviado pelo servidor quando o comando fornecido pelo cliente é inválido.

## Como Reproduzir o Software

Siga os passos abaixo para configurar e executar o software:

### 1. Instalar o Python 3.x
- Baixe e instale o Python na página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. Configurar o Ambiente
- Verifique se o Python está instalado corretamente:  
  ```bash
  python --version
  ```
- Certifique-se de que os arquivos `server.py` e `client.py` estão no mesmo diretório.

### 3. Executar o Servidor
1. Abra um terminal.
2. Navegue até o diretório contendo o arquivo `server.py`.
3. Execute o seguinte comando:  
   ```bash
   python server.py
   ```

### 4. Executar o Cliente
1. Abra outro terminal.
2. Navegue até o diretório contendo o arquivo `client.py`.
3. Execute o seguinte comando:  
   ```bash
   python client.py
   ```

### 5. Interagir com o Software
- O cliente exibe um menu com opções para adicionar ou consultar equipamentos.
- Siga as instruções no terminal para usar o sistema.

### 6. Rodando em Máquinas Diferentes (Opcional)
- Para executar em máquinas diferentes:
  - Substitua `localhost` pelo endereço IP da máquina onde o servidor está rodando no arquivo `client.py`.

## Exemplo de Uso

### Adicionando um Equipamento
No cliente, escolha a opção `1` e insira os seguintes dados:
- **ID**: `101`  
- **Nome**: `Monitor`  
- **Tipo**: `Periférico`  

O servidor responderá:
```
OK-Adicionado com sucesso!
```

### Consultando um Equipamento
No cliente, escolha a opção `2` e insira o ID `101`.  
O servidor retornará:
```
R-101-Monitor-Periférico
```

## Autor

- **Miguel Angelo Dufloth Filho**
