---
Title: "Specifoj: ONKIO"
Abstract: Character encoding standard specifications for the fictional country of *Regnʌ Omnijo*
DateCreated: 2024-10-24
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

> [!Important]
> ONKIO: **O**mnija **N**orma **K**odo por **I**nformo-interŝanĝ**O**
<!-- > ONKIO: Omnija Norma Kodo por Informo-Interŝanĝo -->

Legal
----------------------------------------------------------------------------------------------------------------

> [!WARNING]
> ONKIO table may be updated here without notice.  
> (You can check the past versions in commit histories.)

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/HomeOnMars/projekty_omnijo/blob/master/tek/ONKIO.md">ONKIO</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

ONKIO Tablo
----------------------------------------------------------------------------------------------------------------

> ONKIO Table  
> [Back to OmniCentro Content](../OmniCentro/_OmniCentro.md#teknikaj-specifoj)

----------------------------------------------------------------------------------------------------------------

Table generation code see [onkio.py](onkio.py);  
Differences from the ASCII table are highlighted with **bold** text.

|   ONKIO   |   0x0\_   | 0x1\_  | 0x2\_  | 0x3\_ |    0x4\_    | 0x5\_  | 0x6\_ | 0x7\_ |
| :-------: | :-------: | :----: | :----: | :---: | :---------: | :----: | :---: | :---: |
| **0x\_0** |  *NULL*   | **\\** | **\_** |   0   | ***SPACE*** |   P    | **‐** |   p   |
| **0x\_1** |           | **/**  |   \!   |   1   |      A      |   Q    |   a   |   q   |
| **0x\_2** |           | **\`** | **~**  |   2   |      B      |   R    |   b   |   r   |
| **0x\_3** |           | **\{** |   \#   |   3   |      C      |   S    |   c   |   s   |
| **0x\_4** |   *EOT*   | **\|** | **、**  |   4   |      D      |   T    |   d   |   t   |
| **0x\_5** |           | **\}** | **\@** |   5   |      E      |   U    |   e   |   u   |
| **0x\_6** |           | **"**  | **'**  |   6   |      F      |   V    |   f   |   v   |
| **0x\_7** |  *BELL*   | **\<** | **%**  |   7   |      G      | **Ŭ**  |   g   | **ŭ** |
| **0x\_8** | *BS \\b*  | **\>** | **=**  |   8   |      H      |   X    |   h   |   x   |
| **0x\_9** | *HT \\t*  | **\[** | **\(** |   9   |      I      | **Ʌ**  |   i   | **ʌ** |
| **0x\_a** | *LF \\n*  | **\]** | **\)** | **Δ** |      J      |   Z    |   j   |   z   |
| **0x\_b** | *VT \\v*  | **\*** |   \+   | **λ** |      K      | **Ĉ**  |   k   | **ĉ** |
| **0x\_c** | *FF \\f*  | **$**  | **⌄**  | **Π** |      L      | **Ĝ**  |   l   | **ĝ** |
| **0x\_d** | ***SUB*** | **:**  | **−**  | **Σ** |      M      | **Ĵ**  |   m   | **ĵ** |
| **0x\_e** | ***ESC*** | **;**  | **^**  | **Υ** |      N      | **Ŝ**  |   n   | **ŝ** |
| **0x\_f** | ***DEL*** | **?**  | **—**  | **Ψ** |      O      | **\.** |   o   | **,** |

###  All ONKIO Characters

```text
ABCDEFGHIJKLMNOPQRSTUVŬXɅZĈĜĴŜ
abcdefghijklmnopqrstuvŭxʌzĉĝĵŝ
0123456789ΔλΠΣΥΨ
\/`{|}"<>[]*$:;?_!~#、@'%=()+⌄−^— ‐.,
```

### Notes

- See also *Epopo* specifications in the [Lingvo](Lingvo.md#epopo) page.
- Built-in support for *hexadecimal* characters :-D
	- 10~15 are represented as Greek letters `Δ λ Π Σ Υ Ψ`, as shown in the column `0x3_` in the above table.
	- Note that `Υ` is the Greek letter `γ` (but capitalized), not English letter `Y`.
	- Designs
		- `Δ λ Π` as 10-12 (looks like D L N), and `Σ Υ Ψ` as 13-15 (looks like Z Y W; Σ before Ψ because it is so in Greek letters, it's easier for computers to sort.)
		- `β` was avoided deliberately due to it looks like 8 under certain fonts. So are `δ~6`, `θ/Θ/Ω~0`, `ξ~3`, `Γ~7`, `ζ~2/5`, `Ξ~111`, `Χ~×` (math multiplication symbol).
		- Conventional English characters `A B C D E F` were also avoided, to allow differentiation between numbers and texts.
		- The center of mass of the numbers `ΔλΠΣΥΨ` are the about the same as `0-9`, unlike most lower case Greek letters.
- Only 16 control characters (all in the column `0x0_`) instead of 33 in ASCII table, as most of those extra control characters are obsolete in modern days.
- Removed `CR \r` and moved `DEL` from `0x7f` to `0x0f` to maximize regularity.
- Added symbols
	- `⌄` (projento) for 'per Dx256', the scientific notation operator, and the separator in [Omnijaro](Unuoj.md#omnijaro) calendar expression
	- `—` (em dash)
	- `−` (minus)
	- `‐` (hyphen)
	- `、` (enumeration comma) (Replacing the ampersand `&` in most functions)
- Removed the ampersand `&`.
- Recast symbol `%` as 'modulus operator'.
- Letters
	- Letters and the most common punctuation marks are contained within `0x4_` to `0x7_`. This is designed to make compression of pure Epopo text mildly easier (and more fun to encode with techniques like ROT13-equivalent and such).
	- English letters are mostly untouched from ASCII (except `W Y`), so plain ASCII texts should hopefully still be mostly legible if conversion failed or missed. (Most punctuation marks will be messed up though.)
- Arrangement:
	- To reduce the risk of a single bit flip (e.g. from cosmic rays) causing something catastrophic and hard to detect for codes, the special symbols (`0x1_` and `0x2_`) columns are separated into two groups based on their last 4 bits: with odd numbers of 1s and 0s (1, 2, 4, 7, 8, λ, Σ, Υ), and with even numbers of 1s and 0s (0, 3, 5, 6, 9, Δ, Π, Ψ). Each group are safe from single bit flipped into another symbol within the group, but not from the other group in the same column. The two columns are safe from each other.
	- The *odd* group are assigned numerical and logical operators: ``+ - ^ % 、! = ~ * / | < > ` : ; ``
	- The *even* group are assigned grouping operators and other symbols: ``( ) @ # ' — ⌄ { } [ ] " ` $ `` etc 
	- `0x2_` column symbols are more suitable for being included in file names; while `0x1_` are best avoided, as they are more commonly used in shell scripts.

ASCII Table
----------------------------------------------------------------------------------------------------------------

For comparison:

- Reference: (2024-10-18) [Wikipedia](https://en.wikipedia.org/wiki/ASCII).

|   ASCII   |  0x0\_   | 0x1\_ |  0x2\_  | 0x3\_ | 0x4\_ | 0x5\_ | 0x6\_ | 0x7\_ |
| :-------: | :------: | :---: | :-----: | :---: | :---: | :---: | :---: | :---: |
| **0x\_0** |  *NULL*  |       | *SPACE* |   0   |  \@   |   P   |  \`   |   p   |
| **0x\_1** |          |       |   \!    |   1   |   A   |   Q   |   a   |   q   |
| **0x\_2** |          |       |    "    |   2   |   B   |   R   |   b   |   r   |
| **0x\_3** |          |       |   \#    |   3   |   C   |   S   |   c   |   s   |
| **0x\_4** |  *EOT*   |       |    $    |   4   |   D   |   T   |   d   |   t   |
| **0x\_5** |          |       |    %    |   5   |   E   |   U   |   e   |   u   |
| **0x\_6** |          |       |    &    |   6   |   F   |   V   |   f   |   v   |
| **0x\_7** |  *BELL*  |       |    '    |   7   |   G   |   W   |   g   |   w   |
| **0x\_8** | *BS \\b* |       |   \(    |   8   |   H   |   X   |   h   |   x   |
| **0x\_9** | *HT \\t* |       |   \)    |   9   |   I   |   Y   |   i   |   y   |
| **0x\_a** | *LF \\n* | *SUB* |   \*    |   :   |   J   |   Z   |   j   |   z   |
| **0x\_b** | *VT \\v* | *ESC* |   \+    |   ;   |   K   |  \[   |   k   |  \{   |
| **0x\_c** | *FF \\f* |       |    ,    |  \<   |   L   |  \\   |   l   |  \|   |
| **0x\_d** | *CR \\r* |       |   \-    |   =   |   M   |  \]   |   m   |  \}   |
| **0x\_e** |          |       |   \.    |  \>   |   N   |   ^   |   n   |   ~   |
| **0x\_f** |          |       |    /    |   ?   |   O   |  \_   |   o   | *DEL* |
