#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Library for Emblem Generation.

Author: HomeOnMars

Note: Require inkscape in external env
    for converting from svg to png/jpg to work properly.
    If unresponsive, try opening inkscape independently at least once.

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------
"""


# imports (built-in)
import os
from os.path import sep
import subprocess
import xml.dom.minidom    # for pretty-print svg files
from datetime import datetime, UTC; now = lambda: datetime.now(UTC)
from collections.abc import Callable
# imports (3rd party)
import numpy as np
from numpy import sqrt, pi, sin, cos, tan, asin, acos, atan
#   svg.py docs
#       <https://github.com/orsinium-labs/svg.py/tree/master>
#       <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch>
import svg



DEFAULT_LICENSE = 'CC BY-NC-SA 4.0'
LICENSE_URLS: dict[str, str] = {
    'CC BY-NC-SA 4.0': 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
}



# params
# PHI : float = (sqrt(5)+1)/2    # golden ratio
# PHI_INV : float = PHI - 1
KOLOROJ : dict[str, str] = {
    # see also: <https://xkcd.com/color/rgb/>
    'O' : '#E6DAA6',  # Beige  E6DAA6 / Gold  FFD700 / Silver  C0C0C0
    'C' : '#00BFFF',  # Blue
    'D' : '#D2691E',  # Orange
    'G' : '#9370DB',  # Purple
    'R' : '#5E9B8A',  # Green
    'x0': '#B7E1A1',  # ^ light grey green  B7E1A1 / beige  E6DAA6
    'x1': '#D6B4FC',  # < light violet  D6B4FC
    'x2': '#95D0FC',  # > light blue  95D0FC
    'Radio': '#FFD700', # Gold
    'White': '#FFFFFF', # as background
}
colors_dict = KOLOROJ.copy()

# funcs
#   angle conversion
# #   theta units convert (hex -> deg)
# def t(theta: float) -> float:
#     """Convert angle from hex to deg."""
#     return theta*(360/16)
# def ts(theta1: float, theta2: float) -> tuple[float, float]:
#     """Convert angles from hex to deg."""
#     return (t(theta1), t(theta2))

sin_deg = lambda ang: sin(ang/180*pi)
cos_deg = lambda ang: cos(ang/180*pi)
tan_deg = lambda ang: tan(ang/180*pi)

def asin_deg(ratio) -> float:
    """asin, returns in [-90, 90]"""
    return asin(ratio) / pi * 180

def acos_deg(ratio) -> float:
    """acos, returns in [0, 180]"""
    return acos(ratio) / pi * 180

def atan_deg(ratio) -> float:
    """atan, returns in [-90, 90]"""
    return atan(ratio) / pi * 180

# def acos_degs(*args) -> tuple[float, float]:
#     return tuple([acos_deg(ratio) for ratio in args])

# def atan_degs(*args) -> tuple[float, float]:
#     return tuple([atan_deg(ratio) for ratio in args])

#------------------------------------------------------------------------------



class Emblemo:
    """Drawing Emblems."""

    def __init__(
        self,
        name: str = "",
        title: None|str = None, # if None, will be the same as name
        scale_y: float = 270,   # 4320 for 8K resolution
        halflim_y: float = 1.,  # half of the math coord limit
        ratio_xy: float = 1.,   # x / y
        center: None|tuple[float, float] = None, # coord of center in [-1, 1]
        colors: dict = KOLOROJ,
        # see kwargs in self.elem_metadata()
        meta_dict: None|dict[str, str] = None,
        **kwargs,
    ):
        self.name: str = name
        self.title: str = f"{self.name} Emblem" if title is None else title
        self._scale_y: int|float = scale_y
        self._scale_x: int|float = None     # will be inited with `ratio_xy`
        self._halflim_y: float = halflim_y
        self._halflim_x: float = None   # will be inited with `ratio_xy`
        self._cx: None|float = None  # will be inited with `center`
        self._cy: None|float = None  # will be inited with `center`
        self.ratio_xy = ratio_xy
        self.colors: dict[str, str] = colors.copy()

        self._dat = svg.SVG(
            width=self.scale_x, height=self.scale_y,
            elements=[],
            preserveAspectRatio = svg.PreserveAspectRatio(
                alignment='xMidYMid', scale_type='meet'),
        )
        
        self._meta_dict: dict[str, str] = meta_dict
        if meta_dict is not None:
            self.dat.elements.append(
                self.elem_metadata(**meta_dict)
            )
        self.add_group()

        if name:
            attr = f'_set_as_{name}'
            if attr not in dir(self):
                raise ValueError(f"Unrecognized Emblem Name '{name}'.")
            getattr(self, attr)(center=center, **kwargs)
        
        self._set_center(center_default=(0, 0))



    # I/O

    def __repr__(self):
        return str(self.dat)

    def __str__(self):
        txt = str(self.dat)
        return xml.dom.minidom.parseString(txt).toprettyxml(indent="  ")

    @property
    def dat(self):
        return self._dat

    @property
    def cg(self):
        """Current Group"""
        return self._dat.elements[-1]

    def add_group(self):
        self._dat.elements.append(svg.G(elements=[]))
        return self

    def define(self, elem: svg.Element):
        """Add defs such as markers or color transitions."""
        self._dat.elements.insert(0 if self._meta_dict is None else 1, elem)
        return self

    @property
    def elems(self):
        return self.cg.elements

    def draw(self, elem: svg.Element):
        self.elems.append(elem)
        return self

    def save(
        self,
        # noext means no extension
        output_path_noext: None|str = None,
        output_exts: set[str] = {'.svg'},
        verbose: bool = True,
    ):
        """Output to files.
        
        Will output '.svg' file regardless of whether it is in the output_exts.
        """

        if not output_exts:
            return
        
        if output_path_noext is None:
            output_path_noext = f'.{sep}{self.name}'
        
        # output to .svg
        ext = '.svg'
        output_path = f"{output_path_noext}{ext}"
        if os.path.exists(output_path) and ext not in output_exts:
            if verbose: print(f"Skipping '{output_path}';")
        else:
            output_exts = set(output_exts) - {ext}
            if verbose:
                print(f"Saving to '{output_path}'...", end=' ', flush=True)
            with open(output_path, 'wb') as f:
                f.write(
                    xml.dom.minidom.parseString(str(self.dat)).toprettyxml(
                        indent="  ", encoding="utf-8"))
            if verbose:
                print(f"Done;", flush=True)

        for ext in output_exts:
            cmds: list[str] = [
                'convert',
                f'{output_path_noext}.svg',     # input
                f'{output_path_noext}{ext}',    # output
            ]
            if verbose:
                print(f"\tRunning '{' '.join(cmds)}'...", end=' ', flush=True)
            subprocess.run(cmds)
            if verbose:
                print(f"Done;", flush=True)

        return self

    def elem_metadata(
        self,
        creator: str,
        license: None|str = None,    # e.g. 'CC BY-NC-SA 4.0',
        dcmitype: str = "Image",
    ) -> svg.Metadata:
        """Gen metadata for svg.
        
        Note: will also include a date timestamp of now.
        """

        # See <http://purl.org/dc/dcmitype/Image>
        if dcmitype not in {'Image', 'StillImage', 'MovingImage', 'Text'}:
            raise ValueError(f"Unrecognized {dcmitype = }.")

        date = now()

        # See <https://www.dublincore.org/specifications/dublin-core/dcq-rdf-xml/>
        metadata = f"""
    <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <cc:Work>
            <dc:type rdf:resource="http://purl.org/dc/dcmitype/{dcmitype}"/>
            <dc:date>{date.isoformat()}</dc:date>
            <dc:format>image/svg+xml</dc:format>
            <dc:title>{self.title}</dc:title>
            <dc:creator>{creator}</dc:creator>"""

        if license is not None:
            license_url = LICENSE_URLS[license]
            metadata += f"""
            <dc:rights rdf:about="{license_url}">This work © {date.year} by {creator} is licensed under {license}.</dc:rights>"""

        metadata += """
        </cc:Work>
    </rdf:RDF>
    """
        # formatting
        metadata = ''.join([line.strip() for line in metadata.splitlines()])
        return svg.Metadata(text=metadata)



    # scales

    @property
    def scale(self) -> float:
        """Math unit to canvas unit."""
        return self.scale_y / self.lim_y

    @property
    def scale_x(self) -> float:
        """Canvas width."""
        return self._scale_x

    @property
    def scale_y(self) -> float:
        """Canvas height."""
        return self._scale_y

    @property
    def lim_x(self) -> float:
        """Math coord width."""
        return self._halflim_x * 2

    @property
    def lim_y(self) -> float:
        """Math coord height."""
        return self._halflim_y * 2

    @property
    def center(self) -> None|tuple[float, float]:
        if self._cx is None or self._cy is None:
            return None
        return (self._cx, self._cy)

    @center.setter
    def center(self, value: None|tuple[float, float]):
        if value is None:
            self._cx = None
            self._cy = None
            return
        self._cx, self._cy = value
        return

    @property
    def ratio_xy(self) -> float:
        return self.scale_x / self.scale_y

    @ratio_xy.setter
    def ratio_xy(self, ratio_xy: float):
        # Note: x dim will be contracted/extended
        _scale_x = ratio_xy*self._scale_y
        if isinstance(self._scale_y, int) and int(_scale_x) == _scale_x:
            self._scale_x = int(_scale_x)
        else:
            self._scale_x = _scale_x
        self._halflim_x = ratio_xy*self._halflim_y

    @property
    def xlims(self) -> tuple[float, float]:
        return (-self._halflim_x-self._cx, self._halflim_x-self._cx)

    @property
    def ylims(self) -> tuple[float, float]:
        return (-self._halflim_y-self._cy, self._halflim_y-self._cy)

    def _x(self, x: float) -> float:
        """Translate math x coord (-X, X') to canvas x coord (0, width)."""
        return (x - self.xlims[0]) / self.lim_x * self.scale_x

    def _y(self, y: float) -> float:
        """Translate math y coord (-Y, Y') to canvas y coord (height, 0)."""
        return (self.ylims[1] - y) / self.lim_y * self.scale_y

    def _xy(self, xy: tuple[float, float]) -> tuple[float, float]:
        """Translate math xy coord to canvas xy coord."""
        return self._x(xy[0]), self._y(xy[1])

    def _r(self, r: float) -> float:
        """Translate radius from math coord (-1, 1) to canvas coord."""
        return r * self.scale

    @staticmethod
    def _url(id: str) -> str:
        return f"url('#{id}')"


    # drawing components

    def elem_arc(
        self,
        radius : float|tuple[float, float],
        thetas : tuple[float, float],   # in deg
        center : tuple[float, float] = (0., 0.),
        angle  : float = -0.,    # in deg, counter-clockwise
        color  : None = None,
        fill   : None|str = 'none',
        linewidth_fac: float = 12/128,
        **kwargs,
    ) -> svg.Element:
        """Draw an arc in ax."""

        # get radius
        try: len(radius)
        except TypeError: radius = (radius, radius)
        stroke_width = self._r(linewidth_fac)

        _rx = self._r(radius[0])
        _ry = self._r(radius[1])

        _pts = tuple([[
            self._x(
                center[0]
                + radius[0] * cos_deg(thetas[i]) * cos_deg(angle)
                - radius[1] * sin_deg(thetas[i]) * sin_deg(angle)),
            self._y(
                center[1]
                + radius[0] * cos_deg(thetas[i]) * sin_deg(angle)
                + radius[1] * sin_deg(thetas[i]) * cos_deg(angle)),
        ] for i in range(2)])
        _x0, _y0 = _pts[0]
        _x1, _y1 = _pts[1]

        large_arc = int(abs(thetas[1] - thetas[0]) >= 180)
        sweep = int(thetas[1] < thetas[0])

        elem = svg.Path(d=[
                svg.MoveTo(_x0, _y0),
                svg.Arc(_rx, _ry, -angle, large_arc, sweep, _x1, _y1),
            ],
            stroke=color, stroke_width=stroke_width, fill=fill,
            **kwargs)
        return elem


    
    def elem_hat(
        self,
        radius : float,
        length : float = 1.,
        center : tuple[float, float] = (0., 0.),
        angle  : float = 0.,      # the rotation of the whole system
        theta  : float = 120.,    # the 'openness' of the hat
        color  : None = None,
        fill   : None|str = 'none',
        linewidth_fac: float = 12/128,
        **kwargs,
    ) -> svg.Element:
        """Draw the hat symbol in ax."""

        stroke_width = self._r(linewidth_fac)

        mid_pt = (
            center[0] + cos_deg(angle)*radius,
            center[1] + sin_deg(angle)*radius)

        elem = svg.Path(d=[
                svg.MoveTo(
                    self._x(mid_pt[0] + cos_deg(angle+180+theta/2)*length),
                    self._y(mid_pt[1] + sin_deg(angle+180+theta/2)*length)),
                svg.LineTo(self._x(mid_pt[0]), self._y(mid_pt[1])),
                svg.LineTo(
                    self._x(mid_pt[0] + cos_deg(angle+180-theta/2)*length),
                    self._y(mid_pt[1] + sin_deg(angle+180-theta/2)*length)),
            ],
            stroke=color, stroke_width=stroke_width, fill=fill,
            **kwargs)
        return elem



    # prefab components

    def _draw_O(self, radius=11/16, color=None, **kwargs):
        if color is None: color = self.colors['O']
        self.draw(self.elem_arc(
            radius=radius, thetas=( # ts( 5.5, 19.50)),
                atan_deg(-9/6) + 180,
                atan_deg( 9/2) + 360,),
            color=color, **kwargs))
        return self
    
    def _draw_C(self, radius=9/16, color=None, **kwargs):
        if color is None: color = self.colors['C']
        self.draw(self.elem_arc(
            radius=radius, thetas=( # ts( 2.25, 14.25)),
                atan_deg( 9/9),
                atan_deg(-9/9) + 360,),
            color=color, **kwargs))
        return self
    
    def _draw_G(
        self,
        radius = 7/16,
        color = None,
        linewidth_fac: float = 12/128,
        fill: None|str = 'none',
        **kwargs,
    ):
        if color is None: color = self.colors['G']
        stroke_width = self._r(linewidth_fac)
        # para
        ang = atan_deg(-9/9)+360
        center_tg3 = (cos_deg(ang)*radius/2, sin_deg(ang)*radius/2)
        # get path
        path1_d = self.elem_arc(
            radius=radius, thetas=( atan_deg( 9/9), ang, ),
            color=color, **kwargs).d
        path2_d = self.elem_arc(
            radius=[radius/2, radius*5/8], thetas=(0, 180),
            center=center_tg3, angle=ang, color=color, **kwargs).d
        pathdata = path1_d + path2_d[1:]
        # save
        self.draw(svg.Path(
            d=pathdata,
            stroke=color, stroke_width=stroke_width, fill=fill,
            **kwargs))
        return self

    def _draw_R(
        self, radius=13.875/16, linewidth_fac=18/128, R_h=None, angle=None,
        color=None, **kwargs):
        if color is None: color = self.colors['O']
        if angle is None:
            if R_h is not None:
                angle = asin_deg(R_h / (radius + linewidth_fac))
            else:
                raise ValueError("Please supply R's height in R_h input par.")
        self.draw(self.elem_arc(
            radius=radius, thetas=(angle, -angle),
            color=color, linewidth_fac=linewidth_fac, **kwargs))
        return self



    # set as

    def _set_center(
        self,
        center: None|tuple[float, float] = None,
        center_default: None|tuple[float, float] = (0., 0.),
    ):
        """Set self.center to centerif given, otherwise set to default."""
        if center is not None:
            self.center = center
        elif self.center is None and center_default is not None:
            self.center = center_default
        return



    def _set_as_RO(self, center:None|tuple[float, float]=None):
        """Draw the RO emblem."""
        self._set_center(center, (-1.5/16, 0))
        self._draw_RO()
        return self

    def _draw_RO(self):
        # 16/128  21/(9*16) ~ 18.667
        self._draw_O(linewidth_fac=16/128)#, zorder=0x1001)
        self._draw_R(angle=atan_deg(9/6))#, zorder=0x1000)
        return self



    def _set_as_ROFlago(self, center:None|tuple[float, float]=None, **kwargs):
        # plot
        """Draw the RO Flag."""
        self._set_center(center, (-1.5/16, 0))


        # --- background
        dy_dx = -9/6
        angle = atan_deg(dy_dx) + 90
        slash_loc_xs = (
            self._x(-tan_deg(angle)*self.ylims[0]),    # bottom
            self._x(-tan_deg(angle)*self.ylims[1]),    # top
        )    # slash positions (canvas coord)
        ddx = 80/256    # color transition band width (half)
        ddd = 2**(-20)  # a tiny number
                        # to make sure the color gradient is in correct order

        id_ROColorGradient = "ROColorGradient"
        self.define(svg.Defs(elements=[
            svg.LinearGradient(id=id_ROColorGradient, gradientTransform=[
                svg.Scale(x=1/self.ratio_xy, y=1),
                svg.Translate(
                    x = (self.lim_x/2 + self.center[0]) / self.lim_y - 0.5,
                    y = -self.center[1] / self.lim_y,
                ),
                # Rotate(): x, y: center of rotation
                svg.Rotate(-angle, x=0.5, y=0.5)
            ], elements=[
                svg.Stop(offset=0.5-ddx,
                    stop_color=self.colors['C'],  stop_opacity=0),
                svg.Stop(offset=0.5-ddd,
                    stop_color=self.colors['x2'], stop_opacity=1),
                svg.Stop(offset=0.5+ddd,
                    stop_color=self.colors['x1'], stop_opacity=1),
                svg.Stop(offset=0.5+ddx,
                    stop_color=self.colors['G'],  stop_opacity=0),
            ])
        ]))

        # background
        #   to make the color transition on top sharper
        #   (by varing the opacity as well as color)
        self.draw(svg.Path(
            d=[
                svg.MoveTo(0, self.scale_y),
                svg.LineTo(slash_loc_xs[0], self.scale_y),
                svg.LineTo(slash_loc_xs[1], 0),
                svg.LineTo(0, 0),
                svg.Z(),
            ],
            fill=self.colors['C'],
            **kwargs))
        self.draw(svg.Path(
            d=[
                svg.MoveTo(self.scale_x, self.scale_y),
                svg.LineTo(self.scale_x, 0),
                svg.LineTo(slash_loc_xs[1], 0),
                svg.LineTo(slash_loc_xs[0], self.scale_y),
                svg.Z(),
            ],
            fill=self.colors['G'],
            **kwargs))

        # color transition
        self.draw(svg.Rect(
            x=0, y=0,
            width=self.scale_x, height=self.scale_y,
            fill=self._url(id_ROColorGradient),
        ))

        # main symbol
        self._draw_RO()

        return self



    def _set_as_OCFD(self, center:None|tuple[float, float]=None):
        """Draw the OCFD emblem."""
        self._set_center(center)

        linewidth_fac: float = 16/128
        radius: float = 9/16
        color  : None = self.colors['D']
        fill   : None|str = 'none'
        kwargs = {}

        angle  : float = atan_deg(8/6) # 60    # in deg

        h = radius * cos_deg(angle)
        r = radius
        y0 = 3/256
        stroke_width = self._r(linewidth_fac)

        self.draw(svg.Path(d=[
                svg.MoveTo(self._x(h*(6/9)), self._y(y0+h)),
                svg.LineTo(self._x(-r*sin_deg(angle)), self._y(y0+h)),
                svg.LineTo(self._x(0),  self._y(y0-radius)),
                svg.LineTo(self._x( r*sin_deg(angle)), self._y(y0+h)),
                svg.LineTo(
                    self._x((r-linewidth_fac/4)*sin_deg(angle)), self._y(y0+h)),
                svg.LineTo(
                    self._x((-linewidth_fac/4)*sin_deg(angle)),
                    self._y(y0-radius)),
            ],
            stroke=color, stroke_width=stroke_width, fill=fill,
            **kwargs))

        # self.add_group()
        # self._draw_RO()

        return self



    def _set_as_OCFE(self, center:None|tuple[float, float]=None):
        """Draw the OCFE emblem."""
        self._set_center(center)

        linewidth_fac: float = 6/128
        stroke_width = self._r(linewidth_fac)
        stroke_linejoin = 'round'  # "Literal['miter', 'round', 'bevel', 'inherit'] | None"
        radius: float = 8.5/16
        kwargs = {}

        id_OCFEMarker = "OCFEMarker"
        self.define(svg.Marker(
            id=id_OCFEMarker,
            markerUnits='strokeWidth',
            refX=2.5,
            refY=2.5,
            markerWidth=5,
            markerHeight=5,
            elements=[
                svg.Circle(
                    cx=2.5,
                    cy=2.5,
                    r=1.5,
                    fill=self.colors['White'],
                    stroke=self.colors['C'],
                ),
            ],
        ))

        # h = radius * 0.625 / 8
        # d = radius * 0.625
        d0 = radius * cos_deg(atan_deg(9/6))
        h0 = radius * sin_deg(atan_deg(9/6))
        h1 = h0 / 8 * 5
        d1 = sqrt(radius**2 - h1**2)

        ptss = [[ # layer 0
            (-d0,  h0),
            (-radius, 0),
            (-d0, -h0),
        ], [ # layer 1
            ( d1,  h1),
            ( d1, -h1),
        ]]

        self.draw(svg.Path(
            d=[
                # svg.MoveTo(*self._xy(ptss[1][0])),
                svg.MoveTo(*self._xy(ptss[0][0])),
                svg.LineTo(*self._xy(ptss[1][1])),
                svg.LineTo(*self._xy(ptss[0][1])),
                svg.LineTo(*self._xy(ptss[1][0])),
                svg.LineTo(*self._xy(ptss[0][2])),
                # svg.LineTo(*self._xy(ptss[1][1])),
            ],
            fill='none',
            stroke=self.colors['C'],
            stroke_width=stroke_width,
            stroke_linejoin=stroke_linejoin,
            marker_start=self._url(id_OCFEMarker),
            marker_mid=self._url(id_OCFEMarker),
            marker_end=self._url(id_OCFEMarker),
            **kwargs))

        # self.add_group()
        # self._draw_RO()

        return self



    def _set_as_OCFI(
        self,
        center:None|tuple[float, float]=None,
        fill:bool=False,
    ):
        """Draw the OCFI emblem."""
        self._set_center(center)

        linewidth_fac: float = 10/128
        stroke_width = self._r(linewidth_fac)
        stroke_linejoin = 'round'  # "Literal['miter', 'round', 'bevel', 'inherit'] | None"
        radius: float = 9.25/16
        kwargs = {}

        # u for unit
        # The OCFI sigil is based on a hexagon of side length of 2u
        u = radius / 2
        # x1 is the x coord of the right side of that hexagon
        x1 = 2*u*cos_deg(30)
        # x2 is the x coord of the central triangle
        x2 = 2*x1*sin_deg(18)

        pts = [
            # external hexagon
            (  0,  2*u),    # 0
            (-x1,    u),    # 1
            (-x1,   -u),    # 2
            (  0, -2*u),    # 3
            ( x1,   -u),    # 4
            ( x1,    u),    # 5
            # internal triangle (moved slightly downward to improve looks)
            ( x2,  0.8*u),    # 6
            (-x2,  0.8*u),    # 7
            (  0, -1.2*u),    # 8
        ]
        tridefs = [
            # {'d': (0, 1, 2, 3, 4, 5), 'fill': None},
            {'d': (6, 7, 8), 'fill': 'O'}, # central triangle
            {'d': (0, 7, 6), 'fill': 'x1'}, # middle upper
            {'d': (0, 1, 7), 'fill': 'x2'}, # left upper
            {'d': (1, 2, 7), 'fill': 'x2'}, # left middle
            {'d': (2, 8, 7), 'fill': 'x1'}, # left middle
            {'d': (2, 3, 8), 'fill': 'x2'}, # left lower
            {'d': (3, 4, 8), 'fill': 'x2'}, # right lower
            {'d': (4, 6, 8), 'fill': 'x1'}, # right middle
            {'d': (4, 5, 6), 'fill': 'x2'}, # right middle
            {'d': (5, 0, 6), 'fill': 'x2'}, # right upper
        ]

        for tridef in tridefs:
            self.draw(svg.Path(
                d=[
                    svg.MoveTo(*self._xy(pts[tridef['d'][0]]))]
                + [
                    svg.LineTo(*self._xy(pts[d]))
                    for d in tridef['d'][1:]]
                + [svg.Z()],
                fill = (
                    self.colors.get(tridef.get('fill', None), 'none')
                    if fill else 'none'
                ),
                stroke=self.colors['G'],
                stroke_width=stroke_width,
                stroke_linejoin=stroke_linejoin,
                **kwargs))
        self.cg.transform = svg.Rotate(-60, self._x(0), self._y(0))

        # self.add_group()
        # self._draw_RO()

        return self



    def _set_as_OCG(self, center:None|tuple[float, float]=None):
        """Draw the OCG emblem."""
        self._set_center(center)
        # --- arcs
        self._draw_O()
        self._draw_C()
        self._draw_G()
        # --- hats
        self.draw(self.elem_hat(radius=14.5/16, length=9.5/16,
                angle=90, theta=128, color=self.colors['x0']))
        for i in range(1, 3):
            self.draw(self.elem_hat(radius=15.25/16, length=7.5/16,
                    angle=90+120*i, color=self.colors[f'x{i}']))
        return self



    def _set_as_OCR(self, center:None|tuple[float, float]=None):
        """Draw the OCR emblem."""
        self._set_center(center)
        # --- arcs
        self._draw_O()
        self._draw_C()
        # draw R
        self.draw(self.elem_arc(
            radius=6.75/16, thetas=(90, -112.5),
            color=self.colors['R'], linewidth_fac=16/128))



    def _set_as_OCRR(self, center:None|tuple[float, float]=None):
        """Draw the OCRR emblem."""
        self._set_center(center, (-3/16, 0))
        # --- arcs
        #    wid is half line width
        O_rad, O_wid = 11/16, 18/128
        self._draw_O(
            radius=O_rad, color=self.colors['x0'],   linewidth_fac=O_wid)
        self._draw_C(
            radius=8/16, color=self.colors['Radio'], linewidth_fac=18/128)
        # draw R
        #   depends on _draw_O angle
        R_h = sin(atan( 3/1)) * (O_rad + O_wid)
        # R_h = O_rad + O_wid
        self._draw_R(
            R_h=R_h, radius=14/16, linewidth_fac=18/128,
            color=self.colors['x2'])
        self._draw_R(
            R_h=R_h, radius=17/16, linewidth_fac=18/128,
            color=self.colors['x1'])



if __name__ == '__main__':

    redraw_all: bool = False
    debug: bool = True
    meta_dict = {
        'creator': "HomeOnMars",
        'license': 'CC BY-NC-SA 4.0',
    }
    ROFlagoTitle = "Regnʌ Omnijo (RO) flag (fictional) for my world-building project"
    exts = {'.svg', '.png'}    # png files support transparent background

    if redraw_all:
        Emblemo("OCFD", meta_dict=meta_dict).save(None, exts)
        Emblemo("OCFE", meta_dict=meta_dict).save(None, exts)
        Emblemo("OCFI", meta_dict=meta_dict).save(None, exts)
        Emblemo("OCFI", meta_dict=meta_dict, fill=True).save(
            "OCFI.kolor", exts)
        Emblemo("OCG",  meta_dict=meta_dict).save(None, exts)
        Emblemo("OCR",  meta_dict=meta_dict).save(None, exts)
        Emblemo("OCRR", meta_dict=meta_dict).save(None, exts)
        Emblemo("RO",   meta_dict=meta_dict).save(None, exts)
        exts = {'.svg', '.jpg'}    # jpg files are smaller
        Emblemo("ROFlago", meta_dict=meta_dict, title=ROFlagoTitle,
            halflim_y=1.0, ratio_xy=16/9).save(None, exts)
        Emblemo(
            "ROFlago", meta_dict=meta_dict, title=ROFlagoTitle,
            halflim_y=1.0, ratio_xy=1/1,  scale_y=2160,
            ).save("ROFlago.emb", exts)
        Emblemo(
            "ROFlago", meta_dict=meta_dict, title=ROFlagoTitle,
            halflim_y=1.0, ratio_xy=16/9, scale_y=2160
            ).save("ROFlago.plen", exts)
        Emblemo(
            "ROFlago", meta_dict=meta_dict, title=ROFlagoTitle,
            halflim_y=9/8, ratio_xy=5/3,  scale_y=2160
            ).save("ROFlago.x5y3", exts)
    if debug:
        # pass
        Emblemo("OCFD", meta_dict=meta_dict).save(None, exts)
        Emblemo("OCFE", meta_dict=meta_dict).save(None, exts)
        Emblemo("OCFI", meta_dict=meta_dict).save(None, exts)
        Emblemo("OCFI", meta_dict=meta_dict, fill=True).save(
            "OCFI.kolor", exts)
