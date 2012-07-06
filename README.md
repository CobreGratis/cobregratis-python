# Python Wrapper para a API do Cobre Grátis

Essa biblioteca é um conjunto de classes em Python para acessar as informações do [Cobre Grátis](http://cobregratis.com.br) através da [API](https://github.com/BielSystems/cobregratis-api).

Todas as classes são herdadas do pyactiveresource. Veja a documentação do [pyactiveresource](https://code.google.com/p/pyactiveresource/) para mais informações.

## Instalando

    git clone https://github.com/BielSystems/cobregratis-python.git

### Configurando seu token

```python
from cobregratis.bank_billet import BankBillet

BankBillet.user = 'seu_token'
BankBillet.password = 'X'
```

## Uso

```python
bank_billets = BankBillet.find()
```

Veja um exemplo no arquivo [example.py](https://github.com/BielSystems/cobregratis-python/blob/master/example.py)

## Licença

Esse código é livre para ser usado dentro dos termos da licença [MIT license](http://www.opensource.org/licenses/mit-license.php).

## Bugs, Issues, Agradecimentos, etc

Comentários são bem-vindos. Envie seu feedback através do [issue tracker do GitHub](http://github.com/BielSystems/cobregratis-python/issues)

## Autor

[**Rafael Lima**](http://github.com/rafaelp) trabalhando na [BielSystems](http://bielsystems.com.br)

Blog: [http://rafael.adm.br](http://rafael.adm.br)

Twitter: [http://twitter.com/rafaelp](http://twitter.com/rafaelp)