class Vigenere(object):    
    def __init__(self):
        self.A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def cipher(self, key, mesage):
        self.B = []
        self.C = []
        self.D = []
        self.E = []
        self.F = []
        self.k = key
        self.m = mesage
        for i in range(len(self.k)):
            self.B.append(self.k[i])
        for i in range(len(self.m)):
            self.C.append(self.m[i])

        for i in range(len(self.B)):#chave
            for j in range(len(self.A)):
                if self.A[j] == self.B[i]:
                    self.D.append(j)#chave em num

        for i in range(len(self.C)):#mensagem
            for j in range(len(self.A)):
                if self.A[j] == self.C[i]:
                    self.E.append(j)#mensagem em num

        if len(self.B) < len(self.C):
            for i in range(len(self.C)-len(self.B)):
                self.D.append(self.D[i])

        for i in range(len(self.E)):
            x = self.D[i]
            y = self.E[i]
            self.F.append(self.A[(x+y)%26])
            #print self.F[i]

        return self.F

        pass

    def decipher(self, key, code):
        self.B = []
        self.C = []
        self.D = []
        self.E = []
        self.F = []
        self.k = key
        self.c = code

        for i in range(len(self.k)):
            self.B.append(self.k[i])
        for i in range(len(self.c)):
            self.C.append(self.c[i])

        for i in range(len(self.B)):#chave
            for j in range(len(self.A)):
                if self.A[j] == self.B[i]:
                    self.D.append(j)#chave em num

        for i in range(len(self.C)):#codigo
            for j in range(len(self.A)):
                if self.A[j] == self.C[i]:
                    self.E.append(j)#codigo em num

        if len(self.B) < len(self.C):
            for i in range(len(self.C)-len(self.B)):
                self.D.append(self.D[i])

        for i in range(len(self.E)):
            x = self.D[i]
            y = self.E[i]
            self.F.append(self.A[(y-x+26)%26])
            #print self.F[i]

        return self.F

        pass

a = Vigenere()
a.cipher('pedro', 'joaopedro')
a.decipher('pedro','ysdfdthuf')
