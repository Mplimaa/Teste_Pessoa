# Projeto: Classe Pessoa com Teste de unidade em Python

Este projeto contém a implementação de uma classe `Pessoa` com atributos básicos como nome, idade, CPF e endereço. O projeto também inclui testes de unidade para garantir o correto funcionamento dos métodos relacionados ao CPF.

## Estrutura do Projeto


 pessoa.py # Implementação da classe Pessoa
 test_pessoa.py # Testes para a classe Pessoa


- Inicialização com nome, idade, CPF e endereço.
- Métodos:
  - `falar()` e `andar()` para interações simples.
  - `get_cpf()` e `set_cpf()` com validação básica.
  - `get_endereco()` e `set_endereco()`.



## Como Executar

### Requisitos
- Python 3.x instalado
- baixado os pacotes do Pytest na pasta do repositório 

### Execução Manual (Modo Interativo)
```bash
python pessoa.py



Utilize o framework pytest para rodar os testes da classe.
pip install pytest

pytest test_pessoa.py -> pra testar o cpf , este arquivo acessa a classe pessoa para efetivar o teste



Testes Incluídos

test_get_cpf(): Verifica se o CPF 123.456.789-00 é retornado corretamente.
test_set_cpf_valido(): Testa a alteração do CPF de:  123.456.789-00  para: 987.654.321-00 com um valor válido.
test_set_cpf_invalido(): Nesta função, se o cpf for igual a 123.456.789-00, irá retornar que está inválido, caso contrário for informado o nome cpf na instancia do objeto está correto.
O método test_set_cpf_invalido, Garante que o CPF não muda se for inválido, caso contrário sim. No resultado do teste com pytest, se ficar verde passou, se ficar vermelho é falha.

Correção do metodo set_endereco() ok -> trocado o operador da comparação da Quantidade de string do endereço para <= 200

Melhorias Futuras
Melhorar a validação do CPF (atualmente baseada apenas no comprimento da string).
Adicionar mais testes para métodos como get_endereco() e set_endereco().


Obs: Repositório criado somente para fins educacionais, Michele Lima - 2025.
