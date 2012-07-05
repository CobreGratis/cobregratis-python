#!/usr/bin/python
# -*- coding: utf-8 -*-

from cobregratis.bank_billet import BankBillet
from pyactiveresource.connection import UnauthorizedAccess
import sys

def main():
  BankBillet.user = '3NIAl4KWk87sFBbpqOUCSURED4zIx3Xiqz8gXSDtFF77YIADbRnoCXRjCHQ3'
  BankBillet.password = 'X'
  try:
    bank_billets = BankBillet.find()
    for bank_billet in bank_billets:
      print "Nosso Número: %s" % bank_billet.our_number
      print "Vencimento: %s" % bank_billet.expire_at
      print "Valor: %s" % bank_billet.amount
      print "Sacado: %s" % bank_billet.name
      print "================================="
  except UnauthorizedAccess:
    print "Access Denied"

if __name__ == '__main__':
  main()