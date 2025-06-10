manu_frnds = {"Bagio","amal","Annan","pd","kd"}

bagio_frnds = {"manu","amal","Annan","achu","tony","Kunjappi"}

all_new_frnds = manu_frnds.union(bagio_frnds)
print(all_new_frnds)

muatual_frnds = manu_frnds.intersection(bagio_frnds)
print(muatual_frnds)

new_frnd_bagi = all_new_frnds.difference(bagio_frnds)
print(new_frnd_bagi)