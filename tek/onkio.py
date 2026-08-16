#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ONKIO table and ASCII table generation.
ONKIO: Omnija Norma Kodo por Informo-interŝanĝO,
i.e. a fictional ASCII-equivalent table for Esperanto/E++.
(ASCII: American Standard Code for Information Interchange.)

Note: Esperanto letter hx/Hx is not present in this table,
    since we eliminated it in E++.

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


# ONKIO vs ASCII
#    ONKIO: Omnija Norma Kodo por Informo-Interŝanĝo (fictional)
#    ASCII: American Standard Code for Information Interchange

# print both ONKIO and ASCII tables as markdown tables
#------------------------------------------------------------------------------

from math import nan, isnan

# escapable characters for markdown formatting
MARKDOWN_ESCAPABLES : set = {
    '\\', '`', '*', '_', '#', '+', '-', '.', '!', '|',
    '{', '}', '[', ']', '<', '>' , '(', ')', '@',
}

print_dict = lambda dat: print("\n".join([f"{k}: {v}" for k, v in dat.items()]))



class tkt(str):
    """ONKIO teksto (str).
    
    It is here to mark that this str is in ONKIO.

    Assuming inputs are already encoded as ONKIO.
    Items are in chr. Use ord() to get back codepoint.
    """
    def __new__(cls, dat: list[int]|str):
        if isinstance(dat, str):
            return str.__new__(cls, dat)
        else:
            return str.__new__(cls, ''.join([chr(i) for i in dat]))


class ONKIO:
    """Difino de la ONKIO (Omnija Norma Kodo por Informo-interŝanĝO).

    Definition of the ONKIO encoding system.
    """
    # ONKIO kodpunkta defino (ONKIO code point def)
    # ONKIO kodpunkto: str (en Unikodo)
    __KODOJ: dict[int, str] = {ascii_c: chr(ascii_c) for ascii_c in range(128)}
    __KODOJ.update({    # Differences
        # Letters
        0x57: chr(0x16c),   # W -> Ŭ
        0x77: chr(0x16d),   # w -> ŭ
        0x59: chr(0x245),   # Y -> Ʌ
        0x79: chr(0x28c),   # y -> ʌ
        0x5b: chr(0x108),   # [ -> Ĉ
        0x7b: chr(0x109),   # { -> ĉ
        0x5c: chr(0x11c),   # \ -> Ĝ
        0x7c: chr(0x11d),   # | -> ĝ
        0x5d: chr(0x134),   # ] -> Ĵ
        0x7d: chr(0x135),   # } -> ĵ
        0x5e: chr(0x15c),   # ^ -> Ŝ
        0x7e: chr(0x15d),   # ~ -> ŝ
        0x40: chr(0x20),    # @ -> SPACE
        0x60: chr(0x2010),  # ` -> ‐  (hyphen)
        0x5f: chr(0x2e),    #  _  -> .
        0x7f: chr(0x2c),    # DEL -> ,
        # Hexadecimal characters
        0x3a: chr(0x394),   # : -> Δ
        0x3b: chr(0x3bb),   # ; -> λ
        0x3c: chr(0x3a0),   # < -> Π
        0x3d: chr(0x3a3),   # = -> Σ
        0x3e: chr(0x3a5),   # > -> Υ
        0x3f: chr(0x3a8),   # ? -> Ψ
        # Punctuation & Symbols
        0x10: chr(0x5c),    # 0x10 -> \
        0x11: chr(0x2f),    # 0x11 -> /
        0x12: chr(0x60),    # 0x12 -> `
        0x13: chr(0x7b),    # 0x13 -> {
        0x14: chr(0x7c),    # 0x14 -> |
        0x15: chr(0x7d),    # 0x15 -> }
        0x16: chr(0x22),    # 0x16 -> "
        0x17: chr(0x3c),    # 0x17 -> <
        0x18: chr(0x3e),    # 0x18 -> >
        0x19: chr(0x5b),    # 0x19 -> [
        0x1a: chr(0x5d),    # 0x1a -> ]
        0x1b: chr(0x2a),    # 0x1b -> *
        0x1c: chr(0x24),    # 0x1c -> $
        0x1d: chr(0x3a),    # 0x1d -> :
        0x1e: chr(0x3b),    # 0x1e -> ;
        0x1f: chr(0x3f),    # 0x1f -> ?
        0x20: chr(0x5f),    # SPACE -> _
        0x22: chr(0x7e),    # " -> ~
        0x24: chr(0x3001),  # $ -> 、 (enumeration comma)
        0x25: chr(0x40),    # % -> @
        0x26: chr(0x27),    # & -> '
        0x27: chr(0x25),    # ' -> %
        0x28: chr(0x3d),    # ( -> =
        0x29: chr(0x28),    # ) -> (
        0x2a: chr(0x29),    # * -> )
        0x2c: chr(0x2304),  # , -> ⌄  (projento)
        0x2d: chr(0x2212),  # - -> −  (minus)
        0x2e: chr(0x5e),    # . -> ^
        0x2f: chr(0x2014),  # / -> —  (em-dash)
        # Control Sequences (limit to 0x0_)
        0x0d: chr(0x1a),    # 0x0d -> SUB
        0x0e: chr(0x1b),    # 0x0e -> ESC
        0x0f: chr(0x7f),    # 0x0f -> DEL
        # Mirroring
        0x2212: chr(0x0d),  # −  (minus)    -> 0x0d (\r)
        0x2014: chr(0x0e),  # —  (em-dash)  -> 0x0e
        0x2304: chr(0x0f),  # ⌄  (projento) -> 0x0f
        0x2010: chr(0x2d),  # ‐  (hyphen)   -> -
        0x3001: chr(0x26),  # 、 (enumeration comma) -> &
        0x394:  chr(0x10),  # Δ -> 0x10
        0x3bb:  chr(0x11),  # λ -> 0x11
        0x3a0:  chr(0x12),  # Π -> 0x12
        0x3a3:  chr(0x13),  # Σ -> 0x13
        0x3a5:  chr(0x14),  # Υ -> 0x14
        0x3a8:  chr(0x15),  # Ψ -> 0x15
        0x108:  chr(0x16),  # Ĉ -> 0x16
        0x109:  chr(0x17),  # ĉ -> 0x17
        0x11c:  chr(0x18),  # Ĝ -> 0x18
        0x11d:  chr(0x19),  # ĝ -> 0x19
        0x134:  chr(0x1c),  # Ĵ -> 0x1c
        0x135:  chr(0x1d),  # ĵ -> 0x1d
        0x15c:  chr(0x1e),  # Ŝ -> 0x1e
        0x15d:  chr(0x1f),  # ŝ -> 0x1f
        0x16c:  chr(0x57),  # Ŭ -> W
        0x16d:  chr(0x77),  # ŭ -> w
        0x245:  chr(0x59),  # Ʌ -> Y
        0x28c:  chr(0x79),  # ʌ -> y
    })
    # Normalize
    #    finish mirroring (should not be necessary, but just in case)
    #    i.e. ensure 1 to 1 complete mapping back and forth
    _o2a = set(__KODOJ.keys())
    _a2o = set([ord(a) for _, a in __KODOJ.items()])
    _a, _o = 0, None
    for _a, _o in zip(sorted(_o2a - _a2o), sorted(_a2o - _o2a)):
        __KODOJ[_o] = chr(_a)
    del _a, _o, _o2a, _a2o

    # inversa: ASCII -> ONKIO
    __KODOJ_INV: dict[str, int] = {c: i for i, c in __KODOJ.items()}



    def __init__(self):
        pass

    def __getitem__(self, index: int) -> str:
        return self.__KODOJ[index]

    @classmethod
    def al_ascii(cls, tkt_onkio: tkt|int) -> str:
        """Decode ONKIO string / code point into ASCII string."""

        if isinstance(tkt_onkio, str):
            if not isinstance(tkt_onkio, tkt):
                print(f"Warning: input {type(tkt_onkio) = } may not be in ONKIO, since it is not of type 'tkt'.")
            res = ''.join([
                cls.__KODOJ[ord(c)] if ord(c) in cls.__KODOJ else c
                for c in tkt_onkio
            ])
        elif isinstance(tkt_onkio, int):
            res = cls.__KODOJ[
                tkt_onkio] if tkt_onkio in cls.__KODOJ else chr(tkt_onkio)
        else:
            raise TypeError(f"Unrecognized input {type(tkt_onkio) = }")
        return res

    @classmethod
    def al_onkio(cls, txt_ascii: str) -> tkt:
        """Encode ASCII string into ONKIO string."""
        res = [
            cls.__KODOJ_INV[c] if c in cls.__KODOJ_INV else ord(c)
            for c in txt_ascii
        ]
        return tkt(res)


    @classmethod
    def ak_alfabeto(cls, tipo:None|str=None) -> dict[str, str]|str:
        """Akiri Alfabeto de Epopo."""
        alfabeto = {
            '0': cls.al_ascii(tkt([i for i in range(0x30, 0x40)])),
            'A': cls.al_ascii(tkt([i for i in range(0x41, 0x5f)])),
            'a': cls.al_ascii(tkt([i for i in range(0x61, 0x7f)])),
            '_': cls.al_ascii(tkt([i for i in range(0x10, 0x30)]
                + [0x40, 0x60, 0x5f, 0x7f])),
            ' ': cls.al_ascii(tkt([i for i in range(0x00, 0x10)])),
            '*': cls.al_ascii(tkt([i for i in range(0x00, 0x80)])),
        }
        return alfabeto if tipo is None else alfabeto[tipo]

    @classmethod
    def ak_kodoj(cls) -> dict[int, str]:
        """Akiri Kodopunktoj de ONKIO."""
        return cls.__KODOJ.copy()



# formatting and printing as markdown tables
def formatter(c: int|str = '', highlight: bool = False) -> str:
    """Add formatting."""
    if isinstance(c, str):
        if c:
            return '***'+c+'***' if highlight else '*'+c+'*'
        return ''
    elif isnan(c):
        return ''
    else:
        txt = '\\' + chr(c) if chr(c) in MARKDOWN_ESCAPABLES else chr(c)
        if highlight:
            txt = '**'+txt+'**'
        return txt
            
def chr_2_txt_ascii(c: int, highlight: bool = False) -> str:
    """Return markdown text description of ASCII code for char c"""
    if c <= 32:
        if c == 0x00:
            return formatter('NULL', highlight)
        elif c == 0x04:    # End of Transmission
            return formatter('EOT',  highlight)
        elif c == 0x07:    # Alert
            return formatter('BELL', highlight)
        elif c == 0x08:    # Backspace
            return formatter(r'BS \\b', highlight)
        elif c == 0x09:    # horizontal tab
            return formatter(r'HT \\t', highlight)
        elif c == 0x0A:    # line feed
            return formatter(r'LF \\n', highlight)
        elif c == 0x0B:    # vertical tab
            return formatter(r'VT \\v', highlight)
        elif c == 0x0C:    # form feed / clear screen / next page
            return formatter(r'FF \\f', highlight)
        elif c == 0x0D:    # carriage return
            return formatter(r'CR \\r', highlight)
        elif c == 0x1A:    # Windows end-of-file
            return formatter('SUB', highlight)
        elif c == 0x1B:    # GCC escape sequence initializer
            return formatter('ESC', highlight)
        elif c == 0x20:
            return formatter('SPACE', highlight)
        else:    # uncommon control char
            # return formatter('0x'+hex(i)[-1]+hex(j)[-1]+'')
            return formatter()
    elif c == 127:
        return formatter('DEL', highlight)
    return formatter(c, highlight)



def chr_2_txt_onkio(c: int, highlight: bool = False) -> str:
    """Return markdown text description of ONKIO code for char c"""
    return chr_2_txt_ascii(ord(ONKIO.al_ascii(c)), highlight)



def get_md_table(
    chr_2_txt = chr_2_txt_ascii,    # type: function
    highlight_func = None,    # type: None|function
    title: str = '',
    nrow: int = 16,
    ncol: int = 8,
) -> str:
    """Get ascii table in markdown format."""
    # init paras
    entry = lambda s='': f"|{s:^13}"
    
    txt  = entry(title) + ''.join(
        [entry(hex(i) + '\\_') for i in range(ncol)]
    ) + '|\n'
    txt += entry(":-------:") + ''.join(
        [entry(":-----:") for i in range(ncol)]
    ) + '|\n'
    for j in range(nrow):    # row
        txt += entry('**0x\\_'+hex(j)[-1]+'**')
        for i in range(ncol):    # col
            c = i*nrow+j  # character code
            highlight = False if highlight_func is None else highlight_func(c)
            txt += entry(chr_2_txt(c, highlight=highlight))
        txt += '|\n'
    return txt



#------------------------------------------------------------------------------

if __name__ == '__main__':
    onkio_kodoj = ONKIO.ak_kodoj()
    txt_ascii = get_md_table(chr_2_txt_ascii, title='ASCII')
    txt_onkio = get_md_table(
        chr_2_txt_onkio, title='ONKIO',
        highlight_func=lambda c: onkio_kodoj[c] != chr(c))
    print(txt_ascii)
    print('\n\n\n')
    print(txt_onkio)
