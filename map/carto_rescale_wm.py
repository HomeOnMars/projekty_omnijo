#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Rescale Carto Mod output when exporting worldmap as playable area

Author: HomeOnMars

-------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2025 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------------------
"""

# built-in libs
from os import sep
import subprocess

# 3rd-party libs
from osgeo import gdal
gdal.UseExceptions()


def rescale_wm(
    scale : float = 4,    # new / old
    # folder: remember the 'sep' at the end
    folder: str   = f'Data{sep}WorldMap_x4{sep}',
    dry_run: bool = False,
    verbose: bool = True,
):
    # --- init ---
    
    if verbose:
        print()
        subprocess.run(['pwd', '-P'])

    file = gdal.Open(f'{folder}GeoTIFF{sep}Terrain.tif')
    trans_pars = file.GetGeoTransform()
    nx, ny = file.RasterXSize, file.RasterYSize
    # calc center coord, which will be maintained the same
    x0 = trans_pars[0] + nx/2 * trans_pars[1] + ny/2 * trans_pars[2]
    y0 = trans_pars[3] + nx/2 * trans_pars[4] + ny/2 * trans_pars[5]
    # get new trans_pars
    ds_x_2, ds_y_2 = (    # haldwidth new
        nx/2 * trans_pars[1]*scale + ny/2 * trans_pars[2]*scale,
        nx/2 * trans_pars[4]*scale + ny/2 * trans_pars[5]*scale
    )
    ullr = [
        x0 - ds_x_2, y0 - ds_y_2,
        x0 + ds_x_2, y0 + ds_y_2,
    ]
    if False:
        trans_pars_new = [
            None,
            trans_pars[1] * scale,
            trans_pars[2] * scale,
            None,
            trans_pars[4] * scale,
            trans_pars[5] * scale,
        ]
        trans_pars_new[0] = x0 - nx/2 * trans_pars_new[1] - ny/2 * trans_pars_new[2]
        trans_pars_new[3] = y0 - nx/2 * trans_pars_new[4] - ny/2 * trans_pars_new[5]
    if verbose:
        print(f"{nx, ny = }\t{x0, y0 = }\n{trans_pars     = }\n{ullr = }")

    # --- prepare output ---

    cmds: list[list[str]] = []
    # cmds.append(['pwd', '-P'])

    # Fix worldmap
    cmds.append([
        'gdal_translate',
        '-a_scale', f'{scale}',    # scale up height
        '-a_ullr', *[f"{par:.9f}" for par in ullr],
        f'{folder}GeoTIFF{sep}Terrain.tif',    # input
        f'{folder}GeoTIFF{sep}Terrain_corrected.tif'    # output
    ])
    cmds.append([
        'gdal_translate',
        '-a_scale', f'{scale}',    # scale up height
        '-a_ullr', *[f"{par:.9f}" for par in ullr],
        f'{folder}GeoTIFF{sep}Water.tif',    # input
        f'{folder}GeoTIFF{sep}Water_corrected.tif'    # output
    ])

    # --- run ---

    for cmd in cmds:
        if verbose: print(f"\t$ {' '.join(cmd)}")
        if not dry_run: subprocess.run(cmd)

    return



if __name__ == '__main__':
    for scale, folder in (
        ( 4, f'Data{sep}WorldMap_x4{sep}',),
        (64, f'Data{sep}WorldMap_x64{sep}',),
    ):
        rescale_wm(
            scale=scale, folder=folder,
            dry_run = False,
        )
