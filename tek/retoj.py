#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Networks specification details and verification:
Analysis of train/truck engine's ability to haul cars.

Code author: HomeOnMars



----------------------------------------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2024 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

----------------------------------------------------------------------------------------------------------------
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
MLu = u.MLu
# U = u.U
UoSx = u.UoSx
kphx = u.kph_csl
ton = u.t_csl
# percent = units.percent
pojentvo = 1/256 * 100 * units.percent
people = units.dimensionless_unscaled

# load_per_FEU = 20 * ton    # 20t per trailer / DKU/FEU / 2 NKU/TEU; note default CSL2 is 25t per FEU
# note: in CSL2, by default,
#    truck can carry 1 DKU/FEU;
#    freight train can carry 12 DKU/FEUs;
#    container ships can carry 7(height)*6(width)*5(length)+6*5*0.5=225 DKU/FEUs;
#    assuming 20t per DKU, this means truck / train / ships should carry 20t / 240t / 4500t goods.
# Planned adjustments:
#    adjust trains to carry 24 DKUs (with 24 trailers and 1 engine;
#        as 2u/16m per trailer, this means a 400m long train; reserve 56u/448m for rail junctions)
#        480t goods per train
#    adjust cargo airplanes to carry 5 DKU-equivalent weight (i.e. 100t goods per plane)
#    adjust container ships to carry 216 DKU (i.e. 4320t goods per ship, or 9 trains per ship);

def n_car_f(
    v, grad,
    load_full = 40*ton,    # cargo+trailer weight
    load_capa = 20*ton,    # cargo weight alone (per FEU container)
    engine_p = 0x46*MLu,   #6760*hp,    # engine power  (ref: see <https://en.wikipedia.org/wiki/British_Rail_Class_92>)
    engine_m = 120*ton,    # engine weight (ref: see <https://en.wikipedia.org/wiki/British_Rail_Class_92>)
    car_len  = 18*u.m_csl,     # length per train car
    C_rr = 0.0003,     # rolling resistence (see <https://en.wikipedia.org/wiki/Rolling_resistance#Rolling_resistance_coefficient_examples>)
    #    for air resistence calc, see this article here <https://www.engineeringtoolbox.com/drag-coefficient-d_627.html>
    C_d  = 0.2, # drag coefficient- for high speed trian, see <https://iopscience.iop.org/article/10.1088/1757-899X/184/1/012015/pdf> table 1.
    rho_air = 1.225*units.kg/units.m**3,    # air density
    A_d  = (3*4/2*u.m_csl**2).to(units.m**2),    # frontal area (for calc air drag)
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
    A_d  = (3*4/2*u.m_csl**2).to(units.m**2),     # frontal area (for calc air drag)
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
    max_v = (max_v * (units.m / units.s)).to(UoSx)
    return max_v


def print_info(**params):
    txt = f"\t{params = }"
    if 'grad' in params:
        txt += f"\n\t\tgrad =  {presi_Hx(params['grad'].to_value(pojentvo), sc=4, e_sep=''):>8}⌄⌄\t={params['grad'].to(units.percent):8.3f}"
    if 'v' in params:
        n_car, capa, length = n_car_f(**params)
        txt += f"\n\t\tv =  {presi_Hx(params['v'].to_value(UoSx), sc=4, e_sep=''):>8} UoSx\t={params['v'].to(kphx):8.2f}"
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
        'engine_p': 0x60*MLu, # 9300*hp,
        'A_d': (3.5*5.5/2.5*u.m_csl**2).to(units.m**2),
    }
    print_info(grad=  0*pojentvo, v=0x38*UoSx, **KE_pars)
    print_info(grad=  4*pojentvo, v=0x20*UoSx, **KE_pars)
    print_info(grad=9.5*pojentvo, v=0x10*UoSx, **KE_pars)
    print_info(grad=0xE*pojentvo, v= 0xB*UoSx, **KE_pars)


    print("\nHigh Speed Rail (per car)\n")
    # Using China Railway CRH3 (Velaro CN) info as reference / rough guideline
    #   see <https://pedestrianobservations.com/2012/03/13/table-of-train-weights>
    #   see also <https://en.wikipedia.org/wiki/China_Railway_CRH3>
    #   Engine power exaggerated from 772hp (for a 24m car with a power ratio of 24kW/t) to 1700hp
    #   Also assuming proper frontal design reducing effective area for air drag
    #   And assuming lighter full load weight load_full=40t instead of more realistic 56t estimate
    #   Because we are amazing
    V_pars = {
        'engine_p' : 0x12*MLu, # 1744*hp,
        'engine_m' : 0*ton,
        'load_full': 40*ton,
        'load_capa': 120*people,
        'car_len'  : 24*u.m_csl,
        'A_d': (3.5*5.5/6*u.m_csl**2).to(units.m**2),
    }
    # # Case: 'engine_p' : 0x10*MLu
    # print_info(grad=   0*pojentvo, v=0x80*UoSx, **V_pars)
    # print_info(grad=   4*pojentvo, v=0x60*UoSx, **V_pars)
    # print_info(grad=   5*pojentvo, v=0x5B*UoSx, **V_pars)
    # print_info(grad= 9.5*pojentvo, v=0x40*UoSx, **V_pars)
    # print_info(grad= 0xB*pojentvo, v=0x3A*UoSx, **V_pars)
    # print_info(grad= 0xE*pojentvo, v=0x2F*UoSx, **V_pars)
    # print_info(grad=0x12*pojentvo, v=0x26*UoSx, **V_pars)
    # print_info(grad=0x15*pojentvo, v=0x20*UoSx, **V_pars)
    # print_info(grad=0x20*pojentvo, v=0x16*UoSx, **V_pars)

    # # Case: 'engine_p' : 0x12*MLu
    print_info(grad=   0*pojentvo, v=0x86*UoSx, **V_pars)
    print_info(grad=   5*pojentvo, v=0x60*UoSx, **V_pars)
    print_info(grad= 0xB*pojentvo, v=0x40*UoSx, **V_pars)
    print_info(grad= 0xF*pojentvo, v=0x32*UoSx, **V_pars)
    print_info(grad=0x12*pojentvo, v=0x2A*UoSx, **V_pars)
    print_info(grad=0x18*pojentvo, v=0x20*UoSx, **V_pars)
    print_info(grad=0x20*pojentvo, v=0x18*UoSx, **V_pars)


    print("\nMetro (per car)\n")
    #   Engine power exaggerated from 772hp (for a 24m car with a power ratio of 24kW/t) to "only" 1200hp
    #       Note: third rail cannot support high speed (>160kph),
    #       so 200kph is only for train tracks with overhead wires (not for in-game metro tracks)
    E_pars = {
        'engine_p' : 0xC*MLu, # 1163*hp,
        'engine_m' : 0*ton,
        'load_full': 35*ton,
        'load_capa': 204*people,
        'car_len'  : 24*u.m_csl,
        'A_d': (3.5*4/1.5*u.m_csl**2).to(units.m**2),
    }
    print_info(grad=   0*pojentvo, v=0x50*UoSx, **E_pars)
    print_info(grad= 0xA*pojentvo, v=0x30*UoSx, **E_pars)
    print_info(grad= 0xF*pojentvo, v=0x24*UoSx, **E_pars)
    print_info(grad=0x14*pojentvo, v=0x1C*UoSx, **E_pars)


    print("\nTram (per car)\n")
    T_pars = {
        'engine_p' : 6*MLu, # 581*hp,
        'engine_m' : 0*ton,
        'load_full': 20*ton,
        'load_capa': 90*people,
        'car_len'  : 12*u.m_csl,
        'A_d': (3*4/1.5*u.m_csl**2).to(units.m**2),
    }
    print_info(grad=   0*pojentvo, v=0x44*UoSx, **T_pars)
    print_info(grad=0x18*pojentvo, v=0x15*UoSx, **T_pars)
    print_info(grad=0x20*pojentvo, v=0x10*UoSx, **T_pars)
    print_info(grad=0x40*pojentvo, v= 0x8*UoSx, **T_pars)


    print("\nRoad\n")
    # As the rubber-on-asphalt(wet) static friction coeff is ~0.5 (<https://en.wikibooks.org/wiki/Physics_Study_Guide/Frictional_coefficients>)
    #   max grad should be <= 50 % to prevent wheelslip
    
    # Assuming more powerful trucks: 775hp (instead of 600hp realistic estimate
    #   (See Iveco Eurocargo specifications <https://www.iveco.com/Eurocargo>
    #   <https://static.iveco.com.au/download/media%2F5524d082-2a03-40c0-96de-9d6ab73f3681.pdf/Eurocargo%20Specifications.pdf>
    #   For Engine Maximum Output, GVM (Gross Vehicle Mass) and GCM (Gross Combination Mass) info))
    W_pars = {    # Semi truck
        'engine_p' : 9*MLu, # 775*hp, # Semi truck
        # 'engine_m' : 5*ton,
        'load_full': 40*ton,    # Semi truck
        # 'load_full': 35*ton,    # box truck
        'C_rr': 0.006,
        'C_d' : 0.8,
        'A_d': (2*3/1.25*u.m_csl**2).to(u.m**2),
    }
    print_info(grad=   0*pojentvo, **W_pars)
    print_info(grad= 0xA*pojentvo, **W_pars)
    print_info(grad= 0xD*pojentvo, **W_pars)
    print_info(grad=0x12*pojentvo, **W_pars)
    print_info(grad=0x18*pojentvo, **W_pars)
    print_info(grad=0x20*pojentvo, **W_pars)
    print_info(grad=0x28*pojentvo, **W_pars)
    print_info(grad=0x40*pojentvo, **W_pars)
    print_info(grad=0x60*pojentvo, **W_pars)


    print("\nLocal Road\n")
    W_pars = {    # private cars
        'engine_p' : 1*MLu, # 97*hp,
        'load_full': 2.5*ton,
        'C_rr': 0.006,
        'C_d' : 0.8,
        'A_d': (2*1.5/1.25*u.m_csl**2).to(u.m**2),
    }
    print_info(grad=   0*pojentvo, **W_pars)
    print_info(grad= 0xA*pojentvo, **W_pars)
    print_info(grad= 0xD*pojentvo, **W_pars)
    print_info(grad=0x12*pojentvo, **W_pars)
    print_info(grad=0x18*pojentvo, **W_pars)
    print_info(grad=0x20*pojentvo, **W_pars)
    print_info(grad=0x28*pojentvo, **W_pars)
    print_info(grad=0x40*pojentvo, **W_pars)
    print_info(grad=0x60*pojentvo, **W_pars)


    print("\nBike\n")
    # Ref: <https://en.wikipedia.org/wiki/Electric_bicycle#Range> (2025-12-30)
    B_pars = {    # e-bike
        'load_full': 5/32*ton,   # 156.25*u.kg_csl
        'engine_p' : 4/0x100*MLu,   # approx 1129*u.W
        'C_rr': 0.007,
        'C_d' : 0.7,
        'A_d': (0.4*u.m**2),
    }
    print_info(grad=   0*pojentvo, **B_pars)
    print_info(grad=0x12*pojentvo, **B_pars)
    print_info(grad=0x20*pojentvo, **B_pars)
    print_info(grad=0x28*pojentvo, **B_pars)
    print_info(grad=0x40*pojentvo, **B_pars)

#---------------------------------------------------------------------------------------------------------------
