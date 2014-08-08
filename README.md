# Python Wrapper para a API do Cobre Grátis

Essa biblioteca é um conjunto de classes em Python para acessar as informações do [Cobre Grátis](http://cobregratis.com.br) através da [API](https://github.com/CobreGratis/cobregratis-api).

Todas as classes são herdadas do pyactiveresource. Veja a documentação do [pyactiveresource](https://code.google.com/p/pyactiveresource/) para mais informações.

## Instalando

    git clone https://github.com/CobreGratis/cobregratis-python.git

### Configurando seu token

```python
from cobregratis.bank_billet import BankBillet

BankBillet.user = 'seu_token'
BankBillet.password = 'X'
```

## Uso

```python

# criar um boleto
amount = 230.50
expire_at = '2015-07-22'
name = 'Rafael Lima'
bank_billet = BankBillet.create({'amount':amount,'expire_at':expire_at,'name':name})

# listar todos os boletos
bank_billets = BankBillet.find()
if not bank_billets:
  print "Nenhum boleto bancário"
else:
  for bank_billet in bank_billets:
    print "Nosso Número: %s" % bank_billet.our_number
    print "Vencimento: %s" % bank_billet.expire_at
    print "Valor: %s" % bank_billet.amount
    print "Sacado: %s" % bank_billet.name
    print "URL: %s" % bank_billet.external_link
    print "================================="
```

Veja um exemplo no arquivo [example.py](https://github.com/CobreGratis/cobregratis-python/blob/master/example.py)

## Licença

Esse código é livre para ser usado dentro dos termos da licença [MIT license](http://www.opensource.org/licenses/mit-license.php).

## Bugs, Issues, Agradecimentos, etc

Comentários são bem-vindos. Envie seu feedback através do [issue tracker do GitHub](http://github.com/CobreGratis/cobregratis-python/issues)

## Autor

[**Rafael Lima**](http://github.com/rafaelp) trabalhando na [CobreGratis](http://bielsystems.com.br)

Blog: [http://rafael.adm.br](http://rafael.adm.br)

Twitter: [http://twitter.com/rafaelp](http://twitter.com/rafaelp)