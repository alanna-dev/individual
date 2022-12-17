class Individual:
    
    __cont = 1
    
    def __init__(self, genotipo = str, nome = None, blood_type = None, aglutinogeneos = None, aglutininas = None):
        self.__genotipo = genotipo
        self.__nome = nome
        self.__blood_type = blood_type
        self.__aglutinogeneos = aglutinogeneos
        self.__aglutininas = aglutininas
        
        
        self.__genotipos = ["AA", "Ai", "BB", "Bi", "AB", "ii"]
        if self.__genotipo not in self.__genotipos:
            raise ValueError(f'Insert a valid genotype. They are: {self.__genotipos}.')
        else:
            pass
        
        
        if self.__nome == None:
            self.__nome = 'Indiv' + str(Individual.__cont)
            Individual.__cont += 1
        else:
            pass
        
        
        if (self.__genotipo == "AA" or self.__genotipo == "Ai"):
            self.__blood_type = "A"
            self.__aglutinogeneos = "A"
            self.__aglutininas = "B"
        elif (self.__genotipo == "BB" or self.__genotipo == "Bi"):
            self.__blood_type = "B"
            self.__aglutinogeneos = "B"
            self.__aglutininas = "A"
        elif (self.__genotipo == "AB"):
            self.__blood_type = "AB"
            self.__aglutinogeneos = "A e B"
            self.__aglutininas = "A e B"
        else:
            self.__blood_type = "O"
            self.__aglutinogeneos = None
            self.__aglutininas = None
          
    
    @property
    def name(self):
        return self.__nome
    
    
    @property
    def genotype(self):
        return self.__genotipo
    
    
    @property
    def blood_type(self):
        return self.__blood_type
    
    
    @property
    def agglutinogens(self):
        return self.__aglutinogeneos
    
    
    @property
    def agglutinins(self):
        return self.__aglutininas
    
    
    def offsprings_genotypes(self, indiv2):
        genotypes = []
        if self.__genotipo == "AA" and indiv2.genotype == "AA":
            indiv2 = genotypes.append("AA")
        elif self.__genotipo == "AA" and indiv2.genotype == "Ai":
            indiv2 = genotypes.append("Ai")
        elif self.__genotipo == "AA" and indiv2.genotype == "BB":
            indiv2 = genotypes.append("AB")
        elif self.__genotipo == "AA" and indiv2.genotype == "Bi":
            indiv2 = genotypes.append("AB ou Bi")
        elif self.__genotipo == "AA" and indiv2.genotype == "AB":
            indiv2 = genotypes.append("AA ou AB")
        elif self.__genotipo == "AA" and indiv2.genotype == "ii":
            indiv2 = genotypes.append("Ai")
        elif self.__genotipo == "Ai" and indiv2.genotype == "Ai":
            indiv2 = genotypes.append("AA, Ai ou ii")
        elif self.__genotipo == "Ai" and indiv2.genotype == "BB":
            indiv2 = genotypes.append("AB ou Bi")
        elif self.__genotipo == "Ai" and indiv2.genotype == "Bi":
            indiv2 = genotypes.append("AB,Ai,Bi ou ii")
        elif self.__genotipo == "Ai" and indiv2.genotype == "AB":
            indiv2 = genotypes.append("AA,AB,Ai ou Bi")
        elif self.__genotipo == "Ai" and indiv2.genotype == "ii":
            indiv2 = genotypes.append("Ai ou ii")
        elif self.__genotipo == "BB" and indiv2.genotype == "BB":
            indiv2 = genotypes.append("BB")
        elif self.__genotipo == "BB" and indiv2.genotype == "Bi":
            indiv2 = genotypes.append("BB ou Bi")
        elif self.__genotipo == "BB" and indiv2.genotype == "AB":
            indiv2 = genotypes.append("BB ou AB")
        elif self.__genotipo == "BB" and indiv2.genotype == "ii":
            indiv2 = genotypes.append("Bi")
        elif self.__genotipo == "Bi" and indiv2.genotype == "Bi":
            indiv2 = genotypes.append("BB,Bi ou ii")
        elif self.__genotipo == "Bi" and indiv2.genotype == "AB":
            indiv2 = genotypes.append("BB,AB,Ai ou Bi")
        elif self.__genotipo == "Bi" and indiv2.genotype == "ii":
            indiv2 = genotypes.append("Bi ou ii")
        elif self.__genotipo == "AB" and indiv2.genotype == "AB":
            indiv2 = genotypes.append("AB, AA ou BB")
        elif self.__genotipo == "AB" and indiv2.genotype == "ii":
            indiv2 = genotypes.append("Ai, Bi")
        elif self.__genotipo == "ii" and indiv2.genotype == "ii":
            indiv2 = genotypes.append("ii")
        else:
            pass
        return genotypes
    
    
    def offsprings_blood_types(self, indiv2):
        blood_types = []
        if self.__genotipo == "AA" and indiv2.genotype == "AA":
            indiv2 = blood_types.append("A")
        elif self.__genotipo == "AA" and indiv2.genotype == "Ai":
            indiv2 = blood_types.append("A")
        elif self.__genotipo == "AA" and indiv2.genotype == "BB":
            indiv2 = blood_types.append("AB")
        elif self.__genotipo == "AA" and indiv2.genotype == "Bi":
            indiv2 = blood_types.append("AB ou B")
        elif self.__genotipo == "AA" and indiv2.genotype == "AB":
            indiv2 = blood_types.append("A ou AB")
        elif self.__genotipo == "AA" and indiv2.genotype == "ii":
            indiv2 = blood_types.append("A")
        elif self.__genotipo == "Ai" and indiv2.genotype == "Ai":
            indiv2 = blood_types.append("A ou O")
        elif self.__genotipo == "Ai" and indiv2.genotype == "BB":
            indiv2 = blood_types.append("AB ou B")
        elif self.__genotipo == "Ai" and indiv2.genotype == "Bi":
            indiv2 = blood_types.append("AB, A, B ou O")
        elif self.__genotipo == "Ai" and indiv2.genotype == "AB":
            indiv2 = blood_types.append("A, AB ou B")
        elif self.__genotipo == "Ai" and indiv2.genotype == "ii":
            indiv2 = blood_types.append("A ou O")
        elif self.__genotipo == "BB" and indiv2.genotype == "BB":
            indiv2 = blood_types.append("B")
        elif self.__genotipo == "BB" and indiv2.genotype == "Bi":
            indiv2 = blood_types.append("B")
        elif self.__genotipo == "BB" and indiv2.genotype == "AB":
            indiv2 = blood_types.append("B ou AB")
        elif self.__genotipo == "BB" and indiv2.genotype == "ii":
            indiv2 = blood_types.append("B")
        elif self.__genotipo == "Bi" and indiv2.genotype == "Bi":
            indiv2 = blood_types.append("B ou O")
        elif self.__genotipo == "Bi" and indiv2.genotype == "AB":
            indiv2 = blood_types.append("AB, A ou B")
        elif self.__genotipo == "Bi" and indiv2.genotype == "ii":
            indiv2 = blood_types.append("B ou O")
        elif self.__genotipo == "AB" and indiv2.genotype == "AB":
            indiv2 = blood_types.append("AB, A ou B")
        elif self.__genotipo == "AB" and indiv2.genotype == "ii":
            indiv2 = blood_types.append("A ou B")
        elif self.__genotipo == "ii" and indiv2.genotype == "ii":
            indiv2 = blood_types.append("O")
        else:
            pass
        return blood_types
    
    
    def can_donate(self, indiv2):
        if self.__blood_type == "O":
            return True
        elif self.__blood_type == "AB" and indiv2.blood_type == "AB":
            return True
        elif self.__blood_type == "B" and (indiv2.blood_type == "AB" or indiv2.blood_type == "B"):
            return True
        elif self.__blood_type == "A" and (indiv2.blood_type == "AB" or indiv2.blood_type == "A"):
            return True
        else:
            return False
        
    def can_receive(self, indiv2):
        if self.__blood_type == "AB":
            return True
        elif self.__blood_type == "B" and (indiv2.blood_type == "B" or indiv2.blood_type == "O"):
            return True
        elif self.__blood_type == "A" and (indiv2.blood_type == "A" or indiv2.blood_type == "O"):
            return True
        elif self.__blood_type == "O" and indiv2.blood_type == "O":
            return True
        else:
            return False
