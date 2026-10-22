---
Title: "Specifoj: UnuXitʌ Omnijo"
Abstract: Unit system specifications for the fictional country of *Regnʌ Omnijo*
DateCreated: 2024-10-18
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
aliases:
  - UXO
---

Legal
----------------------------------------------------------------------------------------------------------------

> [!WARNING]
> Standards here may also be updated without notices.  

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

Informoj
----------------------------------------------------------------------------------------------------------------

> Information (regarding the unit system)  
> [Back to OmniCentro Content](../OmniCentro/_OmniCentro.md#teknikaj-specifoj)

----------------------------------------------------------------------------------------------------------------

> When sync-ing with the world is no longer an option, ***de-sync***.  
> <span style="color:grey">
> —— <span style="color:#95D0FC">La Arkitekto</span> (fictional)
> </span>

The unit system of Omnijo (UnuXitʌ Omnijo, *UXO*) is based on an alternative version of **Planck natural units**— See [Wikipedia](https://en.wikipedia.org/wiki/Natural_units#Planck_units) and this [Physics Stack Exchange post](https://physics.stackexchange.com/q/3089).

> [!TIP] Planck Unit System Quick Summary
> - Reduced [Planck length](https://simple.wikipedia.org/wiki/Planck_length#) $$l_P \equiv \sqrt{\frac{8 \pi G \hbar}{c^3}}$$
> - Reduced Planck mass $$m_P \equiv \sqrt{\frac{\hbar c}{8 \pi G}}$$
> - Reduced Planck time $$t_P \equiv \sqrt{\frac{8 \pi G \hbar}{c^5}}$$
> - Reduced Planck temperature $$T_P \equiv \sqrt{\frac{\hbar c^5}{8 \pi G k_B^2}}$$
> 
> In which,  
> - $c$ is the [speed of light](https://en.wikipedia.org/wiki/Speed_of_light) in vaccum
> - $\hbar$ is the [reduced Planck constant](https://en.wikipedia.org/wiki/Planck_constant#Reduced_Planck_constant) (\~ photon energy per frequency)
> - $G$ is the [gravitational constant](https://en.wikipedia.org/wiki/Gravitational_constant) (\~ strength of gravity per mass; note that $8 \pi G / c^4 = \kappa$ is the Einstein gravitational constant as used in [Einstein Field Equations](https://en.wikipedia.org/wiki/Einstein_field_equations#Mathematical_form) in General Relativity)
> - $k_B$ is the [Boltzmann constant](https://en.wikipedia.org/wiki/Boltzmann_constant) (molecular energy scale per temperature)
> 
> Under this unit system, we have the benefit of
> $$ c = \hbar = 8 \pi G = k_B = 1 $$

See also [Lingvo](./Lingvo.md#algebro) page for prefix acronyms *H, J, G, M, D, T, I* for Hx10, Hx100, Hx1000, Hx 1 0000 = 1⌄4, 1⌄8, 1⌄Π, 1⌄40, etc; also for Hexadecimal pre/suffix *H* vs Decimal pre/suffix *D*.

Bazaj Unuoj
----------------------------------------------------------------------------------------------------------------

> Base units

### Longeco

> Length

> [!IMPORTANT]
> Base length unit: ***Utro*** `U` (Omnija meter)
>
> $$
> 	\textrm{U}
> 	\equiv 7 \times 2^{111_D} \  l_P
> 	= \text{3.8⌄1Π} \  l_P
> 	\approx 1.4725_D \  \textrm{m}
> $$

> [!Deprecated]- Deprecated Old Definitions
> Deprecated old Utro definition with normal Planck natural unit: $$\text{U} \equiv 11977_D \times 2^{105_D} \  l'_P = 5.Σ92_H \times 10_H^{{1Σ}_H} \  l'_P \approx 7.8525_D \  \text{m}$$ No longer in use, ignore.

Utroj are calilbrated such that 1U is approximately human scale, while the speed of light $c = 1000 \ 0000_H \textrm{U/Ŝ}$ precisely under the [time definition Ŝ](#tempo).

> [!NOTE]
> Useful length unit: ***Ŭtro*** `Ŭ` (CSL length unit)
> 
> $$\text{Ŭ} = \frac{10_H}{3} \  \text{U} \approx 7.8534_D \  \text{m}$$
> 
> - 1 cell width in-game (Cities Skylines 2) is considered as 1 Ŭ exactly
> - Using `Ŭ` instead of `ŭ`, as the [convention](./Lingvo.md#algebro) here is to use capital letter as the first letter

- *HekUtro*  (`HU`) $$\text{HU} \equiv 16_D \  \text{U} \approx 23.560_D \  \text{m}$$
- *JentUtro* (`JU`) $$\text{JU} \equiv 256_D \  \text{U} \approx 376.96_D \  \text{m}$$
- *GilUtro*  (`GU`) $$\text{GU} \equiv 16_D^3 \  \text{U} \approx 6.0314_D \  \text{km}$$
- *MuniUtro*  (`MU`) $$\text{MU} \equiv 16_D^4 \  \text{U} \approx 96.502_D \  \text{km}$$
- One Earth radius is approximately $$R_{\oplus} \approx 42.05_H \  \text{MU} \approx 6371.0_D \  \text{km}$$
- One astronomical unit is approximately $$\text{au} \approx 17.Δ7_H \  \text{DU} \approx 1.4960_D \times 10_D^{8} \  \text{km}$$
- One light-year is approximately $$\text{lyr} \approx 16.Σ3_H \  \text{TU} \approx 9.4607_D \times 10_D^{12_D} \  \text{km}$$
- *hekonUtro* (`hU`) $$\text{hU} \equiv \frac{1}{16_D} \  \text{U} \approx 9.2032_D \  \text{cm}$$
- Nanosvarmo scale *dunionUtro*  (`dU`) $$\text{dU} \equiv 10_H^{-8} \  \text{U} \approx 0.34284_D \  \text{nm}$$

#### Trakmezurilo

> Track gauge

> [!TBC] FIX DESCRIPTIONS BELOW #ToDo/ToImplement 

Track and loading gauges in *RO* are:

- Track gauge  
	1 U (\= 3 hŬ)
- Loading gauge (max width)
	- *Tram*  
		6 hŬ (≈ Dx2.9447 m)
  - *Train/Metro*  
		7 hŬ (≈ Dx3.4354 m)
- Loading gauge (max height, overhead wires, measured in-game in CSL2)  
	- *Tram*  
		9 hŬ (≈ Dx4.4170 m)  
		Tram track are fully embedded at ground level.
  - *Train*  
		Π hŬ (≈ Dx5.8894 m) (above ground)  
		This includes 2 jŬ (≈ Dx6.13 cm) height of the train track. The pure height difference from top of the track to the overhead wires is λ.Υ hŬ (≈ Dx5.8280 m).
- Loading gauge (max height excl. pantograph)  
	- *Tram/Metro*  
		8 hŬ (≈ Dx3.9262 m)
	- *Train*  
		λ hŬ (≈ Dx5.3986 m)
	- Note:
		keep a minimum 3/4 hU electrical clearance inbetween the top of trains and the overhead wires.
- Capacity  
	Assuming each seat is 1 hU wide and 2 hU long, and the cabin is 5 hU tall, this implies a capacity of passengers per U car length of
	- *Tram*:
		<!-- single floor, longitudinal seating layout, 2 seats + 2 standing per 1 hU length, i.e.   -->
		7 passengers/m / 9 passengers/m (door)  
		Dx60 passengers/Ŭ (excluding driver's cabins at both ends),  
		or Dx224 passengers per 4U-long tram.
	- *Metro*:
		<!-- single floor, longitudinal seating layout, driverless, 2 seats + 3 standing per 1 hU length, i.e.   -->
		8 passengers/m (window) / Δ passengers/m (door)  
		Dx68 passengers/Ŭ,  
		or Dx816 passengers per 12U-long metro train.
	- *Train (local)*:
		<!-- double-decker, transverse seating layout, driverless, 6 seats per 2 hU length (plus 1 empty hU for corridors), 1 U single-decker (same stats as metro) + ½ U for stairs/toilets + 1½ U double-decker, i.e.   -->
		Average \~Dx74.67 passengers/Ŭ (excluding driver's cabins),  
		or Dx224 passengers per 3U-long train car,  
		or Dx1792 passengers per 24U-long train.
	- *Train (high speed)*:
		<!-- single floor, transverse seating layout, driverless, 6 seats per 2 hU length (plus 1 empty hU for corridors), i.e.   -->
		6 passengers/m  
		Dx48 passengers/Ŭ
		(excluding driver's cabins, toilets, first class, etc),  
		or Dx120 passengers per 3U-long train car,  
		or Dx960 passengers per 24U-long train.
	- *Train (cargo)*:
		<!-- double-stack, i.e. 2MP/car, i.e.   -->
		8GP/Ŭ, i.e. 38t per car, i.e. \~1kt per engine (hauling 20 cars each) ***FIX THIS*** #ToDo/ToImplement 

Note that the RO track gauge is incompatible with the standard gauge (Dx 1.4725 m) with a difference of 3.74 cm. While fundamentally a result of the author's desire for mathematical simplicity, let's rationalize the reason behind this as part of Omnijo's intentional effort to technologically isolate itself from the rest of the world without directly imposing on people's freedom… Basically one of the main points of coming up with its own unit system in the first place. (The other being satisfying the <span style="color:Beige">Queen</span>'s OCD tendencies.)

The RO loading gauge for trains is \~29cm wider and \~75cm taller than the [European standards](https://en.wikipedia.org/wiki/Loading_gauge#European_standards), and \~4cm wider and \~60cm taller than the [Chinese standards](https://en.wikipedia.org/wiki/Loading_gauge#China).

#### Kontnera Mezurilo

> Container dimensions

> [!TBC] FIX DESCRIPTIONS BELOW #ToDo/ToImplement 

Standard RO container dimensions:

| Name | Width (External, Hx jU) | Height (External, Hx jU) | Length (External, Hx jU) | Internal Dimensions (Hx jU) | Internal Volume (Hx hU^3) | Expected Net weight (Hx MP) | Max Net weight (Hx MP) | Max Gross weight (Hx MP) |
| ---- | --: | --: | --: | :-------------: | :-----: | :-: | :--: | :-: |
|  NKU |  54 |  54 |  Δ8 |  4Ψ x  4Π x  Δ0 |   ΥΔ.88 | 0.8 | 1.08 | 1.2 |
|  DKU |  54 |  54 | 150 |  4Ψ x  4Π x 148 |  1Υ0.ΠΔ | 1.0 | 1.18 | 1.4 |

- Width (External)
  - Hx 5.4 hU (≈ Dx2.5766 m)
    - \~Dx0.1382 m wider than ISO standard.
    - This is constrained by the [standard truck width](https://en.wikipedia.org/wiki/Lane#Lane_width) (2025-10-24) (which is in turn limited by lane width for roads), which is Dx2.6m.
    - Assume a gap of 1jU and a wall thickness of 1½jU on either side, this means an internal width of 4.ΨhU (≈ Dx2.4232 m).
- Height (External)
  - Hx 5.4 hU (≈ Dx2.5766 m)
    - \~Dx0.0142 m shorter than ISO standard.
    - This allows cargo trains to vertically stack 2 containers per car.
    - The matching width and height allows the containers to be potentially stacked sideways (with special inter-direction connecting units in-between), which would hopefully benefit us once we get to space where there is no more definitive concept of the "down" direction.
    - Assume a gap of 4jU thick of wall + interlocking mechanism on either side, this means an internal height of 4.ΠhU (≈ Dx2.3312 m).
- Length (External)
  - Hx Δ.8 hU (≈ Dx5.1532 m)
    - > Container name: **NKU** (Norma KontenerUnuo)
    - \~Dx0.9047 m shorter than ISO [TEU](https://en.wikipedia.org/wiki/Twenty-foot_equivalent_unit) (2025-10-24) standard.
    - Assume a gap of 1jU and a 3jU thick of wall + door locking mechanism on either side, this means an internal length of Δ.0hU (≈ Dx4.9078 m).
    - Internal volume: Hx ΥΔ.88 hU^3 (≈ Dx27.72 m^3)
  - Hx 15 hU (≈ Dx10.3064 m)
    - > Container name: **DKU** (Duobla KontenerUnuo)
    - \~Dx1.8856 m shorter than ISO FEU standard.
    - Precisely 4 times longer than its widths and heights, for easier stacking in any directions (e.g. in space) (Now you can build a fort out of it!).
    - Assume a gap of 1jU and a 3jU thick of wall + door locking mechanism on either side, this means an internal length of 14.8hU (≈ Dx10.0610 m).
    - Internal volume: Hx 1Υ0.ΠΔ hU^3 (≈ Dx56.84 m^3)

The <span style="color:Beige">Queen</span> only really starts to push this standard (both on and off the island) after her 8th coronation anniversary, apparently triggered by the following short period of near-worldwide embargo on her island… But that's another story.  
From there, the RO containers standard gradually spreads across the world.

TBD: decide if I should cave and set the NKU dimensions to be 1:2.5 instead of 1:2.

### Maso

> Mass

> [!IMPORTANT]
> Base mass unit: ***Pakmo*** `P` (Omnija kilogram)
> 
> $$
> 	\text{P}
> 	\equiv 2^{28_D} \  m_P
> 	= 1⌄7 \  m_P
> 	\approx 1.1654_D \  \text{kg}
> $$

> [!Deprecated]- Deprecated Old Definitions
> Deprecated old Pakmo definition with normal Planck natural unit: $$\text{P} \equiv 2^{24_D} \  m'_P = 1⌄6 \  m'_P \approx 0.365_D \  \text{kg}$$ No longer in use, ignore.

- *GilPakmo* (`GP`)

$$
  \text{GP}
  \equiv 2^{12_D} \  \text{P}
  \approx 4.7734_D \  \text{t}
$$

1 DKU container is, on average, assumed to carry 4 GP worth of goods ($1 \  \text{DKU} \approx 4 \  \text{GP} \approx 19.093_D \  \text{t}$).

- *MuniPakmo* (`MP`)

$$
  \textrm{MP}
  \equiv 2^{16_D} \  \textrm{P}
  \approx 76.374_D \  \textrm{t}
$$

which is the weight allowance for 4 DKU containers, used when engineering road/rail/ship designs etc. 

### Tempo

> Time

> [!IMPORTANT]
> Base time unit: ***Ŝekunto*** `Ŝ` (Omnija second)
>
> $$
> 	\text{Ŝ}
> 	\equiv 7 \times 2^{139_D} \  t_P
> 	= \text{3.8⌄23} \  t_P
> 	\approx 1.3185_D \  \text{s}
> $$

> [!Deprecated]- Deprecated Old Definitions
> Deprecated old Ŝekunto definition with normal Planck natural unit: $$\text{Ŝ} \equiv 35931_D \times 2^{129_D} \  t'_P = 1.18λ6⌄24 \  t'_P \approx 1.3183_D \  \text{s}$$ No longer in use, ignore.

Ŝekuntoj are calilbrated such that each Earth day is about $16_D^4 \  Ŝ$, with an approximate difference of only Dx 8.5 SI seconds per day[^Unuoj-5].

[^Unuoj-5]: Note that this difference is much larger than the old def of $1149807 \times 2^{124_D} t'_P$, which has only Dx 0.043 SI seconds difference per day. I prefer the current one because the arbitrary factor `7` is much smaller and simpler (simplicity is beauty in itself!); and that the 9 s difference is still small enough for day-to-day usage (high precision usage like for astronomical purposes will have to use alternative timing system anyway); and that RO will expand beyond Earth one day, so the simplicity of def should take priority over aligning precisely to Earth's rotation cycle, which is also slowing down over millennia.

- ***Ŝekunto*** `Ŝ`: Omnija second
- *munionŜekuntoj* `mŜ`: $$\text{mŜ} \equiv 0.0001_H \  \text{Ŝ} \approx 0.02_D \  \text{ms}$$
- ***Ĉimuto*** `Ĉ`: Omnija Minute $$\text{Ĉ} \equiv \text{JŜ} \approx 5.626_D \  \text{min}$$
- ***Ĝoro*** `Ĝ`: Omnija Hour $$\text{Ĝ} \equiv \text{GŜ} \approx 1.500_D \  \text{hour}$$
- ***Tago*** `⚻` / *MuniŜekuntoj* `MŜ`: Omnija Day $$⚻ = \text{MŜ} = 16_D \  \text{Ĝ} = 256_D \  \text{Ĉ} = 65536_D \  \text{Ŝ}$$
	- Omnijo labour law enforces 7.5-hour (5-Ĝora) workday (30 hours / Hx14Ĝ work per week, as each week have 4 workdays).  
			Each day is divided into 3 shifts:  
			0Ĝ (00:00) -> 6Ĝ (09:00) -> λĜ (16:30) -> Hx10Ĝ (00:00) (midnight next day).  
			Companies have the freedom to shift the beginning of the workday to be up to 1Ĝ earlier.
	- Seven days of the week  
		Usually just use digits 0—6 for Sunday to Saturday, though alternative letter representations are also available below. The symbols are selected to avoid the ones already used in the base-32 ONKIO character set (see [unuoj.py](unuoj.py) `TX_SYMBOLS_DICT['ONKIO']` dict).

| Siglo | Epopo | Esperanto | English |
| :-: | ------ | -------- | --------- |
| Z | Zimanĉo  | Dimanĉo  | Sunday    |
| L | Lundo    | Lundo    | Monday    |
| A | Mardo    | Mardo    | Tuesday   |
| B | Berkredo | Merkredo | Wednesday |
| Ʌ | Ʌaŭdo    | Ĵaŭdo    | Thursday  |
| V | Vendredo | Vendredo | Friday    |
| S | Sabato   | Sabato   | Saturday  |

> [!NOTE]
> the *Omnijaro* weekday cycles are de-synced from Gregorian calendars, due to the extra day(s) at the end of each year.  

- ***Semajno*** `⚝`: Omnija Week
	- Four weeks of the month: labeled as `O`, `I`, `Q`, `U` in that order.
- ***Monato*** `☾`: Omnija Month
- ***Ĵaro*** `Ĵ`: Omnija Unit Year
	- Unit year — Length is precisely Hx 16Σ 34ΠΠ Ŝ (Dx 23 934 156 Ŝ, or about 365.242181 SI days).
	- Hx 80 Ĵ is exactly Hx 80 J under the [Omnijaro calendar rules](#omnijaro-difino), assuming no extra leap seconds added or subtracted.
- ***Jaro*** `J`: Omnija Calendar Year (Earth-specific)
	- Calendar year — Length varies depending on which year it is.
- ***DuniŜekunto*** `DŜ`: Omnija Century (kinda)
	- 1 DŜ = Hx10000⚻ ≈ Dx 179.45 yr

#### Omnijaro

> `Omnijaro` Calendar System (Ø+\* (0xD8))

##### Omnijaro Difino

> Omnijaro definition

- Each non-leap year (*`komunjaro`*) has 13 months plus 1 day exactly, and each months has 4 weeks exactly

  $$1J_\textrm{komun} = Σ \  ☾ + 1 \ ⚻ - 9 \  Ĉ - 34_H \ Ŝ  = 34_H \  ⚝ + Ψ : 6 : ΠΠ = 16Σ_H ⚻ \approx 365_D \  ⚻$$
- Name for the months see [Lingvo](./Lingvo.md#tempo) page.
- Leap year (*`superjaro`*) has 2 extra days outside the normal 13 months:

  $$1J_\textrm{super} = Σ \  ☾ + 2 \  ⚻ - 9 \  Ĉ - 34_H \ Ŝ = 34_H \  ⚝ + 1 \  ⚻ + Ψ : 6 : ΠΠ \approx 366_D \  ⚻$$
- Leap year happens every 4 years, except every Dx128 years. (So ~3 skipped leap years per 400 years— a nice coincidence of hexadecimal system.)  
	More specifically, it happens at Ø+\* years ending with $0_H, 4_H, 8_H, Π_H$, except Ø+\* years ending with $00_H, 80_H$.  
  This is to sync the *Omnijaro* Calendar with [Solar Year](https://en.wikipedia.org/wiki/Tropical_year), so that solstices happens at around the same days in the year.
- Winter Solstice[^Tagoj-Solstico] always happens on the first or last day of the year in the *Omnijaro* calendar. The 1 or 2 extra days are added at the end of the year as the "fake" Dx13th Month ($☾_Σ$, or *`Sigamonato`*), which has only 1 or 2 days (plus/minus extra seconds).
- Ø+\* years ending with $00_H, 80_H$ (i.e. the special non-leapyear) have the solstice happening at approximately midnight between the old and the new year.  
	Because of this, one can imagine Ø+0 is set as 2026-06-22, though I'd really rather left the definition open for interpretation.
- Dx13th Month $☾_Σ$ and the first week of the year are holidays.
- Solstices and Equinoxes are national holidays.
- Any changes to the calendar years system (such as adding leap seconds to sync with Earth's orbit, or more drastic changes in the event of Earth's rotation period or orbit changes significantly) should in principle only be added / removed in Dx13th Month $☾_Σ$.
- In other words, extra seconds may be added or subtracted in $☾_Σ$ to keep the days in sync with [Mean Solar Time](https://en.wikipedia.org/wiki/Solar_time#Mean_solar_time). This means Subtracting Hx 9Ĉ 34Ŝ (≈ Dx 51 minutes 46.3 seconds).
- This means that on average, one Omnija Calendar Year is approximately $1 J \approx 365.24218_D ⚻$ currently, considering both leap years and added seconds.

[^Tagoj-Solstico]: a.k.a. Northern Solstice, since *Insulʌ Omnijo* is located in the Southern Hemisphere.

##### Omnijaro Notacio

> Omnijaro Notations

> [!IMPORTANT]
> **Omnija Epoch**: `2026-06-21T09:30:00+00:00` (ISO 8601 format)  
> A.k.a. 2026-06-21T00:00:00-09:30  
> Northern Solstice 2026, one year before Serena's coronation day.

See also [unuoj.py](unuoj.py) `Datotempo` class.

Two styles:

###### Tempstampo (timestamp) style

Using the number of mŜ (in hexadecimal) after the Omnija Epoch.  
The benefits of the Omnija time unit system is that one can easily read the number of days from the timestamp.

E.g. 2027-12-22T02:41:00+00:00 (Southern Solstice 2027):

> 224 Δ977 1ΨΣ8

Here, '224' is the number of days since the Omnija Epoch in hexadecimal, and 'Δ:9:77' is the Ĝoro:Ĉimuto:Ŝekunto in Omnija timezone, and '1ΨΣ8' is the munionŜekuntoj left over.  
Note: this does not trivially apply before the Omnija Epoch, where the timestamp is negative; And that the added seconds at the end of each year — as well as the SI/RO unit difference — means that the Ĝoro:Ĉimuto:Ŝekunto does not match percisely with the ONKIO style format.

Code Illustration:

```python
from projekty_omnijo.tek.unuoj import Datotempo, datetime, UTC, presi_Hx
tempstampo = Datotempo(datetime(2027, 12, 22, 2, 41, tzinfo=UTC)).tempstampo
print(f"Dx {tempstampo}")
print(presi_Hx(tempstampo, e_sep=''))
```

Result:

```text
Dx 2356485234648 mŜ
Hx 224Δ9771ΨΣ8 mŜ
```

###### ONKIO style (Earth-specific)

- Designed for human-readability
- Start with the 'Ø' symbol to signify the ONKIO Omnijaro calendar format (if dates are included), followed by '-/+' sign and the calendar year (not unit year) number
- Use hyphen to connect year, month, and week-day
- Use letters instead of numbers to represent week and day
- Use '⌄' to separate the dates from time
- Write as `Ĝoro:Ĉimuto:Ŝekunto`
- Ŝekunto has 2 digits while the other 2 has 1, so you can easily tell which ones are which
	- I.e., this helps differentiate between Δ:97 (ΔĈ 97Ŝ) and Δ:9 (ΔĜ 9Ĉ)

Default timezone is Omnijo timezone.

> [!NOTE]
> How to add time zone info: TBD. #ToDo/ToDecide 

E.g. 2027-12-22T02:41:00+00:00 (Southern Solstice 2027):

> Ø+1‐6‐Q1⌄λ:2:Δλ.1ΨΣ8

Code Illustration:

```python
from projekty_omnijo.tek.unuoj import Datotempo, datetime, UTC
t = Datotempo(datetime(2027, 12, 22, 2, 41, tzinfo=UTC))
print(t.iso)
print(t.onkio)
```

Result:

```text
2027-12-22T02:40:59.999984+00:00
Ø+1‐6‐Q1⌄λ:2:Δλ.1ΨΣ8
```

### Temperaturo

> Temperature

> [!IMPORTANT]
> Base temperature unit: ***Zoro*** `Z` (Omnija Kelvin)
>
> $$
>   \text{Z}
>   \equiv 49_D \times 2^{-110_D} \  T_P
>   = \text{Π.4⌄-1λ} \  T_P
>   \approx 1.067_D \  \text{K}
> $$

> [!Deprecated]- Deprecated Old Definitions
> Deprecated old Zoro definition with normal Planck natural unit: $$\text{Z} \equiv 10011_D \times 2^{-120_D} \  T'_P \approx 1.067_D \  \text{K}$$ No longer in use, ignore.

The Zoroj is calilbrated such that Hx100 Z is approximately the [triple point of water](https://en.wikipedia.org/wiki/Triple_point#Triple_point_of_water):
$$
	\text{JZ}
	\equiv 100_H \text{Z}
	\approx 273.10_D \  \text{K}
	\approx -0.051_D \  \degree \text{C}
$$

The boiling point of water is approximately
$$
  100_D \degree \text{C}
  \approx 15Σ.Π9_H \  \text{Z}
$$

$\textrm{Z} = 0$ is exactly the absolute zero temperature.

> [!NOTE]
> Useful temperature unit: ***Zorumgrado*** `°Ž` (0x017D)
> (Omnija degree Celsius)

(Add a caron above 'Z' to make sure people don't confuse `°Ž` with `Z`.)

$$
  X \degree \text{\v{Z}}
  = (100_H + X) \  \text{Z}
$$

Normal body temperature ranges approximately
from $122_H \  \text{Z} = 22_H \degree \text{\v{Z}} \approx 36.2_D \degree \text{C}$
to   $123_H \ \text{Z} = 23_H \degree \text{\v{Z}} \approx 37.3_D \degree \text{C}$.

Ideal room temperature (for thermostat) ranges approximately
from $110_H \  \text{Z} = 10_H \degree \text{\v{Z}} \approx 17.0_D \degree \text{C}$
to   $118_H \  \text{Z} = 18_H \degree \text{\v{Z}} \approx 25.6_D \degree \text{C}$.  
When quoting room temperature in Omnijo, generally it is referring
to   $114_H \  \text{Z} = 14_H \degree \text{\v{Z}} \approx 21.3_D \degree \text{C}$.

### Ŝargo

> Charge

> [!IMPORTANT]
> Base electric charge unit: ***Elektrio*** `E` (Omnija Coulomb)
>
> $$
>   \text{E}
>   \equiv \frac{1}{3} \times 65536_D^4 \  e
>   \approx 0.98516_D \  \text{C}
> $$

Multiplied by 1/3 because quarks have -1/3 e or 2/3 e charges. *Elektrio* is short for *Elektronkvarnitriono*.

### Angulo

> Angle

> [!IMPORTANT]
> Base angle unit: ***Cirklo*** `Ck` (Circle)
>
> $$
>   \text{Ck}
>   \equiv 2 \pi \  \text{rad}
>   = 360_D \degree
> $$

Ck is just a full circle.

- *hekonCirklo* (`hCk`)  $$\text{hCk} \equiv \frac{1}{10_H} \  \text{Ck} = 22.5_D \degree$$
- *jentonCirklo* (`jCk`)  $$\text{jCk} \equiv \frac{1}{100_H} \  \text{Ck} = 1.40625_D \degree$$
- *gilonCirklo* (`gCk`)  $$\text{gCk} \equiv \frac{1}{1000_H} \  \text{Ck} \approx 5.2734_D \  \text{arcmin}$$
- *munionCirklo* (`mCk`)  $$\text{mCk} \equiv \frac{1}{10000_H} \  \text{Ck} \approx 19.775_D \  \text{arcsec}$$
- *dunionCirklo* (`dCk`)  $$\text{dCk} \equiv \frac{1}{10000_H^2} \  \text{Ck} \approx 0.30175_D \  \text{mas}$$

$\text{mas}$ means milliarcsecond.

Note: The angular diameter of the closest star, Proxima Centauri, is Dx 1.02 ± 0.08 mas[^Unuoj-0], or approximately Hx 3.61 dCk.

[^Unuoj-0]: Reference see this ESO article "[How Small are Small Stars Really?](https://www.eso.org/public/news/eso0232/)" (2025-05-21)

### Nombro

> Dimensionless quantities / pure numbers

> [!IMPORTANT]
> Base dimensionless unit: ***Nuo*** `_` (i.e. one)
>
> $$\text{Nuo} \equiv 1$$

- *Pohekvo*  (`⌄`)

$$
  1 ⌄
  \equiv \frac{1}{10_H}
  = \frac{1}{16_D}
  = 6.25 \  \%
$$

- *Pojentvo*  (`⌄⌄`): Hexadecimal equivalent of percent

$$
  1 ⌄⌄
  \equiv \frac{1}{100_H}
  = \frac{1}{256_D}
  = 0.390625 \  \%
$$

### Bito

> Bits and bytes

> [!IMPORTANT]
> Base Bit unit: ***Bito*** `Bit` (Bit, or `B`)
> 
> Omnijo also uses `HB` (Dx 16 Bits) as the byte-equivalent concept in its computational systems, instead of 8 bits like the rest of the world.  

- *HekBito* (`HBito`)  $$\text{HBito} = 10_H \text{Bito} = 2 \text{B}_\text{SI}$$
- *GilBito* (`GBito`)  $$\text{GBito} \equiv 1000_H \  \text{Bito} = ½ \  \text{kB}_\text{SI}$$
- *MuniBito* (`MBito`)  $$\text{MBito} \equiv 10000_H \  \text{Bito} = 8 \  \text{kB}_\text{SI}$$
- *DuniBito* (`DBito`)  $$\text{DBito} \equiv 10000_H^2 \  \text{Bito} = ½ \  \text{GB}_\text{SI}$$
- *TriniBito* (`TBito`)  $$\text{TBito} = 32_D \  \text{TB}_\text{SI}$$
- *KvarniBito* (`RBito`)  $$\text{RBito} = 2 \  \text{EB}_\text{SI}$$

Derivitaj Unuoj
----------------------------------------------------------------------------------------------------------------

> Derived units

### Rapido

> Speed

Standard: Utro por Ŝekuntoj, or U/Ŝ:

$$
	\text{U/Ŝ}
	= \text{JU/Ĉ}
	= \text{GU/Ĝ}
	\approx 1.1168_D \  \text{m/s}
	\approx 4.0205_D \  \text{kph}
$$

#### Speed of light

The speed of light (in vacuum) is exactly

$$
  c
  = 1000 \ 0000_H \  \text{U/Ŝ}
  =        1000_H \  \text{MU/Ŝ}
$$

So when speed exceeds 1 MU/Ŝ (or ≈0.025\%c), relativistic effects should be considered. Also, this means that light in vacuum travels precisely 1 GU in 1 mŜ.

#### Human walking speed

Human walking speed ≈ Dx 1.4 U/Ŝ ≈ 5 kph, or Hx 1.0 \~ 1.8 U/Ŝ (4 \~ 6 kph)[^Unuoj-1].
A 1Ĉ (≈5.6min) walking distance can thus be defined as Hx40U or **Dx64U**, which is approximately Dx503m (or Dx512 CSL meters).

[^Unuoj-1]: Source (2025-07-03) [Wikipedia](https://en.wikipedia.org/wiki/Preferred_walking_speed).

Human jogging speed ranges from Hx 1.8 U/Ŝ (≈ 6 kph) to Hx 2.8 U/Ŝ (≈ Dx 10 kph) [^Unuoj-2].

[^Unuoj-2]: Source: (2025-07-03) [Wikipedia](https://en.wikipedia.org/wiki/Jogging#Definition).

Biking speed (e-bike, relaxing): ≈ 5 U/Ŝ  (≈ Dx 20 kph)[^Unuoj-3].

[^Unuoj-3]: Source: (2025-12-30) [Wikipedia](https://en.wikipedia.org/wiki/Electric_bicycle#Range).

Walkable distances:

| Time (Dx min) | Time (HxĈ) | Distance (Hx U) | Distance (Dx Ŭ) | Distance (Dx $m_\text{CSL}$) |
| :------------ | :--------: | :-------------: | :-------------: | :--------------------------: |
| Dx  6 min     |     1Ĉ     |       140       |       60        |             480              |
| Dx 11 min     |     2Ĉ     |       280       |       120       |             960              |
| Dx 17 min     |     3Ĉ     |       3Π0       |       180       |             1440             |
| Dx 23 min     |     4Ĉ     |       500       |       240       |             1920             |

#### Speed limits examples

(kph limit is corrected with a multiplication factor of `8m/U`)

|   U/Ŝ | CSL kph (proksimumo) | CSL kph (limo) |
| ----: | :------------------: | -------------: |
| Hx 60 |        Dx 386        |         Dx 385 |
| Hx 57 |        Dx 350        |         Dx 350 |
| Hx 40 |        Dx 257        |         Dx 255 |
| Hx 2λ |        Dx 173        |         Dx 175 |
| Hx 20 |        Dx 129        |         Dx 130 |
| Hx 1Υ |        Dx 121        |         Dx 120 |
| Hx 19 |       Dx  101        |         Dx 100 |
| Hx 16 |        Dx  88        |         Dx  90 |
| Hx 13 |        Dx  76        |         Dx  75 |
| Hx 10 |        Dx 64         |          Dx 65 |
|     Π |        Dx  48        |         Dx  50 |
|     Δ |        Dx  40        |         Dx  40 |
|     8 |        Dx  32        |         Dx  30 |
|     5 |        Dx  20        |         Dx  20 |
|     2 |        Dx  8         |         Dx  10 |

### Potenco

> Power

> [!NOTE]
> Useful Power unit: ***MuniLumro*** `⚡` (0x26A1) (Omnija kW)

$$
  ⚡
  \equiv 10000_H \text{Lu}
  = 10000_H \text{U}^2 \text{P} / \text{Ŝ}^3
  \approx 72.25_D \  \text{kW}_\text{SI}
$$

while the power unit ***Lumro*** is defined as

$$
  \text{Lu}
  \equiv \text{U}^2 \text{P} / \text{Ŝ}^3
  \approx 1.1024_D \  \text{W}_\text{SI}
$$

In CSL2, 1 [electricity unit](https://skylines.paradoxwikis.com/Asset_Properties)

$$
  \text{E}_\text{CSL}
  \equiv 16 \text{kW}_\text{CSL}
  \approx 18.062 \text{kW}_\text{SI}
  \equiv \frac{1}{4}⚡
$$

The equivalency of $\text{E}_\text{CSL} \equiv 4 \text{GLu} = \frac{1}{4}⚡$ is imposed by me to simplify calculations.

#### Skalkomparo: Potenco

> Scale Comparison

> [!TBC] FIX BELOW #ToDo/ToImplement 

- m⚡=   Lu ≈ Dx9.8W  
  Approximately one light bulb's power consumption.
- g⚡=  HLu ≈ Dx156W  
  Approximately one human's food energy intake rate (\~Dx100W) or a gaming laptop's power consumption (Dx100W—Dx300W). Allocate \~4HLu power production per citizen for food/electricity/heating etc.
- j⚡=  JLu ≈ Dx2.5kW  
  Approximately the country's power consumption per **1** person (by *RO* standards), given residential power consumption takes approx 1/4 of total power consumption (incl industrial and commercial etc).  
  Or 4 people's total power consumption (electricity + food & heating etc.),  
  or 8 people (3 household)'s electricity consumption
  (electricity only, \~Dx1/3kW per person).  
  A 10 million population mega city requires Dx25GW of power production.
- ⚡ =  MLu ≈ Dx0.64MW = Dx 40 E_csl
- H⚡= HMLu ≈ Dx10MW  
  Approximately of the scale of a large wind turbine.
- J⚡= JMLu ≈ Dx163MW  
  Supports a small town of 65k population.
- G⚡= GMLu ≈ Dx2.6GW  
  Approximately the output of a well-designed hydroelectric dam in-game, or a mini fusion power plant in RO lore.
- M⚡=  DLu ≈ Dx42GW  
  Supports a city of 1⌄6 = Dx 16 777 216 ≈ 17 million people.  
  [OmniCentro](_OmniCentro.md)'s target power poduction is 1 M⚡(Dx41.94304GW).
- D⚡ = TLu  
  Total solar energy received by Earth (including those reflected into space before reaching ground) is about 4 HD⚡:

$$
  \frac{\pi R_{\oplus}^2}{4 \pi (\textrm{au})^2} L_\odot
  \approx 1.74_D \times 10_D^8 \textrm{GW}
  \approx 3Υ.5_H \textrm{TLu}
  \approx 3.Υ5_H \times 10_H^9 ⚡
  \approx 3Υ \  Υ4Πλ \  466λ_H ⚡
$$

  <!-- \approx 3Υ Υ501 0Π25_H ⚡ -->
- R⚡ = VLu  
  The luminosity output of the sun is about 2 HR⚡:

$$
  L_\odot
  \approx 3.828_D \times 10_D^{17_D} \textrm{GW}
  \approx 20.394_H \textrm{VLu}
  \approx 2.0394_H \times 10_H^{11_H} ⚡
  \approx 20 \  3945 \  851Π \  039Π \  0000_H ⚡
$$

Kromaĵo
----------------------------------------------------------------------------------------------------------------

> Extra

### Konstantoj

> Constants

- *Speed of light* (as already mentioned before in [Utro](#longeco))  $$c = l_P / t_P = 1000_H \  \text{MU/Ŝ}$$
- Reduced Planck constant[^Konst-7]  $$\hbar = c \  l_P \  m_P = \frac{2}{7} \times 10_H^{{-1Π}_H} \  \text{U}^2\text{P}/\text{Ŝ}
  \approx \text{4.9249⌄-1Σ} \  \text{U}^2\text{P}/\text{Ŝ}$$
- Gravitational constant[^Konst-7] $$8 \pi G = c^2 \  l_P / m_P = \frac{2}{7} \times 10_H^{{-7}} \  \text{U}^3/(\text{P}\text{Ŝ}^2) \approx \text{4.9249⌄-8} \  \text{U}^3/(\text{P}\text{Ŝ}^2)$$
- Boltzmann constant $$k_B = c^2 \  m_P / T_P = \text{Π.4⌄-14} \  \text{U}^2\text{P}/(\text{Ŝ}^2\text{Z})$$
- Earth surface gravity  $$g_0 \approx λ.94_H \  \text{U}/\text{Ŝ}^2 = 9.81 \  \text{m}/\text{s}^2$$

[^Konst-7]: The denominator of 7 here ultimately comes from the length of a day from the rotation of the Earth in the [time defintion](#Tempo)— hence sadly it cannot be easily removed without making other trade-offs.

### Monero

> Currency

> [!NOTE]
> Currency unit: ***Sejro*** `🪙` (0x1FA99) (Omnija dollar)

<!-- `💲` (0x1F4B2) -->
<!-- `🪙` (0x1FA99) -->

How much is 1 Sejro worth? Using energy price as calibration: In CSL2 game, each MW gives 🪙Dx2500 per month when exported, which means approximately **🪙Dx0.0034 per kWh**.

Considering the energy price in EU after tax in 2024 are around 0.1 €/kWh to 0.4 €/kWh[^Unuoj-4], this means 1🪙 is approximately somewhere in between 30 € and 120 €.

[^Unuoj-4]: See Figure 1 in [this eurostat webpage](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Electricity_price_statistics) (2025-03-15).

Let us assume the energy price in RO is somewhat akin to Iceland (which is also dominated by hydropower), i.e., **🪙1 ≈ € Dx60**.

On the other hand, wage in CSL2 seems to be 🪙Dx2000 per month for Educated employees. Given that minimum wages in Europe is approximately € Dx2000 per month, it would be reasonable to assume **🪙1 ≈ €2**? (I am very confused.)

Perhaps the energy price in CSL2 was meant to be 🪙Dx2500 per hour, not month? In this case, since CSL2 assumes 1 day equals 1 month, it would imply **🪙1 ≈ €2**, and the world makes sense again.

### Code illustrations

See the corresponding [python script](unuoj.py).
