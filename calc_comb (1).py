# Classe calcolo combinatorio
class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        '''
        modificare questo metodo in modo da verificare la coerenza delle variabili di
        istanza presenti
        '''
        return 0
    def confUtil(self):
      f= open ("word.italian.txt","r")
      for riga in f :
            if self._stringa in riga :
                return( "La stampa", self._stringa, "ha un significato compiuto.")
    f.close()
      
# permutazioni

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        n= len(self._stringa)
        permutazioni = match.factorial(n)
        print ("Il numero 1 di permutazioni è", permutazioni)

    def nPermutConRip(self):
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0
