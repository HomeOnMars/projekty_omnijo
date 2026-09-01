#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RO Standard Unit System *UnuXitʌ Omnijo* Calculations and Hexadecimal Utilities

Code author: HomeOnMars



----------------------------------------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2025 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

----------------------------------------------------------------------------------------------------------------
"""

from datetime import datetime, timedelta, UTC
from typing import Self
import numpy as np
from numpy import pi, e
from astropy import constants as const
from astropy import units
from astropy.units import UnitConversionError
from astropy.coordinates import EarthLocation
POVI_HEALPY: bool = False
try:
    import healpy
    POVI_HEALPY = True
except ModuleNotFoundError as e:
    print(
        f"Warning: healpy not found ({e})\n",
        "post-code related calculations are disabled.")
    






# === Hexadecimal ===



# Note: '-' and '#' must not in below dicts

# base 0x10
HX_SYMBOLS_DICT : dict[str, dict[str, int]] = {
    'ASCII': {k: int(k, base=16) for k in '0123456789ABCDEFabcdef'},
    'ONKIO': {k: i for i, k in enumerate('0123456789ΔλΠΣΥΨ')},
}
HX_SYMBOLS_DICT['ASCII']['Z'] = HX_SYMBOLS_DICT['ASCII']['z'] = 0xD
HX_SYMBOLS_DICT['ASCII']['Y'] = HX_SYMBOLS_DICT['ASCII']['y'] = 0xE
HX_SYMBOLS_DICT['ASCII']['W'] = HX_SYMBOLS_DICT['ASCII']['w'] = 0xF
HX_SYMBOLS = HX_SYMBOLS_DICT['ASCII'] | HX_SYMBOLS_DICT['ONKIO']

HX_SYMBOLS_INV_DICT = {
    c: {v: k for k, v in HX_SYMBOLS_DICT[c].items()}
    for c in {'ONKIO'}
}
HX_SYMBOLS_INV_DICT['ASCII'] = {
    HX_SYMBOLS_DICT['ASCII'][k]: k
    for k in '0123456789ABCZYW'
}
HX_SYMBOLS_INV = HX_SYMBOLS_INV_DICT['ONKIO']

# base 0x20
TX_SYMBOLS_DICT : dict[str, dict[str, int]] = {
    'ASCII': {k: i for i, k in enumerate('0123456789ABCZYWDEFGHJKMNPQRSTUX')},
    'ONKIO': {k: i for i, k in enumerate('0123456789ΔλΠΣΥΨĈEFGHJKMNPQRŜTUX')},
}
TX_SYMBOLS = TX_SYMBOLS_DICT['ASCII'] | TX_SYMBOLS_DICT['ONKIO']
TX_SYMBOLS_INV_DICT = {
    c: {v: k for k, v in TX_SYMBOLS_DICT[c].items()}
    for c in {'ASCII', 'ONKIO'}
}
TX_SYMBOLS_INV = TX_SYMBOLS_INV_DICT['ONKIO']

# base 0x40
#   set(' .\\/:*?\"<>|&')    # forbidden chars
RX_SYMBOLS_DICT : dict[str, dict[str, int]] = {
    'ASCII': {
        k: i for i, k in enumerate(
            '0123456789ABCZYW'
            '[!]#$%V\'()L+,-IO'
            '`abcdefghijklmno'
            'pqrstuvwxyz{@}~_'
        )
    },
    'ONKIO': {
        k: i for i, k in enumerate(
            '0123456789ΔλΠΣΥΨ'
            '_!~#、@\'%=()+⌄−^—'
            '‐abcdefghijklmno'
            'pqrstuvŭxʌzĉĝĵŝ,'
        )
    },
}
RX_SYMBOLS = RX_SYMBOLS_DICT['ASCII'] | RX_SYMBOLS_DICT['ONKIO']
RX_SYMBOLS_INV_DICT = {
    c: {v: k for k, v in RX_SYMBOLS_DICT[c].items()}
    for c in {'ASCII', 'ONKIO'}
}
RX_SYMBOLS_INV = RX_SYMBOLS_INV_DICT['ONKIO']

ALL_SYMBOLS_DICT = {
    chrset: (
        TX_SYMBOLS_DICT[chrset] |
        RX_SYMBOLS_DICT[chrset]
    )
    for chrset in TX_SYMBOLS_DICT
}



# translate Epopo characters to ASCII characters using x-system
ASCIIIFY_CHR = {
    'Ĉ': 'Cx','ĉ': 'cx',
    'Ĝ': 'Gx','ĝ': 'gx',
    'Ĵ': 'Jx','ĵ': 'jx',
    'Ŝ': 'Sx','ŝ': 'sx',
    'Ž': 'Zx','ž': 'zx',
    'Ŭ': 'W', 'ŭ': 'w',
    'Ʌ': 'Y', 'ʌ': 'y',
    '⚻': 'tago',  # capitalized ver already defined
    '⚝': 'Se',
    '☾': 'Monato',
    '⚡': 'potenco',   # word ver (no capitalizing, no prefix)
    '°': 'Deg',
    '🪙': 'OSR',
    chr(0x332): '_',
    '⌄': 'projento',    # capitalized ver already defined
}
ASCIIIFY = {ord(k): v for k, v in ASCIIIFY_CHR.items()}



def Hx(
    n: str,
    base: int = 0x10,
    symbols: dict = HX_SYMBOLS,
    d_sep = '.',
    k_seps = " ,",
    e_sep = '⌄',    #'p'
) -> float:
    """Convert Hexadecimal str to float.

    d_sep: decimal separator
    k_seps: thousands separators (characters to be ignored)
    e_sep: exponent separator
    """
    if not isinstance(n, str):
        raise TypeError("Input 'n' should be a str.")
    n = n.translate({ord(k): None for k in k_seps})
    n = n.lstrip()

    # sign (+/-)
    sign = 1.
    if n and n[0] in {'+'}:
        # remove plus sign
        n = n[1:]
    elif n and n[0] in {'-', chr(0x2212)}:
        sign = -1.
        n = n[1:]
    
    # exponent parts
    ns = n.split(e_sep)
    if len(ns) > 2:
        raise ValueError("Multiple exponent separator detected")
    if len(ns) > 1:
        unit = float(base)**Hx(
            ns[1], base=base, symbols=symbols,
            d_sep=d_sep, k_seps=k_seps, e_sep=e_sep)
        n = ns[0]
    else:
        unit = 1.
        n = ns[0]
        
    # decimal parts
    ns = n.split(d_sep)
    if len(ns) > 2:
        raise ValueError("Multiple decimal separator detected")
    ans = 0.
    for i, v in enumerate(ns[0]):
        p = len(ns[0]) - i - 1
        ans += symbols[v] * base**p
    if len(ns) > 1:
        for i, v in enumerate(ns[1]):
            p = -i - 1
            ans += symbols[v] * base**p
            
    ans *= sign * unit
    return ans

def Tx(n:str, symbols:dict=TX_SYMBOLS, **kwargs) -> float:
    """Convert Base Dx32 str to float.
    
    See Hx() for more info.
    """
    return Hx(n, base=0x20, symbols=symbols, **kwargs)

def Rx(n:str, symbols:dict=RX_SYMBOLS, **kwargs) -> float:
    """Convert Base Dx64 str to float.
    
    See Hx() for more info.
    """
    return Hx(n, base=0x40, symbols=symbols, **kwargs)



def presi_Hx(
    n: float|units.Quantity,
    sc: int = 0x80,
    stop_when_precise: bool = True,
    base: int = 0x10,
    symbols_inv: dict = HX_SYMBOLS_INV,
    d_sep: str = '.',
    e_sep: None|str = None, # '⌄',
    plus_sign: str = "",
    prefix: None|str = None,
    prefix_default: str = 'Hx ',
    **kwargs,
) -> str:
    """Convert Hexadecimal float to str.

    To output without ⌄-notation, set e_sep=''

    Warning: last digit may be an underestimate
    Warning: NOT suitable for long large integers when e_sep=''

    with ⌄-notation (e_sep='⌄'), max supported numbers are about ~'F.FFFF FFFF FF ⌄FF'
        min ~'1⌄-10C'
    
    sc: signifaj ciferoj, or significant digits

    d_sep: decimal separator

    e_sep: exponent separator.
        if None, will use '' if the number is close to 1,
        '⌄' if the number is very large or small.

    plus_sign: str
        set it to "+" to add plus sign when n is not negative

    prefix: prefix string for output
    prefix_default: str
        if None, will use `prefix_default` if n is astropy units, else ''.

    """
    
    # init and checks

    if sc < 1: raise ValueError("Significant digits 'sc' must >= 1.")

    if prefix is None:
        prefix = prefix_default if isinstance(n, units.Quantity) else ''

    if isinstance(n, units.Quantity):
        ans_v = presi_Hx(
            n.value, **{k: v for k, v in locals().items() if k not in {'n'}},
        )
        return f"{ans_v} {n.unit}"    # prefix already added

    # n = np.float64(n)
    sign = n >= 0
    n = abs(n)
    if n == 0:
        return (
            f"{prefix}{plus_sign}0{e_sep}+0" if e_sep
            else f"{prefix}{plus_sign}0")
    if e_sep is None: e_sep = '⌄' if n < 0x10**(-4) or n > 16**4 else ''
    base = np.float64(base)
    log2_base = np.log2(base)
    # grandordo = order of magnitude
    grandordo = np.int64(np.floor(np.log2(n) / log2_base))

    if len(grandordo.shape):
        # input is an array
        raise NotImplementedError("Array input not yet implemented.")

    ans = plus_sign if sign else "-"
    if grandordo < 0 and not e_sep:
        ans += symbols_inv[0] + d_sep + symbols_inv[0]*(-grandordo-1) # "0.0*"

    for i in range(sc if e_sep else max(grandordo+1, sc)):
        
        unit = base**(grandordo-i)
        v = int(np.floor(n / unit))
        n -= v * unit
        ans += symbols_inv[v]
        if stop_when_precise and not n and (e_sep or i >= grandordo):
            break
        if (e_sep and i == 0) or (not e_sep and i == grandordo):
            ans += d_sep
        
    if e_sep:
        ordo = presi_Hx(
            grandordo, sc=0x100, stop_when_precise=True,
            base=base, symbols_inv=symbols_inv, d_sep=d_sep, e_sep='')
        ans += f"{e_sep}{ordo}"
    
    return prefix + ans

def presi_Tx(
    n: float|units.Quantity,
    prefix_default: str = 'Tx ',
    e_sep: None|str = '', # '⌄',
    symbols_inv:dict=TX_SYMBOLS_INV,
    **kwargs,
) -> str:
    """Convert Base Dx32 float to str.

    See presi_Hx() for more info.
    """
    return presi_Hx(
        n, base=0x20, prefix_default=prefix_default, symbols_inv=symbols_inv,
        e_sep=e_sep, **kwargs)

def presi_Rx(
    n: float|units.Quantity,
    prefix_default: str = 'Rx ',
    symbols_inv:dict=RX_SYMBOLS_INV,
    e_sep: None|str = '', # '⌄',
    **kwargs,
) -> str:
    """Convert Base Dx64 float to str.

    See presi_Hx() for more info.
    """
    return presi_Hx(
        n, base=0x40, prefix_default=prefix_default, symbols_inv=symbols_inv,
        e_sep=e_sep, **kwargs)



def factorize(n: int) -> list[int]:
    """Simple helper func to brute-force factorize int."""
    ans = [1]
    leftover = abs(n)
    for i in range(2, leftover+1):
        if leftover % i == 0:
            for j in ans[1:]:    # ignore 1
                if i % j == 0: break
            else:
                ans.append(i)
                leftover = leftover//i
        if i > leftover: break
    return ans



# helper funcs to calc curve degrees from curve radius and back
theta_deg = lambda R, d: np.ceil(2*np.atan(R/d)/np.pi*180)
get_R = lambda theta_deg, d: np.tan(theta_deg/2/180*np.pi)*d






# === Unit System (Base) ===



# --- SI Units ---

# Earth size reference
_WGS84_DEF = (6378137.0*units.m, 6356752.314245*units.m)

# si units
u_si_defs : dict[str, units.UnitBase] = {
    v: getattr(units, v)
    for v in [
        'm', 'cm', 'km', 'Rsun', 'au', 'lyr', 'pc', 'Mpc',
        'kg', 'g', 't',
        's', 'min', 'h', 'd', 'yr',
        'K', 'deg_C',
        'C',
        'percent',
        'rad', 'deg', 'arcmin', 'arcsec',
        'W', 'kW', 'MW', 'GW',  'TW', 'Lsun',
    ]
}
units.def_unit('kph', units.km / units.h, namespace=u_si_defs)
units.def_unit('mph', units.imperial.mi / units.h, namespace=u_si_defs)
units.def_unit(
    'Rearth',
    ((_WGS84_DEF[0]**2*_WGS84_DEF[1])**(1/3)).to(units.km),
    namespace=u_si_defs)
u_si_defs['hp'] = units.imperial.hp



# --- Natural Units ---
# https://en.wikipedia.org/wiki/Natural_units#Planck_units

# u_nat: Planck natural units
u_nat_base : dict[str, units.UnitBase] = {}
u_nat_defs : dict[str, units.UnitBase] = {}
u_nat_base['dist'] = units.def_unit(
    'l_P', (const.hbar * const.G / const.c**3)**0.5,
    namespace=u_nat_defs, format={'latex': r' l_P '})
u_nat_base['mass'] =  units.def_unit(
    'm_P', (const.hbar * const.c / const.G   )**0.5,
    namespace=u_nat_defs, format={'latex': r' m_P '})
u_nat_base['time'] =  units.def_unit(
    't_P', (const.hbar * const.G / const.c**5)**0.5,
    namespace=u_nat_defs, format={'latex': r' t_P '})
u_nat_base['temp'] =  units.def_unit(
    'T_P', (const.hbar * const.c**5 / const.G)**0.5 / const.k_B,
    namespace=u_nat_defs, format={'latex': r' T_P '})
u_nat_base['angl'] = u_nat_defs['rad'] = units.rad



# --- RO Units ---

# u_uxo: RO standard units *UnuXitʌ Omnijo*
u_uxo_prefixes = [
    # Note: prefix only- name may conflict with other unit names
    ('H', ['Hek'   ], 0x10),
    ('J', ['Jent'  ], 0x100),
    ('G', ['Gil'   ], 0x1000),
    ('M', ['Muni'  ], 0x10000),
    ('D', ['Duni'  ], 0x10000**0x2),
    ('T', ['Trini' ], 0x10000**0x3),
    ('R', ['Kvarni'], 0x10000**0x4),
    ('V', ['Kvinni'], 0x10000**0x5),
    ('S', ['Sesni' ], 0x10000**0x6),
    ('E', ['Sepni' ], 0x10000**0x7),
    ('K', ['Okni'  ], 0x10000**0x8),
    ('N', ['Nawni' ], 0x10000**0x9),
    ('A', ['Delni' ], 0x10000**0xA),
    ('B', ['Lomni' ], 0x10000**0xB),
    ('C', ['Nakni' ], 0x10000**0xC),
    ('Z', ['Signi' ], 0x10000**0xD),
    ('L', ['Ganni' ], 0x10000**0xE),
    ('F', ['Fusni' ], 0x10000**0xF),
    ('I', ['Hekni' ], 0x10000**0x10),
    ('h', ['hekon'   ], 0x10**-1),
    ('j', ['jenton'  ], 0x100**-1),
    ('g', ['gilon'   ], 0x1000**-1),
    ('m', ['munion'  ], 0x10000**-1),
    ('d', ['dunion'  ], 0x10000**-0x2),
    ('t', ['trinion' ], 0x10000**-0x3),
    ('r', ['kvarnion'], 0x10000**-0x4),
    ('v', ['kvinnion'], 0x10000**-0x5),
    ('s', ['sesnion' ], 0x10000**-0x6),
    ('e', ['sepnion' ], 0x10000**-0x7),
    ('k', ['oknion'  ], 0x10000**-0x8),
    ('n', ['nawnion' ], 0x10000**-0x9),
    ('a', ['delnion' ], 0x10000**-0xA),
    ('b', ['lomnion' ], 0x10000**-0xB),
    ('c', ['naknion' ], 0x10000**-0xC),
    ('z', ['signion' ], 0x10000**-0xD),
    ('l', ['gannion' ], 0x10000**-0xE),
    ('f', ['fusnion' ], 0x10000**-0xF),
    ('i', ['heknion' ], 0x10000**-0x10),
]
u_uxo_base : dict[str, units.UnitBase] = u_nat_base.copy()
u_uxo_defs : dict[str, units.UnitBase] = {}
#    defs
u_uxo_base['dist'] = units.def_unit(
    # note: 35931 / 3.0 = 11977
    ['U', 'Utro'], 11977 * 2**105 * u_nat_base['dist'],
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['mass'] = units.def_unit(
    ['P', 'Pakmo'], 2**24 * u_nat_base['mass'],
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['time'] = units.def_unit(
    ['Ŝ', 'Ŝekunto'], 35931 * 2**129 * u_nat_base['time'],
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['temp'] = units.def_unit(
    ['Z', 'Zoro'], 10011 * 2**(-120) * u_nat_base['temp'],
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['char'] = units.def_unit(
    ['E', 'Elektrio'], 0x10**0x10/3 * const.e.si,
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['angl'] = units.def_unit(
    ['Ck', 'Cirklo'], 2 * pi * units.rad,
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['xdim'] = units.def_unit(
    # chr(0x332): underscore before char
    [chr(0x332), 'Nuo'], 1 * units.dimensionless_unscaled,
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['byte'] = units.def_unit(
    ['Bit', 'B', 'Bito'], 1 * units.bit,
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
u_uxo_base['mono'] = units.def_unit(    # currency
    ['🪙', 'Sejro'], format={'latex': r' 🪙 '},
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)

# mask units with the same names as SI
_UNITS_MASK_SET = {
    'sp',
    'AU',
    'kph', 'mph',
} | {data[0] for data in u_uxo_prefixes}
# #    extra defs: prefixes
# for prefix_sn, prefix_tab, scale in u_uxo_prefixes:
#     # avoid name collisions with SI units
#     if prefix_sn not in _UNITS_MASK_SET:
#         units.def_unit(
#             [prefix_sn, *prefix_tab],
#             scale*units.dimensionless_unscaled,
#             namespace=u_uxo_defs)



# --- CSL Units ---

# u_csl: Cities units (assumed)
u_csl_base : dict[str, units.UnitBase] = {}
u_csl_defs : dict[str, units.UnitBase] = {}
u_csl_base['dist'] = units.def_unit(
    'm_csl', (u_uxo_defs['U'] / (8*units.m) * units.m).si,
    prefixes=True,
    namespace=u_csl_defs, format={'latex': r' m_\mathrm{CSL} '})
u_csl_base['mass'] =  units.def_unit(
    'kg_csl', (u_uxo_defs['MP'] / (25*units.t) * units.kg).si,
    namespace=u_csl_defs, format={'latex': r' kg_\mathrm{CSL} '})
u_csl_base['time'] =  units.def_unit(
    's_csl', units.s,
    namespace=u_csl_defs, format={'latex': r' s_\mathrm{CSL} '})
u_csl_base['temp'] = u_csl_defs['deg_C'] = units.deg_C
u_csl_base['angl'] = u_csl_defs['deg']   = units.deg






# === Unit System (Expansion) ===



# derive more units
_BASEUNITS_TYPES_BASE = (
    'dist', 'mass', 'time', 'temp', 'char',
    'angl', 'byte', 'mono')
def normalize(u: dict[str, units.UnitBase]) -> dict[str, units.UnitBase]:
    """Derive more units"""
    # derived units
    u['speed']  = u['dist'] / u['time']
    u['accel']  = u['dist'] / u['time']**2
    u['energy'] = u['mass'] * u['dist']**2 / u['time']**2
    u['power']  = u['energy'] / u['time']
    # constants
    u['hbar'] = u['dist']**2 * u['mass'] / u['time']
    u['c'] = u['dist'] / u['time']
    u['G'] = u['dist']**3 / (u['mass'] * u['time']**2)
    u['k_B'] = u['dist']**2 * u['mass'] / (u['time']**2 * u['temp'])
    return u

normalize(u_nat_base)
normalize(u_uxo_base)
normalize(u_csl_base)



# RO unit extra defs
#    time
units.def_unit(
    ['Ĉ', 'Ĉimuto'], u_uxo_defs['JŜ'], namespace=u_uxo_defs)
units.def_unit(
    ['Ĝ', 'Ĝoro'],   u_uxo_defs['GŜ'], namespace=u_uxo_defs)
units.def_unit(
    ['⚻', 'Tago'],   u_uxo_defs['MŜ'], namespace=u_uxo_defs)
units.def_unit(
    ['⚝', 'Semajno'], 7 * u_uxo_defs['Tago'], namespace=u_uxo_defs)
units.def_unit(
    ['☾', 'Monato'],  4 * u_uxo_defs['Semajno'], namespace=u_uxo_defs)
units.def_unit(
    ['Ĵ', 'Ĵaro'], 0x16D3F44 * u_uxo_defs['Ŝ'],
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
#    temperature
Z = u_uxo_defs['Z']
deg_Zx = units.def_unit(
    ['°Ž', 'deg_Zx', 'Zxorumgrado'], namespace=u_uxo_defs)
__Z_DIV_K: float = (1*u_uxo_defs['Z']).to_value(units.K)
__K_DIV_Z: float = (1*units.K).to_value(u_uxo_defs['Z'])
__Z_2_K = lambda Z: Z*__Z_DIV_K
__K_2_Z = lambda K: K*__K_DIV_Z
__degZx_2_K = lambda degZx: __Z_2_K(degZx + 0x100)
__K_2_degZx = lambda K: (__K_2_Z(K) - 0x100)
equivalencies_Zoro = [
    (
        deg_Zx, u_uxo_defs['Z'],
        lambda degZx: degZx + 0x100,
        lambda Z: Z - 0x100,
    ),
    (
        deg_Zx, units.K,
        __degZx_2_K,
        __K_2_degZx,
    ),
]
for eq in units.equivalencies.temperature():
    if eq[0] == units.K:
        _, X, __K_2_X, __X_2_K = eq
        equivalencies_Zoro.append((
            deg_Zx, X,
            # note: using below to make sure K_2_X is referencing to the
            # correct func in units.equivalencies (instead of in parent scope)
            (lambda K_2_X: lambda degZx: K_2_X(__degZx_2_K(degZx)))(__K_2_X),
            (lambda X_2_K: lambda X: __K_2_degZx(X_2_K(X)))(__X_2_K),
        ))
        equivalencies_Zoro.append((
            Z, X,
            (lambda K_2_X: lambda Z: K_2_X(__Z_2_K(Z)))(__K_2_X),
            (lambda X_2_K: lambda X: __K_2_Z(X_2_K(X)))(__X_2_K),
        ))
    elif eq[1] == units.K:
        X, _, __X_2_K, __K_2_X = eq
        equivalencies_Zoro.append((
            X, deg_Zx,
            (lambda X_2_K: lambda X: __K_2_degZx(X_2_K(X)))(__X_2_K),
            (lambda K_2_X: lambda degZx: K_2_X(__degZx_2_K(degZx)))(__K_2_X),
        ))
        equivalencies_Zoro.append((
            X, Z,
            (lambda X_2_K: lambda X: __K_2_Z(X_2_K(X)))(__X_2_K),
            (lambda K_2_X: lambda Z: K_2_X(__Z_2_K(Z)))(__K_2_X),
        ))
equivalencies_temperature = [
    *equivalencies_Zoro,
    *units.equivalencies.temperature()]
del eq, X, Z, __K_2_X, __X_2_K
#    byte
units.def_unit(
    ['Baj', 'Bajto'],  8 * u_uxo_defs['Bit'],
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
#    speed
units.def_unit('UoŜ', u_uxo_defs[ 'U']/u_uxo_defs['Ŝ'], namespace=u_uxo_defs)
units.def_unit('JoĜ', u_uxo_defs['JU']/u_uxo_defs['Ĝ'], namespace=u_uxo_defs)
#    power
units.def_unit(
    ['Lu', 'Lumro'], 0x1 * u_uxo_base['power'],
    prefixes=u_uxo_prefixes, namespace=u_uxo_defs)
units.def_unit(
    ['⚡', 'MLu', 'MuniLumro'], 0x10000 * u_uxo_defs['Lu'],
    namespace=u_uxo_defs)
#    dimless
units.def_unit(
    ['⌄', 'Projento'], u_uxo_defs['Nuo'] / 0x100,
    namespace=u_uxo_defs)



# csl unit extra defs
#    dist
units.def_unit(
    # Earth size is assumed shrinked in CSL
    #    so we don't need to rescale everything when importing shapefiles from Carto to QGIS
    #    in order to have the correct latitude/longitude info
    #    I might decide to change this later
    ['Rearth_csl', 'CSL_Rearth'], ((_WGS84_DEF[0]**2*_WGS84_DEF[1])**(1/3)).to_value(units.m)*u_csl_defs['m_csl'],
    prefixes=True, namespace=u_csl_defs)
#    mass
units.def_unit(
    ['t_csl', 'CSL_t', 'ton_csl', 'CSL_ton'], 1e3*u_csl_defs['kg_csl'],
    prefixes=True, namespace=u_csl_defs)
#    time
units.def_unit(
    ['h_csl', 'CSL_h', 'hr_csl', 'CSL_hr'],  3600*u_csl_defs['s_csl'],
    namespace=u_csl_defs)
#    speed
units.def_unit(
    ['kph_csl', 'CSL_kph'], u_csl_defs['km_csl'] / u_csl_defs['h_csl'],
    format={'latex': r' \mathrm{kph}_\mathrm{CSL} '},
    prefixes=True, namespace=u_csl_defs)
#    power
units.def_unit(
    ['E_csl', 'CSL_E', 'Electricity_csl', 'CSL_Electricity'],
    u_uxo_defs['MLu'] / 40,
    format={'latex': r' E_\mathrm{CSL} '},
    prefixes=True, namespace=u_csl_defs)
units.def_unit(
    ['W_csl', 'CSL_W'], u_csl_defs['E_csl'] / 16 / 1e3,
    format={'latex': r' \mathrm{kW}_\mathrm{CSL} '},
    prefixes=True, namespace=u_csl_defs)



# Extra
class Unuoj:
    """Units System."""
    def __init__(
        self,
        units_base: dict[str, units.UnitBase] = {},
        units_defs: dict[str, units.UnitBase] = {},
    ):
        self._base: dict[str, units.UnitBase] = normalize(units_base)
        self._defs: dict[str, units.UnitBase] = units_defs
        for k, v in units_defs.items():
            setattr(self, k.translate(ASCIIIFY), v)

        self._UNITS_MASK = {
            self._defs[k]
            for k in _UNITS_MASK_SET if k in self._defs
        }
        self._defs_masked = {
            k: v for k, v in self._defs.items() if v not in self._UNITS_MASK}

    def __repr__(self):
        return "\n".join([f"{k+':':8}{v}" for k, v in self._base.items()])

    def enable_equivalencies(self):
        return units.set_enabled_equivalencies(equivalencies_temperature)
    
    def enable_units(self, overwrite:bool=False):
        if overwrite: units.set_enabled_units([])
        return units.add_enabled_units(self._defs_masked)
    
    def enable(self, overwrite:bool=False):
        self.enable_equivalencies()
        self.enable_units(overwrite=overwrite)
        return

u_uxo = unitsUXO = Unuoj(u_uxo_base, u_uxo_defs)
u_nat = unitsNat = Unuoj(u_nat_base, u_nat_defs)
u_csl = unitsCSL = Unuoj(u_csl_base, u_csl_defs)
u = Unuoj(u_uxo_base, u_uxo_defs | u_nat_defs | u_si_defs | u_csl_defs)

# 'bases' var required for astropy unit conversion to_system() method
bases = tuple([
    u_uxo._base[t] for t in _BASEUNITS_TYPES_BASE if t in u_uxo._base])
    # tuple([it for k, it in u_uxo_defs.items()]) #
# units obj in bases required as well
for it in bases:
    globals()[f"unuoj_{it.name.translate(ASCIIIFY)}"] = it






# === Constants ===



class Konstantoj:
    def __init__(self):
        pass

    # get astropy constants
    for ak in {'hbar', 'G', 'c', 'k_B', 'e'}:
        globals()[ak] = getattr(const, ak)

    paperdim_A4 = [210, 297] * units.mm
    @classmethod
    def paperdim_A(cls, n: int):
        return [2**(-0.25-n/2), 2**(0.25-n/2)] * units.m

    # track gauges
    reldistanco_std = (4*units.imperial.foot + 8.5 * units.imperial.inch).si
    reldistanco_uxo = 3 * u.hU

konst = Konstantoj()






# === Unit System (Expansion) ===



class Datotempo:
    # unit used for storage
    _UNUO : units.Unit = u.mSx
    # Omnija Epoch:
    #   Around midnight at OC (2026-06-21T09:22:47.5+00:00)
    #   on the day of Northern Solstice 2026
    #   Note: accounting the extra 7.1 minutes every year for Omnijaro calendar
    _EPOKO: datetime = datetime(2026, 6, 21, 9, 30, tzinfo=UTC)
    # POSIX Epoch's position in Omnija Epoch (in mSx)
    _POSIX: np.int64 = np.int64((-_EPOKO.timestamp()*u.s).to_value(_UNUO))
    # max storable POSIX timestamp in mSx
    _POSIX_MAX: np.int64 = np.iinfo(np.int64).max + _POSIX
    # basic info
    _MONATO_mSx:  np.int64 = np.int64(np.round((1*u.Monato ).to_value(u.mSx)))
    _SEMAJNO_mSx: np.int64 = np.int64(np.round((1*u.Semajno).to_value(u.mSx)))
    _TAGO_mSx:    np.int64 = np.int64(np.round((1*u.Tago   ).to_value(u.mSx)))
    _Gx_mSx:      np.int64 = np.int64(np.round((1*u.Gx     ).to_value(u.mSx)))
    _Cx_mSx:      np.int64 = np.int64(np.round((1*u.Cx     ).to_value(u.mSx)))
    _HSx_mSx:     np.int64 = np.int64(np.round((1*u.HSx    ).to_value(u.mSx)))
    _Sx_mSx:      np.int64 = np.int64(np.round((1*u.Sx     ).to_value(u.mSx)))
    # number of Sx per added/skipped leap day
    _TAGO_Sx: np.int64 = np.int64(np.round((1*u.MSx).to_value(u.Sx)))
    # number of Sx per komunjaro
    _JARO_Sx: np.int64 = np.int64(np.round(
        # note: include the extra seconds added in 13th month
        (365 * u.MSx + 0x144 * u.Sx).to_value(u.Sx)))
    # number of Sx per 3 komunjaro + 1 superjaro
    _JAROJ4_Sx: np.int64 = np.int64(np.round(_JARO_Sx*4 + _TAGO_Sx))
    # number of Sx per 128 jaroj
    _JAROJ128_Sx: np.int64 = np.int64(np.round(_JAROJ4_Sx*32 - _TAGO_Sx))
    # symbols to numbers
    _SEMAJNO_SIMBOLOJ: dict[str, int] = {k: i for i, k in enumerate('OIQU')}
    _TAGO_SIMBOLOJ: dict[str, int] = {i: i for i in range(7)} # {k: i for i, k in enumerate('ZLABɅVS')}
    # numbers to symbols
    _SEMAJNO_SIMBOLOJ_INV = {i: k for k, i in _SEMAJNO_SIMBOLOJ.items()}
    _TAGO_SIMBOLOJ_INV = {i: k for k, i in _TAGO_SIMBOLOJ.items()}


    def __init__(self, tempstampo: None|datetime|units.Quantity=None):
        # mSx since Datotempo._EPOKO
        self.__tempstampo: np.int64 = np.int64(0)

        if tempstampo is not None:
            self.agordi(tempstampo)

    def __repr__(self) -> str:
        datetime_iso = ''
        try:
            datetime_iso = self.datetime.isoformat()
        except OverflowError:
            datetime_iso = "\n\tNote: overflow for python native datetime lib"

        return (
            f"Timestamp Dx {self.__tempstampo:.0f} {type(self)._UNUO}"
            + f"  since {type(self)._EPOKO.isoformat()}"
            + "\n\t" + self.onkio
            + "\n\t" + datetime_iso
        )

    def __str__(self) -> str:
        # return self.datetime.isoformat()
        return self.onkio

    def __copy__(self) -> Self:
        return type(self)(self.tempstampo)

    def kopii(self) -> Self:
        return self.__copy__()

    @property
    def tempstampo(self) -> units.Quantity:
        """Get timestamp (time difference from Datotempo._EPOKO)."""
        return units.Quantity(
            self.__tempstampo, unit=type(self)._UNUO, dtype=np.int64)

    def agordi(self, tempstampo: datetime|units.Quantity) -> Self:
        """Set from timestamp.
        
        tempstampo:
            time difference from Datotempo._EPOKO
            if not of type datetime or units.Quantity,
                will be treated as POSIX timestamp
                (i.e. time difference from UNIX Epoch instead of Omnija Epoch)
        """
        # to units.Quantity
        if not isinstance(tempstampo, (units.Quantity, datetime)):
            raise TypeError(
                f"{type(tempstampo) = } should be"
                " either units.Quantity or datetime.datetime.")
        if isinstance(tempstampo, datetime):
            tempstampo = units.Quantity(
                (tempstampo - type(self)._EPOKO).total_seconds(), unit=u.s)
        self.__tempstampo = np.int64(tempstampo.to_value(type(self)._UNUO))
        return self

    @classmethod
    def generi_el(cls, tempstampo: Self|datetime|units.Quantity) -> Self:
        return cls(tempstampo)

    @classmethod
    def generi_el_posix(cls, posix: float) -> Self:
        # return cls(datetime.fromtimestamp(posix))
        return cls((cls._POSIX*cls._UNUO) + (posix*u.s).to(cls._UNUO))

    @property
    def datetime(self) -> datetime:
        return type(self)._EPOKO + timedelta(
            days=self.tempstampo.to_value(u.d))
    
    @property
    def posix(self) -> float:
        """Return POSIX timestamp.
        
        Warning: Last 2 digits for microseconds are not accurate,
        since the accuracy is limited to Datotempo._UNUO (mSx, or ~20us)
        """
        if self.__tempstampo > type(self)._POSIX_MAX:
            raise NotImplementedError(
                "POSIX timestamp overflown- not yet implemented")
        return units.Quantity(
            self.__tempstampo - type(self)._POSIX, unit=type(self)._UNUO,
        ).to_value(u.s)

    @classmethod
    def nun(cls) -> Self:
        """Now"""
        return cls(datetime.now(UTC))

    @classmethod
    def mak(cls) -> Self:
        """Maximum storable time"""
        res = cls()
        res.__tempstampo = np.iinfo(type(res.__tempstampo)).max
        return res

    @classmethod
    def min(cls) -> Self:
        """Minimum storable time"""
        res = cls()
        res.__tempstampo = np.iinfo(type(res.__tempstampo)).min
        return res



    @classmethod
    def ak_Jaro_kaj_mSx(
        cls, tempstampo: units.Quantity
    ) -> tuple[np.int64, np.int64]:
        """Split a tempstampo into no of calaendar years and the rest."""

        total_Sx, rest_mSx = divmod(tempstampo, 1*u.Sx)
        total_Sx = np.int64(total_Sx)
        rest_mSx = np.int64(rest_mSx.to_value(u.mSx))

        n_128J, rest_Sx = divmod(total_Sx, cls._JAROJ128_Sx)
        rest_Sx += cls._TAGO_Sx    # account for the skipping leap year at 0
        n_4J,   rest_Sx = divmod(rest_Sx,  cls._JAROJ4_Sx)
        rest_Sx -= cls._TAGO_Sx
        if n_4J:    # not skipping leapyear
            if rest_Sx < cls._TAGO_Sx:    # is first day
                n_J = 0
            else:
                rest_Sx -= cls._TAGO_Sx    # account for the leap year at 0
                n_J, rest_Sx = divmod(rest_Sx,  cls._JARO_Sx)
                rest_Sx += cls._TAGO_Sx
        else:    # skipped leapyear
            n_J, rest_Sx = divmod(rest_Sx,  cls._JARO_Sx)

        n_Jaro = n_128J*128 + n_4J*4 + n_J
        rest_mSx += rest_Sx*cls._Sx_mSx

        return n_Jaro, rest_mSx

    @property
    def onkio(self) -> str:
        """Get ONKIO standard string representation of datetime."""

        cls = self

        nn = {}

        n_Jaro,       rest_mSx = cls.ak_Jaro_kaj_mSx(self.tempstampo)
        nn['Monato'], rest_mSx = divmod(rest_mSx, cls._MONATO_mSx)
        n_Semajno,    rest_mSx = divmod(rest_mSx, cls._SEMAJNO_mSx)
        n_Tago,       rest_mSx = divmod(rest_mSx, cls._TAGO_mSx)
        nn['Gx'],     rest_mSx = divmod(rest_mSx, cls._Gx_mSx)
        nn['Cx'],     rest_mSx = divmod(rest_mSx, cls._Cx_mSx)
        nn['HSx'],    rest_mSx = divmod(rest_mSx, cls._HSx_mSx)
        nn['Sx'],     rest_mSx = divmod(rest_mSx, cls._Sx_mSx)

        ss = {
            key: HX_SYMBOLS_INV_DICT['ONKIO'][int(it)]
            for key, it in nn.items()
        } | {
            'Semajno': cls._SEMAJNO_SIMBOLOJ_INV[int(n_Semajno)],
            'Tago': cls._TAGO_SIMBOLOJ_INV[int(n_Tago)],
        }

        res = (
            f"Ø{presi_Hx(int(n_Jaro), plus_sign='+')}" +
            f"‐{ss['Monato']}‐{ss['Semajno']}{ss['Tago']}⌄" +
            f"{ss['Gx']}:{ss['Cx']}:{ss['HSx']}{ss['Sx']}." +
            f"{presi_Hx(int(rest_mSx)):0>4}"
        )
        return res



    @property
    def iso(self) -> str:
        return self.datetime.isoformat()






# === Coordinates and Post Codes ===



type TeraLokoOffsetTipo = None | tuple[     # type
    units.Quantity[units.deg | units.m],    # lon
    units.Quantity[units.deg | units.m],    # lat
    units.Quantity[units.m],      # alt
] | dict[str, units.Quantity[units.deg | units.m]]

class TeraLoko:
    """Locations on Earth (defined by coordinates)."""
    
    _WGS84 = tuple([x.to_value(u.m) * u.m_csl for x in _WGS84_DEF])
    # healpy nside parameter- decide HEALPix Resolution
    #    npix = 12 * nside**2
    # So keep it a 32**X*4,
    # so the result index * 2 express well with our base-32 system
    # *** DO NOT CHANGE THIS UNLESS YOU KNOW WHAT YOU ARE DOING ***
    _NSIDE = 32**4*4
    
    def __init__(
        self,
        posxkodo: None|str = None,
        lon: units.Quantity[units.deg] = 0*u.deg,
        lat: units.Quantity[units.deg] = 0*u.deg,
        alt: units.Quantity[units.m]   = 0*u.U,
    ):
        self._TeroP = self._WGS84
        if posxkodo is not None:
            loko = self._from_posxkodo(posxkodo)
            lon, lat, alt = loko['lon'], loko['lat'], loko['alt']
        self.lon = lon.to(u.deg) % (360*u.deg)    # guaranteed to be within [0, 360]
        self.lat = lat
        self.alt = alt

    def __repr__(self):
        return f"TeraLoko(lat={self.lat}, lon={self.lon}, alt={self.alt})"

    def __str__(self):
        return (
            f"TeraLoko {self.get_posxkodo():16}: " +
            f"lat {self.lat:9.5f}, lon {self.lon:9.5f}, alt {self.alt:6.0f}.")

    @property
    def colat(self):
        """Co-latitude"""
        return 90*u.deg - self.lat

    def _R_at_lat(self, lat=None):
        """Return Circles of latitude radius"""
        a, b = self._TeroP
        if lat is None: lat = self.lat
        return a / np.sqrt(1 + (a/b*np.tan(lat))**2)

    def to_EarthLocation(self) -> EarthLocation:
        return EarthLocation.from_geodetic(
            lon=self.lon, lat=self.lat, height=self.alt, ellipsoid='WGS84')

    def normalize_offset(
        self,
        offset: None
    ) -> tuple[
        units.Quantity[units.deg],    # lon
        units.Quantity[units.deg],    # lat
        units.Quantity[units.m],      # alt
    ]:
        """Interpret offset from center and convert to default format."""
        if offset is None:
            offset = [0*u.deg, 0*u.deg, 0*u.m_csl]
        elif isinstance(offset, dict):
            offset_new = [0*u.deg, 0*u.deg, 0*u.m_csl]
            if 'lon' in offset:
                offset_new[0] = offset['lon']
            if 'lat' in offset:
                offset_new[1] = offset['lat']
            if 'alt' in offset:
                offset_new[2] = offset['alt']
            offset = self.normalize_offset(offset_new)
        elif isinstance(offset, (tuple, list)):
            try: offset[1].to(u.deg)
            except UnitConversionError:
                offset = list(offset)
                try:
                    # approx- assume Earth is a sphere (instead of an ellipse)
                    offset[1] = ((offset[1].to(u.m_csl) / ((self._TeroP[0]+self._TeroP[1])/2))*u.rad)
                except UnitConversionError:
                    raise ValueError("offset[1] should be latitude changes in either degrees or in meters")
                finally:
                    offset[1] = offset[1].to(u.deg)    # needed for lon conversion from m to deg
            try: offset[0].to(u.deg)
            except UnitConversionError:
                offset = list(offset)
                try:
                    offset[0] = ((offset[0].to(u.m_csl) / self._R_at_lat(self.lat + offset[1]))*u.rad).to(u.deg)
                except UnitConversionError:
                    raise ValueError("offset[0] should be longitude changes in either degrees or in meters")
            try: offset[2].to(u.m_csl)
            except UnitConversionError:
                offset = list(offset)
                raise ValueError(
                    "offset[2] should be altitude changes in meters")
        return tuple(offset)

    def get_new_from_offset(
        self,
        offset: TeraLokoOffsetTipo = None,
    ):
        offset = self.normalize_offset(offset)
        return TeraLoko(
            lon=self.lon+offset[0],
            lat=self.lat+offset[1],
            alt=self.alt+offset[2])



    def get_posxkodo(
        self,
        offset: TeraLokoOffsetTipo = None,
        chrset: str = 'ONKIO',
    ) -> str:
        """Get post code from coordinates.

        Output postcode has a length of 11 ~ 14 digits,
            depending on the altitude info.
            Detailed structure see code.
        
        Parameters
        ----------

        Offset: None | (d_lon, d_lat, d_alt) | {
                'lon': d_lon, 'lat': d_lat, 'alt': d_alt}
            Use offset to specify the specifc location with respect to self,
            otherwise return self's postcode.

        chrset: str ('ASCII' | 'ONKIO')
            Output base-32 character style


        Notes
        -----
        Uses HEALPix (Górski et al., 2005) under the hood.
        See https://iopscience.iop.org/article/10.1086/427976
            for more info on the algorithm.
        Also see https://healpy.readthedocs.io/en/latest/
            for the python wrapper module 'healpy' doc.

        Will raise ModuleNotFoundError if healpy module is not available.
        """
        if not POVI_HEALPY:
            raise ModuleNotFoundError("healpy not found, cannot do post code.")
        Tx_symbols_inv = TX_SYMBOLS_INV_DICT[chrset]

        loko = self.get_new_from_offset(offset)
        p_nd = {    # n digits
            'cxelo': 10,    # cell index
            'alt': 0,       # altitude - 1~3 digits
            # 'kon': 1,     # verify - must init as zero
        }
        pdat = {k: 0 for k in p_nd}

        pdat['cxelo'] = healpy.ang2pix(
            self._NSIDE,
            loko.colat.to_value(u.rad),
            loko.lon.to_value(u.rad),
            nest=True,  # always use nest formulation
                        # so existing digits don't change
                        # when add more resolutions
        )*2

        # alt_kodo_N = int(loko.alt.to_value(u.U)*4 + 0x4000)
        pdat['alt'] = int(np.floor(loko.alt.to_value(u.U)*8))
        if pdat['alt'] < 0:
            # last digit of cxelo is odd number if below sea level,
            # even number if above
            pdat['cxelo'] += 1
            pdat['alt'] *= -1
        if pdat['alt'] >= 0x8000:
            raise ValueError(
                f"Altitude out of range" +
                f"[{-(1*u.GU-1*u.m_csl).to(u.m_csl)}, {(1*u.GU).to(u.m_csl)})")
        

        pstr = {
            k: presi_Tx(v, prefix='', e_sep='', symbols_inv=Tx_symbols_inv)
            for k, v in pdat.items()
        }
        for k in pstr:
            if pstr[k] == '0':
                pstr[k] = ''
            if len(pstr[k]) < p_nd[k]:
                pstr[k] = '0' * (p_nd[k] - len(pstr[k])) + pstr[k]

        posxkodo = (
            f"{pstr['cxelo'][:5]}-"     # city & district (res: ~6.4km)
            f"{pstr['cxelo'][5:9]}-"    # street (res: ~6.2m)
            f"{pstr['cxelo'][9:]}"      # door (res: ~1.6m)
            f"{pstr['alt'][::-1]}"      # altitude (res: 1m)
        )

        # add verification digit
        pdat['kon'] = np.sum([
            Tx(v) for v in posxkodo
        ]) % 0x20

        pstr['kon'] = presi_Tx(
            pdat['kon'], prefix='', e_sep='', symbols_inv=Tx_symbols_inv)
        
        assert len(pstr['kon']) == 1
        posxkodo += pstr['kon']

        return posxkodo
    


    @classmethod
    def normalize_posxkodo(cls, posxkodo: str) -> str:
        """Normalize post code into str without hyphen; also check validity"""

        pstr_list = posxkodo.split('-')

        if not pstr_list or not pstr_list[0]:
            raise ValueError(
                f"postcode '{posxkodo}' is empty, or its first field is empty.")
        
        if pstr_list[0][0] not in TX_SYMBOLS:
            raise NotImplementedError('City Name shorthand not yet implemented')
            # add shorthand comprehansion code here

        posxkodo = ''.join(pstr_list)

        if len(posxkodo) < 11:
            raise ValueError("Postcode too short")

        for c in posxkodo:
            if c not in TX_SYMBOLS:
                raise ValueError("Unrecognized Character in post code")
        
        # check integrity
        kon = np.sum([
            Tx(v) for v in posxkodo[:-1]
        ]) % 0x20
        kon_v = Tx(posxkodo[-1])
        if kon != kon_v:
            raise ValueError(
                "Verification failed: "
                f"Last digit should be of value {kon}, but it is {kon_v}.")
        
        return posxkodo


    @classmethod
    def _from_posxkodo(cls, posxkodo: str):
        """Return location dictionary from post code.
        
        see TeraLoko.get_posxkodo() for more info.
        """
        if not POVI_HEALPY:
            raise ModuleNotFoundError("healpy not found, cannot do post code.")

        posxkodo = TeraLoko.normalize_posxkodo(posxkodo)

        # reconstruct lat and lon
        pdat = {
            # note: raw data from posxkodo, not actual loko yet
            'cxelo': int(Tx(posxkodo[:10])),
            'alt'  : int(Tx(posxkodo[10:-1][::-1])),
            'kon'  : int(Tx(posxkodo[-1])),
        }
        
        colat, lon = healpy.pix2ang(cls._NSIDE, pdat['cxelo'] // 2, nest=True)
        colat *= u.rad
        lon *= u.rad

        loko = {
            'lon': lon.to(u.deg),
            'lat': 90*u.deg - colat.to(u.deg),
            'alt': pdat['alt'] * u.m_csl * (-1 if pdat['cxelo'] % 2 else 1),
        }

        return loko
    
    @classmethod
    def from_posxkodo(cls, posxkodo: str):
        """Return new class from post code.
        
        see TeraLoko.get_posxkodo() for more info.
        """
        return TeraLoko(posxkodo=posxkodo)



LOKOJ: dict[str: TeraLoko] = {}
LOKOJ['Nul'] = TeraLoko()
LOKOJ['OC' ] = TeraLoko(lon=-140.25*u.deg, lat=-56.25*u.deg, alt=0*u.U)
LOKOJ['RO' ] = LOKOJ['OC']




# === Testing and Debug ===



if __name__ == '__main__':

    import onkio; ONKIO = onkio.ONKIO()

    # temperature reference points
    temp_refs_C = [0., 22.85, 36.85, 100.] * units.deg_C
    temp_refs_K = temp_refs_C.to(units.K, equivalencies=units.equivalencies.temperature())

    # output
    print("\n".join([
        f"{k:4} unit: {(1*u_uxo_base[k]).si:8.6f} \t [naturalUnit: {(1*v).si:.4e}]"
        for k, v in u_nat_base.items()]))
    print()
    print(f"dist: {konst.reldistanco_std = :7.4f} is {konst.reldistanco_std.to(u_uxo_base['dist']):7.5f}")
    print(f"dist: {konst.reldistanco_uxo.si   = :7.4f} is {konst.reldistanco_uxo.to(u_uxo_base['dist']):7.5f}")
    print(f"temp: {temp_refs_C} is {temp_refs_K}, which is {temp_refs_K.to(u_uxo_base['temp'])} ")

    # sidereal year <https://en.wikipedia.org/wiki/Sidereal_year> (2025-02-28)
    #u_yr = units.d * 365.256363004
    u_yr = units.yr
    u_yr_b = (u_uxo.MSx / (1*u_yr - 1*u_uxo.Jx)).si * units.yr
    print(f"\n# of years before needing to subtract a day: {u_yr_b:.1f}")
    print(f"Added seconds per day: {(1*u_uxo.MSx - 1*units.day).to(units.s):.3f}")
    print(f"Added minutes per year: {(1*u_uxo.Jx - 1*units.year).to(units.min):.3f}")
    assert (128*u.Jx).to_value(u.Sx) == Datotempo._JAROJ128_Sx

    print(
        "\nAbout currency:",
        "Energy price in CSL2 game is",
        f"{2500*u.Sejro / (u.MW*(units.yr/12)).to(u.kW*units.h)}")

    print("\nTesting name collision with SI units... ", end='')
    # units.add_enabled_units(u_uxo_defs)
    u_nat.enable(overwrite=True)
    u_uxo.enable()
    u.enable()
    print("Pass.")

    print("\nTesting Hx/Tx/Rx Symbols integrity...", end='')
    assert not set('-#\'\"').intersection(set(HX_SYMBOLS.keys()))
    assert not set('-#\'\"').intersection(set(TX_SYMBOLS.keys()))
    # cs: char set; ss: str dict;
    for cs, ss in HX_SYMBOLS_INV_DICT.items():
        for i in range(0x10):
            assert i in ss
            assert ss[i] in HX_SYMBOLS_DICT[cs]
    for cs, ss in TX_SYMBOLS_INV_DICT.items():
        for i in range(0x20):
            assert i in ss
            assert ss[i] in TX_SYMBOLS_DICT[cs]
    for cs, ss in RX_SYMBOLS_INV_DICT.items():
        for i in range(0x40):
            assert i in ss
            assert ss[i] in RX_SYMBOLS_DICT[cs]
    for ck in range(0x61, 0x7F):
        assert ONKIO[ck] in RX_SYMBOLS
        assert RX_SYMBOLS[ONKIO[ck]] == ck-0x40
    for cs, d in ALL_SYMBOLS_DICT.items():
        for s, c in d.items():
            if s in TX_SYMBOLS_DICT[cs]:
                assert c == TX_SYMBOLS_DICT[cs][s], f"{cs=}, {c=}, {s=}, {TX_SYMBOLS_DICT[cs][s]=}"
            if s in RX_SYMBOLS_DICT[cs]:
                assert c == RX_SYMBOLS_DICT[cs][s], f"{cs=}, {c=}, {s=}, {RX_SYMBOLS_DICT[cs][s]=}"
    # forbidden / escaped chars in json strings
    #   ("\/" not technically forbidden, but just in case)
    assert not set('\\\"/').intersection(set(RX_SYMBOLS.keys()))
    # forbidden / escaped chars in xml
    assert not set('&<>\"').intersection(set(RX_SYMBOLS.keys()))
    # forbidden / escaped chars in filenames for windows/linux
    assert not set(' /.\\/:*?\"<>|').intersection(set(RX_SYMBOLS.keys()))
    # test ASCII/ONKIO RX symbol compatibility
    for k, v in RX_SYMBOLS_DICT['ASCII'].items():
        # cpt: code point
        cpt: int = ord(k)
        # okc: onkio counterpart char
        okc: str = ONKIO.al_ascii(cpt)
        # no control characters
        assert 32 <= cpt and cpt < 127
        assert (
            okc == RX_SYMBOLS_INV_DICT['ONKIO'][v]
            or okc not in RX_SYMBOLS_DICT['ONKIO'])
        assert (
            (   v in TX_SYMBOLS_INV_DICT['ONKIO']
                and okc == TX_SYMBOLS_INV_DICT['ONKIO'][v])
            or okc not in TX_SYMBOLS_DICT['ONKIO'])
        assert True


    print("Pass.")

    print("\nTesting presi_Hx()...", end='')
    assert presi_Hx(0) == '0'
    assert presi_Hx(31/128) == '0.3Υ'
    assert presi_Hx(-31/128) == '-0.3Υ'
    assert presi_Hx(131/128) == '1.06'
    assert presi_Hx(-131/128) == '-1.06'
    assert presi_Hx(12138, e_sep='') == '2Ψ6Δ'
    assert presi_Hx(-12138, e_sep='⌄') == '-2.Ψ6Δ⌄3'
    assert presi_Hx(9100000000, e_sep='') == '21Υ66Ψλ00'
    print("Pass.")

    print("\nTesting Post Code Calc System...")
    print(
        "\tZero point (lat=lon=alt=0) postcode: "
        f"{LOKOJ['Nul'].get_posxkodo() = }")
    print(f"\tOC postcode: {LOKOJ['OC'].get_posxkodo() = }")
    assert TeraLoko.normalize_posxkodo(
        LOKOJ['Nul'].get_posxkodo()) == '4N00000000Ŝ' # '4N000-0000-0Ŝ'
    assert TeraLoko.normalize_posxkodo(
        LOKOJ['OC' ].get_posxkodo()) == 'Δ74E9N4TRΥE' # 'Δ74E9-N4TR-ΥE'
    def assert_loko(lat, lon, alt):
        loko = TeraLoko(lat=lat, lon=lon, alt=alt)
        p1 = loko.get_posxkodo()
        p2 = TeraLoko(p1).get_posxkodo()
        print(f"\t\t{p1:16}\t{p2:16}\t{loko}")
        assert p1 == p2
        return loko
    print("\tTesting polar locations and post codes...")
    loko = assert_loko(lat= 90*u.deg, lon=  0*u.deg, alt=0*u.m_csl)
    loko = assert_loko(lat= 90*u.deg, lon=180*u.deg, alt=0*u.m_csl)
    loko = assert_loko(lat= 90*u.deg, lon=234*u.deg, alt=0*u.m_csl)
    loko = assert_loko(lat=-90*u.deg, lon=  0*u.deg, alt=0*u.m_csl)
    loko = assert_loko(lat=-90*u.deg, lon=180*u.deg, alt=0*u.m_csl)
    loko = assert_loko(lat=-90*u.deg, lon=234*u.deg, alt=0*u.m_csl)
    print("\tRandomly generating locations and post codes...")
    for _ in range(0x10):
        loko = assert_loko(
            lat = (np.random.rand() * 180 - 90)*u.deg,
            lon = np.random.rand() * 360 * u.deg,
            alt = (np.random.rand() * 65536 - 32768) * u.m_csl,
        )
    print("Pass.")

    print("\n=== PASS ===\n")
