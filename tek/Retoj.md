---
Title: "Specifoj: Retoj"
Abstract: "Road and rail networks specifications for my Cities: Skylines 2 cities"
DateCreated: 2025-01-08
Categories:
  - "[[Worldbuilding]]"
Projects:
  - "[[Omnijo]]"
IsFictional: true
IsOriginal: true
Authors:
  - "[[HomeOnMars]]"
RelatedPages:
  - "[[Regnʌ_Omnijo]]"
---

Legal
----------------------------------------------------------------------------------------------------------------

> [!CAUTION]
> Information collected/generated here is intended for gameplay purposes,
> *so not much effort has been spent on ensuring its accuracy*.  
> Some maybe incorrect or outdated.
> Some are just chosen arbitrarily.  
> Standards here may also be updated without notices.  
> ***Use at your own risk.***

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

Retoj
----------------------------------------------------------------------------------------------------------------

> Networks  
> [Back to OmniCentro Content](../OmniCentro/_OmniCentro.md#teknikaj-specifoj)

----------------------------------------------------------------------------------------------------------------

> [!NOTE]
> Both trains' and trucks' engine power has been exaggerated by 40\% to 110\%
> compared to real life, since *RO* enjoys technological superiority.  
> See [below verification section](#networks-specification-details-and-verification)
> for calculations.

### Vojoj

> Roads

#### Aŭtovojoj

> Motorways

- Gradient $s$ and Curve radius $R$ limit:

|             |  max Gradient $s$ (Dx) |  min Curve radius $R$ (Dx) | Speed limit $v_\mathrm{max}$ (Dx) | Speed limit $v_\mathrm{max}$ (Hx) | $\theta_\mathrm{64U}$ | $\theta_\mathrm{32U}$ | $\theta_\mathrm{16U}$ | $\theta_\mathrm{8U}$ | Notes |
| ----------- | :-------: | :----------: | :--------: | :--------: | --- | --- | --- | --- | ----- |
| -           |  3.7 \%   |  616m (77U)  |  130 km/h  |  60 JoĜ | $101\degree$ | $135\degree$ | $157\degree$ | $169\degree$ | |
| -           |  5.1 \%   |  424m (53U)  |  110 km/h  |  50 JoĜ | -            | $118\degree$ | $147\degree$ | $163\degree$ | |
| Recommended |  7   \%   |  272m (34U)  |   90 km/h  |  40 JoĜ | -            |  $94\degree$ | $128\degree$ | $154\degree$ | |
| Soft Limit  | 10   \%   |  160m (20U)  |   65 km/h  |  30 JoĜ | -            | -            | $103\degree$ | $137\degree$ | Mountains Only |
| Hard Limit  | 20   \%   |   40m  (5U)  |   35 km/h  |  18 JoĜ | -            | -            | -            |  -           | Mountains Only |

  - $\theta_{d}$ refers to the angle displayed
    when building a 2-phase curve of $d$ - $d$ in game.  
    i.e., $\theta_\mathrm{64u}$ is the angle displayed in game
    when building a curve with 1 bend
    and the shorter one of the two arms of the curve is at least 64u (512m).
  - Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/Grade_(slope)#Roads): US
  - Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/International_E-road_network#Road_design_standards): EU
    - According to the source,
      $R \geq 1000 \mathrm{m}$ for $v_\mathrm{max} \simeq 140 \mathrm{km/h}$;
      and
      $R \geq  120 \mathrm{m}$ for $v_\mathrm{max} \simeq  60 \mathrm{km/h}$.
    - ~~Assuming the Curve radius limit $R \propto v_\mathrm{max}^2$,
      i.e.
      $R \approx v_\mathrm{max}^2 / (30 \mathrm{mh/km})$ for lower  limit,
      and
      $R \approx v_\mathrm{max}^2 / (20 \mathrm{mh/km})$ for higher limit~~.
  - Source: (2024-08-23) [Xin et al. (2021)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0256301): for $R$
    - [figure 8](https://doi.org/10.1371/journal.pone.0256301.g008):
      Predictions of speed thresholds of the truck in a sharp turn
  - Speed unit 'JoĜ' see [Units](Unuoj.md#rapido) page.

#### Stratoj

> Streets

Stratoj here generally refers to roads with pedestrian access (i.e. sidewalks), regardless of it being a road or a street.

Arterial / Collector / Local Roads:

- Gradient limit: (Arbitrarily set to:)

|             | max Gradient $s$ (Dx) | Speed limit $v_\mathrm{max}$ (Dx) | Speed limit $v_\mathrm{max}$ (Hx) | Notes |
| ----------- | :-------: | :-------: | :-------: | ----------- |
| Recommended |  10  \%   |  65 km/h  |  30 JoĜ | `St-Dt` Distributor (2+ Ŭ lanes per direction, no parking, no zoning, tram tracks in the middle)   |
||||||
| Recommended |  15  \%   |  45 km/h  |  20 JoĜ | `St-Ĉf` Local roads (main or low ped activity, tram tracks on the sides)  <br>`St-Sc` Station Roads (for elevated metro stations with optional trams stops)  <br>`St-K` Industrial roads |
| Recommended |  21  \%\* |  35 km/h  |  18 JoĜ | `St-Lk` Local roads (High Ped Activity) |
| Hard Limit  |  33  \%\* |  20 km/h  |  10 JoĜ | `St-Lk` Local roads / Pedestrian Roads |
||||||
| Recommended |  33  \%\* |  10 km/h  |   8 JoĜ | `St-H`  Pedestrian Roads |

  \* Note that vanilla game by default only allow up to $20 \%$ gradient.

- Regarding Speed limits,
  See also:
  - [Units](Unuoj.md#rapido) page;
  - (2025-01-26) [Hussain et al. (2019)](https://doi.org/10.1016/j.aap.2019.05.033) Meta-analysis on pedestrian fatality vs vehicle speed.
- Parking:
  - Default **Price**:
    - Cars: `🪙32` per day/month per spot.
    - Motorcycles: `🪙24` per day/month per spot.
    - Bicycles: Free.
  - Price can be higher
    near high density transit centers
    or wherever deemed necessary.
    No limit has been set on the maximum price.
  - Default **Restrictions** near residential areas:
    - *Maximum* 1 spot per 1u2 (1 grid cell) ground footprint,
      *regardless of builing height or density*.
    - In medium/high density zones, most parking space should be *accessible*,
      since they are expected to be used mostly by the disabled,
      who enjoys subsidies for the parking space costs-
      even though few of them live on the island.

#### Biciklovojoj

> Bike paths

- Gradient limit:

  |             | max Gradient $s$ (Dx) | Speed limit $v_\mathrm{max}$ (Dx) | Speed limit $v_\mathrm{max}$ (Hx) | Notes |
  | ----------- | :-------: | :-------: | :-------: | ----------- |
  | Recommended |   7  \%   |  30 km/h  |  15 JoĜ | |
  |             |  11  \%   |  20 km/h  |  10 JoĜ | |
  |             |  15  \%   |  15 km/h  |   Π JoĜ | |
  | Hard Limit  |  21  \%   |  10 km/h  |   8 JoĜ | |

  - Assuming [e-bike](https://en.wikipedia.org/wiki/Electric_bicycle)
    (2025-12-30).

#### Piedvojoj

> Pedestrian paths

- TBD

### Reloj

> Rails

#### Kargaj kaj malnovaj personaj fervojoj

> Cargo and old passenger railways

- Gradient $s$ and Curve radius $R$ limit:

  |             | max Gradient $s$ (Dx) | min Curve radius $R$ (Dx) | Speed limit $v_\mathrm{max}$ (Dx) | Speed limit $v_\mathrm{max}$ (Hx) | $\theta_\mathrm{64U}$ | $\theta_\mathrm{32U}$ | $\theta_\mathrm{16U}$ | $\theta_\mathrm{8U}$ | Real world examples |
  | ----------- | :--------------: | :------------------: | :--------------------------: | :-----: | --- | --- | --- | --- | ------------------- |
  | Recommended |  1.6 \%  | 1024m (128U) |  175 km/h  |  80 JoĜ | $127\degree$ | $152\degree$ | $166\degree$ | $173\degree$ | (Note: 185km/h for passenger trains; 130km/h for cargo trains) |
  | -           |  1.6 \%  |  576m (72U)   |  130 km/h  |  60 JoĜ |  $97\degree$ | $133\degree$ | $155\degree$ | $168\degree$ | |
  | Soft Limit  |  3.6 \%  |  144m  (18U)  |   65 km/h  |  30 JoĜ | -            | -            |  $97\degree$ | $133\degree$ | Lithgow Zig Zag |
  | Hard Limit  |  5.5 \%  |   64m   (8U)  |   45 km/h  |  20 JoĜ | -            | -            | -            |  $90\degree$ | (Ramps only)    |

  - $\theta_{d}$ refers to the angle displayed when building a 2-phase curve of $d$ - $d$ in game.
    i.e., $\theta_\mathrm{64U}$ is the angle displayed in game when building a curve with 1 bend and the shorter one of the two arms of the curve is at least 64U.
  - Curve radius is obtained by $R \propto v_\mathrm{max}^2$ (See [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant).)
  - Assuming tilting trains.
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant): $R$ info
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples (see Lithgow Zig Zag)
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
  - Note: Liberties have been taken for the hard limit of $s$ due to steep terrain in the map. Also steeper is more fun.
  - Speed unit 'JoĜ' see [Units](Unuoj.md#rapido) page.
- Length / Power
  - Train length:
    25 (16m/2U-long) cars (**400m/50U**, 1 engine + 24 trailers)  
    In practice, use
    21 (16m/2U-long) cars (**336m/42U**, 1 engine & 20 trailers)
    to fit the vanilla port intermodal train station.  
    Extra long trains may go up to 126 cars (2km, 6 engines & 120 trailers).
  - For track intersections: $\geq$ 448m/56U.
  - Assumed power consumption:
    9496hp / 7.1MW / λ⚡ per engine.
  - Due to advanced [*regenerative braking*](https://en.wikipedia.org/wiki/Regenerative_braking) system,
    kinetic energies from trains travelling downhill
    or decelerating to stop at stations
    can be recovered for later uses (e.g. propelling trains uphill
    or accelerating trains when leaving stations).
    So the total power used per train is often less than the above requirements.

#### Altrapidaj fervojoj

> High-speed railways

- Gradient $s$ and Curve radius $R$ limit:

  |             | max Gradient $s$ (Dx) | min Curve radius $R$ (Dx) | Speed limit $v_\mathrm{max}$ (Dx) | Speed limit $v_\mathrm{max}$ (Hx) | $\theta_\mathrm{256U}$ | $\theta_\mathrm{128U}$ | $\theta_\mathrm{64U}$ | $\theta_\mathrm{32U}$ | Real world examples |
  | ----------- | :------: | :------------: | :--------: | :--------: | --- | --- | --- | --- | ------------------- |
  | -           |  1.5 \%  |  6808m (851U)  |  395 km/h  | 120 JoĜ | -            | -            | $172\degree$ | $176\degree$ | |
  | Recommended |  2   \%  |  5376m (672U)  |  350 km/h  | 100 JoĜ | $139\degree$ | $159\degree$ | $170\degree$ | $175\degree$ | (2025-03-02) [Beijing-Shanghai High-Speed Railway](https://en.wikipedia.org/wiki/Beijing%E2%80%93Shanghai_high-speed_railway) |
  | -           |  2.6 \%  |  4120m (515U)  |  305 km/h  |  Υ0 JoĜ | -            | -            | -            | -            | |
  | -           |  3.3 \%  |  3024m (378U)  |  260 km/h  |  Π0 JoĜ | -            | -            | -            | -            | |
  | Soft Limit  |  4.2 \%  |  2104m (263U)  |  220 km/h  |  Δ0 JoĜ | $92\degree$  | $129\degree$ | $153\degree$ | $167\degree$ | |
  | -           |  5.5 \%  |  1344m (168U)  |  175 km/h  |  80 JoĜ | -            | -            | -            | -            | |
  | Hard Limit  |  7.5 \%  |   760m  (95U)  |  130 km/h  |  60 JoĜ | -            | -            | $113\degree$ | $143\degree$ | (*Tunnels* only) |
  | -           |  7.5 \%  |    88m  (11U)  |   45 km/h  |  20 JoĜ | -            | -            | -            | -            | (*Tunnels* only) |

  - Note: Steeper than 5.5\% gradient tracks must be put in **tunnels**
    to shield them from snow and ice,
    thus ensuring trains can climb and brake safely.
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples
- Length / Power
  - Assumed EMU (Electric Multiple Unit).
  - Train length
    <!-- - 12 (20m/2.5u-long) train cars (**240m/30U**). -->
    - 16 (24m/3U-long)  train cars (**384m/48U**)
    - 20 (20m/2½U-long) train cars (**400m/50U**)
    - 24 (16m/2U-long)  train cars (**384m/48U**)
    - Half length permitted
  - For track intersections: $\geq$ 448m/56U.
  - Track and loading gauges see [Unuoj page](Unuoj.md#trakmezurilo).
  - [Track center distance](https://en.wikipedia.org/wiki/Track_spacing#Regulations):
    Minimum 5m, suggested ≥6m.
  - Assumed power consumption:
    1726hp / 1.29MW / 2⚡ per (24m/3U-long) train car —
    Dx20.6MW / Hx20⚡ for a full length train.
  - Due to advanced [*regenerative braking*](https://en.wikipedia.org/wiki/Regenerative_braking) system,
    kinetic energies from trains travelling downhill
    or decelerating to stop at stations
    can be recovered for later uses (e.g. propelling trains uphill
    or accelerating trains when leaving stations).
    So the total power used per train is often less than the above requirements.

#### Metrooj / personaj fervojoj

> Metro / subway / passenger railways

- Gradient $s$ and Curve radius $R$ limit:

  |             | max Gradient $s$ | min Curve radius $R$  | Speed limit $v_\mathrm{max}$ (Dx) | Speed limit $v_\mathrm{max}$ (Hx) | $\theta_\mathrm{64U}$ | $\theta_\mathrm{32U}$ | $\theta_\mathrm{16U}$ | $\theta_\mathrm{8U}$ | Real world examples |
  | ----------- | :--------------: | :------------------------: | :----------------------------: | :--------: | --- | --- | --- | --- | ------------------- |
  | -           |  3.5 \%  | 1024m (128U) |  175 km/h  |  80 JoĜ | $127\degree$ | $152\degree$ | $166\degree$ | $173\degree$ | (Note: overhead-wire-powered tracks only (No third rail metro tracks)) |
  | Recommended |  5.4 \%  |  576m (72U)  |  130 km/h  |  60 JoĜ | $97\degree$ | $133\degree$ | $155\degree$ | $168\degree$ | ($s$) Höllentalbahn (Black Forest), Germany;  <br>($R$) Assuming tilting trains. |
  | Hard Limit  |  7.3 \%  |  320m (40U)  |  100 km/h  |  48 JoĜ | -                 | $103\degree$ | $137\degree$  | $158\degree$ | ($s$) Bernina Railway, Switzerland;  <br>($R$) Bay Area Rapid Transit, United States. |

  - Assuming [*tilting trains*](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant).
  - Assuming trains are powered by
    [*linear induction motor*](https://en.wikipedia.org/wiki/Linear_induction_motor#)
    to climb/descend safely on steep gradients;
    and (magically) improved third rails that are capable of
    transmitting more power and running faster trains without arcing.
  - Note: curve radius restrictions may be relaxed when exiting / entering stations where speed is slow.
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
  - Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples
    - Note: $R$ can go as low as 64m (8u) as seen in Central line, London Underground, United Kingdom; but that's probably too tight.
  - Source: (2024-08-27) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant): $R$ info.
- Length / Power
  - Assumed EMU (Electric Multiple Unit).
  - Train length
    - 8  (24m/3U-long)  train cars (**192m/24U**)
    - 10 (20m/2½U-long) train cars (**200m/25U**)
    - 12 (16m/2U-long) train cars (**192m/24U**)
    - Half length permitted
  - For track intersections: $\geq$ 240m/30U.
  - Track and loading gauges see [Unuoj page](Unuoj.md#trakmezurilo).
  - Assumed power consumption:
    1187hp / 0.9MW / Hx1.6⚡ per (24m/3U-long) train car —
    7.1MW / λ⚡ for a full length train.
  - Stop spacing:
    - Try to keep at least Dx128U (1km, or 5 trains long)
      between metro stations' track connection point;
    - Hard minimum: Dx72U (576m / 3 trains).
    - Ideally \~Dx256U (2km / Dx11 trains), especially in rural area.
- Additional Notes
  - Due to proper designs,
    metros in OmniCentro are capable of (and generally are) running 24/7:
    The wide separation of the tracks
    (track center separation $\geq$ 6m for overhead-wire-powered systems;
    $\geq$ 7m for third-rail-powered systems.
    Here I take the liberty and assume $\geq$ 6m for both.)
    allows maintenance to be done for one side of the dual tracks at night,
    while the night metro running on the other at a reduced frequency.
    Sides alternate each night.
    This is much akin to the real life
    [Copenhagen Metro](https://en.wikipedia.org/wiki/Copenhagen_Metro)
    (2025-02-04).
  - Due to advanced [*regenerative braking*](https://en.wikipedia.org/wiki/Regenerative_braking) system,
    kinetic energies from trains travelling downhill
    or decelerating to stop at stations
    can be recovered for later uses (e.g. propelling trains uphill
    or accelerating trains when leaving stations).
    So the total power used per train is often less than the above requirements.

#### Tramoj

> Trams

- Gradient $s$ limit:

  |             | max Gradient $s$ | min Curve radius $R$ (without slowing)  | Speed limit $v_\mathrm{max}$ (Dx) | Speed limit $v_\mathrm{max}$ (Hx) | Real world examples |
  | ----------- | :--------------: | :--------------: | :--------------------------: | :--------: | ------------------- |
  | Recommended |   9.6 \%  |  384m (48U)  |  90 km/h  |  40 JoĜ | Sheffield Supertram, Sheffield |
  | Recommended |  13   \%  |  216m (27U)  |  65 km/h  |  30 JoĜ | Lisbon Tramways, Portugal |
  | Hard Limit  |  20   \%  |   96m (12U)  |  45 km/h  |  20 JoĜ | |

  - Note: Faster than 65 km/h speed can only be achieved on separated tracks.
  - Note: Steeper than 10\% (especially 13\%) gradient tracks
    assumes *rack-assist* trams
    ([Wikipedia](https://en.wikipedia.org/wiki/Rack_railway#)),
    to ensure safe operations under heavy snows and ice.  
    Rack railways here are magically made faster and more efficient,
    because RO enjoys technological superiority by lore.
  - Curve radius limit here can be ignored, as trams slow down near intersections.
    It is larger than metro when speed is fast,
    because tram tracks are assumed to be non-tilting.
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
- Length / Power
  - Assumed EMU (Electric Multiple Unit).
  - Assumed non-tilting trains.
  - Train length
    - 8  (10m/1¼U-long) tram cars (**80m/10U**)
    - 1/4, 2/4, 3/4 length permitted
    - 3/2 length permitted on special considerations
  - Track and loading gauges see [Unuoj page](Unuoj.md#trakmezurilo).
  - Assumed power consumption:
    810hp / 0.6MW / Hx0.Ψ⚡ per (16m/2U-long) train car —
    total 2.4MW / 5.Δ⚡ for a full length tram.

#### Monoreloj

> Monorails

- Gradient $s$ and Curve radius $R$ limit:

|             | max Gradient $s$ | min Curve radius $R$  | Speed limit $v_\mathrm{max}$ | $\theta_\mathrm{64u}$ | $\theta_\mathrm{32u}$ | $\theta_\mathrm{16u}$ | $\theta_\mathrm{8u}$ | Real world examples |
| ----------- | :--------------: | :------------------------: | :----------------------------: | --- | --- | --- | --- | ------------------- |
| Recommended |  10  \%  |  TBD                     |  80 km/h  | -                 | -                 | -                 | -                 | TBD               |
| Hard Limit  |  12  \%  |  TBD                     |  70 km/h  | -                 | -                 | -                 | -                 | TBD               |

- Source: (2024-09-28) [Miller et al. (2014)](https://www.researchgate.net/publication/301302321_Monorails_for_sustainable_transportation_-_a_review)
  - Table 4.1 $s$ info (Multiplied by 2 since its estimated values seems too conservative in general- see above; same as the speed limit $v_\mathrm{max}$. Also it's a game and steeper/faster is more fun.)

### Networks specification details and verification

> For nerds (like me) only.

#### Angle $\theta_{d}$ equation

$\theta_{d} = 2 \tan^{-1}{\frac{R}{d}}$

```python
    # python code
    import numpy as np
    # Remember to translate radian into degree
    theta_deg = lambda R, d: np.ceil(2*np.atan(R/d)/np.pi*180)
    get_R = lambda theta_deg, d: np.tan(theta_deg/2/180*np.pi)*d
    # Example
    print([(d, theta_deg(R=263, d=d)) for d in (256, 128, 64, 32)])
    print(theta_deg(R=4000, d=512), get_R(theta_deg=166, d=512))
```

#### Analysis of train/truck engine's ability to haul cars

See my python code in [retoj.py](retoj.py).
