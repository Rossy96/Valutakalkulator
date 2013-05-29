print "Valutakalkulator"

from urllib2 import Request, urlopen, URLError

def hent_kurs(fra, til):
    request = Request('http://rate-exchange.appspot.com/currency?from=%s&to=%s' % (fra, til))
    response = urlopen(request)
    doc = response.read()
    lst = doc.split(',')
    rate = lst[1].split()
    return float(rate[1])

usd = hent_kurs('USD', 'NOK')
pund = hent_kurs('GBP', 'NOK')
euro = hent_kurs('EUR', 'NOK')

kurser = ['pund', 'usd', 'euro']

def fra_nok():
        mengde = float(raw_input("Velg mengde NOK kr: "))
        valuta = raw_input("Velg valuta: usd, euro eller pund: ")
        if valuta in kurser:
            print "%.2f %s" % (mengde / eval(valuta.lower()), valuta)
        else :
            print "Ukjent Valuta"

def til_nok():
        valuta = raw_input("Velg valuta: usd, euro eller pund: ")
        if valuta in kurser:
            mengde = float(raw_input("Velg mengde %s: " % valuta.lower()))
            print "%.2f Nok" % (mengde * eval(valuta.lower()))
            
        else:
            print"Ukjent valuta"


while True:
    print "\nKurs usd %.2f, euro %.2f, pund %.2f" % (usd, euro, pund)
    noknok = raw_input("Velg: Til NOK eller fra NOK: ")
    if noknok.lower() == "fra nok" or noknok.lower() == 'fra':
        fra_nok()
    elif noknok.lower() == "til nok" or noknok.lower() == 'til':
        til_nok()
    elif noknok.lower() == "stopp":
        break
    else :
        print "Ukjent kommando"
            
    
        
