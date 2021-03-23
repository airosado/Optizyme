fig = plt.figure(figsize=(25,10))
rxn_time = []
t = 0
while(t<100):
    r2 = rand.uniform(0,1.0)
    dt = math.log(1/r2)
    rxn_time.append(dt)
    t += 1

plt.plot(range(len(rxn_time))