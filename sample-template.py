from pycbc import noise
import pycbc.psd
from pycbc.waveform import get_td_waveform
import pylab

flow = 30.0
delta_f = 1.0 / 16
flen = int(2048 / delta_f) + 1
# noinspection PyUnresolvedReferences
psd = pycbc.psd.aLIGOZeroDetHighPower(flen, delta_f, flow)
delta_t = 1.0 / 4096
tsamples = int(32 / delta_t)
n_ts = pycbc.noise.noise_from_psd(tsamples, delta_t, psd, seed=127)
hp, hc = get_td_waveform(approximant="SEOBNRv4_opt", mass1=32, mass2=56, delta_t=1.0/4096, f_lower=30)
n_ts = list(n_ts)
noises = []
plus_p = list(hp)
wave = []

for i in n_ts:
    noises.append(i*10**5)

for i in range(1217):
    wave.append(noises[i]+plus_p[i])

# print(len(wave), len(plus_p), len(noises))

pylab.plot(wave)
# # pylab.plot(n_ts[:1217]+plus_p)
# # pylab.plot(hp.sample_times, hp, label='Plus Polarization')
# # pylab.plot(hp.sample_times, hc, label='Cross Polarization')
pylab.ylabel('Strain')
pylab.xlabel('Time (s)')
pylab.show()
