hiver = ['janvier', 'fevrier', 'mars']
printemps = ['avril', 'mai', 'juin']
ete = ['juillet', 'aout', 'septembre']
automne = ['octobre', 'novembre', 'decembre']

saisons = [hiver, printemps, ete, automne]

assert saisons[2] == ete
assert saisons[1][0] == 'avril'
assert saisons[1:2] == [printemps], saisons[1:2]
assert saisons[:] == [hiver, printemps, ete, automne]
assert saisons[:][1] == printemps
