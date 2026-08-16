#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
OmniCentro Climate Calculations.

Author: HomeOnMars



-------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2024 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------------------
"""

import numpy as np
from astropy import units as u
from matplotlib import pyplot as plt



# helper gaussian func for months; 12 and 6 because there are 12 months in a year
# i_month=6 for hot July
gaussian = lambda i_month=6, sig=2: np.exp(-0.5*(((np.arange(12)-i_month+6)%12-6)/sig)**2)



# Climate of [Reykjavik](https://en.wikipedia.org/wiki/Reykjav%C3%ADk#Climate) (2024-10-23)

# record temperature max by month
Tr_max= np.array([11.6, 10.2, 14.2, 17.1, 20.6, 22.4, 25.7, 24.8, 20.1, 15.7, 12.7, 12.0])*u.deg_C + (
    1.0 + 6.0*gaussian(6) - 1.0*gaussian(0, sig=0.5) + 1.0*gaussian(1, sig=0.5))*u.deg_C
# average temperature max by month
T_max = np.array([ 3.2,  3.3,  4.2,  6.9, 10.1, 13.0, 14.9, 14.1, 11.4,  7.6,  4.7,  3.3])*u.deg_C + (
    -0.5 + 4.0*gaussian(6))*u.deg_C
# record temperature min by month
Tr_min= np.array([-24.5, -17.6, -16.4, -16.4, -7.7, -0.7, 1.4, -0.4, -4.4, -10.6, -15.1, -16.8])*u.deg_C + (
    1.0 + 8.0*gaussian(0, sig=4) + 5.0*gaussian(0, sig=0.5) + 4.0*gaussian(3, sig=0.5) - 2.0*gaussian(11, sig=0.5))*u.deg_C
# average temperature min by month
T_min = np.array([-1.7, -1.9, -1.3,  1.0,  4.0,  7.2,  9.1,  8.6,  6.2,  2.7, -0.1,  1.6])*u.deg_C + (
    -2.75 + 1.0*gaussian(0, sig=4) + 4.0*gaussian(3) + 3.0*gaussian(6) + 1.0*gaussian(9) + 2.0*gaussian(10, sig=1) - 3.0*gaussian(11, sig=0.5))*u.deg_C
# average temperature by month
T_avg = np.array([ 0.7,  0.5,  1.2,  3.7,  6.7,  9.8, 11.6, 11.0,  8.5,  4.9,  2.2,  0.8])*u.deg_C + (
    0.0  + 1.0*gaussian(3) + 3.0*gaussian(6) - 0.5*gaussian(0, sig=0.5))*u.deg_C
# chance of rain
rain_p=((np.array([15.3, 15.0, 14.2, 12.0, 10.8,  9.3, 10.3, 11.6, 15.0, 13.1, 13.7, 14.6]) / 30) - 1/16) * 100*u.percent
# amount of rain
rain_v= np.array([87.1, 90.6, 80.7, 59.0, 52.6, 43.3, 49.9, 64.5, 87.0, 79.8, 86.5, 94.9])*u.mm - 10*u.mm


# Cloudiness data see https://weatherspark.com/y/31501/Average-Weather-in-Reykjav%C3%ADk-Iceland-Year-Round#Figures-CloudCover
clouds_raw= np.array([
    # each column represens: (in unit of percent)
    # chance of <= 20% / 40% / 60% / 80% clouds
    # values approximated from weatherspark graph by eyeballing
    [ 7, 13, 22, 39],    # Jan
    [ 8, 14, 24, 41],    # Feb
    [ 9, 16, 29, 46],    # Mar
    [12, 22, 38, 53],    # Apr
    [16, 28, 43, 57],    # May
    [15, 25, 39, 55],    # Jun
    [14, 24, 38, 56],    # Jul
    [15, 24, 36, 53],    # Aug
    [14, 23, 35, 50],    # Sep
    [12, 22, 35, 50],    # Oct
    [ 9, 17, 30, 45],    # Nov
    [ 8, 15, 27, 43],    # Dec
], dtype=np.float64)*u.percent
clouds_ref= np.array([0., 20., 40., 60., 80., 100.])*u.percent
clouds_refmid = (clouds_ref[1:]+clouds_ref[:-1])/2
clouds  = 100*u.percent - (100*u.percent - clouds_raw*1.5)*(6/8)
clouds  = np.where(clouds > 100*u.percent, 100*u.percent, clouds)
clouds  = np.hstack((    # normalize by add before 0 and after 100
    np.full(clouds.shape[0], 0)[:, np.newaxis]*u.percent,
    clouds,
    np.full(clouds.shape[0], 100.)[:, np.newaxis]*u.percent)
)
clouds_samples_fac : int = 4    # 4 becuase 0.75*4 is an integer
clouds_samples = [    # generate samples according to the CDF described by cloud
    np.concatenate([     # CDF: Cumulative distribution function
        np.linspace(clouds_ref[i], clouds_ref[i+1], int(chance.value*clouds_samples_fac))
        for i, chance in enumerate(np.diff(cloud))
    ]) for cloud in clouds
]
# average cloud intensity
cloudy_def : int = 8/16*100*u.percent    # cloudy def: > 50.00% of the sky is covered by clouds
cloud_p = np.array([
    np.count_nonzero(sample > cloudy_def) / sample.size
    for sample in clouds_samples])*100*u.percent
# exaggerate differences from average cloud chance for gameplay purposes
cloud_p = np.mean(cloud_p) + (cloud_p - np.mean(cloud_p))*2
cloudy_mean = np.mean(np.concatenate(clouds_samples))
cloud_v = np.array([    # exaggerate cloudiness differences in-between seasons for gameplay purposes
    (cloudy_mean - 3*(cloudy_mean - np.mean(sample))).to_value(u.dimensionless_unscaled)
    for sample in clouds_samples
]) * 100*u.percent - 6.25*u.percent
# cloud_d = np.array([
#     np.std(sample[sample > cloudy_def])
#     for sample in clouds_samples
# ])


ss = {
    'vintro'   : {'indeksoj': [11,  0,  1]},
    'printempo': {'indeksoj': [ 2,  3,  4]},
    'somero'   : {'indeksoj': [ 5,  6,  7]},
    'awtuno'   : {'indeksoj': [ 8,  9, 10]},
}

for k in ss.keys():
    ss[k]['T_min_v'] = np.min(T_min[ss[k]['indeksoj']])*0.75 + np.mean(T_min[ss[k]['indeksoj']])*0.25
    ss[k]['T_min_d'] =(np.std(T_min[ss[k]['indeksoj']])**2 + (np.mean((T_avg - Tr_min)[ss[k]['indeksoj']])/4)**2)**0.5
    ss[k]['T_max_v'] = np.max(T_max[ss[k]['indeksoj']])*0.75 + np.mean(T_max[ss[k]['indeksoj']])*0.25
    ss[k]['T_max_d'] =(np.std(T_max[ss[k]['indeksoj']])**2 + (np.mean((Tr_max - T_avg)[ss[k]['indeksoj']])/4)**2)**0.5
    ss[k]['rain_p' ] = np.mean(rain_p[ss[k]['indeksoj']])
    ss[k]['rain_v' ] = np.mean(rain_v[ss[k]['indeksoj']])
    ss[k]['rain_d' ] = (np.std(rain_v[ss[k]['indeksoj']])*1.5+np.std(rain_v)*0.5)
    # exaggerate differences from average for gameplay purposes
    ss[k]['cloud_p' ] = np.mean(cloud_p[ss[k]['indeksoj']])
    ss[k]['cloud_v' ] = np.mean(cloud_v[ss[k]['indeksoj']])
    ss[k]['cloud_d' ] = np.std(np.concatenate([
        clouds_samples[index][clouds_samples[index] > cloudy_def]
        for index in ss[k]['indeksoj']
    ])) * (0.5 + 1.0 * ss[k]['cloud_v' ]/cloudy_mean)



if __name__ == '__main__':
    for k in ss.keys():
        print(f"{k}")
        print(f"\tT_min: \t{ss[k]['T_min_v'] :6.3f} +/- {ss[k]['T_min_d'] :6.3f}")
        print(f"\tT_max: \t{ss[k]['T_max_v'] :6.3f} +/- {ss[k]['T_max_d'] :6.3f}")
        print(f"\tCloud: \t({ss[k]['cloud_p']:7.3f} )  {ss[k]['cloud_v']:7.3f} +/- {ss[k]['cloud_d']:6.3f}")
        print(f"\tRain : \t({ss[k]['rain_p'] :7.3f} )  {ss[k]['rain_v'] :7.3f} +/- {ss[k]['rain_d'] :6.3f}")
    
    if False:    # commented
        plt.plot(T_min, label='T_min')
        plt.plot(T_max, label='T_max')
        plt.plot(T_avg, label='T_avg')
        plt.plot(Tr_min, label='Tr_min')
        plt.plot(Tr_max, label='Tr_max')
        plt.legend()