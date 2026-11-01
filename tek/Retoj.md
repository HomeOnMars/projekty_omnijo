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

**Gradient $s$ and curve radius $R$ limit**:

|             | Max<br>Gradient<br>$s$ | Min<br>Curve Radius<br>$R$ (Dx CSL) | Speed Limit<br>$v_\text{max}$ | $\theta_\text{64Ŭ}$ | $\theta_\text{32Ŭ}$ | $\theta_\text{16Ŭ}$ | $\theta_\text{8Ŭ}$ | Notes          |
| ----------- | ---------------------: | ----------------------------------: | ----------------------------: | ------------------: | ------------------: | ------------------: | -----------------: | -------------- |
| -           |           3.9\%<br>Δ⌄⌄ |                       640 m<br>80 Ŭ |         130 km/h<br>Hx 20 U/Ŝ |                103° |                137° |                158° |               169° |                |
| Recommended |          7.0\%<br>12⌄⌄ |                       360 m<br>45 Ŭ |         100 km/h<br>Hx 18 U/Ŝ |                   - |                110° |                141° |               160° |                |
| Soft Limit  |          9.4\%<br>18⌄⌄ |                       160 m<br>20 Ŭ |          65 km/h<br>Hx 10 U/Ŝ |                   - |                   - |                103° |               137° | Mountains Only |
| -           |         12.5\%<br>20⌄⌄ |                       90 m<br>11¼ Ŭ |              50 km/h<br>Π U/Ŝ |                   - |                   - |                   - |               110° | Mountains Only |
| Hard Limit  |         15.6\%<br>28⌄⌄ |                         64 m<br>8 Ŭ |              40 km/h<br>Δ U/Ŝ |                   - |                   - |                   - |                90° | Mountains Only |

- $\theta_{d}$ refers to the angle displayed when building a 2-phase curve of $d$ - $d$ in game.
	- i.e., $\theta_\text{64Ŭ}$ is the angle displayed in game when building a curve with 1 bend and the shorter one of the two arms of the curve is at least 64 Ŭ (512 m).
- Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/Grade_(slope)#Roads): US
- Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/International_E-road_network#Road_design_standards): EU
	- According to the source, $R \geq 1000 \text{m}$ for $v_\text{max} \simeq 140 \text{km/h}$; and $R \geq  120 \text{m}$ for $v_\text{max} \simeq  60 \text{km/h}$.
	- ~~Assuming the Curve radius limit $R \propto v_\text{max}^2$, i.e. $R \approx v_\text{max}^2 / (30 \text{mh/km})$ for lower  limit, and $R \approx v_\text{max}^2 / (20 \text{mh/km})$ for higher limit~~.
- Source: (2024-08-23) [Xin et al. (2021)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0256301): for $R$
	- [figure 8](https://doi.org/10.1371/journal.pone.0256301.g008): Predictions of speed thresholds of the truck in a sharp turn
- Speed unit 'U/Ŝ' see [Units](Unuoj.md#rapido) page.

#### Stratoj

> Streets

Stratoj here generally refers to roads with pedestrian access (i.e. sidewalks), regardless of it being a road or a street.

Arterial / Collector / Local Roads:

**Gradient $s$ limit** (Arbitrarily set to:)

|             | Max<br>Gradient<br>$s$ | Speed Limit<br>$v_\text{max}$ | Notes                                                                                                                                                     |
| ----------- | ---------------------: | ----------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommended |          9.4\%<br>18⌄⌄ |          65 km/h<br>Hx 10 U/Ŝ | `St-Dt` Distributor (2+ Ŭ lanes per direction, no parking, no zoning, tram tracks in the middle)                                                          |
| Recommended |         12.5\%<br>20⌄⌄ |              50 km/h<br>Π U/Ŝ | `St-K` Industrial roads                                                                                                                                   |
| Recommended |         15.6\%<br>28⌄⌄ |              40 km/h<br>Δ U/Ŝ | `St-Ĉf` Local roads (main or low ped activity, tram tracks on the sides)<br>`St-Sc` Station Roads (for elevated metro stations with optional trams stops) |
| Recommended |       25\%[^1]<br>40⌄⌄ |              30 km/h<br>8 U/Ŝ | `St-Lk` Local roads (High Ped Activity)                                                                                                                   |
| Hard Limit  |     37.5\%[^1]<br>60⌄⌄ |              20 km/h<br>5 U/Ŝ | `St-Lk` Local roads / Pedestrian Roads                                                                                                                    |
| Recommended |     37.5\%[^1]<br>60⌄⌄ |              10 km/h<br>2 U/Ŝ | `St-H`  Pedestrian Roads                                                                                                                                  |

[^1]: Note that vanilla game by default only allow up to 20 \% gradient.

- Regarding Speed limits, see also:
	- [Units](Unuoj.md#rapido) page;
	- (2025-01-26) [Hussain et al. (2019)](https://doi.org/10.1016/j.aap.2019.05.033) Meta-analysis on pedestrian fatality vs vehicle speed.
- Parking:
	- Default **Price**:
		- Cars: `🪙32` per day/month per spot.
		- Motorcycles: `🪙24` per day/month per spot.
		- Bicycles: Free.
	- Price can be higher near high density transit centers or wherever deemed necessary. No limit has been set on the maximum price.
	- Default **Restrictions** near residential areas:
		- *Maximum* 1 spot per 1 $\text{Ŭ}^2$ (1 grid cell) ground footprint, *regardless of building height or density*.
		- In medium/high density zones, most parking space should be *accessible*, since they are expected to be used mostly by the disabled, who enjoys subsidies for the parking space costs— even though few of them live on the island.

#### Biciklovojoj

> Bike paths

**Gradient $s$ limit:**

|             | Max<br>Gradient<br>$s$ | Speed Limit<br>$v_\text{max}$ |
| ----------- | ---------------------: | ----------------------------: |
| Recommended |          7.0\%<br>12⌄⌄ |              30 km/h<br>8 U/Ŝ |
|             |         12.5\%<br>20⌄⌄ |              20 km/h<br>5 U/Ŝ |
|             |         15.6\%<br>28⌄⌄ |              15 km/h<br>4 U/Ŝ |
| Hard Limit  |       25\%[^1]<br>40⌄⌄ |              10 km/h<br>2 U/Ŝ |

- Assuming [e-bike](https://en.wikipedia.org/wiki/Electric_bicycle) (2025-12-30).

#### Piedvojoj

> Pedestrian paths

- TBD

### Reloj

> Rails

#### Kargaj kaj malnovaj personaj fervojoj

> Cargo and old passenger railways

**Gradient $s$ and curve radius $R$ limit**:

|             | Max<br>Gradient<br>$s$ | Min<br>Curve Radius<br>$R$ (Dx CSL) | Speed Limit<br>$v_\text{max}$ | $\theta_\text{64Ŭ}$ | $\theta_\text{32Ŭ}$ | $\theta_\text{16Ŭ}$ | $\theta_\text{8Ŭ}$ | Real World Examples                                              |
| ----------- | ---------------------: | ----------------------------------: | ----------------------------: | ------------------: | ------------------: | ------------------: | -----------------: | ---------------------------------------------------------------- |
| Recommended |           1.6\%<br>4⌄⌄ |                     1296 m<br>162 Ŭ |         195 km/h<br>Hx 30 U/Ŝ |                137° |                158° |                169° |               175° | Note: 195km/h for passenger trains;<br>130km/h for cargo trains. |
| Recommended |           1.6\%<br>4⌄⌄ |                       576 m<br>72 Ŭ |         130 km/h<br>Hx 20 U/Ŝ |                 97° |                133° |                155° |               168° |                                                                  |
| Soft Limit  |         3.7\%<br>9.8⌄⌄ |                       144 m<br>18 Ŭ |          65 km/h<br>Hx 10 U/Ŝ |                   - |                   - |                 97° |               133° | Lithgow Zig Zag                                                  |
| Hard Limit  |           5.5\%<br>Υ⌄⌄ |                        69 m<br>8⅝ Ŭ |              45 km/h<br>λ U/Ŝ |                   - |                   - |                   - |                95° | (Ramps only)                                                     |

- Notes
	- $\theta_{d}$ refers to the angle displayed when building a 2-phase curve of $d$ - $d$ in game.
		i.e., $\theta_\text{64U}$ is the angle displayed in game when building a curve with 1 bend and the shorter one of the two arms of the curve is at least 64U.
	- Curve radius is obtained by $R \propto v_\text{max}^2$ (See [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant).)
	- Assuming tilting trains.
	- Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant): $R$ info
	- Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples (see Lithgow Zig Zag)
	- Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
	- Note: Liberties have been taken for the hard limit of $s$ due to steep terrain in the map. Also steeper is more fun.
	- Speed unit 'U/Ŝ' see [Units](Unuoj.md#rapido) page.
- Length / Power
	- Train length: 25 (16m/2U-long) cars (**400m/50Ŭ**, 1 engine + 24 trailers)  
		- In practice, use 21 (16m/2U-long) cars (**336m/42Ŭ**, 1 engine & 20 trailers) to fit the vanilla port intermodal train station
		- Extra long trains may go up to 126 cars (2km, 6 engines & 120 trailers).
	- For track intersections: $\geq$ 448m/56Ŭ.
	- Assumed power consumption: 9300 hp / 6.9MW / Hx 60 ⚡ per engine.
	- Due to advanced [*regenerative braking*](https://en.wikipedia.org/wiki/Regenerative_braking) system, kinetic energies from trains travelling downhill or decelerating to stop at stations can be recovered for later uses (e.g. propelling trains uphill or accelerating trains when leaving stations). So the total power used per train is often less than the above requirements.

#### Altrapidaj fervojoj

> High-speed railways

**Gradient $s$ and curve radius $R$ limit**:

|             | Max<br>Gradient<br>$s$ | Min<br>Curve Radius<br>$R$ (Dx CSL) | Speed Limit<br>$v_\text{max}$ | $\theta_\text{256Ŭ}$ | $\theta_\text{128Ŭ}$ | $\theta_\text{64Ŭ}$ | $\theta_\text{32Ŭ}$ | Real World Examples                                                                                                           |
| ----------- | ---------------------: | ----------------------------------: | ----------------------------: | -------------------: | -------------------: | ------------------: | ------------------: | :---------------------------------------------------------------------------------------------------------------------------- |
| -           |           1.2\%<br>3⌄⌄ |                     7200 m<br>900 Ŭ |         455 km/h<br>Hx 6Ψ U/Ŝ |                 149° |                 164° |                172° |                176° |                                                                                                                               |
| Recommended |           2.0\%<br>5⌄⌄ |                     5376 m<br>672 Ŭ |         395 km/h<br>Hx 60 U/Ŝ |                 139° |                 159° |                170° |                175° | (2025-03-02) [Beijing-Shanghai High-Speed Railway](https://en.wikipedia.org/wiki/Beijing%E2%80%93Shanghai_high-speed_railway) |
| Soft Limit  |           4.3\%<br>λ⌄⌄ |                     2400 m<br>300 Ŭ |         260 km/h<br>Hx 40 U/Ŝ |                 100° |                 134° |                156° |                168° |                                                                                                                               |
| Hard Limit  |          7.0\%<br>12⌄⌄ |                     1032 m<br>129 Ŭ |         170 km/h<br>Hx 2Δ U/Ŝ |                    - |                  91° |                128° |                153° | (*Tunnels* only)                                                                                                              |
| -           |          7.0\%<br>12⌄⌄ |                         72 m<br>9 Ŭ |              45 km/h<br>λ U/Ŝ |                    - |                    - |                   - |                   - | (*Tunnels* only)                                                                                                              |

- Notes
	- Note: Steeper than 5.5\% gradient tracks must be put in **tunnels** to shield them from snow and ice, thus ensuring trains can climb and brake safely.
	- Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
	- Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples
- Length / Power
	- Assumed EMU (Electric Multiple Unit).
	- Train length
		- 16 (24m/3Ŭ-long)  train cars (**384m/48Ŭ**)
		- 20 (20m/2½Ŭ-long) train cars (**400m/50Ŭ**)
		- 24 (16m/2Ŭ-long)  train cars (**384m/48Ŭ**)
		- Half length permitted
  - For track intersections: $\geq$ 448 m / 56 Ŭ.
  - Track and loading gauges see [Unuoj page](Unuoj.md#trakmezurilo).
  - [Track center distance](https://en.wikipedia.org/wiki/Track_spacing#Regulations): Minimum 5m, suggested ≥6m.
  - Assumed power consumption: 1744 hp / 1.30MW / Hx 12 ⚡ per (24m/3Ŭ-long) train car— Dx 20.8 MW / Hx 120 ⚡ for a full length train.
  - Due to advanced [*regenerative braking*](https://en.wikipedia.org/wiki/Regenerative_braking) system, kinetic energies from trains travelling downhill or decelerating to stop at stations can be recovered for later uses (e.g. propelling trains uphill or accelerating trains when leaving stations). So the total power used per train is often less than the above requirements.

#### Metrooj / personaj fervojoj

> Metro / subway / passenger railways

**Gradient $s$ and curve radius $R$ limit**:

|             | Max<br>Gradient<br>$s$ | Min<br>Curve Radius<br>$R$ (Dx CSL) | Speed Limit<br>$v_\text{max}$ | $\theta_\text{64Ŭ}$ | $\theta_\text{32Ŭ}$ | $\theta_\text{16Ŭ}$ | $\theta_\text{8Ŭ}$ | Real World Examples                                                                   |
| ----------- | ---------------------: | ----------------------------------: | ----------------------------: | ------------------: | ------------------: | ------------------: | -----------------: | :------------------------------------------------------------------------------------ |
| -           |           3.9\%<br>Δ⌄⌄ |                     1024 m<br>128 Ŭ |         195 km/h<br>Hx 30 U/Ŝ |                127° |                152° |                166° |               173° | (Note: overhead-wire-powered tracks only, no third rail metro tracks)                 |
| Recommended |           5.9\%<br>Ψ⌄⌄ |                       576 m<br>72 Ŭ |         145 km/h<br>Hx 24 U/Ŝ |                 97° |                133° |                155° |               168° | ($s$) Höllentalbahn (Black Forest), Germany;  <br>($R$) Assuming tilting trains.      |
| Hard Limit  |          7.8\%<br>14⌄⌄ |                       336 m<br>42 Ŭ |         115 km/h<br>Hx 1Π U/Ŝ |                   - |                106° |                139° |               159° | ($s$) Bernina Railway, Switzerland;  <br>($R$) Bay Area Rapid Transit, United States. |

- Notes
	- Assuming [*tilting trains*](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant).
	- Assuming trains are powered by [*linear induction motor*](https://en.wikipedia.org/wiki/Linear_induction_motor#) to climb/descend safely on steep gradients; and (magically) improved third rails that are capable of transmitting more power and running faster trains without arcing.
	- Note: curve radius restrictions may be relaxed when exiting / entering stations where speed is slow.
	- Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
	- Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples
		- Note: $R$ can go as low as 64m (8Ŭ) as seen in Central line, London Underground, United Kingdom; but that's probably too tight.
	- Source: (2024-08-27) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant): $R$ info.
- Length / Power
	- Assumed EMU (Electric Multiple Unit).
	- Train length
		- 8  (24m/3Ŭ-long)  train cars (**192m/24Ŭ**)
		- 10 (20m/2½Ŭ-long) train cars (**200m/25Ŭ**)
		- 12 (16m/2Ŭ-long) train cars (**192m/24Ŭ**)
		- Half length permitted
	- For track intersections: $\geq$ 240m/30Ŭ.
	- Track and loading gauges see [Unuoj page](Unuoj.md#trakmezurilo).
	- Assumed power consumption: 1163 hp / 0.867 MW / Π ⚡ per (24m/3Ŭ-long) train car— 6.9 MW / Hx 60 ⚡ for a full length train.
- Stop spacing:
	- Try to keep at least Dx 120 Ŭ (1km, or 5 trains long) between metro stations' track connection point;
	- Hard minimum: Dx 72 Ŭ (576m / 3 trains).
	- Ideally $\gtrsim$ Dx 240 Ŭ (2km / Dx 10 trains), especially outside CBDs.
- Additional Notes
	- Due to proper designs, metros in OmniCentro are capable of (and generally are) running 24/7: The wide separation of the tracks (track center separation $\geq$ 6m for overhead-wire-powered systems; $\geq$ 7m for third-rail-powered systems. Here I take the liberty and assume $\geq$ 6m for both.) allows maintenance to be done for one side of the dual tracks at night, while the night metro running on the other at a reduced frequency. Sides alternate each night. This is much akin to the real life [Copenhagen Metro](https://en.wikipedia.org/wiki/Copenhagen_Metro) (2025-02-04).
	- Due to advanced [*regenerative braking*](https://en.wikipedia.org/wiki/Regenerative_braking) system, kinetic energies from trains travelling downhill or decelerating to stop at stations can be recovered for later uses (e.g. propelling trains uphill or accelerating trains when leaving stations). So the total power used per train is often less than the above requirements.

#### Tramoj

> Trams

**Gradient $s$ and curve radius $R$ limit**:

|             | Max<br>Gradient<br>$s$ | Min<br>Curve Radius<br>$R$ (Dx CSL) | Speed Limit<br>$v_\text{max}$ | Real world examples            |
| ----------- | ---------------------: | ----------------------------------: | ----------------------------: | :----------------------------- |
| Recommended |          9.4\%<br>18⌄⌄ |                       384 m<br>48 Ŭ |          85 km/h<br>Hx 15 U/Ŝ | Sheffield Supertram, Sheffield |
| Recommended |         12.5\%<br>20⌄⌄ |                       216 m<br>27 Ŭ |          65 km/h<br>Hx 10 U/Ŝ | Lisbon Tramways, Portugal      |
| Hard Limit  |         25.0\%<br>40⌄⌄ |                        54 m<br>6¾ Ŭ |              30 km/h<br>8 U/Ŝ |                                |

- Notes
	- Note: Faster than 65 km/h speed can only be achieved on separated tracks.
	- Note: Steeper than 12.5\% gradient tracks assumes *rack-assist* trams ([Wikipedia](https://en.wikipedia.org/wiki/Rack_railway#)), to ensure safe operations under heavy snows and ice. Rack railways here are magically made faster and more efficient, because RO enjoys technological superiority by lore.
	- Curve radius limit here can be ignored, as trams slow down near intersections. It is larger than metro when speed is fast, because tram tracks are assumed to be non-tilting.
	- Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
- Length / Power
	- Assumed EMU (Electric Multiple Unit).
	- Assumed non-tilting trains.
	- Train length
		- 8  (10m/1¼Ŭ-long) tram cars (**80m/10Ŭ**)
		- 1/4, 2/4, 3/4 length permitted
		- 3/2 length permitted on special considerations
	- Track and loading gauges see [Unuoj page](Unuoj.md#trakmezurilo).
	- Assumed power consumption: 581 hp / 0.433 MW / 6 ⚡ per (12m/1½Ŭ-long) train car— total 3.5 MW / Hx 30 ⚡ for a full length tram.

#### Monoreloj

> Monorails

**Gradient $s$ and curve radius $R$ limit**:

|             | Max<br>Gradient<br>$s$ | Min<br>Curve Radius<br>$R$ | Speed Limit<br>$v_\text{max}$ | Real world examples |
| ----------- | ---------------------: | -------------------------: | ----------------------------: | :------------------ |
| Recommended |          9.4\%<br>18⌄⌄ |                        TBD |          80 km/h<br>Hx 14 U/Ŝ | TBD                 |
| Hard Limit  |         12.5\%<br>20⌄⌄ |                        TBD |          70 km/h<br>Hx 12 U/Ŝ | TBD                 |

- Source: (2024-09-28) [Miller et al. (2014)](https://www.researchgate.net/publication/301302321_Monorails_for_sustainable_transportation_-_a_review)
	- Table 4.1 $s$ info (Multiplied by 2 since its estimated values seems too conservative in general- see above; same as the speed limit $v_\text{max}$. Also it's a game and steeper/faster is more fun.)

### Networks specification details and verification

#### Angle $\theta_{d}$ equation

$$\theta_{d} = 2 \tan^{-1}{\frac{R}{d}}$$

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
