#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Networks specification details and verification:
Analysis of train/truck engine's ability to haul cars.

Code author: HomeOnMars



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
from numpy import sqrt, sin, cos, pi
from astropy import units
from astropy import constants as const
if __package__:
    from .unuoj import u, presi_Hx
else:
    from  unuoj import u, presi_Hx

# getting how many containers/trailers can a train engine haul
g = const.g0
hp = units.imperial.hp
JLu = u.JLu    # power unit name provisional
U = u.U
kph  = u.kph
JoGx = u.JoGx
kphx = (1*u.kph * (U / (8*u.m))).to(u.kph)
ton = u.MP / 24    # 1 gp ~ 1.49563 t
percent = units.percent


# load_per_FEU = 24 * ton    # 24t per trailer / FEU / 2TEU; note default CSL2 is 25t per FEU
# note: in CSL2, by default,
#    truck can carry 1 FEU;
#    freight train can carry 12 FEUs;
#    container ships can carry 7(height)*6(width)*5(length)+6*5*0.5=225 FEUs;
#    assuming 24t per FEU, this means truck / train / ships should carry 24t / 288t / 5400t goods.
# Planned adjustments:
#    adjust trains to carry 24 FEUs (with 24 trailers and 1 engine;
#        as 2u/16m per trailer, this means a 400m long train; reserve 56u/448m for rail junctions)
#        576t goods per train
#    adjust cargo airplanes to carry 5 FEU-equivalent weight (i.e. 120t goods per plane)
#    adjust container ships to carry 224 FEUs (i.e. 5376t goods per ship, or 9.33 trains per ship);

def n_car_f(
    v, grad,
    load_full = 40*ton,    # cargo+trailer weight
    load_capa = 24*ton,    # cargo weight alone (per FEU container)
    engine_p = 0x7D0*JLu,   #6760*hp,    # engine power  (ref: see <https://en.wikipedia.org/wiki/British_Rail_Class_92>)
    engine_m = 120*ton,    # engine weight (ref: see <https://en.wikipedia.org/wiki/British_Rail_Class_92>)
    car_len  = 2*U,     # length per train car
    C_rr = 0.0003,     # rolling resistence (see <https://en.wikipedia.org/wiki/Rolling_resistance#Rolling_resistance_coefficient_examples>)
    #    for air resistence calc, see this article here <https://www.engineeringtoolbox.com/drag-coefficient-d_627.html>
    C_d  = 0.2, # drag coefficient- for high speed trian, see <https://iopscience.iop.org/article/10.1088/1757-899X/184/1/012015/pdf> table 1.
    rho_air = 1.225*units.kg/units.m**3,    # air density
    A_d  = (3*4/2*(U/8)**2).to(u.m**2),    # frontal area (for calc air drag)
):
    """Calc how many cars can this train engine haul."""
    #n_car = (engine_p / ((grad/sqrt(1+grad**2) + (1.+air_fac)*C_rr/sqrt(1+grad**2))*load_full*g*v) - engine_m/load_full).si
    n_car = (
        engine_p / v / (
            # gravity and rolling resistance force
            (grad/sqrt(1+grad**2) + C_rr/sqrt(1+grad**2))*load_full*g
            # air drag force
            + 0.5 * C_d * rho_air * A_d * v**2
        )
        - engine_m/load_full
    ).si
    # how much cargo (in tons) can this train engine haul
    capa  = int(n_car)*load_capa
    # how long will this train (part) be
    length= int(n_car+1)*car_len    # +1 to account train engine itself
    return n_car, capa, length


def max_v_f(
    grad,
    load_full,  # total vehicle weight
    engine_p,   # engine power
    C_rr = 0.0003,  # rolling resistence
    C_d  = 0.2,     # drag coefficient
    rho_air = 1.225*units.kg/units.m**3,    # air density
    A_d  = (3*4/2*(U/8)**2).to(u.m**2),     # frontal area (for calc air drag)
):
    """Calc max speed for this vehicle on the specified grads"""
    # n_car = (
    #     engine_p / v / (
    #         # gravity and rolling resistance force
    #         (grad/sqrt(1+grad**2) + C_rr/sqrt(1+grad**2))*load_full*g
    #         # air drag force
    #         + 0.5 * C_d * rho_air * A_d * v**2
    #     )
    # ).si
    max_v_eq = np.polynomial.Polynomial([
        -engine_p.si.value,
        (
            (grad/sqrt(1+grad**2) + C_rr/sqrt(1+grad**2))*load_full*g
        ).si.value,  # * v
        0,  # * v**2
        (0.5 * C_d * rho_air * A_d).si.value,  # * v**3
    ])
    max_v_eq_roots = max_v_eq.roots()
    max_v_roots = [
        v for v in max_v_eq_roots[np.isreal(max_v_eq_roots)] if v > 0]
    if len(max_v_roots) != 1:
        # something went wrong
        print(f"Error: root finding failed (v solved to be {max_v_roots})")
    max_v = max_v_roots[0].real if len(max_v_roots) else np.nan
    max_v = (max_v * (u.m / u.s)).to(JoGx)
    return max_v


def print_info(**params):
    txt = f"\t{params = }"
    if 'v' in params:
        n_car, capa, length = n_car_f(**params)
        txt += f"\n\t\tv =  {presi_Hx(params['v'].to_value(JoGx), sc=4, e_sep=''):>8} JoGx\t={params['v'].to(kphx):8.2f}"
        txt += f"\n\t{n_car = :6.3f}\t{capa = :4.0f}\t{length = :4.0f}\n"
    else:
        max_v = max_v_f(**params)
        txt += f"\n\tmax_v = {presi_Hx(max_v, sc=4, e_sep='')}  |  {max_v.to(kphx):6.3f}\n"
    print(txt)
    return txt


if __name__ == '__main__':
    # Assuming more powerful electric trains: 9500hp (in contrast to 6760hp realistic estimate
    #   (from UK class 92 electric freight locomotive <https://en.wikipedia.org/wiki/British_Rail_Class_92> ))
    # remember we need to drag 24 cars, so n_car > 24 is minimum.
    #
    # For "per car" cases, we need to pull the car itself, so n_car must >= 1

    print("\nRail\n")
    # As the steel-on-steel static friction coeff is only 0.15~0.6 (<https://hypertextbook.com/facts/2005/steel.shtml>),
    #   max grad should be <= 15% (on the safe side) to prevent wheelslip
    #   for all kinds of adhesive rails
    #       (It's mostly 0.4 (which means max 40% grad),
    #       but just in case someone put oil on it
    #       reducing it to 0.15 (<https://www.engineeringtoolbox.com/friction-coefficients-d_778.html>),
    #       let's go with 15%)
    KE_pars = {
        'engine_p': 0xB00*JLu, #(9500*hp).to(hp),
    }
    print_info(grad=0.0*percent, v=0xBE*JoGx, **KE_pars)
    print_info(grad=1.6*percent, v=0x60*JoGx, **KE_pars)
    print_info(grad=3.6*percent, v=0x30*JoGx, **KE_pars)
    print_info(grad=5.5*percent, v=0x20*JoGx, **KE_pars)


    print("\nHigh Speed Rail (per car)\n")
    # Using China Railway CRH3 (Velaro CN) info as reference / rough guideline
    #   see <https://pedestrianobservations.com/2012/03/13/table-of-train-weights>
    #   see also <https://en.wikipedia.org/wiki/China_Railway_CRH3>
    #   Engine power exaggerated from 772hp (for a 24m car with a power ratio of 24kW/t) to 1700hp
    #   Also assuming proper frontal design reducing effective area for air drag
    #   And assuming lighter full load weight load_full=48t instead of more realistic 56t estimate
    #   Because we are amazing
    V_pars = {
        'engine_p' : 0x200*JLu, #(1726*hp).to(hp),
        'engine_m' : 0*ton,
        'load_full': 48*ton,
        'car_len'  : 3 * U,
        'A_d': (3*4/3.5*(U/8)**2).to(u.m**2),
    }
    print_info(grad=0.0*percent, v=0x188*JoGx, **V_pars)
    print_info(grad=1.5*percent, v=0x120*JoGx, **V_pars)
    print_info(grad=2.0*percent, v=0x100*JoGx, **V_pars)
    print_info(grad=2.6*percent, v=0xE0*JoGx, **V_pars)
    print_info(grad=3.3*percent, v=0xC0*JoGx, **V_pars)
    print_info(grad=4.2*percent, v=0xA0*JoGx, **V_pars)
    print_info(grad=5.5*percent, v=0x80*JoGx, **V_pars)
    print_info(grad=7.5*percent, v=0x60*JoGx, **V_pars)
    print_info(grad=23.5*percent,v=0x20*JoGx, **V_pars)


    print("\nMetro (per car)\n")
    #   Engine power exaggerated from 772hp (for a 24m car with a power ratio of 24kW/t) to "only" 1200hp
    #       Note: third rail cannot support high speed (>160kph),
    #       so 200kph is only for train tracks with overhead wires (not for in-game metro tracks)
    E_pars = {
        'engine_p' : 0x160*JLu, #(1200*hp).to(hp),
        'engine_m' : 0*ton,
        'load_full': 45*ton,
        'car_len'  : 3 * U,
    }
    print_info(grad=0.0*percent, v=0x11F*JoGx, **E_pars)
    print_info(grad=3.5*percent, v=0x88*JoGx, **E_pars)
    print_info(grad=5.4*percent, v=0x60*JoGx, **E_pars)
    print_info(grad=7.3*percent, v=0x48*JoGx, **E_pars)


    print("\nTram (per car)\n")
    T_pars = {
        'engine_p' : 0xF0*JLu, #(810*hp).to(hp),
        'engine_m' : 0*ton,
        'load_full': 26*ton,
        'load_capa': 16*ton,
        'car_len'  : 1.5 * U,
    }
    print_info(grad= 0.0*percent, v=0xFC*JoGx, **T_pars)
    print_info(grad= 9.6*percent, v=0x40*JoGx, **T_pars)
    print_info(grad=13.0*percent, v=0x30*JoGx, **T_pars)
    print_info(grad=20.0*percent, v=0x20*JoGx, **T_pars)


    print("\nRoad\n")
    # As the rubber-on-asphalt(wet) static friction coeff is ~0.5 (<https://en.wikibooks.org/wiki/Physics_Study_Guide/Frictional_coefficients>)
    #   max grad should be <= 50 % to prevent wheelslip
    
    # Assuming more powerful trucks: 863hp (instead of 600hp realistic estimate
    #   (See Iveco Eurocargo specifications <https://www.iveco.com/Eurocargo>
    #   <https://static.iveco.com.au/download/media%2F5524d082-2a03-40c0-96de-9d6ab73f3681.pdf/Eurocargo%20Specifications.pdf>
    #   For Engine Maximum Output, GVM (Gross Vehicle Mass) and GCM (Gross Combination Mass) info))
    W_pars = {
        'engine_p' : 0x100*JLu, #(863*hp).to(hp),
        # 'engine_m' : 5*ton,
        # 'load_full': 40*ton,    # Semi truck (5/3*u.MP)
        'load_full': 34.4*ton,    # box truck (23/16*u.MP)
        'C_rr': 0.006,
        'C_d' : 0.8,
        'A_d': (2*3/1.25*(U/8)**2).to(u.m**2),
    }
    print_info(grad=0*percent, **W_pars)
    print_info(grad=3.7*percent, **W_pars)
    print_info(grad=5.1*percent, **W_pars)
    print_info(grad=7.0*percent, **W_pars)


    print("\nLocal Road\n")
    
    print_info(grad=10*percent, **W_pars)
    print_info(grad=15*percent, **W_pars)
    print_info(grad=21*percent, **W_pars)
    print_info(grad=33*percent, **W_pars)


    print("\nBike\n")
    # Ref: <https://en.wikipedia.org/wiki/Electric_bicycle#Range> (2025-12-30)
    B_pars = {
        'load_full': 0.1171875*ton,   # 1.25*u.JP
        'engine_p' : 5/16*JLu,   # approx 786*u.W
        'C_rr': 0.007,
        'C_d' : 0.7,
        'A_d': (0.4*u.m**2),
    }
    print_info(grad=0*percent, **B_pars)
    print_info(grad=4*percent, **B_pars)
    print_info(grad=7*percent, **B_pars)
    print_info(grad=11*percent, **B_pars)
    print_info(grad=15*percent, **B_pars)
    print_info(grad=21*percent, **B_pars)

#------------------------------------------------------------------------------
