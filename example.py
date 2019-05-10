class BondYield:
    def __init__(self, TenorID, BondYield):
        self.TenorID = TenorID
        self.BondYield = BondYield

    def __repr__(self):
        return f'<BondYield {self.TenorID} - {self.BondYield}>'

# maak een list met BondYield objecten
bond_yield_table = [
    BondYield(18, 3.14),
    BondYield(18, 4.234234),
    BondYield(19, 5.23432),
    BondYield(19, 7.324234),
]

# vraag 1: select distinct TenorID from bond_yield_table
[y.TenorID for y in bond_yield_table] # [18, 18, 19, 19]
set([y.TenorID for y in bond_yield_table]) # {18, 19}
list(set([y.TenorID for y in bond_yield_table])) # [18, 19]
print("Antwoord 1")
print(list(set([y.TenorID for y in bond_yield_table])))

# vraag 2: select count(*) from bond_yield_table
print("Antwoord 2")
print(len(bond_yield_table))

# vraag 3: select * where tenorid = 18
print("Antwoord 3a")
for b in bond_yield_table:
    if b.TenorID == 18:
        print(b)

print("Antwoord 3b")
print([b for b in bond_yield_table if b.TenorID == 18])
