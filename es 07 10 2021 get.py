class telefono:

   
    garanzia = 1
    antivirus = True
    cover = 0

    
    def __init__(self,proprietario, marca, modello, memoria, colore):

        
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.memoria = memoria 
        self.colore = colore
        
        telefono.cover +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n memoria: {self.memoria}\n colore: {self.colore}\n garanzia: {self.garanzia}' 
    
giovanni = telefono("giovanni","samsung","s21",128, "rosso")

marco = telefono("marco","iphone","13",128, "verde")

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)

print("\nLa singola scheda è:")
print (giovanni.scheda())
print (marco.scheda())
print("\ntelefono totali: ",telefono.cover)

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(giovanni.__dict__)
print(marco.__dict__)
