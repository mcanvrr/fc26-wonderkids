# FC 26 Wonderkid List - Veri Seti ile Tam Tarama (POT ≥ 82)

## Giriş ve metodoloji

Bu dosya **otomatik üretilmiştir** (`scripts/generate_fc26_wonderkid_list.py`). Ham veri: [EAFC26-DataHub](https://github.com/ismailoksuz/EAFC26-DataHub) içindeki Kaggle tabanlı **`players.csv`** (yaklaşık 18,405 oyuncu, `fifa_version`=26, son satır tarihi **2025-09-19**). **Not:** Bu dışa aktarım, yüzünüzdeki FC 26 sürümünden (ör. Mart 2026 title update) farklı olabilir; kesin değerler için kendi kariyer save’inizdeki gözlemciyi kullanın.

- **Filtre:** `potential >= 82`, `age <= 23`
- **Pozisyon:** `player_positions` alanındaki her kod (GK, CB, LB, …) ilgili tabloya bir satır üretir; aynı oyuncu çok mevkiliyse **birden fazla bölümde** görünür (scout mantığı: her hat için ayrı aday).
- **Para birimi:** `value_eur` / `wage_eur` yaklaşık **£**’ye çevrilmiştir (EUR × 0,86; maaş haftalık).
- **Türk oyuncular:** `nationality_name == Türkiye` olanlar **Notlar** sütununda `Türk Yeteneği` ile işaretlenir; her bölüm sonundaki öneri alt başlığında önceliklendirilir.

### Veri kapsamı özeti (bu filtreye göre)

- **Benzersiz oyuncu sayısı (filtre içi):** 643
- **Tablo satır sayıları (çok mevkili tekrarlar dahil):**
  - Kaleciler (GK / KL): **28** satır
  - Stoperler (CB / D(M)): **120** satır
  - Sol Bekler (LB / D(Sol)): **66** satır
  - Sağ Bekler (RB / D(Sağ)): **56** satır
  - Defansif Orta Saha (CDM / DOS): **116** satır
  - Merkez Orta Saha (CM / OS(M)): **225** satır
  - Ofansif Orta Saha (CAM / OOS): **173** satır
  - Sağ Kanat & Sağ Orta Saha (RM / RW): **198** satır
  - Sol Kanat & Sol Orta Saha (LM / LW): **188** satır
  - Santraforlar (ST / CF / SNT): **119** satır

## 1. Kaleciler (GK / KL)

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L. Chevalier | Fransa | KL (GK) | Paris Saint-Germain | 23 | £37.8M | 83 | 88 | £43k | +5 | — | 3★ | 1★ | 189 / 84 | — |
| A. Trubin | Ukrayna | KL (GK) | SL Benfica | 23 | £31.0M | 80 | 87 | £10k | +7 | — | 2★ | 1★ | 199 / 86 | — |
| S. Lammens | Belçika | KL (GK) | Manchester United | 22 | £23.6M | 78 | 87 | £31k | +9 | — | 4★ | 1★ | 193 / 92 | — |
| K. Tzolakis | Yunanistan | KL (GK) | Olympiacos FC | 22 | £26.2M | 79 | 86 | £15k | +7 | — | 3★ | 1★ | 193 / 80 | — |
| G. Restes | Fransa | KL (GK) | Toulouse FC | 20 | £22.8M | 78 | 86 | £8k | +8 | — | 3★ | 1★ | 188 / 82 | — |
| M. Vandevoordt | Belçika | KL (GK) | RB Leipzig | 23 | £12.5M | 76 | 86 | £18k | +10 | — | 3★ | 1★ | 192 / 81 | — |
| M. Epolo | Belçika | KL (GK) | Standard de Liège | 20 | £5.59M | 73 | 85 | £4k | +12 | — | 2★ | 1★ | 187 / 77 | High Growth |
| B. Verbruggen | Hollanda | KL (GK) | Brighton & Hove Albion | 22 | £15.9M | 78 | 84 | £34k | +6 | — | 4★ | 1★ | 193 / 89 | — |
| J. Trafford | İngiltere | KL (GK) | Manchester City | 22 | £12.5M | 76 | 84 | £35k | +8 | — | 3★ | 1★ | 197 / 90 | — |
| J. Urbig | Almanya | KL (GK) | FC Bayern München | 21 | £6.88M | 74 | 84 | £13k | +10 | — | 4★ | 1★ | 189 / 83 | — |
| R. Roefs | Hollanda | KL (GK) | Sunderland | 22 | £6.88M | 74 | 84 | £19k | +10 | — | 3★ | 1★ | 192 / 72 | — |
| M. Penders | Belçika | KL (GK) | RC Strasbourg Alsace | 19 | £4.73M | 73 | 84 | £18k | +11 | — | 2★ | 1★ | 200 / 95 | — |
| R. Owusu-Oduro | Hollanda | KL (GK) | AZ Alkmaar | 20 | £3.44M | 71 | 84 | £4k | +13 | — | 3★ | 1★ | 188 / 82 | Hidden Gem, Ucuz Cevher, High Growth |
| D. Seimen | Almanya | KL (GK) | SC Paderborn 07 | 19 | £1.72M | 66 | 84 | £3k | +18 | — | 4★ | 1★ | 190 / 89 | Hidden Gem, Ucuz Cevher, High Growth |
| F. Jörgensen | Danimarka | KL (GK) | Chelsea | 23 | £11.6M | 77 | 83 | £39k | +6 | — | 3★ | 1★ | 192 / 85 | — |
| N. Atubolu | Almanya | KL (GK) | SC Freiburg | 23 | £11.6M | 77 | 83 | £12k | +6 | — | 3★ | 1★ | 190 / 99 | — |
| E. Caprile | İtalya | KL (GK) | Cagliari | 23 | £11.2M | 76 | 83 | £5k | +7 | — | 3★ | 1★ | 191 / 74 | — |
| L. Hornicek | Czechia | KL (GK) | Sporting Clube de Braga | 22 | £5.16M | 73 | 83 | £5k | +10 | — | 2★ | 1★ | 194 / 90 | — |
| F. Stanković | Sırbistan | KL (GK) | Venezia | 23 | £6.88M | 74 | 82 | £2k | +8 | — | 3★ | 1★ | 187 / 79 | — |
| S. Turati | İtalya | KL (GK) | Sassuolo | 23 | £6.88M | 74 | 82 | £8k | +8 | — | 2★ | 1★ | 188 / 85 | — |
| Z. Suzuki | Japonya | KL (GK) | Parma | 22 | £6.88M | 74 | 82 | £8k | +8 | — | 3★ | 1★ | 190 / 91 | — |
| P. Loretz | İsviçre | KL (GK) | FC Luzern | 22 | £3.96M | 72 | 82 | £4k | +10 | — | 3★ | 1★ | 191 / 81 | — |
| R. Risser | Fransa | KL (GK) | RC Lens | 20 | £3.78M | 72 | 82 | £6k | +10 | — | 3★ | 1★ | 193 / 82 | — |
| Kauã Santos | Brezilya | KL (GK) | Eintracht Frankfurt | 22 | £3.10M | 71 | 82 | £8k | +11 | — | 1★ | 1★ | 196 / 84 | — |
| J. Beadle | İngiltere | KL (GK) | Birmingham City | 20 | £2.92M | 70 | 82 | £13k | +12 | — | 3★ | 1★ | 201 / 85 | High Growth |
| E. Jaouen | Fransa | KL (GK) | Stade de Reims | 19 | £2.15M | 68 | 82 | £1k | +14 | — | 2★ | 1★ | 197 / 82 | High Growth |
| T. Pereira Cardoso | Luxembourg | KL (GK) | Borussia Mönchengladbach | 19 | £1.81M | 67 | 82 | £3k | +15 | — | 3★ | 1★ | 190 / 87 | High Growth |
| L. Brughmans | Belçika | KL (GK) | KRC Genk | 17 | £538k | 59 | 82 | £0k | +23 | — | 3★ | 1★ | 197 / 85 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Kaleciler (GK / KL))

- **L. Brughmans** (KRC Genk) — OVR 59, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **D. Seimen** (SC Paderborn 07) — OVR 66, POT 84: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **T. Pereira Cardoso** (Borussia Mönchengladbach) — OVR 67, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **E. Jaouen** (Stade de Reims) — OVR 68, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **J. Beadle** (Birmingham City) — OVR 70, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **R. Owusu-Oduro** (AZ Alkmaar) — OVR 71, POT 84: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 2. Stoperler (CB / D(M))

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W. Pacho | Ekvador | D(M) (CB) | Paris Saint-Germain | 23 | £71.4M | 86 | 89 | £95k | +3 | — | 3★ | 2★ | 188 / 81 | — |
| P. Hincapié | Ekvador | D(M) (CB, LB, LM) | Arsenal | 23 | £44.7M | 83 | 89 | £70k | +6 | — | 2★ | 3★ | 184 / 77 | — |
| D. Huijsen | İspanya | D(M) (CB) | Real Madrid | 20 | £48.2M | 82 | 89 | £108k | +7 | Aerial threat | 5★ | 2★ | 197 / 87 | — |
| J. Hato | Hollanda | D(M) (LB, CB) | Chelsea | 19 | £24.9M | 78 | 89 | £56k | +11 | — | 3★ | 2★ | 182 / 76 | — |
| J. Mokio | Belçika | D(M) (CDM, CM, LB, CB) | Ajax | 17 | £3.27M | 70 | 89 | £4k | +19 | — | 3★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| Pau Cubarsí | İspanya | D(M) (CB) | FC Barcelona | 18 | £34.8M | 82 | 88 | £55k | +6 | — | 4★ | 2★ | 184 / 69 | — |
| C. Lukeba | Fransa | D(M) (CB, LB) | RB Leipzig | 22 | £38.3M | 80 | 88 | £41k | +8 | — | 2★ | 2★ | 183 / 84 | — |
| J. Gvardiol | Hırvatistan | D(M) (LB, CB, LM) | Manchester City | 23 | £46.0M | 84 | 87 | £112k | +3 | — | 5★ | 3★ | 185 / 80 | — |
| Murillo | Brezilya | D(M) (CB) | Nottingham Forest | 22 | £40.9M | 83 | 87 | £86k | +4 | Strength | 3★ | 2★ | 180 / 75 | — |
| O. Diomande | Côte d'Ivoire | D(M) (CB) | Sporting CP | 21 | £34.4M | 80 | 87 | £15k | +7 | Strength | 3★ | 2★ | 190 / 93 | — |
| E. Bitshiabu | Fransa | D(M) (CB) | RB Leipzig | 20 | £10.8M | 75 | 87 | £25k | +12 | Aerial threat, Strength | 3★ | 2★ | 196 / 95 | High Growth |
| F. Jeltsch | Almanya | D(M) (CB) | VfB Stuttgart | 18 | £4.30M | 72 | 87 | £13k | +15 | — | 4★ | 2★ | 187 / 86 | Hidden Gem, Ucuz Cevher, High Growth |
| L. Vušković | Hırvatistan | D(M) (CB) | Hamburger SV | 18 | £4.30M | 72 | 87 | £29k | +15 | — | 3★ | 2★ | 193 / 86 | Hidden Gem, Ucuz Cevher, High Growth |
| Gonçalo Inácio | Portekiz | D(M) (CB) | Sporting CP | 23 | £30.1M | 81 | 86 | £19k | +5 | — | 2★ | 2★ | 185 / 81 | — |
| António Silva | Portekiz | D(M) (CB) | SL Benfica | 21 | £25.4M | 78 | 86 | £13k | +8 | — | 2★ | 2★ | 187 / 82 | — |
| L. Yoro | Fransa | D(M) (CB) | Manchester United | 19 | £24.5M | 78 | 86 | £42k | +8 | — | 3★ | 2★ | 190 / 75 | — |
| Tomás Araújo | Portekiz | D(M) (CB, RB, RM) | SL Benfica | 23 | £24.9M | 78 | 86 | £15k | +8 | — | 2★ | 3★ | 187 / 81 | — |
| Z. Debast | Belçika | D(M) (CDM, CB, CM) | Sporting CP | 21 | £25.8M | 78 | 86 | £13k | +8 | — | 4★ | 3★ | 191 / 76 | — |
| Asencio | İspanya | D(M) (CB, RB, RM) | Real Madrid | 22 | £18.9M | 77 | 86 | £90k | +9 | — | 3★ | 2★ | 184 / 79 | — |
| G. Scalvini | İtalya | D(M) (CB) | Atalanta | 21 | £18.9M | 77 | 86 | £34k | +9 | — | 3★ | 2★ | 194 / 75 | — |
| K. Koulierakis | Yunanistan | D(M) (CB) | VfL Wolfsburg | 21 | £18.9M | 77 | 86 | £26k | +9 | — | 2★ | 2★ | 185 / 78 | — |
| M. Smets | Belçika | D(M) (CB) | KRC Genk | 21 | £13.3M | 76 | 86 | £15k | +10 | — | 3★ | 2★ | 184 / 76 | — |
| A. Gray | İngiltere | D(M) (CDM, CB, RB, RM) | Tottenham Hotspur | 19 | £9.89M | 75 | 86 | £41k | +11 | — | 4★ | 2★ | 187 / 70 | — |
| J. Ordoñez | Ekvador | D(M) (CB) | Club Brugge KV | 21 | £10.3M | 75 | 86 | £16k | +11 | — | 3★ | 2★ | 188 / 80 | — |
| P. Comuzzo | İtalya | D(M) (CB) | Fiorentina | 20 | £8.17M | 74 | 86 | £22k | +12 | — | 2★ | 2★ | 183 / 75 | High Growth |
| J. Branthwaite | İngiltere | D(M) (CB) | Everton | 23 | £21.5M | 79 | 85 | £34k | +6 | Aerial threat | 5★ | 2★ | 195 / 74 | — |
| F. Boyomo | Kamerun | D(M) (CB, RB) | CA Osasuna | 23 | £22.4M | 78 | 85 | £25k | +7 | — | 2★ | 2★ | 181 / 86 | — |
| A. Khusanov | Uzbekistan | D(M) (CB) | Manchester City | 21 | £18.9M | 77 | 85 | £56k | +8 | — | 3★ | 2★ | 186 / 84 | — |
| C. Matsima | Fransa | D(M) (CB) | FC Augsburg | 23 | £18.9M | 77 | 85 | £24k | +8 | — | 3★ | 2★ | 193 / 80 | — |
| Mosquera | İspanya | D(M) (CB) | Arsenal | 21 | £18.9M | 77 | 85 | £59k | +8 | — | 3★ | 2★ | 188 / 79 | — |
| W. Goes | Hollanda | D(M) (CB) | AZ Alkmaar | 21 | £18.9M | 77 | 85 | £13k | +8 | — | 3★ | 2★ | 188 / 73 | — |
| Dário Essugo | Portekiz | D(M) (CDM, CM, CB) | Chelsea | 20 | £9.89M | 75 | 85 | £50k | +10 | — | 3★ | 2★ | 178 / 79 | — |
| L. Querfeld | Avusturya | D(M) (CB) | 1. FC Union Berlin | 21 | £10.3M | 75 | 85 | £18k | +10 | — | 3★ | 2★ | 190 / 83 | — |
| S. Mouriño | Uruguay | D(M) (CB, RB, RM) | Villarreal CF | 23 | £7.31M | 74 | 85 | £22k | +11 | — | 3★ | 2★ | 183 / 76 | — |
| Yarek | İspanya | D(M) (CB, LB) | PSV | 20 | £6.02M | 73 | 85 | £10k | +12 | — | 3★ | 2★ | 192 / 75 | High Growth |
| L. Miller | Scotland | D(M) (CM, CDM, CAM, CB) | Udinese | 18 | £3.70M | 71 | 85 | £7k | +14 | — | 4★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Acheampong | İngiltere | D(M) (RB, CB, CDM, RM) | Chelsea | 19 | £3.10M | 70 | 85 | £28k | +15 | — | 3★ | 2★ | 190 / 85 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Simić | Sırbistan | D(M) (CB) | Al Ittihad | 20 | £3.10M | 70 | 85 | £10k | +15 | — | 3★ | 2★ | 186 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| Pau Navarro | İspanya | D(M) (CB, RB, CM) | Villarreal CF | 20 | £3.10M | 70 | 85 | £12k | +15 | — | 3★ | 2★ | 185 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| T. Ramírez | Arjantin | D(M) (CB) | Argentinos Juniors | 18 | £2.84M | 69 | 85 | £4k | +16 | — | 3★ | 2★ | 185 / 78 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Gadou | Fransa | D(M) (CB) | FC Red Bull Salzburg | 18 | £1.72M | 66 | 85 | £3k | +19 | — | 2★ | 2★ | 195 / 78 | Hidden Gem, Ucuz Cevher, High Growth |
| L. Colwill | İngiltere | D(M) (CB) | Chelsea | 22 | £23.6M | 80 | 84 | £82k | +4 | — | 3★ | 2★ | 187 / 83 | — |
| Arnau Martínez | İspanya | D(M) (RB, RM, CB, RW) | Girona FC | 22 | £21.5M | 79 | 84 | £26k | +5 | — | 3★ | 2★ | 182 / 72 | — |
| I. Zabarnyi | Ukrayna | D(M) (CB) | Paris Saint-Germain | 22 | £21.1M | 79 | 84 | £56k | +5 | — | 3★ | 2★ | 189 / 80 | — |
| Lucas Beraldo | Brezilya | D(M) (CB, LB, LM) | Paris Saint-Germain | 21 | £17.6M | 78 | 84 | £42k | +6 | — | 2★ | 2★ | 182 / 78 | — |
| M. Thiaw | Almanya | D(M) (CB) | Newcastle United | 23 | £17.2M | 78 | 84 | £71k | +6 | Aerial threat | 4★ | 2★ | 194 / 89 | — |
| R. Calafiori | İtalya | D(M) (LB, CB) | Arsenal | 23 | £18.1M | 78 | 84 | £75k | +6 | — | 4★ | 3★ | 188 / 86 | — |
| Eduardo Quaresma | Portekiz | D(M) (CB, RB, RM) | Sporting CP | 23 | £16.8M | 77 | 84 | £14k | +7 | — | 3★ | 3★ | 184 / 79 | — |
| M. Sarr | Fransa | D(M) (CB) | RC Strasbourg Alsace | 19 | £12.9M | 76 | 84 | £49k | +8 | Aerial threat | 3★ | 2★ | 194 / 77 | — |
| Renato Veiga | Portekiz | D(M) (CB, CDM) | Villarreal CF | 21 | £13.3M | 76 | 84 | £21k | +8 | — | 3★ | 2★ | 190 / 88 | — |
| V. Gómez | Arjantin | D(M) (CB, LB) | Real Betis Balompié | 22 | £13.3M | 76 | 84 | £19k | +8 | — | 2★ | 2★ | 181 / 75 | — |
| C. Mawissa | Fransa | D(M) (CB, LB, LM) | AS Monaco | 20 | £9.89M | 75 | 84 | £16k | +9 | — | 5★ | 2★ | 184 / 77 | — |
| J. Jacquet | Fransa | D(M) (CB) | Stade Rennais FC | 19 | £9.89M | 75 | 84 | £14k | +9 | — | 2★ | 2★ | 188 / 77 | — |
| K. De Winter | Belçika | D(M) (CB) | AC Milan | 23 | £7.31M | 74 | 84 | £25k | +10 | — | 3★ | 2★ | 191 / 75 | — |
| N. Collins | Almanya | D(M) (CB, RB, RM) | Eintracht Frankfurt | 21 | £7.74M | 74 | 84 | £15k | +10 | — | 3★ | 2★ | 191 / 84 | — |
| Z. Van Den Bosch | Belçika | D(M) (CB) | Royal Antwerp FC | 21 | £7.74M | 74 | 84 | £13k | +10 | — | 4★ | 2★ | 191 / 78 | — |
| E. Bayram | Türkiye | D(M) (CB) | KVC Westerlo | 22 | £5.59M | 73 | 84 | £8k | +11 | — | 2★ | 2★ | 192 / 78 | Türk Yeteneği |
| A. Kozubal | Polonya | D(M) (CM, CDM, CB) | Lech Poznań | 20 | £3.87M | 71 | 84 | £5k | +13 | — | 3★ | 2★ | 176 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| V. Milosavljević | Sırbistan | D(M) (CB) | AFC Bournemouth | 18 | £3.01M | 70 | 84 | £18k | +14 | — | 2★ | 2★ | 192 / 87 | Hidden Gem, Ucuz Cevher, High Growth |
| Vitor Reis | Brezilya | D(M) (CB) | Girona FC | 19 | £3.01M | 70 | 84 | £28k | +14 | — | 3★ | 2★ | 186 / 77 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Heaven | İngiltere | D(M) (CB, LB) | Manchester United | 18 | £2.58M | 69 | 84 | £18k | +15 | — | 3★ | 2★ | 189 / 84 | Hidden Gem, Ucuz Cevher, High Growth |
| Jon Martín | İspanya | D(M) (CB) | Real Sociedad | 19 | £2.49M | 68 | 84 | £9k | +16 | — | 3★ | 2★ | 185 / 83 | Hidden Gem, Ucuz Cevher, High Growth |
| O. El Hilali | Fas | D(M) (RB, CB, RM) | RCD Espanyol | 21 | £13.8M | 77 | 83 | £14k | +6 | — | 3★ | 3★ | 183 / 75 | — |
| R. Flamingo | Hollanda | D(M) (CB) | PSV | 22 | £13.3M | 77 | 83 | £16k | +6 | — | 4★ | 3★ | 185 / 73 | — |
| S. van den Berg | Hollanda | D(M) (CB, RB) | Brentford | 23 | £12.9M | 77 | 83 | £46k | +6 | — | 3★ | 2★ | 192 / 87 | — |
| J. Quansah | İngiltere | D(M) (CB) | Bayer 04 Leverkusen | 22 | £10.3M | 75 | 83 | £40k | +8 | — | 3★ | 2★ | 190 / 80 | — |
| Kike Salas | İspanya | D(M) (CB, LB) | Sevilla FC | 23 | £9.89M | 75 | 83 | £20k | +8 | — | 3★ | 2★ | 186 / 80 | — |
| L. Agoumé | Fransa | D(M) (CDM, CM, CB) | Sevilla FC | 23 | £10.3M | 75 | 83 | £20k | +8 | — | 3★ | 3★ | 188 / 72 | — |
| L. Pirola | İtalya | D(M) (CB, LB) | Olympiacos FC | 23 | £9.89M | 75 | 83 | £20k | +8 | — | 3★ | 2★ | 185 / 79 | — |
| V. Brazhko | Ukrayna | D(M) (CDM, CM, CB) | Dynamo Kyiv | 23 | £10.3M | 75 | 83 | £15k | +8 | — | 3★ | 2★ | 184 / 77 | — |
| Y. Baas | Hollanda | D(M) (CB, LB) | Ajax | 22 | £10.3M | 75 | 83 | £12k | +8 | — | 2★ | 2★ | 182 / 71 | — |
| M. Rosenfelder | Almanya | D(M) (CB, RB, RM) | SC Freiburg | 22 | £7.74M | 74 | 83 | £17k | +9 | — | 3★ | 3★ | 186 / 76 | — |
| J. Orozco Chiquete | Meksika | D(M) (CB) | Serbest Oyuncu | 23 | — | 73 | 83 | — | +10 | — | 3★ | 2★ | 189 / 76 | Serbest Oyuncu |
| Stefan Bajcetic | İspanya | D(M) (CDM, CM, CB) | Liverpool | 20 | £5.59M | 73 | 83 | £36k | +10 | — | 3★ | 3★ | 185 / 77 | — |
| A. Bah | Sierra Leone | D(M) (CB) | OGC Nice | 19 | £4.04M | 72 | 83 | £35k | +11 | — | 2★ | 2★ | 195 / 82 | Ucuz Cevher |
| W. Kambwala | Fransa | D(M) (CB) | Villarreal CF | 20 | £4.13M | 72 | 83 | £15k | +11 | — | 3★ | 2★ | 192 / 85 | Ucuz Cevher |
| T. Mykhavko | Ukrayna | D(M) (CB) | Dynamo Kyiv | 20 | £3.10M | 70 | 83 | £8k | +13 | — | 3★ | 2★ | 187 / 78 | Ucuz Cevher, High Growth |
| J. Spileers | Belçika | D(M) (CB, RB) | Club Brugge KV | 20 | £2.75M | 69 | 83 | £9k | +14 | — | 3★ | 2★ | 188 / 79 | Ucuz Cevher, High Growth |
| M. Young | Hollanda | D(M) (CB, RB, RM) | Sparta Rotterdam | 19 | £2.67M | 69 | 83 | £3k | +14 | — | 3★ | 2★ | 182 / 78 | Ucuz Cevher, High Growth |
| Y. Özcan | Türkiye | D(M) (CB, LB, LM) | RSC Anderlecht | 19 | £2.67M | 69 | 83 | £23k | +14 | — | 2★ | 2★ | 185 / 75 | Türk Yeteneği, Ucuz Cevher, High Growth |
| A. Faye | Senegal | D(M) (CB) | FC Lorient | 20 | £2.32M | 68 | 83 | £16k | +15 | — | 3★ | 2★ | 191 / 70 | Ucuz Cevher, High Growth |
| B. Kovačević | Sırbistan | D(M) (CB) | Cádiz CF | 21 | £2.41M | 68 | 83 | £3k | +15 | — | 3★ | 2★ | 194 / 78 | Ucuz Cevher, High Growth |
| T. Tati | Fransa | D(M) (CB) | FC Nantes | 17 | £2.06M | 67 | 83 | £3k | +16 | — | 2★ | 2★ | 190 / 79 | Ucuz Cevher, High Growth |
| A. Bouwman | Hollanda | D(M) (CB) | Ajax | 17 | £1.46M | 65 | 83 | £2k | +18 | — | 3★ | 2★ | 188 / 71 | Ucuz Cevher, High Growth |
| D. Odogu | Almanya | D(M) (CB) | AC Milan | 19 | £1.46M | 65 | 83 | £7k | +18 | — | 3★ | 2★ | 191 / 83 | Ucuz Cevher, High Growth |
| C. Donovan | Scotland | D(M) (RB, CB, RM) | Celtic | 18 | £1.20M | 64 | 83 | £7k | +19 | — | 3★ | 3★ | 180 / 76 | Ucuz Cevher, High Growth |
| G. Doué | Côte d'Ivoire | D(M) (RB, CB, RM) | RC Strasbourg Alsace | 22 | £12.9M | 77 | 82 | £34k | +5 | — | 3★ | 3★ | 187 / 84 | — |
| I. Doukouré | Fransa | D(M) (CB, CDM, CM) | RC Strasbourg Alsace | 21 | £9.46M | 76 | 82 | £28k | +6 | — | 3★ | 2★ | 183 / 83 | — |
| Javi Rodríguez | İspanya | D(M) (RB, CB) | RC Celta | 22 | £9.89M | 76 | 82 | £19k | +6 | — | 3★ | 3★ | 178 / 70 | — |
| M. Estève | Fransa | D(M) (CB) | Burnley | 23 | £9.46M | 76 | 82 | £36k | +6 | — | 3★ | 2★ | 193 / 87 | — |
| C. Egan-Riley | İngiltere | D(M) (CB) | Olympique de Marseille | 22 | £9.03M | 75 | 82 | £24k | +7 | — | 3★ | 2★ | 183 / 74 | — |
| César Tárrega | İspanya | D(M) (CB) | Valencia CF | 23 | £9.03M | 75 | 82 | £23k | +7 | — | 3★ | 2★ | 193 / 78 | — |
| Francés | İspanya | D(M) (CB, RB, LB, RM) | Girona FC | 22 | £9.03M | 75 | 82 | £20k | +7 | — | 4★ | 2★ | 181 / 70 | — |
| Alexandre Penetra | Portekiz | D(M) (CB, RB) | AZ Alkmaar | 23 | £7.31M | 74 | 82 | £12k | +8 | — | 2★ | 2★ | 186 / 79 | — |
| Gerard Martín | İspanya | D(M) (LB, CB, LM) | FC Barcelona | 23 | £7.74M | 74 | 82 | £42k | +8 | — | 3★ | 3★ | 186 / 76 | — |
| M. Di Cesare | Arjantin | D(M) (CB) | Racing Club | 23 | £7.31M | 74 | 82 | £12k | +8 | Strength | 2★ | 2★ | 186 / 86 | — |
| B. Humphreys | İngiltere | D(M) (LB, CB, RB) | Burnley | 22 | £5.59M | 73 | 82 | £29k | +9 | — | 5★ | 2★ | 187 / 79 | — |
| D. Tıknaz | Türkiye | D(M) (CDM, CM, CB) | Beşiktaş JK | 20 | £4.13M | 72 | 82 | £15k | +10 | — | 3★ | 2★ | 193 / 76 | Türk Yeteneği |
| A. Nagalo | Burkina Faso | D(M) (CB) | PSV | 22 | £3.35M | 71 | 82 | £9k | +11 | — | 3★ | 2★ | 185 / 75 | — |
| A. Anselmino | Arjantin | D(M) (CB) | Borussia Dortmund | 20 | £3.10M | 70 | 82 | £30k | +12 | — | 4★ | 2★ | 186 / 83 | High Growth |
| J. Adjetey | Gana | D(M) (CB) | FC Basel 1893 | 21 | £3.18M | 70 | 82 | £8k | +12 | — | 4★ | 2★ | 188 / 82 | High Growth |
| J. Belocian | Fransa | D(M) (CB, LB, LM) | Bayer 04 Leverkusen | 20 | £3.10M | 70 | 82 | £21k | +12 | — | 3★ | 2★ | 182 / 73 | High Growth |
| J. Canvot | Fransa | D(M) (CB, CDM, CM) | Crystal Palace | 18 | £3.01M | 70 | 82 | £21k | +12 | — | 3★ | 2★ | 188 / 79 | High Growth |
| G. Leoni | İtalya | D(M) (CB) | Liverpool | 18 | £2.58M | 69 | 82 | £21k | +13 | — | 4★ | 2★ | 196 / 84 | High Growth |
| L. Høgsberg | Danimarka | D(M) (CB, RB, LB, RM) | RC Strasbourg Alsace | 19 | £2.67M | 69 | 82 | £13k | +13 | — | 3★ | 2★ | 187 / 70 | High Growth |
| T. Bindon | New Zealand | D(M) (CB, RB) | Sheffield United | 20 | £2.75M | 69 | 82 | £22k | +13 | — | 3★ | 2★ | 190 / 76 | High Growth |
| T. Slotsager | Danimarka | D(M) (CB) | Hellas Verona FC | 19 | £2.67M | 69 | 82 | £4k | +13 | — | 3★ | 2★ | 189 / 79 | High Growth |
| A. Kalogeropoulos | Yunanistan | D(M) (CB) | Olympiacos FC | 20 | £2.32M | 68 | 82 | £9k | +14 | — | 3★ | 2★ | 187 / 80 | High Growth |
| M. Faye | Senegal | D(M) (CB) | Cremonese | 20 | £2.32M | 68 | 82 | £7k | +14 | — | 3★ | 2★ | 186 / 81 | High Growth |
| C. Yirenkyi | Gana | D(M) (CM, CDM, CB) | FC Nordsjælland | 19 | £2.06M | 67 | 82 | £4k | +15 | — | 3★ | 2★ | 181 / 73 | High Growth |
| K. Corbanie | Belçika | D(M) (RB, CDM, CB, CM) | Royal Antwerp FC | 20 | £1.98M | 67 | 82 | £6k | +15 | — | 2★ | 2★ | 187 / 75 | High Growth |
| A. Kinteh | Gambia | D(M) (CB) | Tromsø IL | 18 | £1.46M | 65 | 82 | £1k | +17 | — | 3★ | 2★ | 186 / 75 | High Growth |
| A. Tape | Fransa | D(M) (CB) | Bayer 04 Leverkusen | 17 | £1.46M | 65 | 82 | £7k | +17 | — | 3★ | 2★ | 180 / 79 | High Growth |
| M. Courcoul | Fransa | D(M) (CDM, CM, CB) | Angers SCO | 18 | £1.46M | 65 | 82 | £3k | +17 | — | 3★ | 2★ | 182 / 70 | High Growth |
| Y. Saidu | Gana | D(M) (CM, CB, CDM) | Real Zaragoza | 20 | £1.63M | 65 | 82 | £2k | +17 | — | 4★ | 2★ | 184 / 73 | High Growth |
| K. Potulski | Polonya | D(M) (CB) | 1. FSV Mainz 05 | 17 | £860k | 62 | 82 | £3k | +20 | — | 3★ | 2★ | 195 / 85 | High Growth |
| M. Palma | Almanya | D(M) (CB) | Udinese | 17 | £860k | 62 | 82 | £2k | +20 | — | 3★ | 2★ | 194 / 85 | High Growth |
| L. Jakirović | Hırvatistan | D(M) (CB, LB) | Dinamo Zagreb | 17 | £838k | 61 | 82 | £2k | +21 | — | 3★ | 2★ | 190 / 76 | High Growth |
| A. Natali | İtalya | D(M) (CB) | AZ Alkmaar | 17 | £624k | 60 | 82 | £4k | +22 | — | 3★ | 2★ | 186 / 77 | High Growth |
| B. Manguelle | Belçika | D(M) (CB) | KRC Genk | 17 | £624k | 60 | 82 | £2k | +22 | — | 3★ | 2★ | 185 / 74 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Stoperler (CB / D(M)))

- **Y. Özcan** (RSC Anderlecht) — OVR 69, POT 83: Türk kadrosu için doğal hedef; düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **D. Tıknaz** (Beşiktaş JK) — OVR 72, POT 82: Türk kadrosu için doğal hedef; düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **E. Bayram** (KVC Westerlo) — OVR 73, POT 84: Türk kadrosu için doğal hedef; düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **A. Natali** (AZ Alkmaar) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **B. Manguelle** (KRC Genk) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **L. Jakirović** (Dinamo Zagreb) — OVR 61, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 3. Sol Bekler (LB / D(Sol))

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E. Camavinga | Fransa | D(Sol) (CM, CDM, LB) | Real Madrid | 22 | £63.2M | 83 | 90 | £150k | +7 | — | 3★ | 4★ | 185 / 77 | — |
| Nuno Mendes | Portekiz | D(Sol) (LB, LM) | Paris Saint-Germain | 23 | £74.0M | 86 | 89 | £95k | +3 | Speedster, Acrobat | 4★ | 3★ | 180 / 70 | — |
| P. Hincapié | Ekvador | D(Sol) (CB, LB, LM) | Arsenal | 23 | £44.7M | 83 | 89 | £70k | +6 | — | 2★ | 3★ | 184 / 77 | — |
| J. Hato | Hollanda | D(Sol) (LB, CB) | Chelsea | 19 | £24.9M | 78 | 89 | £56k | +11 | — | 3★ | 2★ | 182 / 76 | — |
| J. Mokio | Belçika | D(Sol) (CDM, CM, LB, CB) | Ajax | 17 | £3.27M | 70 | 89 | £4k | +19 | — | 3★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| C. Lukeba | Fransa | D(Sol) (CB, LB) | RB Leipzig | 22 | £38.3M | 80 | 88 | £41k | +8 | — | 2★ | 2★ | 183 / 84 | — |
| Álvaro Carreras | İspanya | D(Sol) (LB, LM) | Real Madrid | 22 | £38.7M | 80 | 88 | £112k | +8 | — | 4★ | 3★ | 186 / 78 | — |
| J. Gvardiol | Hırvatistan | D(Sol) (LB, CB, LM) | Manchester City | 23 | £46.0M | 84 | 87 | £112k | +3 | — | 5★ | 3★ | 185 / 80 | — |
| Balde | İspanya | D(Sol) (LB, LM) | FC Barcelona | 21 | £42.6M | 83 | 87 | £69k | +4 | Speedster | 4★ | 3★ | 175 / 69 | — |
| M. Lewis-Skelly | İngiltere | D(Sol) (LB, CM) | Arsenal | 18 | £24.1M | 78 | 87 | £55k | +9 | — | 3★ | 3★ | 178 / 72 | — |
| M. Kerkez | Macaristan | D(Sol) (LB, LM) | Liverpool | 21 | £35.7M | 82 | 86 | £70k | +4 | — | 3★ | 3★ | 180 / 71 | — |
| L. Hall | İngiltere | D(Sol) (LB) | Newcastle United | 20 | £26.2M | 80 | 86 | £70k | +6 | — | 3★ | 2★ | 179 / 71 | — |
| T. Livramento | İngiltere | D(Sol) (RB, LB, RM) | Newcastle United | 22 | £27.1M | 80 | 86 | £82k | +6 | — | 4★ | 3★ | 181 / 71 | — |
| J. Seys | Belçika | D(Sol) (RB, LB, RM) | Club Brugge KV | 20 | £6.02M | 73 | 86 | £14k | +13 | — | 4★ | 2★ | 178 / 63 | High Growth |
| João Costa | Brezilya | D(Sol) (RM, LM, LB, RB) | Al Ettifaq | 20 | £3.87M | 71 | 86 | £12k | +15 | — | 3★ | 3★ | 178 / 69 | Hidden Gem, Ucuz Cevher, High Growth |
| Miguel Gutiérrez | İspanya | D(Sol) (LB, LM) | Napoli | 23 | £29.7M | 81 | 85 | £72k | +4 | — | 3★ | 2★ | 180 / 73 | — |
| N. Brown | Almanya | D(Sol) (LB, LM) | Eintracht Frankfurt | 22 | £19.4M | 77 | 85 | £22k | +8 | — | 3★ | 4★ | 180 / 64 | — |
| Yarek | İspanya | D(Sol) (CB, LB) | PSV | 20 | £6.02M | 73 | 85 | £10k | +12 | — | 3★ | 2★ | 192 / 75 | High Growth |
| D. León | Paraguay | D(Sol) (LB, LM) | Manchester United | 18 | £1.55M | 64 | 85 | £9k | +21 | — | 2★ | 2★ | 177 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| D. Udogie | İtalya | D(Sol) (LB) | Tottenham Hotspur | 22 | £24.5M | 80 | 84 | £72k | +4 | — | 3★ | 3★ | 186 / 73 | — |
| I. Maatsen | Hollanda | D(Sol) (LB, LM) | Aston Villa | 23 | £21.1M | 79 | 84 | £73k | +5 | — | 2★ | 3★ | 178 / 68 | — |
| Lucas Beraldo | Brezilya | D(Sol) (CB, LB, LM) | Paris Saint-Germain | 21 | £17.6M | 78 | 84 | £42k | +6 | — | 2★ | 2★ | 182 / 78 | — |
| R. Calafiori | İtalya | D(Sol) (LB, CB) | Arsenal | 23 | £18.1M | 78 | 84 | £75k | +6 | — | 4★ | 3★ | 188 / 86 | — |
| R. Lewis | İngiltere | D(Sol) (RB, LB, CM) | Manchester City | 20 | £17.2M | 77 | 84 | £56k | +7 | — | 3★ | 3★ | 170 / 64 | — |
| V. Gómez | Arjantin | D(Sol) (CB, LB) | Real Betis Balompié | 22 | £13.3M | 76 | 84 | £19k | +8 | — | 2★ | 2★ | 181 / 75 | — |
| C. Mawissa | Fransa | D(Sol) (CB, LB, LM) | AS Monaco | 20 | £9.89M | 75 | 84 | £16k | +9 | — | 5★ | 2★ | 184 / 77 | — |
| P. Dorgu | Danimarka | D(Sol) (LB, LM) | Manchester United | 20 | £7.74M | 74 | 84 | £35k | +10 | — | 2★ | 2★ | 185 / 70 | — |
| K. Sabbe | Belçika | D(Sol) (RB, LB, RM) | Club Brugge KV | 20 | £3.70M | 71 | 84 | £11k | +13 | — | 3★ | 2★ | 172 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| Y. Medina | Ekvador | D(Sol) (LB, LW, LM) | KRC Genk | 20 | £3.18M | 70 | 84 | £9k | +14 | Speedster | 2★ | 3★ | 175 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Heaven | İngiltere | D(Sol) (CB, LB) | Manchester United | 18 | £2.58M | 69 | 84 | £18k | +15 | — | 3★ | 2★ | 189 / 84 | Hidden Gem, Ucuz Cevher, High Growth |
| Diego Moreira | Belçika | D(Sol) (LM, LB, RM) | RC Strasbourg Alsace | 20 | £14.2M | 77 | 83 | £31k | +6 | — | 3★ | 4★ | 179 / 73 | — |
| Q. Hartman | Hollanda | D(Sol) (LB, LM) | Burnley | 23 | £13.3M | 77 | 83 | £39k | +6 | — | 3★ | 3★ | 183 / 77 | — |
| J. Hinshelwood | İngiltere | D(Sol) (CDM, RB, LB, RM) | Brighton & Hove Albion | 20 | £9.89M | 75 | 83 | £40k | +8 | — | 4★ | 3★ | 181 / 76 | — |
| Kike Salas | İspanya | D(Sol) (CB, LB) | Sevilla FC | 23 | £9.89M | 75 | 83 | £20k | +8 | — | 3★ | 2★ | 186 / 80 | — |
| L. Pirola | İtalya | D(Sol) (CB, LB) | Olympiacos FC | 23 | £9.89M | 75 | 83 | £20k | +8 | — | 3★ | 2★ | 185 / 79 | — |
| M. Ruggeri | İtalya | D(Sol) (LM, LB) | Atlético Madrid | 22 | £10.8M | 75 | 83 | £36k | +8 | — | 3★ | 3★ | 187 / 69 | — |
| V. Barco | Arjantin | D(Sol) (LB, LM, CM) | RC Strasbourg Alsace | 20 | £10.3M | 75 | 83 | £26k | +8 | — | 3★ | 3★ | 170 / 66 | — |
| Y. Baas | Hollanda | D(Sol) (CB, LB) | Ajax | 22 | £10.3M | 75 | 83 | £12k | +8 | — | 2★ | 2★ | 182 / 71 | — |
| N. O'Reilly | İngiltere | D(Sol) (LB, CM, CAM) | Manchester City | 20 | £5.59M | 73 | 83 | £41k | +10 | — | 2★ | 3★ | 193 / 77 | — |
| Y. Özcan | Türkiye | D(Sol) (CB, LB, LM) | RSC Anderlecht | 19 | £2.67M | 69 | 83 | £23k | +14 | — | 2★ | 2★ | 185 / 75 | Türk Yeteneği, Ucuz Cevher, High Growth |
| H. Amass | İngiltere | D(Sol) (LB, LM) | Sheffield Wednesday | 18 | £2.32M | 68 | 83 | £16k | +15 | — | 3★ | 2★ | 178 / 75 | Ucuz Cevher, High Growth |
| D. Svensson | İsveç | D(Sol) (LB, CM, LM) | Borussia Dortmund | 23 | £12.9M | 77 | 82 | £29k | +5 | — | 4★ | 2★ | 178 / 72 | — |
| Q. Merlin | Fransa | D(Sol) (LB, LM) | Stade Rennais FC | 23 | £9.46M | 76 | 82 | £18k | +6 | — | 2★ | 3★ | 174 / 68 | — |
| E. Diouf | Senegal | D(Sol) (LB, LM) | West Ham United | 20 | £9.03M | 75 | 82 | £32k | +7 | — | 2★ | 3★ | 183 / 75 | — |
| Francés | İspanya | D(Sol) (CB, RB, LB, RM) | Girona FC | 22 | £9.03M | 75 | 82 | £20k | +7 | — | 4★ | 2★ | 181 / 70 | — |
| Fresneda | İspanya | D(Sol) (RB, RM, LB) | Sporting CP | 20 | £7.74M | 74 | 82 | £9k | +8 | — | 4★ | 3★ | 181 / 79 | — |
| Gerard Martín | İspanya | D(Sol) (LB, CB, LM) | FC Barcelona | 23 | £7.74M | 74 | 82 | £42k | +8 | — | 3★ | 3★ | 186 / 76 | — |
| L. Ullrich | Almanya | D(Sol) (LB, LM) | Borussia Mönchengladbach | 21 | £7.74M | 74 | 82 | £15k | +8 | — | 2★ | 2★ | 180 / 73 | — |
| S. Iling-Junior | İngiltere | D(Sol) (LM, LB, LW) | West Bromwich Albion | 21 | £8.17M | 74 | 82 | £46k | +8 | — | 4★ | 3★ | 182 / 75 | — |
| A. Boiro | Senegal | D(Sol) (LB, LM) | Athletic Club | 23 | £5.59M | 73 | 82 | £21k | +9 | — | 3★ | 3★ | 183 / 76 | — |
| B. Humphreys | İngiltere | D(Sol) (LB, CB, RB) | Burnley | 22 | £5.59M | 73 | 82 | £29k | +9 | — | 5★ | 2★ | 187 / 79 | — |
| K. Paredes | ABD | D(Sol) (LW, LM, LB) | VfL Wolfsburg | 22 | £6.02M | 73 | 82 | £26k | +9 | — | 3★ | 4★ | 175 / 61 | — |
| S. Dahl | İsveç | D(Sol) (LB, LM) | SL Benfica | 22 | £5.59M | 73 | 82 | £10k | +9 | — | 3★ | 3★ | 171 / 68 | — |
| Álex Valle | İspanya | D(Sol) (LB, LM) | Como | 21 | £4.30M | 72 | 82 | £30k | +10 | — | 3★ | 3★ | 183 / 57 | — |
| L. Mincarelli | Fransa | D(Sol) (LB, LM) | Montpellier HSC | 21 | £3.44M | 71 | 82 | £3k | +11 | — | 3★ | 2★ | 180 / 65 | — |
| M. Del Blanco | Arjantin | D(Sol) (LB, CM, LM) | Club Atlético Unión | 21 | £3.44M | 71 | 82 | £5k | +11 | — | 3★ | 3★ | 170 / 68 | — |
| J. Belocian | Fransa | D(Sol) (CB, LB, LM) | Bayer 04 Leverkusen | 20 | £3.10M | 70 | 82 | £21k | +12 | — | 3★ | 2★ | 182 / 73 | High Growth |
| L. Leroux | Fransa | D(Sol) (CM, LB, LM) | FC Nantes | 19 | £3.27M | 70 | 82 | £7k | +12 | — | 2★ | 3★ | 184 / 75 | High Growth |
| Š. Hrgović | Hırvatistan | D(Sol) (LB, RB, LM) | Hajduk Split | 21 | £3.27M | 70 | 82 | £9k | +12 | — | 3★ | 2★ | 173 / 69 | High Growth |
| L. Høgsberg | Danimarka | D(Sol) (CB, RB, LB, RM) | RC Strasbourg Alsace | 19 | £2.67M | 69 | 82 | £13k | +13 | — | 3★ | 2★ | 187 / 70 | High Growth |
| Héctor Fort | İspanya | D(Sol) (RB, LB, LM) | Elche CF | 18 | £2.32M | 68 | 82 | £16k | +14 | — | 3★ | 3★ | 185 / 78 | High Growth |
| A. Aznou | Fas | D(Sol) (LB) | Everton | 19 | £1.81M | 66 | 82 | £8k | +16 | — | 3★ | 3★ | 178 / 70 | High Growth |
| E. Dijkstra | Hollanda | D(Sol) (RB, LB, RM) | AZ Alkmaar | 18 | £1.20M | 64 | 82 | £3k | +18 | — | 4★ | 3★ | 173 / 67 | High Growth |
| A. Garcia | İngiltere | D(Sol) (LB, RW, LW, RM) | Reading FC | 17 | £946k | 63 | 82 | £0k | +19 | — | 2★ | 3★ | 180 / 67 | High Growth |
| L. Jetten | Hollanda | D(Sol) (LB, LM) | Ajax | 18 | £946k | 62 | 82 | £2k | +20 | — | 3★ | 2★ | 166 / 61 | High Growth |
| L. Jakirović | Hırvatistan | D(Sol) (CB, LB) | Dinamo Zagreb | 17 | £838k | 61 | 82 | £2k | +21 | — | 3★ | 2★ | 190 / 76 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Sol Bekler (LB / D(Sol)))

- **Y. Özcan** (RSC Anderlecht) — OVR 69, POT 83: Türk kadrosu için doğal hedef; düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **L. Jakirović** (Dinamo Zagreb) — OVR 61, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **L. Jetten** (Ajax) — OVR 62, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **D. León** (Manchester United) — OVR 64, POT 85: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **A. Garcia** (Reading FC) — OVR 63, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **E. Dijkstra** (AZ Alkmaar) — OVR 64, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 4. Sağ Bekler (RB / D(Sağ))

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G. Read | Hollanda | D(Sağ) (RB, RM) | Feyenoord | 19 | £11.2M | 75 | 88 | £9k | +13 | — | 3★ | 3★ | 183 / 70 | High Growth |
| T. Livramento | İngiltere | D(Sağ) (RB, LB, RM) | Newcastle United | 22 | £27.1M | 80 | 86 | £82k | +6 | — | 4★ | 3★ | 181 / 71 | — |
| Tomás Araújo | Portekiz | D(Sağ) (CB, RB, RM) | SL Benfica | 23 | £24.9M | 78 | 86 | £15k | +8 | — | 2★ | 3★ | 187 / 81 | — |
| Asencio | İspanya | D(Sağ) (CB, RB, RM) | Real Madrid | 22 | £18.9M | 77 | 86 | £90k | +9 | — | 3★ | 2★ | 184 / 79 | — |
| A. Gray | İngiltere | D(Sağ) (CDM, CB, RB, RM) | Tottenham Hotspur | 19 | £9.89M | 75 | 86 | £41k | +11 | — | 4★ | 2★ | 187 / 70 | — |
| J. Seys | Belçika | D(Sağ) (RB, LB, RM) | Club Brugge KV | 20 | £6.02M | 73 | 86 | £14k | +13 | — | 4★ | 2★ | 178 / 63 | High Growth |
| João Costa | Brezilya | D(Sağ) (RM, LM, LB, RB) | Al Ettifaq | 20 | £3.87M | 71 | 86 | £12k | +15 | — | 3★ | 3★ | 178 / 69 | Hidden Gem, Ucuz Cevher, High Growth |
| F. Boyomo | Kamerun | D(Sağ) (CB, RB) | CA Osasuna | 23 | £22.4M | 78 | 85 | £25k | +7 | — | 2★ | 2★ | 181 / 86 | — |
| J. Aramburu | Venezuela | D(Sağ) (RB, RM) | Real Sociedad | 22 | £19.4M | 77 | 85 | £26k | +8 | — | 3★ | 2★ | 176 / 71 | — |
| Wesley | Brezilya | D(Sağ) (RB, RM) | Roma | 21 | £19.4M | 77 | 85 | £28k | +8 | Acrobat | 3★ | 3★ | 178 / 75 | — |
| Martim Fernandes | Portekiz | D(Sağ) (RB, RM) | FC Porto | 19 | £9.89M | 75 | 85 | £8k | +10 | — | 2★ | 2★ | 181 / 73 | — |
| S. Mouriño | Uruguay | D(Sağ) (CB, RB, RM) | Villarreal CF | 23 | £7.31M | 74 | 85 | £22k | +11 | — | 3★ | 2★ | 183 / 76 | — |
| J. Acheampong | İngiltere | D(Sağ) (RB, CB, CDM, RM) | Chelsea | 19 | £3.10M | 70 | 85 | £28k | +15 | — | 3★ | 2★ | 190 / 85 | Hidden Gem, Ucuz Cevher, High Growth |
| Pau Navarro | İspanya | D(Sağ) (CB, RB, CM) | Villarreal CF | 20 | £3.10M | 70 | 85 | £12k | +15 | — | 3★ | 2★ | 185 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| Arnau Martínez | İspanya | D(Sağ) (RB, RM, CB, RW) | Girona FC | 22 | £21.5M | 79 | 84 | £26k | +5 | — | 3★ | 2★ | 182 / 72 | — |
| M. Gusto | Fransa | D(Sağ) (RB, RM) | Chelsea | 22 | £21.5M | 79 | 84 | £77k | +5 | — | 3★ | 3★ | 178 / 74 | — |
| C. Bradley | Northern Ireland | D(Sağ) (RB, RM) | Liverpool | 21 | £18.1M | 78 | 84 | £52k | +6 | — | 3★ | 3★ | 181 / 75 | — |
| Eduardo Quaresma | Portekiz | D(Sağ) (CB, RB, RM) | Sporting CP | 23 | £16.8M | 77 | 84 | £14k | +7 | — | 3★ | 3★ | 184 / 79 | — |
| R. Lewis | İngiltere | D(Sağ) (RB, LB, CM) | Manchester City | 20 | £17.2M | 77 | 84 | £56k | +7 | — | 3★ | 3★ | 170 / 64 | — |
| Carmona | İspanya | D(Sağ) (RB, RM, RW) | Sevilla FC | 23 | £13.8M | 76 | 84 | £21k | +8 | — | 3★ | 3★ | 183 / 80 | — |
| N. Collins | Almanya | D(Sağ) (CB, RB, RM) | Eintracht Frankfurt | 21 | £7.74M | 74 | 84 | £15k | +10 | — | 3★ | 2★ | 191 / 84 | — |
| A. Khalaili | Israel | D(Sağ) (RM, RB, RW) | Union Saint-Gilloise | 20 | £5.59M | 73 | 84 | £11k | +11 | — | 4★ | 4★ | 183 / 77 | — |
| E. Baum | Almanya | D(Sağ) (RB, RM) | Eintracht Frankfurt | 19 | £4.73M | 72 | 84 | £12k | +12 | — | 3★ | 2★ | 180 / 73 | Hidden Gem, High Growth |
| K. Sabbe | Belçika | D(Sağ) (RB, LB, RM) | Club Brugge KV | 20 | £3.70M | 71 | 84 | £11k | +13 | — | 3★ | 2★ | 172 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| S. Renders | Belçika | D(Sağ) (RB, RM) | Royal Antwerp FC | 17 | £1.03M | 62 | 84 | £2k | +22 | — | 3★ | 2★ | 176 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| O. El Hilali | Fas | D(Sağ) (RB, CB, RM) | RCD Espanyol | 21 | £13.8M | 77 | 83 | £14k | +6 | — | 3★ | 3★ | 183 / 75 | — |
| S. van den Berg | Hollanda | D(Sağ) (CB, RB) | Brentford | 23 | £12.9M | 77 | 83 | £46k | +6 | — | 3★ | 2★ | 192 / 87 | — |
| Tiago Santos | Portekiz | D(Sağ) (RB, RM) | Lille OSC | 22 | £13.8M | 77 | 83 | £21k | +6 | — | 3★ | 3★ | 175 / 71 | — |
| Z. El Ouahdi | Fas | D(Sağ) (RB, RM, RW) | KRC Genk | 23 | £12.5M | 76 | 83 | £17k | +7 | — | 3★ | 3★ | 172 / 66 | — |
| J. Hinshelwood | İngiltere | D(Sağ) (CDM, RB, LB, RM) | Brighton & Hove Albion | 20 | £9.89M | 75 | 83 | £40k | +8 | — | 4★ | 3★ | 181 / 76 | — |
| Juanlu Sánchez | İspanya | D(Sağ) (RB, CAM, RM) | Sevilla FC | 21 | £10.3M | 75 | 83 | £16k | +8 | — | 3★ | 3★ | 186 / 70 | — |
| M. Rosenfelder | Almanya | D(Sağ) (CB, RB, RM) | SC Freiburg | 22 | £7.74M | 74 | 83 | £17k | +9 | — | 3★ | 3★ | 186 / 76 | — |
| Y. Regeer | Hollanda | D(Sağ) (CM, RB, CDM) | Ajax | 21 | £6.02M | 73 | 83 | £9k | +10 | — | 4★ | 3★ | 177 / 68 | — |
| K. Nedeljković | Sırbistan | D(Sağ) (RB, RM) | RB Leipzig | 19 | £4.13M | 72 | 83 | £34k | +11 | — | 2★ | 2★ | 184 / 72 | Ucuz Cevher |
| J. Spileers | Belçika | D(Sağ) (CB, RB) | Club Brugge KV | 20 | £2.75M | 69 | 83 | £9k | +14 | — | 3★ | 2★ | 188 / 79 | Ucuz Cevher, High Growth |
| M. Young | Hollanda | D(Sağ) (CB, RB, RM) | Sparta Rotterdam | 19 | £2.67M | 69 | 83 | £3k | +14 | — | 3★ | 2★ | 182 / 78 | Ucuz Cevher, High Growth |
| Pedro Lima | Brezilya | D(Sağ) (RB, RM) | FC Porto | 19 | £2.32M | 68 | 83 | £15k | +15 | — | 2★ | 3★ | 178 / 57 | Ucuz Cevher, High Growth |
| C. Donovan | Scotland | D(Sağ) (RB, CB, RM) | Celtic | 18 | £1.20M | 64 | 83 | £7k | +19 | — | 3★ | 3★ | 180 / 76 | Ucuz Cevher, High Growth |
| G. Doué | Côte d'Ivoire | D(Sağ) (RB, CB, RM) | RC Strasbourg Alsace | 22 | £12.9M | 77 | 82 | £34k | +5 | — | 3★ | 3★ | 187 / 84 | — |
| Yan Couto | Brezilya | D(Sağ) (RB, RM) | Borussia Dortmund | 23 | £12.9M | 77 | 82 | £29k | +5 | — | 3★ | 4★ | 168 / 60 | — |
| Javi Rodríguez | İspanya | D(Sağ) (RB, CB) | RC Celta | 22 | £9.89M | 76 | 82 | £19k | +6 | — | 3★ | 3★ | 178 / 70 | — |
| Francés | İspanya | D(Sağ) (CB, RB, LB, RM) | Girona FC | 22 | £9.03M | 75 | 82 | £20k | +7 | — | 4★ | 2★ | 181 / 70 | — |
| Alexandre Penetra | Portekiz | D(Sağ) (CB, RB) | AZ Alkmaar | 23 | £7.31M | 74 | 82 | £12k | +8 | — | 2★ | 2★ | 186 / 79 | — |
| Fresneda | İspanya | D(Sağ) (RB, RM, LB) | Sporting CP | 20 | £7.74M | 74 | 82 | £9k | +8 | — | 4★ | 3★ | 181 / 79 | — |
| Andrés García | İspanya | D(Sağ) (RB, RM) | Aston Villa | 22 | £5.59M | 73 | 82 | £46k | +9 | — | 4★ | 3★ | 183 / 82 | — |
| B. Humphreys | İngiltere | D(Sağ) (LB, CB, RB) | Burnley | 22 | £5.59M | 73 | 82 | £29k | +9 | — | 5★ | 2★ | 187 / 79 | — |
| M. Zanotti | İtalya | D(Sağ) (RB, RM) | FC Lugano | 22 | £5.59M | 73 | 82 | £8k | +9 | — | 3★ | 3★ | 173 / 71 | — |
| Pubill | İspanya | D(Sağ) (RB, RM) | Atlético Madrid | 22 | £5.59M | 73 | 82 | £29k | +9 | — | 3★ | 2★ | 190 / 86 | — |
| Wagner Pina | Cabo Verde | D(Sağ) (RM, RB) | Trabzonspor | 22 | £4.73M | 72 | 82 | £24k | +10 | — | 2★ | 3★ | 180 / 72 | — |
| Š. Hrgović | Hırvatistan | D(Sağ) (LB, RB, LM) | Hajduk Split | 21 | £3.27M | 70 | 82 | £9k | +12 | — | 3★ | 2★ | 173 / 69 | High Growth |
| L. Høgsberg | Danimarka | D(Sağ) (CB, RB, LB, RM) | RC Strasbourg Alsace | 19 | £2.67M | 69 | 82 | £13k | +13 | — | 3★ | 2★ | 187 / 70 | High Growth |
| T. Bindon | New Zealand | D(Sağ) (CB, RB) | Sheffield United | 20 | £2.75M | 69 | 82 | £22k | +13 | — | 3★ | 2★ | 190 / 76 | High Growth |
| Héctor Fort | İspanya | D(Sağ) (RB, LB, LM) | Elche CF | 18 | £2.32M | 68 | 82 | £16k | +14 | — | 3★ | 3★ | 185 / 78 | High Growth |
| K. Corbanie | Belçika | D(Sağ) (RB, CDM, CB, CM) | Royal Antwerp FC | 20 | £1.98M | 67 | 82 | £6k | +15 | — | 2★ | 2★ | 187 / 75 | High Growth |
| E. Dijkstra | Hollanda | D(Sağ) (RB, LB, RM) | AZ Alkmaar | 18 | £1.20M | 64 | 82 | £3k | +18 | — | 4★ | 3★ | 173 / 67 | High Growth |
| J. von der Hitz | Almanya | D(Sağ) (RM, RB, RW) | 1. FC Nürnberg | 18 | £666k | 60 | 82 | £1k | +22 | — | 4★ | 3★ | 177 / 70 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Sağ Bekler (RB / D(Sağ)))

- **J. von der Hitz** (1. FC Nürnberg) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **S. Renders** (Royal Antwerp FC) — OVR 62, POT 84: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **C. Donovan** (Celtic) — OVR 64, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **E. Dijkstra** (AZ Alkmaar) — OVR 64, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **K. Corbanie** (Royal Antwerp FC) — OVR 67, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **Pedro Lima** (FC Porto) — OVR 68, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 5. Defansif Orta Saha (CDM / DOS)

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pedri | İspanya | DOS (CM, CDM, CAM) | FC Barcelona | 22 | £129M | 89 | 93 | £146k | +4 | Dribbler, Playmaker , Tactician , Acrobat, Comp… | 4★ | 4★ | 174 / 60 | — |
| João Neves | Portekiz | DOS (CM, CDM) | Paris Saint-Germain | 20 | £68.4M | 85 | 90 | £77k | +5 | — | 4★ | 3★ | 174 / 66 | — |
| E. Camavinga | Fransa | DOS (CM, CDM, LB) | Real Madrid | 22 | £63.2M | 83 | 90 | £150k | +7 | — | 3★ | 4★ | 185 / 77 | — |
| M. Caicedo | Ekvador | DOS (CDM, CM) | Chelsea | 23 | £80.0M | 87 | 89 | £146k | +2 | Tackling , Tactician | 3★ | 3★ | 178 / 73 | — |
| J. Mokio | Belçika | DOS (CDM, CM, LB, CB) | Ajax | 17 | £3.27M | 70 | 89 | £4k | +19 | — | 3★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| R. Gravenberch | Hollanda | DOS (CDM, CM) | Liverpool | 23 | £57.2M | 85 | 88 | £108k | +3 | Tactician | 4★ | 4★ | 190 / 77 | — |
| Jauregizar | İspanya | DOS (CM, CDM) | Athletic Club | 21 | £27.1M | 78 | 88 | £27k | +10 | — | 4★ | 3★ | 177 / 74 | — |
| Pablo Barrios | İspanya | DOS (CM, CDM) | Atlético Madrid | 22 | £40.0M | 82 | 87 | £59k | +5 | — | 3★ | 3★ | 181 / 75 | — |
| C. Baleba | Kamerun | DOS (CDM, CM) | Brighton & Hove Albion | 21 | £32.7M | 81 | 87 | £60k | +6 | — | 3★ | 3★ | 183 / 77 | — |
| Johnny Cardoso | ABD | DOS (CDM, CM) | Atlético Madrid | 23 | £32.2M | 81 | 87 | £52k | +6 | — | 2★ | 3★ | 182 / 78 | — |
| Andrey Santos | Brezilya | DOS (CM, CDM) | Chelsea | 21 | £36.5M | 80 | 87 | £74k | +7 | — | 3★ | 3★ | 180 / 75 | — |
| G. Sudakov | Ukrayna | DOS (CAM, CM, CDM) | SL Benfica | 22 | £37.0M | 80 | 87 | £22k | +7 | — | 4★ | 3★ | 177 / 68 | — |
| W. Zaïre-Emery | Fransa | DOS (CM, CDM, CAM) | Paris Saint-Germain | 19 | £35.3M | 80 | 87 | £50k | +7 | — | 4★ | 3★ | 178 / 68 | — |
| A. Pavlović | Almanya | DOS (CDM, CM) | FC Bayern München | 21 | £31.8M | 79 | 87 | £37k | +8 | — | 4★ | 3★ | 188 / 75 | — |
| H. Larsson | İsveç | DOS (CM, CDM) | Eintracht Frankfurt | 21 | £27.1M | 78 | 87 | £22k | +9 | — | 3★ | 3★ | 187 / 74 | — |
| A. Vermeeren | Belçika | DOS (CM, CDM, CAM) | Olympique de Marseille | 20 | £19.8M | 77 | 87 | £30k | +10 | — | 4★ | 3★ | 177 / 70 | — |
| L. Bergvall | İsveç | DOS (CM, CDM, CAM) | Tottenham Hotspur | 19 | £19.4M | 77 | 87 | £49k | +10 | — | 3★ | 3★ | 186 / 74 | — |
| A. Wharton | İngiltere | DOS (CDM, CM) | Crystal Palace | 21 | £28.8M | 79 | 86 | £50k | +7 | — | 4★ | 3★ | 182 / 70 | — |
| Marc Casadó | İspanya | DOS (CDM, CM) | FC Barcelona | 21 | £28.8M | 79 | 86 | £52k | +7 | — | 4★ | 3★ | 172 / 66 | — |
| Z. Debast | Belçika | DOS (CDM, CB, CM) | Sporting CP | 21 | £25.8M | 78 | 86 | £13k | +8 | — | 4★ | 3★ | 191 / 76 | — |
| A. Jashari | İsviçre | DOS (CDM, CM) | AC Milan | 22 | £19.4M | 77 | 86 | £30k | +9 | — | 4★ | 2★ | 181 / 82 | — |
| Javi Guerra | İspanya | DOS (CM, CDM) | Valencia CF | 22 | £20.2M | 77 | 86 | £28k | +9 | — | 4★ | 3★ | 187 / 77 | — |
| T. Bischof | Almanya | DOS (CM, CDM, RM, CAM) | FC Bayern München | 20 | £14.2M | 76 | 86 | £31k | +10 | — | 3★ | 3★ | 176 / 66 | — |
| A. Bouaddi | Fransa | DOS (CM, CDM) | Lille OSC | 17 | £9.89M | 75 | 86 | £12k | +11 | — | 3★ | 3★ | 186 / 72 | — |
| A. Gray | İngiltere | DOS (CDM, CB, RB, RM) | Tottenham Hotspur | 19 | £9.89M | 75 | 86 | £41k | +11 | — | 4★ | 2★ | 187 / 70 | — |
| T. Land | Hollanda | DOS (CM, CDM) | FC Groningen | 19 | £2.67M | 68 | 86 | £6k | +18 | — | 4★ | 4★ | 168 / 65 | Hidden Gem, Ucuz Cevher, High Growth |
| E. Anderson | İngiltere | DOS (CDM, CM) | Nottingham Forest | 22 | £25.4M | 80 | 85 | £67k | +5 | — | 4★ | 3★ | 179 / 69 | — |
| A. Varela | Arjantin | DOS (CDM, CM) | FC Porto | 23 | £21.9M | 79 | 85 | £12k | +6 | — | 3★ | 3★ | 177 / 73 | — |
| Nico González | İspanya | DOS (CDM, CM) | Manchester City | 23 | £21.9M | 79 | 85 | £77k | +6 | — | 3★ | 3★ | 188 / 88 | — |
| R. Lavia | Belçika | DOS (CDM, CM) | Chelsea | 21 | £23.2M | 78 | 85 | £59k | +7 | — | 3★ | 3★ | 181 / 76 | — |
| S. Ricci | İtalya | DOS (CDM, CM) | AC Milan | 23 | £22.8M | 78 | 85 | £32k | +7 | — | 3★ | 3★ | 181 / 76 | — |
| K. Mainoo | İngiltere | DOS (CM, CDM) | Manchester United | 20 | £19.8M | 77 | 85 | £45k | +8 | — | 3★ | 3★ | 181 / 80 | — |
| L. Camara | Senegal | DOS (CM, CDM) | AS Monaco | 21 | £20.2M | 77 | 85 | £20k | +8 | — | 3★ | 3★ | 173 / 65 | — |
| Dário Essugo | Portekiz | DOS (CDM, CM, CB) | Chelsea | 20 | £9.89M | 75 | 85 | £50k | +10 | — | 3★ | 2★ | 178 / 79 | — |
| J. Bellingham | İngiltere | DOS (CM, CDM, CAM) | Borussia Dortmund | 19 | £7.74M | 74 | 85 | £21k | +11 | — | 3★ | 3★ | 191 / 75 | — |
| Marc Bernal | İspanya | DOS (CDM, CM) | FC Barcelona | 18 | £5.59M | 73 | 85 | £28k | +12 | — | 3★ | 2★ | 191 / 78 | High Growth |
| L. Miller | Scotland | DOS (CM, CDM, CAM, CB) | Udinese | 18 | £3.70M | 71 | 85 | £7k | +14 | — | 4★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Acheampong | İngiltere | DOS (RB, CB, CDM, RM) | Chelsea | 19 | £3.10M | 70 | 85 | £28k | +15 | — | 3★ | 2★ | 190 / 85 | Hidden Gem, Ucuz Cevher, High Growth |
| N. Rovella | İtalya | DOS (CDM, CM) | Lazio | 23 | £21.1M | 79 | 84 | £27k | +5 | — | 4★ | 3★ | 179 / 70 | — |
| P. Sarr | Senegal | DOS (CM, CDM) | Tottenham Hotspur | 22 | £23.2M | 79 | 84 | £72k | +5 | — | 3★ | 2★ | 184 / 70 | — |
| Renato Veiga | Portekiz | DOS (CB, CDM) | Villarreal CF | 21 | £13.3M | 76 | 84 | £21k | +8 | — | 3★ | 2★ | 190 / 88 | — |
| A. Engels | Belçika | DOS (CM, CDM) | Celtic | 21 | £10.8M | 75 | 84 | £29k | +9 | — | 3★ | 3★ | 185 / 76 | — |
| M. Diomande | Côte d'Ivoire | DOS (CDM, CM) | Rangers FC | 23 | £7.74M | 74 | 84 | £30k | +10 | — | 5★ | 3★ | 183 / 75 | — |
| D. Cissé | Fransa | DOS (CM, CDM) | Stade Rennais FC | 21 | £6.02M | 73 | 84 | £13k | +11 | — | 3★ | 3★ | 188 / 73 | — |
| A. Kozubal | Polonya | DOS (CM, CDM, CB) | Lech Poznań | 20 | £3.87M | 71 | 84 | £5k | +13 | — | 3★ | 2★ | 176 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Tóth | Macaristan | DOS (CDM, CM) | Ferencvárosi Torna Club | 19 | £3.10M | 70 | 84 | £8k | +14 | — | 3★ | 2★ | 181 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| E. Banzuzi | Hollanda | DOS (CM, CDM) | RB Leipzig | 20 | £3.27M | 70 | 84 | £16k | +14 | — | 3★ | 2★ | 191 / 80 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Bangoura | Guinea | DOS (CDM, CM) | KRC Genk | 21 | £3.18M | 70 | 84 | £9k | +14 | — | 3★ | 2★ | 190 / 79 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Manzambi | İsviçre | DOS (CAM, CM, CDM, ST) | SC Freiburg | 19 | £2.24M | 67 | 84 | £7k | +17 | — | 3★ | 4★ | 183 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Onana | Belçika | DOS (CDM, CM) | Aston Villa | 23 | £19.8M | 79 | 83 | £73k | +4 | — | 4★ | 3★ | 192 / 76 | — |
| André | Brezilya | DOS (CDM, CM) | Wolverhampton Wanderers | 23 | £16.8M | 78 | 83 | £46k | +5 | — | 3★ | 2★ | 177 / 77 | — |
| S. Hezze | Arjantin | DOS (CDM, CM) | Olympiacos FC | 23 | £16.8M | 78 | 83 | £24k | +5 | — | 3★ | 3★ | 182 / 77 | — |
| Altimira | İspanya | DOS (CDM, CM) | Real Betis Balompié | 23 | £13.3M | 77 | 83 | £20k | +6 | — | 3★ | 3★ | 188 / 80 | — |
| N. El Aynaoui | Fas | DOS (CM, CDM) | Roma | 23 | £14.2M | 77 | 83 | £36k | +6 | — | 3★ | 3★ | 185 / 77 | — |
| R. Reitz | Almanya | DOS (CM, CDM) | Borussia Mönchengladbach | 23 | £14.2M | 77 | 83 | £22k | +6 | — | 4★ | 3★ | 176 / 72 | — |
| E. Fernández | Arjantin | DOS (CDM, CM) | Bayer 04 Leverkusen | 22 | £10.3M | 75 | 83 | £40k | +8 | — | 5★ | 2★ | 178 / 76 | — |
| J. Hinshelwood | İngiltere | DOS (CDM, RB, LB, RM) | Brighton & Hove Albion | 20 | £9.89M | 75 | 83 | £40k | +8 | — | 4★ | 3★ | 181 / 76 | — |
| L. Agoumé | Fransa | DOS (CDM, CM, CB) | Sevilla FC | 23 | £10.3M | 75 | 83 | £20k | +8 | — | 3★ | 3★ | 188 / 72 | — |
| V. Brazhko | Ukrayna | DOS (CDM, CM, CB) | Dynamo Kyiv | 23 | £10.3M | 75 | 83 | £15k | +8 | — | 3★ | 2★ | 184 / 77 | — |
| A. Scott | İngiltere | DOS (CAM, CDM, CM) | AFC Bournemouth | 21 | £8.17M | 74 | 83 | £34k | +9 | — | 3★ | 3★ | 178 / 68 | — |
| C. Casadei | İtalya | DOS (CM, CDM) | Torino | 22 | £8.17M | 74 | 83 | £23k | +9 | — | 3★ | 2★ | 192 / 77 | — |
| N. Mukau | Congo DR | DOS (CDM, CM) | Lille OSC | 20 | £7.31M | 74 | 83 | £15k | +9 | — | 2★ | 2★ | 186 / 79 | — |
| N. Sadiki | Congo DR | DOS (CM, CDM, CAM) | Sunderland | 20 | £7.74M | 74 | 83 | £28k | +9 | — | 3★ | 2★ | 173 / 77 | — |
| P. Sučić | Hırvatistan | DOS (CM, CDM) | Inter | 21 | £8.17M | 74 | 83 | £15k | +9 | — | 4★ | 3★ | 183 / 76 | — |
| M. Perrone | Arjantin | DOS (CDM, CM) | Como | 22 | £5.59M | 73 | 83 | £40k | +10 | — | 3★ | 2★ | 178 / 64 | — |
| Stefan Bajcetic | İspanya | DOS (CDM, CM, CB) | Liverpool | 20 | £5.59M | 73 | 83 | £36k | +10 | — | 3★ | 3★ | 185 / 77 | — |
| V. Atangana | Fransa | DOS (CDM, CM) | Al Ahli SFC | 19 | £5.16M | 73 | 83 | £16k | +10 | — | 3★ | 2★ | 173 / 68 | — |
| Y. Regeer | Hollanda | DOS (CM, RB, CDM) | Ajax | 21 | £6.02M | 73 | 83 | £9k | +10 | — | 4★ | 3★ | 177 / 68 | — |
| C. Ordoñez | Arjantin | DOS (CDM, CM) | Parma | 20 | £4.13M | 72 | 83 | £9k | +11 | — | 3★ | 2★ | 177 / 65 | Ucuz Cevher |
| O. Højlund | Danimarka | DOS (CM, CDM) | Eintracht Frankfurt | 20 | £4.30M | 72 | 83 | £14k | +11 | — | 3★ | 3★ | 184 / 76 | Ucuz Cevher |
| Marlon Gomes | Brezilya | DOS (CM, CAM, CDM) | Shakhtar Donetsk | 21 | £3.96M | 71 | 83 | £9k | +12 | — | 3★ | 3★ | 184 / 72 | Ucuz Cevher, High Growth |
| C. Ndour | İtalya | DOS (CM, CAM, CDM) | Fiorentina | 20 | £3.27M | 70 | 83 | £15k | +13 | — | 4★ | 3★ | 190 / 84 | Ucuz Cevher, High Growth |
| João Simões | Portekiz | DOS (CM, CAM, CDM) | Sporting CP | 18 | £2.75M | 69 | 83 | £5k | +14 | — | 3★ | 3★ | 175 / 71 | Ucuz Cevher, High Growth |
| J. King | İngiltere | DOS (CM, CDM, CAM) | Fulham FC | 18 | £2.41M | 68 | 83 | £17k | +15 | — | 4★ | 3★ | 173 / 66 | Ucuz Cevher, High Growth |
| H. Armstrong | İngiltere | DOS (CDM, CM) | Preston North End | 18 | £2.15M | 67 | 83 | £8k | +16 | — | 3★ | 2★ | 185 / 70 | Ucuz Cevher, High Growth |
| D. Watson | Scotland | DOS (CM, CDM, CAM) | Kilmarnock | 20 | £1.89M | 66 | 83 | £2k | +17 | — | 3★ | 2★ | 175 / 68 | Ucuz Cevher, High Growth |
| M. Siltanen | Finland | DOS (CDM, CM) | Djurgårdens IF | 18 | £1.81M | 66 | 83 | £2k | +17 | — | 3★ | 2★ | 175 / 67 | Ucuz Cevher, High Growth |
| S. Steur | Hollanda | DOS (CM, CDM) | Ajax | 17 | £1.29M | 64 | 83 | £2k | +19 | — | 4★ | 3★ | 183 / 62 | Ucuz Cevher, High Growth |
| K. Dyer | İngiltere | DOS (CM, CDM) | FC Volendam | 18 | £1.12M | 63 | 83 | £12k | +20 | — | 3★ | 3★ | 178 / 65 | Ucuz Cevher, High Growth |
| N. De Cat | Belçika | DOS (CDM, CM) | RSC Anderlecht | 16 | £1.03M | 63 | 83 | £3k | +20 | — | 3★ | 2★ | 192 / 73 | Ucuz Cevher, High Growth |
| B. Rice | Scotland | DOS (CDM, CM) | Rangers FC | 18 | £860k | 61 | 83 | £5k | +22 | — | 3★ | 2★ | 180 / 70 | Ucuz Cevher, High Growth |
| L. Page | İngiltere | DOS (CM, CDM, CAM) | Leicester City | 16 | £860k | 61 | 83 | £3k | +22 | — | 3★ | 3★ | 173 / 67 | Ucuz Cevher, High Growth |
| I. Doukouré | Fransa | DOS (CB, CDM, CM) | RC Strasbourg Alsace | 21 | £9.46M | 76 | 82 | £28k | +6 | — | 3★ | 2★ | 183 / 83 | — |
| C. Zafeiris | Yunanistan | DOS (CM, CDM) | SK Slavia Praha | 22 | £9.89M | 75 | 82 | £20k | +7 | — | 4★ | 4★ | 173 / 75 | — |
| L. Samardžić | Sırbistan | DOS (CM, CDM, CAM) | Atalanta | 23 | £9.46M | 75 | 82 | £37k | +7 | — | 3★ | 4★ | 184 / 79 | — |
| M. Al Juwair | Saudi Arabia | DOS (CM, CDM, CAM) | Al Qadsiah FC | 22 | £9.89M | 75 | 82 | £23k | +7 | — | 4★ | 3★ | 178 / 70 | — |
| P. Aaronson | ABD | DOS (CM, CDM) | Colorado Rapids | 21 | £9.89M | 75 | 82 | £6k | +7 | — | 3★ | 4★ | 175 / 63 | — |
| Y. Ayari | İsveç | DOS (CM, CDM) | Brighton & Hove Albion | 21 | £9.89M | 75 | 82 | £43k | +7 | — | 3★ | 3★ | 172 / 69 | — |
| M. Röhl | Almanya | DOS (CAM, CM, CDM, ST) | Everton | 22 | £8.17M | 74 | 82 | £18k | +8 | — | 4★ | 3★ | 192 / 79 | — |
| T. Morton | İngiltere | DOS (CDM, CM) | Olympique Lyonnais | 22 | £7.74M | 74 | 82 | £13k | +8 | — | 3★ | 3★ | 185 / 73 | — |
| Y. Musah | ABD | DOS (CM, CDM, RM, CAM) | Atalanta | 22 | £8.17M | 74 | 82 | £26k | +8 | — | 3★ | 4★ | 178 / 71 | — |
| C. Jander | Almanya | DOS (CM, CAM, CDM) | Southampton | 22 | £6.02M | 73 | 82 | £31k | +9 | — | 4★ | 3★ | 183 / 75 | — |
| H. Hackney | İngiltere | DOS (CDM, CM) | Middlesbrough | 23 | £5.59M | 73 | 82 | £20k | +9 | — | 3★ | 3★ | 178 / 70 | — |
| L. Ugochukwu | Fransa | DOS (CDM, CM) | Burnley | 21 | £5.59M | 73 | 82 | £24k | +9 | — | 3★ | 3★ | 191 / 88 | — |
| M. Galarza | Arjantin | DOS (CDM, CM) | Talleres | 23 | £5.59M | 73 | 82 | £9k | +9 | — | 3★ | 2★ | 180 / 71 | — |
| M. Kjaergaard | Danimarka | DOS (CM, CDM, CAM) | FC Red Bull Salzburg | 22 | £6.02M | 73 | 82 | £12k | +9 | — | 3★ | 4★ | 192 / 77 | — |
| Turrientes | İspanya | DOS (CM, CDM) | Real Sociedad | 23 | £5.59M | 73 | 82 | £21k | +9 | — | 3★ | 2★ | 181 / 70 | — |
| D. Tıknaz | Türkiye | DOS (CDM, CM, CB) | Beşiktaş JK | 20 | £4.13M | 72 | 82 | £15k | +10 | — | 3★ | 2★ | 193 / 76 | Türk Yeteneği |
| Gabriel Moscardo | Brezilya | DOS (CDM, CM) | Sporting Clube de Braga | 19 | £4.13M | 72 | 82 | £26k | +10 | — | 3★ | 3★ | 185 / 73 | — |
| M. Amougou | Fransa | DOS (CM, CDM) | RC Strasbourg Alsace | 19 | £4.30M | 72 | 82 | £20k | +10 | — | 3★ | 3★ | 177 / 65 | — |
| M. Delorge | Belçika | DOS (CM, CDM) | KAA Gent | 20 | £4.30M | 72 | 82 | £8k | +10 | — | 3★ | 2★ | 189 / 70 | — |
| S. Charles | Northern Ireland | DOS (CM, CDM) | Southampton | 21 | £4.30M | 72 | 82 | £24k | +10 | — | 3★ | 3★ | 189 / 77 | — |
| Iker Muñoz | İspanya | DOS (CM, CDM) | CA Osasuna | 22 | £3.61M | 71 | 82 | £15k | +11 | — | 3★ | 3★ | 180 / 73 | — |
| K. Sano | Japonya | DOS (CDM, LM, CM) | NEC Nijmegen | 21 | £3.44M | 71 | 82 | £5k | +11 | — | 3★ | 3★ | 176 / 66 | — |
| V. Froholdt | Danimarka | DOS (CM, CDM, CAM) | FC Porto | 19 | £3.44M | 71 | 82 | £5k | +11 | — | 4★ | 3★ | 180 / 74 | — |
| J. Canvot | Fransa | DOS (CB, CDM, CM) | Crystal Palace | 18 | £3.01M | 70 | 82 | £21k | +12 | — | 3★ | 2★ | 188 / 79 | High Growth |
| N. Sattlberger | Avusturya | DOS (CDM, CM) | KRC Genk | 21 | £3.18M | 70 | 82 | £9k | +12 | — | 3★ | 2★ | 191 / 73 | High Growth |
| S. Peck | İngiltere | DOS (CDM, CM) | Sheffield United | 20 | £3.10M | 70 | 82 | £18k | +12 | — | 3★ | 2★ | 185 / 75 | High Growth |
| J. Kałuziński | Polonya | DOS (CDM, CM, CAM) | Medipol Başakşehir FK | 22 | £2.75M | 69 | 82 | £7k | +13 | — | 3★ | 2★ | 184 / 74 | High Growth |
| T. Fukui | Japonya | DOS (CM, CAM, CDM) | FC Arouca | 20 | £2.84M | 69 | 82 | £3k | +13 | — | 3★ | 3★ | 172 / 65 | High Growth |
| C. Yirenkyi | Gana | DOS (CM, CDM, CB) | FC Nordsjælland | 19 | £2.06M | 67 | 82 | £4k | +15 | — | 3★ | 2★ | 181 / 73 | High Growth |
| K. Corbanie | Belçika | DOS (RB, CDM, CB, CM) | Royal Antwerp FC | 20 | £1.98M | 67 | 82 | £6k | +15 | — | 2★ | 2★ | 187 / 75 | High Growth |
| M. Courcoul | Fransa | DOS (CDM, CM, CB) | Angers SCO | 18 | £1.46M | 65 | 82 | £3k | +17 | — | 3★ | 2★ | 182 / 70 | High Growth |
| Y. Saidu | Gana | DOS (CM, CB, CDM) | Real Zaragoza | 20 | £1.63M | 65 | 82 | £2k | +17 | — | 4★ | 2★ | 184 / 73 | High Growth |
| C. Konietzke | İsviçre | DOS (CDM, CM) | FC St.Gallen 1879 | 19 | £1.03M | 63 | 82 | £2k | +19 | — | 3★ | 2★ | 185 / 76 | High Growth |
| B. Mamuzah Lum | Almanya | DOS (CDM, CM) | Hertha BSC | 17 | £645k | 60 | 82 | £1k | +22 | — | 4★ | 2★ | 173 / 66 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Defansif Orta Saha (CDM / DOS))

- **D. Tıknaz** (Beşiktaş JK) — OVR 72, POT 82: Türk kadrosu için doğal hedef; düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **B. Mamuzah Lum** (Hertha BSC) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **L. Page** (Leicester City) — OVR 61, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **B. Rice** (Rangers FC) — OVR 61, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **N. De Cat** (RSC Anderlecht) — OVR 63, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **K. Dyer** (FC Volendam) — OVR 63, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 6. Merkez Orta Saha (CM / OS(M))

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J. Bellingham | İngiltere | OS(M) (CAM, CM) | Real Madrid | 22 | £150M | 90 | 94 | £275k | +4 | Dribbler, Playmaker , Clinical finisher, Comple… | 4★ | 4★ | 186 / 75 | — |
| F. Wirtz | Almanya | OS(M) (CAM, ST, CM) | Liverpool | 22 | £129M | 89 | 93 | £163k | +4 | Dribbler, Playmaker , Crosser, Acrobat, Complet… | 4★ | 4★ | 177 / 71 | — |
| Pedri | İspanya | OS(M) (CM, CDM, CAM) | FC Barcelona | 22 | £129M | 89 | 93 | £146k | +4 | Dribbler, Playmaker , Tactician , Acrobat, Comp… | 4★ | 4★ | 174 / 60 | — |
| J. Musiala | Almanya | OS(M) (CAM, LM, CM, ST) | FC Bayern München | 22 | £115M | 88 | 92 | £95k | +4 | Dribbler, Acrobat, Clinical finisher, Complete … | 4★ | 5★ | 184 / 72 | — |
| D. Doué | Fransa | OS(M) (RW, LW, CM, RM) | Paris Saint-Germain | 20 | £71.8M | 85 | 91 | £86k | +6 | Dribbler, Acrobat | 4★ | 5★ | 181 / 79 | — |
| João Neves | Portekiz | OS(M) (CM, CDM) | Paris Saint-Germain | 20 | £68.4M | 85 | 90 | £77k | +5 | — | 4★ | 3★ | 174 / 66 | — |
| E. Camavinga | Fransa | OS(M) (CM, CDM, LB) | Real Madrid | 22 | £63.2M | 83 | 90 | £150k | +7 | — | 3★ | 4★ | 185 / 77 | — |
| M. Caicedo | Ekvador | OS(M) (CDM, CM) | Chelsea | 23 | £80.0M | 87 | 89 | £146k | +2 | Tackling , Tactician | 3★ | 3★ | 178 / 73 | — |
| Gavi | İspanya | OS(M) (CM, CAM) | FC Barcelona | 20 | £48.2M | 83 | 89 | £73k | +6 | Dribbler, Acrobat | 3★ | 3★ | 173 / 70 | — |
| K. Yıldız | Türkiye | OS(M) (CAM, LM, LW, CM) | Juventus | 20 | £33.1M | 79 | 89 | £69k | +10 | — | 5★ | 4★ | 185 / 75 | Türk Yeteneği |
| Nico Paz | Arjantin | OS(M) (CAM, CM) | Como | 20 | £33.1M | 79 | 89 | £58k | +10 | — | 3★ | 4★ | 186 / 81 | — |
| Rodrigo Mora | Portekiz | OS(M) (CAM, LW, CM, ST) | FC Porto | 18 | £15.1M | 76 | 89 | £8k | +13 | — | 4★ | 4★ | 168 / 56 | High Growth |
| J. Mokio | Belçika | OS(M) (CDM, CM, LB, CB) | Ajax | 17 | £3.27M | 70 | 89 | £4k | +19 | — | 3★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| R. Gravenberch | Hollanda | OS(M) (CDM, CM) | Liverpool | 23 | £57.2M | 85 | 88 | £108k | +3 | Tactician | 4★ | 4★ | 190 / 77 | — |
| Jauregizar | İspanya | OS(M) (CM, CDM) | Athletic Club | 21 | £27.1M | 78 | 88 | £27k | +10 | — | 4★ | 3★ | 177 / 74 | — |
| M. Tillman | ABD | OS(M) (CAM, LW, CM) | Bayer 04 Leverkusen | 23 | £39.6M | 82 | 87 | £69k | +5 | — | 3★ | 4★ | 187 / 71 | — |
| Pablo Barrios | İspanya | OS(M) (CM, CDM) | Atlético Madrid | 22 | £40.0M | 82 | 87 | £59k | +5 | — | 3★ | 3★ | 181 / 75 | — |
| C. Baleba | Kamerun | OS(M) (CDM, CM) | Brighton & Hove Albion | 21 | £32.7M | 81 | 87 | £60k | +6 | — | 3★ | 3★ | 183 / 77 | — |
| Johnny Cardoso | ABD | OS(M) (CDM, CM) | Atlético Madrid | 23 | £32.2M | 81 | 87 | £52k | +6 | — | 2★ | 3★ | 182 / 78 | — |
| Andrey Santos | Brezilya | OS(M) (CM, CDM) | Chelsea | 21 | £36.5M | 80 | 87 | £74k | +7 | — | 3★ | 3★ | 180 / 75 | — |
| Fermín | İspanya | OS(M) (CAM, CM, LW, ST) | FC Barcelona | 22 | £37.0M | 80 | 87 | £69k | +7 | — | 4★ | 3★ | 174 / 64 | — |
| G. Sudakov | Ukrayna | OS(M) (CAM, CM, CDM) | SL Benfica | 22 | £37.0M | 80 | 87 | £22k | +7 | — | 4★ | 3★ | 177 / 68 | — |
| W. Zaïre-Emery | Fransa | OS(M) (CM, CDM, CAM) | Paris Saint-Germain | 19 | £35.3M | 80 | 87 | £50k | +7 | — | 4★ | 3★ | 178 / 68 | — |
| A. Pavlović | Almanya | OS(M) (CDM, CM) | FC Bayern München | 21 | £31.8M | 79 | 87 | £37k | +8 | — | 4★ | 3★ | 188 / 75 | — |
| H. Larsson | İsveç | OS(M) (CM, CDM) | Eintracht Frankfurt | 21 | £27.1M | 78 | 87 | £22k | +9 | — | 3★ | 3★ | 187 / 74 | — |
| M. Lewis-Skelly | İngiltere | OS(M) (LB, CM) | Arsenal | 18 | £24.1M | 78 | 87 | £55k | +9 | — | 3★ | 3★ | 178 / 72 | — |
| A. Vermeeren | Belçika | OS(M) (CM, CDM, CAM) | Olympique de Marseille | 20 | £19.8M | 77 | 87 | £30k | +10 | — | 4★ | 3★ | 177 / 70 | — |
| L. Bergvall | İsveç | OS(M) (CM, CDM, CAM) | Tottenham Hotspur | 19 | £19.4M | 77 | 87 | £49k | +10 | — | 3★ | 3★ | 186 / 74 | — |
| E. Nwaneri | İngiltere | OS(M) (RW, CM, RM) | Arsenal | 18 | £13.8M | 76 | 87 | £58k | +11 | — | 3★ | 3★ | 176 / 70 | — |
| K. Smit | Hollanda | OS(M) (CAM, CM, RM) | AZ Alkmaar | 19 | £4.73M | 72 | 87 | £9k | +15 | — | 4★ | 4★ | 180 / 66 | Hidden Gem, High Growth |
| M. Rogers | İngiltere | OS(M) (CAM, RM, LM, CM) | Aston Villa | 22 | £38.3M | 82 | 86 | £95k | +4 | — | 4★ | 4★ | 188 / 80 | — |
| A. Wharton | İngiltere | OS(M) (CDM, CM) | Crystal Palace | 21 | £28.8M | 79 | 86 | £50k | +7 | — | 4★ | 3★ | 182 / 70 | — |
| Francisco Conceição | Portekiz | OS(M) (CAM, RM, RW, CM) | Juventus | 22 | £30.5M | 79 | 86 | £82k | +7 | Acrobat | 2★ | 4★ | 168 / 61 | — |
| Marc Casadó | İspanya | OS(M) (CDM, CM) | FC Barcelona | 21 | £28.8M | 79 | 86 | £52k | +7 | — | 4★ | 3★ | 172 / 66 | — |
| L. Sučić | Hırvatistan | OS(M) (CM, CAM) | Real Sociedad | 22 | £27.1M | 78 | 86 | £29k | +8 | — | 3★ | 4★ | 185 / 71 | — |
| Z. Debast | Belçika | OS(M) (CDM, CB, CM) | Sporting CP | 21 | £25.8M | 78 | 86 | £13k | +8 | — | 4★ | 3★ | 191 / 76 | — |
| A. Jashari | İsviçre | OS(M) (CDM, CM) | AC Milan | 22 | £19.4M | 77 | 86 | £30k | +9 | — | 4★ | 2★ | 181 / 82 | — |
| Javi Guerra | İspanya | OS(M) (CM, CDM) | Valencia CF | 22 | £20.2M | 77 | 86 | £28k | +9 | — | 4★ | 3★ | 187 / 77 | — |
| T. Bischof | Almanya | OS(M) (CM, CDM, RM, CAM) | FC Bayern München | 20 | £14.2M | 76 | 86 | £31k | +10 | — | 3★ | 3★ | 176 / 66 | — |
| A. Bouaddi | Fransa | OS(M) (CM, CDM) | Lille OSC | 17 | £9.89M | 75 | 86 | £12k | +11 | — | 3★ | 3★ | 186 / 72 | — |
| C. Echeverri | Arjantin | OS(M) (CAM, CM, LW) | Bayer 04 Leverkusen | 19 | £8.60M | 74 | 86 | £46k | +12 | Acrobat | 3★ | 3★ | 170 / 65 | High Growth |
| M. Stroeykens | Belçika | OS(M) (CM, CAM) | RSC Anderlecht | 20 | £8.60M | 74 | 86 | £16k | +12 | — | 3★ | 3★ | 177 / 79 | High Growth |
| L. Miley | İngiltere | OS(M) (CM) | Newcastle United | 19 | £4.73M | 72 | 86 | £38k | +14 | — | 4★ | 3★ | 189 / 75 | Hidden Gem, High Growth |
| P. Wanner | Almanya | OS(M) (CAM, RW, CM) | PSV | 19 | £4.73M | 72 | 86 | £9k | +14 | — | 2★ | 4★ | 185 / 75 | Hidden Gem, High Growth |
| C. Mouzakitis | Yunanistan | OS(M) (CM, CAM) | Olympiacos FC | 18 | £3.70M | 71 | 86 | £11k | +15 | — | 3★ | 3★ | 175 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| K. Karetsas | Yunanistan | OS(M) (CAM, RW, CM) | KRC Genk | 17 | £3.44M | 70 | 86 | £7k | +16 | — | 4★ | 3★ | 171 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| S. Nypan | Norveç | OS(M) (CM, CAM, ST) | Middlesbrough | 18 | £3.01M | 69 | 86 | £25k | +17 | — | 4★ | 4★ | 183 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| T. Land | Hollanda | OS(M) (CM, CDM) | FC Groningen | 19 | £2.67M | 68 | 86 | £6k | +18 | — | 4★ | 4★ | 168 / 65 | Hidden Gem, Ucuz Cevher, High Growth |
| L. Karl | Almanya | OS(M) (CAM, RM, CM) | FC Bayern München | 17 | £1.29M | 63 | 86 | £5k | +23 | — | 3★ | 4★ | 168 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| E. Anderson | İngiltere | OS(M) (CDM, CM) | Nottingham Forest | 22 | £25.4M | 80 | 85 | £67k | +5 | — | 4★ | 3★ | 179 / 69 | — |
| A. Varela | Arjantin | OS(M) (CDM, CM) | FC Porto | 23 | £21.9M | 79 | 85 | £12k | +6 | — | 3★ | 3★ | 177 / 73 | — |
| Amad | Côte d'Ivoire | OS(M) (CAM, RW, RM, CM) | Manchester United | 22 | £24.1M | 79 | 85 | £64k | +6 | Acrobat | 4★ | 4★ | 173 / 67 | — |
| Marcos Leonardo | Brezilya | OS(M) (ST, CAM, CM) | Al Hilal | 22 | £24.5M | 79 | 85 | £38k | +6 | — | 4★ | 4★ | 175 / 72 | — |
| Nico González | İspanya | OS(M) (CDM, CM) | Manchester City | 23 | £21.9M | 79 | 85 | £77k | +6 | — | 3★ | 3★ | 188 / 88 | — |
| M. Soulé | Arjantin | OS(M) (CAM, RM, CM) | Roma | 22 | £24.5M | 78 | 85 | £39k | +7 | — | 4★ | 4★ | 176 / 69 | — |
| P. Nebel | Almanya | OS(M) (CAM, CM, RM) | 1. FSV Mainz 05 | 22 | £24.5M | 78 | 85 | £23k | +7 | Acrobat | 4★ | 3★ | 169 / 67 | — |
| R. Lavia | Belçika | OS(M) (CDM, CM) | Chelsea | 21 | £23.2M | 78 | 85 | £59k | +7 | — | 3★ | 3★ | 181 / 76 | — |
| S. Ricci | İtalya | OS(M) (CDM, CM) | AC Milan | 23 | £22.8M | 78 | 85 | £32k | +7 | — | 3★ | 3★ | 181 / 76 | — |
| K. Mainoo | İngiltere | OS(M) (CM, CDM) | Manchester United | 20 | £19.8M | 77 | 85 | £45k | +8 | — | 3★ | 3★ | 181 / 80 | — |
| L. Camara | Senegal | OS(M) (CM, CDM) | AS Monaco | 21 | £20.2M | 77 | 85 | £20k | +8 | — | 3★ | 3★ | 173 / 65 | — |
| Mateus Fernandes | Portekiz | OS(M) (CAM, CM) | West Ham United | 20 | £14.2M | 76 | 85 | £36k | +9 | — | 4★ | 4★ | 178 / 72 | — |
| O. Gloukh | Israel | OS(M) (CAM, LW, CM) | Ajax | 21 | £14.6M | 76 | 85 | £12k | +9 | — | 4★ | 4★ | 171 / 68 | — |
| Dário Essugo | Portekiz | OS(M) (CDM, CM, CB) | Chelsea | 20 | £9.89M | 75 | 85 | £50k | +10 | — | 3★ | 2★ | 178 / 79 | — |
| S. Mayulu | Fransa | OS(M) (CM) | Paris Saint-Germain | 19 | £10.3M | 75 | 85 | £35k | +10 | — | 5★ | 3★ | 183 / 69 | — |
| C. Harder | Danimarka | OS(M) (ST, CAM, LW, CM) | RB Leipzig | 20 | £8.17M | 74 | 85 | £28k | +11 | — | 3★ | 3★ | 185 / 71 | — |
| Gustavo Sá | Portekiz | OS(M) (CAM, CM) | Famalicão | 20 | £8.17M | 74 | 85 | £8k | +11 | — | 3★ | 3★ | 186 / 80 | — |
| J. Bellingham | İngiltere | OS(M) (CM, CDM, CAM) | Borussia Dortmund | 19 | £7.74M | 74 | 85 | £21k | +11 | — | 3★ | 3★ | 191 / 75 | — |
| A. Milambo | Hollanda | OS(M) (CM, CAM) | Brentford | 20 | £6.45M | 73 | 85 | £30k | +12 | — | 3★ | 4★ | 179 / 68 | High Growth |
| K. Páez | Ekvador | OS(M) (CAM, RW, CM) | RC Strasbourg Alsace | 18 | £6.02M | 73 | 85 | £40k | +12 | — | 3★ | 4★ | 178 / 71 | High Growth |
| Marc Bernal | İspanya | OS(M) (CDM, CM) | FC Barcelona | 18 | £5.59M | 73 | 85 | £28k | +12 | — | 3★ | 2★ | 191 / 78 | High Growth |
| L. Miller | Scotland | OS(M) (CM, CDM, CAM, CB) | Udinese | 18 | £3.70M | 71 | 85 | £7k | +14 | — | 4★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| Pau Navarro | İspanya | OS(M) (CB, RB, CM) | Villarreal CF | 20 | £3.10M | 70 | 85 | £12k | +15 | — | 3★ | 2★ | 185 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Ouédraogo | Almanya | OS(M) (CAM, CM) | RB Leipzig | 19 | £3.10M | 69 | 85 | £14k | +16 | — | 3★ | 4★ | 191 / 89 | Hidden Gem, Ucuz Cevher, High Growth |
| Alejandro Granados | İspanya | OS(M) (CM, CAM) | Club Brugge KV | 19 | £1.72M | 65 | 85 | £5k | +20 | — | 4★ | 2★ | 180 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Lerma | Ekvador | OS(M) (LM, CAM, CM, LW) | Independiente del Valle | 17 | £1.55M | 64 | 85 | £3k | +21 | — | 3★ | 4★ | 176 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Saibari | Fas | OS(M) (CAM, CM) | PSV | 23 | £22.8M | 79 | 84 | £20k | +5 | — | 4★ | 4★ | 185 / 81 | — |
| N. Rovella | İtalya | OS(M) (CDM, CM) | Lazio | 23 | £21.1M | 79 | 84 | £27k | +5 | — | 4★ | 3★ | 179 / 70 | — |
| P. Sarr | Senegal | OS(M) (CM, CDM) | Tottenham Hotspur | 22 | £23.2M | 79 | 84 | £72k | +5 | — | 3★ | 2★ | 184 / 70 | — |
| E. Millot | Fransa | OS(M) (CAM, CM) | Al Ahli SFC | 22 | £19.4M | 78 | 84 | £32k | +6 | — | 2★ | 4★ | 174 / 66 | — |
| H. Elliott | İngiltere | OS(M) (CAM, CM, RW) | Aston Villa | 22 | £19.4M | 78 | 84 | £65k | +6 | Acrobat | 3★ | 3★ | 168 / 64 | — |
| H. Haraldsson | Iceland | OS(M) (CAM, LM, CM) | Lille OSC | 22 | £19.4M | 78 | 84 | £24k | +6 | — | 4★ | 3★ | 178 / 71 | — |
| K. Taylor | Hollanda | OS(M) (CM, CAM) | Ajax | 23 | £18.9M | 78 | 84 | £15k | +6 | — | 5★ | 3★ | 182 / 73 | — |
| A. Garnacho | Arjantin | OS(M) (CAM, LW, LM, CM) | Chelsea | 21 | £18.5M | 77 | 84 | £60k | +7 | — | 4★ | 3★ | 180 / 72 | — |
| G. Konstantelias | Yunanistan | OS(M) (CAM, RW, CM) | PAOK | 22 | £18.5M | 77 | 84 | £24k | +7 | — | 4★ | 4★ | 178 / 66 | — |
| R. Lewis | İngiltere | OS(M) (RB, LB, CM) | Manchester City | 20 | £17.2M | 77 | 84 | £56k | +7 | — | 3★ | 3★ | 170 / 64 | — |
| B. El Khannouss | Fas | OS(M) (CAM, LM, CM) | VfB Stuttgart | 21 | £14.6M | 76 | 84 | £28k | +8 | — | 3★ | 4★ | 180 / 70 | — |
| C. Chukwuemeka | İngiltere | OS(M) (CAM, CM) | Borussia Dortmund | 21 | £14.6M | 76 | 84 | £25k | +8 | — | 3★ | 4★ | 187 / 77 | — |
| C. Uche | Nijerya | OS(M) (ST, CAM, CM) | Crystal Palace | 22 | £14.6M | 76 | 84 | £25k | +8 | — | 3★ | 3★ | 190 / 80 | — |
| A. Engels | Belçika | OS(M) (CM, CDM) | Celtic | 21 | £10.8M | 75 | 84 | £29k | +9 | — | 3★ | 3★ | 185 / 76 | — |
| B. Gruda | Almanya | OS(M) (CAM, RM, CM) | Brighton & Hove Albion | 21 | £8.17M | 74 | 84 | £40k | +10 | — | 3★ | 4★ | 178 / 70 | — |
| M. Diomande | Côte d'Ivoire | OS(M) (CDM, CM) | Rangers FC | 23 | £7.74M | 74 | 84 | £30k | +10 | — | 5★ | 3★ | 183 / 75 | — |
| Pablo Torre | İspanya | OS(M) (CAM, CM) | RCD Mallorca | 22 | £8.17M | 74 | 84 | £20k | +10 | — | 4★ | 4★ | 173 / 63 | — |
| Alvyn Sanches | İsviçre | OS(M) (CAM, CM, ST) | BSC Young Boys | 22 | £6.02M | 73 | 84 | £14k | +11 | — | 3★ | 4★ | 183 / 68 | — |
| D. Cissé | Fransa | OS(M) (CM, CDM) | Stade Rennais FC | 21 | £6.02M | 73 | 84 | £13k | +11 | — | 3★ | 3★ | 188 / 73 | — |
| Pablo Marín | İspanya | OS(M) (CM, CAM) | Real Sociedad | 21 | £6.02M | 73 | 84 | £17k | +11 | — | 3★ | 3★ | 178 / 71 | — |
| N. Pisilli | İtalya | OS(M) (CM, CAM) | Roma | 20 | £4.73M | 72 | 84 | £21k | +12 | — | 3★ | 2★ | 180 / 75 | Hidden Gem, High Growth |
| V. Carboni | Arjantin | OS(M) (CAM, ST, RM, CM) | Genoa | 20 | £4.73M | 72 | 84 | £13k | +12 | — | 3★ | 3★ | 185 / 78 | Hidden Gem, High Growth |
| A. Kozubal | Polonya | OS(M) (CM, CDM, CB) | Lech Poznań | 20 | £3.87M | 71 | 84 | £5k | +13 | — | 3★ | 2★ | 176 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Maza | Cezayir | OS(M) (CAM, CM) | Bayer 04 Leverkusen | 19 | £3.78M | 71 | 84 | £23k | +13 | — | 3★ | 4★ | 180 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Devine | İngiltere | OS(M) (CAM, CM) | Preston North End | 20 | £3.27M | 70 | 84 | £29k | +14 | — | 3★ | 3★ | 182 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Tóth | Macaristan | OS(M) (CDM, CM) | Ferencvárosi Torna Club | 19 | £3.10M | 70 | 84 | £8k | +14 | — | 3★ | 2★ | 181 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| C. Rigg | İngiltere | OS(M) (CAM, CM) | Sunderland | 18 | £3.18M | 70 | 84 | £17k | +14 | — | 3★ | 3★ | 177 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| E. Banzuzi | Hollanda | OS(M) (CM, CDM) | RB Leipzig | 20 | £3.27M | 70 | 84 | £16k | +14 | — | 3★ | 2★ | 191 / 80 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Bangoura | Guinea | OS(M) (CDM, CM) | KRC Genk | 21 | £3.18M | 70 | 84 | £9k | +14 | — | 3★ | 2★ | 190 / 79 | Hidden Gem, Ucuz Cevher, High Growth |
| N. Weiper | Almanya | OS(M) (ST, CAM, CM) | 1. FSV Mainz 05 | 20 | £3.35M | 70 | 84 | £11k | +14 | — | 3★ | 3★ | 192 / 83 | Hidden Gem, Ucuz Cevher, High Growth |
| S. Pafundi | İtalya | OS(M) (CAM, CM, ST) | Sampdoria | 19 | £2.67M | 68 | 84 | £5k | +16 | — | 3★ | 3★ | 166 / 64 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Manzambi | İsviçre | OS(M) (CAM, CM, CDM, ST) | SC Freiburg | 19 | £2.24M | 67 | 84 | £7k | +17 | — | 3★ | 4★ | 183 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| Unai Hernández | İspanya | OS(M) (LM, CM, CAM, LW) | Al Shabab | 20 | £1.89M | 66 | 84 | £8k | +18 | — | 3★ | 3★ | 171 / 65 | Hidden Gem, Ucuz Cevher, High Growth |
| T. Nyoni | İngiltere | OS(M) (CM, CAM) | Liverpool | 18 | £1.38M | 64 | 84 | £11k | +20 | — | 3★ | 3★ | 180 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Onana | Belçika | OS(M) (CDM, CM) | Aston Villa | 23 | £19.8M | 79 | 83 | £73k | +4 | — | 4★ | 3★ | 192 / 76 | — |
| André | Brezilya | OS(M) (CDM, CM) | Wolverhampton Wanderers | 23 | £16.8M | 78 | 83 | £46k | +5 | — | 3★ | 2★ | 177 / 77 | — |
| I. Moriba | Guinea | OS(M) (CM) | RC Celta | 22 | £18.5M | 78 | 83 | £22k | +5 | — | 4★ | 4★ | 185 / 73 | — |
| M. Baturina | Hırvatistan | OS(M) (CAM, CM) | Como | 22 | £18.5M | 78 | 83 | £61k | +5 | — | 4★ | 3★ | 172 / 68 | — |
| S. Hezze | Arjantin | OS(M) (CDM, CM) | Olympiacos FC | 23 | £16.8M | 78 | 83 | £24k | +5 | — | 3★ | 3★ | 182 / 77 | — |
| S. Steijn | Hollanda | OS(M) (CAM, CM) | Feyenoord | 23 | £18.1M | 78 | 83 | £14k | +5 | — | 3★ | 3★ | 173 / 59 | — |
| Aimar Oroz | İspanya | OS(M) (CM, CAM, LM) | CA Osasuna | 23 | £14.2M | 77 | 83 | £25k | +6 | — | 3★ | 3★ | 177 / 72 | — |
| Altimira | İspanya | OS(M) (CDM, CM) | Real Betis Balompié | 23 | £13.3M | 77 | 83 | £20k | +6 | — | 3★ | 3★ | 188 / 80 | — |
| H. Diarra | Senegal | OS(M) (CM, CAM) | Sunderland | 21 | £14.6M | 77 | 83 | £34k | +6 | — | 2★ | 2★ | 178 / 75 | — |
| N. El Aynaoui | Fas | OS(M) (CM, CDM) | Roma | 23 | £14.2M | 77 | 83 | £36k | +6 | — | 3★ | 3★ | 185 / 77 | — |
| R. Reitz | Almanya | OS(M) (CM, CDM) | Borussia Mönchengladbach | 23 | £14.2M | 77 | 83 | £22k | +6 | — | 4★ | 3★ | 176 / 72 | — |
| Gabri Veiga | İspanya | OS(M) (CAM, CM, LM) | FC Porto | 23 | £12.9M | 76 | 83 | £10k | +7 | — | 4★ | 4★ | 184 / 71 | — |
| S. Nanasi | İsveç | OS(M) (CAM, LM, CM) | RC Strasbourg Alsace | 23 | £12.9M | 76 | 83 | £34k | +7 | — | 3★ | 4★ | 178 / 71 | — |
| E. Fernández | Arjantin | OS(M) (CDM, CM) | Bayer 04 Leverkusen | 22 | £10.3M | 75 | 83 | £40k | +8 | — | 5★ | 2★ | 178 / 76 | — |
| L. Agoumé | Fransa | OS(M) (CDM, CM, CB) | Sevilla FC | 23 | £10.3M | 75 | 83 | £20k | +8 | — | 3★ | 3★ | 188 / 72 | — |
| O. Hutchinson | İngiltere | OS(M) (CAM, RM, CM) | Nottingham Forest | 21 | £10.8M | 75 | 83 | £44k | +8 | — | 3★ | 3★ | 174 / 65 | — |
| V. Barco | Arjantin | OS(M) (LB, LM, CM) | RC Strasbourg Alsace | 20 | £10.3M | 75 | 83 | £26k | +8 | — | 3★ | 3★ | 170 / 66 | — |
| V. Brazhko | Ukrayna | OS(M) (CDM, CM, CB) | Dynamo Kyiv | 23 | £10.3M | 75 | 83 | £15k | +8 | — | 3★ | 2★ | 184 / 77 | — |
| A. Scott | İngiltere | OS(M) (CAM, CDM, CM) | AFC Bournemouth | 21 | £8.17M | 74 | 83 | £34k | +9 | — | 3★ | 3★ | 178 / 68 | — |
| A. Zakharyan | Russia | OS(M) (RM, CM, LM, RW) | Real Sociedad | 22 | £8.17M | 74 | 83 | £22k | +9 | — | 4★ | 3★ | 182 / 73 | — |
| C. Casadei | İtalya | OS(M) (CM, CDM) | Torino | 22 | £8.17M | 74 | 83 | £23k | +9 | — | 3★ | 2★ | 192 / 77 | — |
| C. Uzun | Türkiye | OS(M) (CAM, ST, CM) | Eintracht Frankfurt | 19 | £7.74M | 74 | 83 | £15k | +9 | — | 3★ | 4★ | 186 / 70 | Türk Yeteneği |
| G. Fabbian | İtalya | OS(M) (CM, CAM) | Bologna | 22 | £8.17M | 74 | 83 | £28k | +9 | — | 4★ | 3★ | 186 / 75 | — |
| M. Šín | Czechia | OS(M) (CAM, RM, CM) | AZ Alkmaar | 21 | £8.17M | 74 | 83 | £11k | +9 | — | 4★ | 3★ | 180 / 70 | — |
| N. Mukau | Congo DR | OS(M) (CDM, CM) | Lille OSC | 20 | £7.31M | 74 | 83 | £15k | +9 | — | 2★ | 2★ | 186 / 79 | — |
| N. Sadiki | Congo DR | OS(M) (CM, CDM, CAM) | Sunderland | 20 | £7.74M | 74 | 83 | £28k | +9 | — | 3★ | 2★ | 173 / 77 | — |
| P. Sučić | Hırvatistan | OS(M) (CM, CDM) | Inter | 21 | £8.17M | 74 | 83 | £15k | +9 | — | 4★ | 3★ | 183 / 76 | — |
| M. Perrone | Arjantin | OS(M) (CDM, CM) | Como | 22 | £5.59M | 73 | 83 | £40k | +10 | — | 3★ | 2★ | 178 / 64 | — |
| N. O'Reilly | İngiltere | OS(M) (LB, CM, CAM) | Manchester City | 20 | £5.59M | 73 | 83 | £41k | +10 | — | 2★ | 3★ | 193 / 77 | — |
| Stefan Bajcetic | İspanya | OS(M) (CDM, CM, CB) | Liverpool | 20 | £5.59M | 73 | 83 | £36k | +10 | — | 3★ | 3★ | 185 / 77 | — |
| V. Atangana | Fransa | OS(M) (CDM, CM) | Al Ahli SFC | 19 | £5.16M | 73 | 83 | £16k | +10 | — | 3★ | 2★ | 173 / 68 | — |
| Y. Regeer | Hollanda | OS(M) (CM, RB, CDM) | Ajax | 21 | £6.02M | 73 | 83 | £9k | +10 | — | 4★ | 3★ | 177 / 68 | — |
| C. Ordoñez | Arjantin | OS(M) (CDM, CM) | Parma | 20 | £4.13M | 72 | 83 | £9k | +11 | — | 3★ | 2★ | 177 / 65 | Ucuz Cevher |
| O. Højlund | Danimarka | OS(M) (CM, CDM) | Eintracht Frankfurt | 20 | £4.30M | 72 | 83 | £14k | +11 | — | 3★ | 3★ | 184 / 76 | Ucuz Cevher |
| Marlon Gomes | Brezilya | OS(M) (CM, CAM, CDM) | Shakhtar Donetsk | 21 | £3.96M | 71 | 83 | £9k | +12 | — | 3★ | 3★ | 184 / 72 | Ucuz Cevher, High Growth |
| C. Ndour | İtalya | OS(M) (CM, CAM, CDM) | Fiorentina | 20 | £3.27M | 70 | 83 | £15k | +13 | — | 4★ | 3★ | 190 / 84 | Ucuz Cevher, High Growth |
| João Simões | Portekiz | OS(M) (CM, CAM, CDM) | Sporting CP | 18 | £2.75M | 69 | 83 | £5k | +14 | — | 3★ | 3★ | 175 / 71 | Ucuz Cevher, High Growth |
| M. Krattenmacher | Almanya | OS(M) (CAM, ST, CM) | Hertha BSC | 19 | £2.84M | 69 | 83 | £15k | +14 | — | 5★ | 3★ | 180 / 75 | Ucuz Cevher, High Growth |
| J. King | İngiltere | OS(M) (CM, CDM, CAM) | Fulham FC | 18 | £2.41M | 68 | 83 | £17k | +15 | — | 4★ | 3★ | 173 / 66 | Ucuz Cevher, High Growth |
| H. Armstrong | İngiltere | OS(M) (CDM, CM) | Preston North End | 18 | £2.15M | 67 | 83 | £8k | +16 | — | 3★ | 2★ | 185 / 70 | Ucuz Cevher, High Growth |
| I. Babadi | Hollanda | OS(M) (CAM, CM, LW) | Royal Antwerp FC | 20 | £2.32M | 67 | 83 | £6k | +16 | — | 4★ | 3★ | 178 / 68 | Ucuz Cevher, High Growth |
| D. Watson | Scotland | OS(M) (CM, CDM, CAM) | Kilmarnock | 20 | £1.89M | 66 | 83 | £2k | +17 | — | 3★ | 2★ | 175 / 68 | Ucuz Cevher, High Growth |
| M. Siltanen | Finland | OS(M) (CDM, CM) | Djurgårdens IF | 18 | £1.81M | 66 | 83 | £2k | +17 | — | 3★ | 2★ | 175 / 67 | Ucuz Cevher, High Growth |
| Rodri Mendoza | İspanya | OS(M) (CM, RM, CAM) | Elche CF | 20 | £1.89M | 66 | 83 | £5k | +17 | — | 3★ | 3★ | 182 / 72 | Ucuz Cevher, High Growth |
| V. Tsukanov | Ukrayna | OS(M) (CM, CAM, RM) | Shakhtar Donetsk | 19 | £1.55M | 65 | 83 | £3k | +18 | — | 3★ | 2★ | 170 / 68 | Ucuz Cevher, High Growth |
| S. Steur | Hollanda | OS(M) (CM, CDM) | Ajax | 17 | £1.29M | 64 | 83 | £2k | +19 | — | 4★ | 3★ | 183 / 62 | Ucuz Cevher, High Growth |
| K. Dyer | İngiltere | OS(M) (CM, CDM) | FC Volendam | 18 | £1.12M | 63 | 83 | £12k | +20 | — | 3★ | 3★ | 178 / 65 | Ucuz Cevher, High Growth |
| N. De Cat | Belçika | OS(M) (CDM, CM) | RSC Anderlecht | 16 | £1.03M | 63 | 83 | £3k | +20 | — | 3★ | 2★ | 192 / 73 | Ucuz Cevher, High Growth |
| B. Rice | Scotland | OS(M) (CDM, CM) | Rangers FC | 18 | £860k | 61 | 83 | £5k | +22 | — | 3★ | 2★ | 180 / 70 | Ucuz Cevher, High Growth |
| C. Comotto | İtalya | OS(M) (CM) | Spezia | 17 | £860k | 61 | 83 | £3k | +22 | — | 3★ | 2★ | 185 / 70 | Ucuz Cevher, High Growth |
| L. Page | İngiltere | OS(M) (CM, CDM, CAM) | Leicester City | 16 | £860k | 61 | 83 | £3k | +22 | — | 3★ | 3★ | 173 / 67 | Ucuz Cevher, High Growth |
| F. Onyeka | Almanya | OS(M) (CAM, CM) | VfL Bochum 1848 | 18 | £666k | 60 | 83 | £5k | +23 | — | 4★ | 3★ | 186 / 72 | Ucuz Cevher, High Growth |
| D. Svensson | İsveç | OS(M) (LB, CM, LM) | Borussia Dortmund | 23 | £12.9M | 77 | 82 | £29k | +5 | — | 4★ | 2★ | 178 / 72 | — |
| F. Lemaréchal | Fransa | OS(M) (CAM, CM) | RC Strasbourg Alsace | 21 | £10.3M | 76 | 82 | £29k | +6 | — | 4★ | 3★ | 180 / 73 | — |
| I. Doukouré | Fransa | OS(M) (CB, CDM, CM) | RC Strasbourg Alsace | 21 | £9.46M | 76 | 82 | £28k | +6 | — | 3★ | 2★ | 183 / 83 | — |
| C. Alcaraz | Arjantin | OS(M) (CAM, CM, ST) | Everton | 22 | £9.89M | 75 | 82 | £28k | +7 | — | 3★ | 4★ | 176 / 70 | — |
| C. Zafeiris | Yunanistan | OS(M) (CM, CDM) | SK Slavia Praha | 22 | £9.89M | 75 | 82 | £20k | +7 | — | 4★ | 4★ | 173 / 75 | — |
| L. Samardžić | Sırbistan | OS(M) (CM, CDM, CAM) | Atalanta | 23 | £9.46M | 75 | 82 | £37k | +7 | — | 3★ | 4★ | 184 / 79 | — |
| M. Al Juwair | Saudi Arabia | OS(M) (CM, CDM, CAM) | Al Qadsiah FC | 22 | £9.89M | 75 | 82 | £23k | +7 | — | 4★ | 3★ | 178 / 70 | — |
| P. Aaronson | ABD | OS(M) (CM, CDM) | Colorado Rapids | 21 | £9.89M | 75 | 82 | £6k | +7 | — | 3★ | 4★ | 175 / 63 | — |
| Y. Ayari | İsveç | OS(M) (CM, CDM) | Brighton & Hove Albion | 21 | £9.89M | 75 | 82 | £43k | +7 | — | 3★ | 3★ | 172 / 69 | — |
| F. Rieder | İsviçre | OS(M) (CAM, CM, RM) | FC Augsburg | 23 | £8.17M | 74 | 82 | £22k | +8 | — | 3★ | 3★ | 179 / 74 | — |
| Fábio Carvalho | Portekiz | OS(M) (CAM, CM, RM) | Brentford | 22 | £8.17M | 74 | 82 | £40k | +8 | — | 4★ | 4★ | 170 / 62 | — |
| Hannibal | Tunisia | OS(M) (CM, CAM) | Burnley | 22 | £8.17M | 74 | 82 | £34k | +8 | — | 3★ | 3★ | 182 / 70 | — |
| J. Breum | Danimarka | OS(M) (CAM, LM, CM) | Go Ahead Eagles | 21 | £8.17M | 74 | 82 | £8k | +8 | — | 2★ | 3★ | 178 / 68 | — |
| K. Danois | Fransa | OS(M) (CM) | AJ Auxerre | 21 | £8.17M | 74 | 82 | £13k | +8 | — | 3★ | 2★ | 183 / 72 | — |
| M. Röhl | Almanya | OS(M) (CAM, CM, CDM, ST) | Everton | 22 | £8.17M | 74 | 82 | £18k | +8 | — | 4★ | 3★ | 192 / 79 | — |
| T. Morton | İngiltere | OS(M) (CDM, CM) | Olympique Lyonnais | 22 | £7.74M | 74 | 82 | £13k | +8 | — | 3★ | 3★ | 185 / 73 | — |
| Y. Musah | ABD | OS(M) (CM, CDM, RM, CAM) | Atalanta | 22 | £8.17M | 74 | 82 | £26k | +8 | — | 3★ | 4★ | 178 / 71 | — |
| A. Lescano | Arjantin | OS(M) (CM, CAM, RW) | Argentinos Juniors | 23 | £5.59M | 73 | 82 | £9k | +9 | — | 3★ | 3★ | 182 / 67 | — |
| C. Jander | Almanya | OS(M) (CM, CAM, CDM) | Southampton | 22 | £6.02M | 73 | 82 | £31k | +9 | — | 4★ | 3★ | 183 / 75 | — |
| H. Hackney | İngiltere | OS(M) (CDM, CM) | Middlesbrough | 23 | £5.59M | 73 | 82 | £20k | +9 | — | 3★ | 3★ | 178 / 70 | — |
| K. Fitz-Jim | Hollanda | OS(M) (CM, CAM) | Ajax | 21 | £6.02M | 73 | 82 | £9k | +9 | — | 3★ | 3★ | 174 / 68 | — |
| L. Ugochukwu | Fransa | OS(M) (CDM, CM) | Burnley | 21 | £5.59M | 73 | 82 | £24k | +9 | — | 3★ | 3★ | 191 / 88 | — |
| M. Galarza | Arjantin | OS(M) (CDM, CM) | Talleres | 23 | £5.59M | 73 | 82 | £9k | +9 | — | 3★ | 2★ | 180 / 71 | — |
| M. Kjaergaard | Danimarka | OS(M) (CM, CDM, CAM) | FC Red Bull Salzburg | 22 | £6.02M | 73 | 82 | £12k | +9 | — | 3★ | 4★ | 192 / 77 | — |
| Paulo Bernardo | Portekiz | OS(M) (CM) | Celtic | 23 | £5.59M | 73 | 82 | £29k | +9 | — | 4★ | 3★ | 184 / 78 | — |
| Peque | İspanya | OS(M) (CAM, LW, ST, CM) | Sevilla FC | 22 | £6.02M | 73 | 82 | £18k | +9 | — | 4★ | 3★ | 172 / 65 | — |
| Turrientes | İspanya | OS(M) (CM, CDM) | Real Sociedad | 23 | £5.59M | 73 | 82 | £21k | +9 | — | 3★ | 2★ | 181 / 70 | — |
| Unai Gómez | İspanya | OS(M) (CAM, CM, LM) | Athletic Club | 22 | £6.02M | 73 | 82 | £22k | +9 | — | 3★ | 3★ | 183 / 74 | — |
| B. Dárdai | Macaristan | OS(M) (CAM, CM) | VfL Wolfsburg | 19 | £4.30M | 72 | 82 | £18k | +10 | — | 3★ | 3★ | 189 / 71 | — |
| D. Tıknaz | Türkiye | OS(M) (CDM, CM, CB) | Beşiktaş JK | 20 | £4.13M | 72 | 82 | £15k | +10 | — | 3★ | 2★ | 193 / 76 | Türk Yeteneği |
| Gabriel Moscardo | Brezilya | OS(M) (CDM, CM) | Sporting Clube de Braga | 19 | £4.13M | 72 | 82 | £26k | +10 | — | 3★ | 3★ | 185 / 73 | — |
| L. Valente | Hollanda | OS(M) (CAM, CM) | Feyenoord | 21 | £4.73M | 72 | 82 | £8k | +10 | — | 3★ | 3★ | 189 / 78 | — |
| M. Amougou | Fransa | OS(M) (CM, CDM) | RC Strasbourg Alsace | 19 | £4.30M | 72 | 82 | £20k | +10 | — | 3★ | 3★ | 177 / 65 | — |
| M. Delorge | Belçika | OS(M) (CM, CDM) | KAA Gent | 20 | £4.30M | 72 | 82 | £8k | +10 | — | 3★ | 2★ | 189 / 70 | — |
| S. Charles | Northern Ireland | OS(M) (CM, CDM) | Southampton | 21 | £4.30M | 72 | 82 | £24k | +10 | — | 3★ | 3★ | 189 / 77 | — |
| Iker Muñoz | İspanya | OS(M) (CM, CDM) | CA Osasuna | 22 | £3.61M | 71 | 82 | £15k | +11 | — | 3★ | 3★ | 180 / 73 | — |
| K. Sano | Japonya | OS(M) (CDM, LM, CM) | NEC Nijmegen | 21 | £3.44M | 71 | 82 | £5k | +11 | — | 3★ | 3★ | 176 / 66 | — |
| M. Del Blanco | Arjantin | OS(M) (LB, CM, LM) | Club Atlético Unión | 21 | £3.44M | 71 | 82 | £5k | +11 | — | 3★ | 3★ | 170 / 68 | — |
| M. Yalcouyé | Mali | OS(M) (CM, RM, CAM, RW) | Swansea City | 19 | £3.44M | 71 | 82 | £28k | +11 | — | 2★ | 3★ | 169 / 69 | — |
| V. Froholdt | Danimarka | OS(M) (CM, CDM, CAM) | FC Porto | 19 | £3.44M | 71 | 82 | £5k | +11 | — | 4★ | 3★ | 180 / 74 | — |
| J. Canvot | Fransa | OS(M) (CB, CDM, CM) | Crystal Palace | 18 | £3.01M | 70 | 82 | £21k | +12 | — | 3★ | 2★ | 188 / 79 | High Growth |
| L. Leroux | Fransa | OS(M) (CM, LB, LM) | FC Nantes | 19 | £3.27M | 70 | 82 | £7k | +12 | — | 2★ | 3★ | 184 / 75 | High Growth |
| N. Sattlberger | Avusturya | OS(M) (CDM, CM) | KRC Genk | 21 | £3.18M | 70 | 82 | £9k | +12 | — | 3★ | 2★ | 191 / 73 | High Growth |
| S. Peck | İngiltere | OS(M) (CDM, CM) | Sheffield United | 20 | £3.10M | 70 | 82 | £18k | +12 | — | 3★ | 2★ | 185 / 75 | High Growth |
| U. Tohumcu | Almanya | OS(M) (CAM, CM) | TSG 1899 Hoffenheim | 20 | £3.27M | 70 | 82 | £12k | +12 | — | 4★ | 3★ | 175 / 71 | High Growth |
| J. Kałuziński | Polonya | OS(M) (CDM, CM, CAM) | Medipol Başakşehir FK | 22 | £2.75M | 69 | 82 | £7k | +13 | — | 3★ | 2★ | 184 / 74 | High Growth |
| T. Fukui | Japonya | OS(M) (CM, CAM, CDM) | FC Arouca | 20 | £2.84M | 69 | 82 | £3k | +13 | — | 3★ | 3★ | 172 / 65 | High Growth |
| M. Kömür | Almanya | OS(M) (CAM, CM) | FC Augsburg | 19 | £2.49M | 68 | 82 | £9k | +14 | — | 4★ | 3★ | 183 / 77 | High Growth |
| C. Yirenkyi | Gana | OS(M) (CM, CDM, CB) | FC Nordsjælland | 19 | £2.06M | 67 | 82 | £4k | +15 | — | 3★ | 2★ | 181 / 73 | High Growth |
| K. Corbanie | Belçika | OS(M) (RB, CDM, CB, CM) | Royal Antwerp FC | 20 | £1.98M | 67 | 82 | £6k | +15 | — | 2★ | 2★ | 187 / 75 | High Growth |
| K. Wätjen | Almanya | OS(M) (CM, CAM, RM) | VfL Bochum 1848 | 19 | £2.06M | 67 | 82 | £9k | +15 | — | 3★ | 3★ | 184 / 72 | High Growth |
| N. Nartey | Danimarka | OS(M) (CM) | Brøndby IF | 19 | £2.06M | 67 | 82 | £4k | +15 | — | 3★ | 2★ | 180 / 74 | High Growth |
| S. Idumbo | Belçika | OS(M) (CAM, LM, RM, CM) | AS Monaco | 20 | £2.15M | 67 | 82 | £8k | +15 | — | 3★ | 3★ | 171 / 61 | High Growth |
| T. Jørgensen | Danimarka | OS(M) (CM) | Viborg FF | 19 | £2.06M | 67 | 82 | £3k | +15 | — | 3★ | 2★ | 177 / 72 | High Growth |
| M. Courcoul | Fransa | OS(M) (CDM, CM, CB) | Angers SCO | 18 | £1.46M | 65 | 82 | £3k | +17 | — | 3★ | 2★ | 182 / 70 | High Growth |
| Y. Saidu | Gana | OS(M) (CM, CB, CDM) | Real Zaragoza | 20 | £1.63M | 65 | 82 | £2k | +17 | — | 4★ | 2★ | 184 / 73 | High Growth |
| J. Meza | Arjantin | OS(M) (CM) | River Plate | 17 | £1.29M | 64 | 82 | £3k | +18 | — | 3★ | 2★ | 183 / 69 | High Growth |
| S. Pnevmonidis | Yunanistan | OS(M) (CAM, LW, ST, CM) | Olympiacos FC | 18 | £1.29M | 64 | 82 | £4k | +18 | — | 3★ | 4★ | 178 / 61 | High Growth |
| T. Parmo | Arjantin | OS(M) (CAM, CM) | Independiente | 17 | £1.29M | 64 | 82 | £2k | +18 | — | 3★ | 3★ | 171 / 68 | High Growth |
| C. Konietzke | İsviçre | OS(M) (CDM, CM) | FC St.Gallen 1879 | 19 | £1.03M | 63 | 82 | £2k | +19 | — | 3★ | 2★ | 185 / 76 | High Growth |
| J. Janssen | Danimarka | OS(M) (CM) | FC Nordsjælland | 18 | £1.03M | 63 | 82 | £3k | +19 | — | 3★ | 2★ | 181 / 72 | High Growth |
| N. Darvich | Almanya | OS(M) (CAM, CM, RM) | VfB Stuttgart | 18 | £946k | 62 | 82 | £4k | +20 | — | 4★ | 4★ | 184 / 73 | High Growth |
| B. Mamuzah Lum | Almanya | OS(M) (CDM, CM) | Hertha BSC | 17 | £645k | 60 | 82 | £1k | +22 | — | 4★ | 2★ | 173 / 66 | High Growth |
| J. Obando | Kolombiya | OS(M) (CAM, CM) | Atlético Nacional | 18 | £666k | 60 | 82 | £3k | +22 | — | 3★ | 3★ | 175 / 70 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Merkez Orta Saha (CM / OS(M)))

- **D. Tıknaz** (Beşiktaş JK) — OVR 72, POT 82: Türk kadrosu için doğal hedef; düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **C. Uzun** (Eintracht Frankfurt) — OVR 74, POT 83: Türk kadrosu için doğal hedef; düşük başlangıç OVR ile gizli cevher profili.
- **K. Yıldız** (Juventus) — OVR 79, POT 89: Türk kadrosu için doğal hedef; güçlü büyüme payı.
- **F. Onyeka** (VfL Bochum 1848) — OVR 60, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **B. Mamuzah Lum** (Hertha BSC) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **J. Obando** (Atlético Nacional) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 7. Ofansif Orta Saha (CAM / OOS)

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J. Bellingham | İngiltere | OOS (CAM, CM) | Real Madrid | 22 | £150M | 90 | 94 | £275k | +4 | Dribbler, Playmaker , Clinical finisher, Comple… | 4★ | 4★ | 186 / 75 | — |
| F. Wirtz | Almanya | OOS (CAM, ST, CM) | Liverpool | 22 | £129M | 89 | 93 | £163k | +4 | Dribbler, Playmaker , Crosser, Acrobat, Complet… | 4★ | 4★ | 177 / 71 | — |
| Pedri | İspanya | OOS (CM, CDM, CAM) | FC Barcelona | 22 | £129M | 89 | 93 | £146k | +4 | Dribbler, Playmaker , Tactician , Acrobat, Comp… | 4★ | 4★ | 174 / 60 | — |
| J. Musiala | Almanya | OOS (CAM, LM, CM, ST) | FC Bayern München | 22 | £115M | 88 | 92 | £95k | +4 | Dribbler, Acrobat, Clinical finisher, Complete … | 4★ | 5★ | 184 / 72 | — |
| C. Palmer | İngiltere | OOS (CAM, RM, ST) | Chelsea | 23 | £93.7M | 87 | 90 | £159k | +3 | Dribbler, Playmaker , Complete midfielder | 3★ | 4★ | 185 / 76 | — |
| Gavi | İspanya | OOS (CM, CAM) | FC Barcelona | 20 | £48.2M | 83 | 89 | £73k | +6 | Dribbler, Acrobat | 3★ | 3★ | 173 / 70 | — |
| A. Güler | Türkiye | OOS (RM, CAM, RW) | Real Madrid | 20 | £48.6M | 81 | 89 | £108k | +8 | — | 3★ | 4★ | 175 / 70 | Türk Yeteneği |
| K. Yıldız | Türkiye | OOS (CAM, LM, LW, CM) | Juventus | 20 | £33.1M | 79 | 89 | £69k | +10 | — | 5★ | 4★ | 185 / 75 | Türk Yeteneği |
| Nico Paz | Arjantin | OOS (CAM, CM) | Como | 20 | £33.1M | 79 | 89 | £58k | +10 | — | 3★ | 4★ | 186 / 81 | — |
| Estêvão | Brezilya | OOS (RM, CAM, RW) | Chelsea | 18 | £25.4M | 78 | 89 | £56k | +11 | Speedster, Acrobat | 2★ | 4★ | 176 / 70 | — |
| Rodrigo Mora | Portekiz | OOS (CAM, LW, CM, ST) | FC Porto | 18 | £15.1M | 76 | 89 | £8k | +13 | — | 4★ | 4★ | 168 / 56 | High Growth |
| H. Ekitiké | Fransa | OOS (ST, CAM) | Liverpool | 23 | £47.7M | 83 | 88 | £103k | +5 | — | 3★ | 4★ | 189 / 70 | — |
| R. Cherki | Fransa | OOS (RW, RM, CAM) | Manchester City | 21 | £45.1M | 81 | 88 | £86k | +7 | Dribbler | 5★ | 5★ | 177 / 71 | — |
| F. Mastantuono | Arjantin | OOS (CAM, RW, ST) | Real Madrid | 17 | £18.9M | 77 | 88 | £59k | +11 | — | 3★ | 3★ | 177 / 71 | — |
| A. Nusa | Norveç | OOS (LM, CAM, LW) | RB Leipzig | 20 | £15.5M | 76 | 88 | £28k | +12 | Acrobat | 4★ | 4★ | 183 / 77 | High Growth |
| X. Simons | Hollanda | OOS (CAM, LM, ST) | Tottenham Hotspur | 22 | £50.3M | 84 | 87 | £108k | +3 | Dribbler, Acrobat | 3★ | 4★ | 179 / 58 | — |
| M. Tillman | ABD | OOS (CAM, LW, CM) | Bayer 04 Leverkusen | 23 | £39.6M | 82 | 87 | £69k | +5 | — | 3★ | 4★ | 187 / 71 | — |
| Fermín | İspanya | OOS (CAM, CM, LW, ST) | FC Barcelona | 22 | £37.0M | 80 | 87 | £69k | +7 | — | 4★ | 3★ | 174 / 64 | — |
| G. Sudakov | Ukrayna | OOS (CAM, CM, CDM) | SL Benfica | 22 | £37.0M | 80 | 87 | £22k | +7 | — | 4★ | 3★ | 177 / 68 | — |
| W. Zaïre-Emery | Fransa | OOS (CM, CDM, CAM) | Paris Saint-Germain | 19 | £35.3M | 80 | 87 | £50k | +7 | — | 4★ | 3★ | 178 / 68 | — |
| A. Vermeeren | Belçika | OOS (CM, CDM, CAM) | Olympique de Marseille | 20 | £19.8M | 77 | 87 | £30k | +10 | — | 4★ | 3★ | 177 / 70 | — |
| L. Bergvall | İsveç | OOS (CM, CDM, CAM) | Tottenham Hotspur | 19 | £19.4M | 77 | 87 | £49k | +10 | — | 3★ | 3★ | 186 / 74 | — |
| K. Smit | Hollanda | OOS (CAM, CM, RM) | AZ Alkmaar | 19 | £4.73M | 72 | 87 | £9k | +15 | — | 4★ | 4★ | 180 / 66 | Hidden Gem, High Growth |
| M. Greenwood | İngiltere | OOS (RM, CAM, RW) | Olympique de Marseille | 23 | £37.4M | 82 | 86 | £40k | +4 | Acrobat | 5★ | 4★ | 181 / 80 | — |
| M. Rogers | İngiltere | OOS (CAM, RM, LM, CM) | Aston Villa | 22 | £38.3M | 82 | 86 | £95k | +4 | — | 4★ | 4★ | 188 / 80 | — |
| K. Adeyemi | Almanya | OOS (RM, LW, CAM, RW) | Borussia Dortmund | 23 | £33.5M | 81 | 86 | £41k | +5 | Speedster, Acrobat | 4★ | 4★ | 180 / 77 | — |
| M. Akliouche | Fransa | OOS (RM, CAM, RW) | AS Monaco | 23 | £28.8M | 80 | 86 | £29k | +6 | — | 3★ | 4★ | 183 / 63 | — |
| Francisco Conceição | Portekiz | OOS (CAM, RM, RW, CM) | Juventus | 22 | £30.5M | 79 | 86 | £82k | +7 | Acrobat | 2★ | 4★ | 168 / 61 | — |
| Moleiro | İspanya | OOS (LM, CAM, LW) | Villarreal CF | 21 | £30.5M | 79 | 86 | £28k | +7 | — | 4★ | 4★ | 171 / 68 | — |
| L. Sučić | Hırvatistan | OOS (CM, CAM) | Real Sociedad | 22 | £27.1M | 78 | 86 | £29k | +8 | — | 3★ | 4★ | 185 / 71 | — |
| M. Tel | Fransa | OOS (ST, LW, CAM) | Tottenham Hotspur | 20 | £20.2M | 77 | 86 | £58k | +9 | — | 4★ | 4★ | 183 / 77 | — |
| T. Bischof | Almanya | OOS (CM, CDM, RM, CAM) | FC Bayern München | 20 | £14.2M | 76 | 86 | £31k | +10 | — | 3★ | 3★ | 176 / 66 | — |
| Y. Bonny | Fransa | OOS (ST, CAM) | Inter | 21 | £14.6M | 76 | 86 | £20k | +10 | — | 3★ | 4★ | 189 / 86 | — |
| J. Bahoya | Fransa | OOS (LM, CAM, LW) | Eintracht Frankfurt | 20 | £10.8M | 75 | 86 | £18k | +11 | Speedster | 3★ | 4★ | 180 / 76 | — |
| C. Echeverri | Arjantin | OOS (CAM, CM, LW) | Bayer 04 Leverkusen | 19 | £8.60M | 74 | 86 | £46k | +12 | Acrobat | 3★ | 3★ | 170 / 65 | High Growth |
| M. Stroeykens | Belçika | OOS (CM, CAM) | RSC Anderlecht | 20 | £8.60M | 74 | 86 | £16k | +12 | — | 3★ | 3★ | 177 / 79 | High Growth |
| L. Sauer | Slovakia | OOS (LW, CAM, LM) | Feyenoord | 19 | £4.73M | 72 | 86 | £8k | +14 | — | 3★ | 4★ | 184 / 74 | Hidden Gem, High Growth |
| M. Carrizo | Arjantin | OOS (RM, CAM, ST, RW) | Vélez Sarsfield | 19 | £4.73M | 72 | 86 | £7k | +14 | — | 3★ | 3★ | 180 / 67 | Hidden Gem, High Growth |
| P. Wanner | Almanya | OOS (CAM, RW, CM) | PSV | 19 | £4.73M | 72 | 86 | £9k | +14 | — | 2★ | 4★ | 185 / 75 | Hidden Gem, High Growth |
| C. Mouzakitis | Yunanistan | OOS (CM, CAM) | Olympiacos FC | 18 | £3.70M | 71 | 86 | £11k | +15 | — | 3★ | 3★ | 175 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| K. Karetsas | Yunanistan | OOS (CAM, RW, CM) | KRC Genk | 17 | £3.44M | 70 | 86 | £7k | +16 | — | 4★ | 3★ | 171 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| S. Nypan | Norveç | OOS (CM, CAM, ST) | Middlesbrough | 18 | £3.01M | 69 | 86 | £25k | +17 | — | 4★ | 4★ | 183 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| L. Karl | Almanya | OOS (CAM, RM, CM) | FC Bayern München | 17 | £1.29M | 63 | 86 | £5k | +23 | — | 3★ | 4★ | 168 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| Amad | Côte d'Ivoire | OOS (CAM, RW, RM, CM) | Manchester United | 22 | £24.1M | 79 | 85 | £64k | +6 | Acrobat | 4★ | 4★ | 173 / 67 | — |
| Marcos Leonardo | Brezilya | OOS (ST, CAM, CM) | Al Hilal | 22 | £24.5M | 79 | 85 | £38k | +6 | — | 4★ | 4★ | 175 / 72 | — |
| M. Soulé | Arjantin | OOS (CAM, RM, CM) | Roma | 22 | £24.5M | 78 | 85 | £39k | +7 | — | 4★ | 4★ | 176 / 69 | — |
| P. Nebel | Almanya | OOS (CAM, CM, RM) | 1. FSV Mainz 05 | 22 | £24.5M | 78 | 85 | £23k | +7 | Acrobat | 4★ | 3★ | 169 / 67 | — |
| E. Ben Seghir | Fas | OOS (LM, CAM, LW) | Bayer 04 Leverkusen | 20 | £14.2M | 76 | 85 | £37k | +9 | — | 3★ | 4★ | 178 / 72 | — |
| Mateus Fernandes | Portekiz | OOS (CAM, CM) | West Ham United | 20 | £14.2M | 76 | 85 | £36k | +9 | — | 4★ | 4★ | 178 / 72 | — |
| O. Gloukh | Israel | OOS (CAM, LW, CM) | Ajax | 21 | £14.6M | 76 | 85 | £12k | +9 | — | 4★ | 4★ | 171 / 68 | — |
| C. Harder | Danimarka | OOS (ST, CAM, LW, CM) | RB Leipzig | 20 | £8.17M | 74 | 85 | £28k | +11 | — | 3★ | 3★ | 185 / 71 | — |
| Gustavo Sá | Portekiz | OOS (CAM, CM) | Famalicão | 20 | £8.17M | 74 | 85 | £8k | +11 | — | 3★ | 3★ | 186 / 80 | — |
| J. Bellingham | İngiltere | OOS (CM, CDM, CAM) | Borussia Dortmund | 19 | £7.74M | 74 | 85 | £21k | +11 | — | 3★ | 3★ | 191 / 75 | — |
| T. Dibling | İngiltere | OOS (RM, RW, CAM) | Everton | 19 | £7.74M | 74 | 85 | £20k | +11 | — | 3★ | 3★ | 186 / 79 | — |
| A. Milambo | Hollanda | OOS (CM, CAM) | Brentford | 20 | £6.45M | 73 | 85 | £30k | +12 | — | 3★ | 4★ | 179 / 68 | High Growth |
| K. Páez | Ekvador | OOS (CAM, RW, CM) | RC Strasbourg Alsace | 18 | £6.02M | 73 | 85 | £40k | +12 | — | 3★ | 4★ | 178 / 71 | High Growth |
| C. Kostoulas | Yunanistan | OOS (ST, CAM, RM) | Brighton & Hove Albion | 18 | £4.73M | 72 | 85 | £33k | +13 | — | 3★ | 3★ | 185 / 75 | Hidden Gem, High Growth |
| L. Miller | Scotland | OOS (CM, CDM, CAM, CB) | Udinese | 18 | £3.70M | 71 | 85 | £7k | +14 | — | 4★ | 2★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| B. Touré | Côte d'Ivoire | OOS (LM, LW, CAM) | TSG 1899 Hoffenheim | 19 | £3.27M | 70 | 85 | £11k | +15 | Speedster | 2★ | 4★ | 175 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Ouédraogo | Almanya | OOS (CAM, CM) | RB Leipzig | 19 | £3.10M | 69 | 85 | £14k | +16 | — | 3★ | 4★ | 191 / 89 | Hidden Gem, Ucuz Cevher, High Growth |
| Alejandro Granados | İspanya | OOS (CM, CAM) | Club Brugge KV | 19 | £1.72M | 65 | 85 | £5k | +20 | — | 4★ | 2★ | 180 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Lerma | Ekvador | OOS (LM, CAM, CM, LW) | Independiente del Valle | 17 | £1.55M | 64 | 85 | £3k | +21 | — | 3★ | 4★ | 176 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Saibari | Fas | OOS (CAM, CM) | PSV | 23 | £22.8M | 79 | 84 | £20k | +5 | — | 4★ | 4★ | 185 / 81 | — |
| João Pedro | Brezilya | OOS (ST, CAM) | Chelsea | 23 | £23.2M | 79 | 84 | £90k | +5 | — | 4★ | 4★ | 188 / 82 | — |
| N. Woltemade | Almanya | OOS (ST, CAM) | Newcastle United | 23 | £23.2M | 79 | 84 | £90k | +5 | Aerial threat | 3★ | 4★ | 199 / 90 | — |
| E. Millot | Fransa | OOS (CAM, CM) | Al Ahli SFC | 22 | £19.4M | 78 | 84 | £32k | +6 | — | 2★ | 4★ | 174 / 66 | — |
| H. Elliott | İngiltere | OOS (CAM, CM, RW) | Aston Villa | 22 | £19.4M | 78 | 84 | £65k | +6 | Acrobat | 3★ | 3★ | 168 / 64 | — |
| H. Haraldsson | Iceland | OOS (CAM, LM, CM) | Lille OSC | 22 | £19.4M | 78 | 84 | £24k | +6 | — | 4★ | 3★ | 178 / 71 | — |
| K. Taylor | Hollanda | OOS (CM, CAM) | Ajax | 23 | £18.9M | 78 | 84 | £15k | +6 | — | 5★ | 3★ | 182 / 73 | — |
| A. Garnacho | Arjantin | OOS (CAM, LW, LM, CM) | Chelsea | 21 | £18.5M | 77 | 84 | £60k | +7 | — | 4★ | 3★ | 180 / 72 | — |
| G. Konstantelias | Yunanistan | OOS (CAM, RW, CM) | PAOK | 22 | £18.5M | 77 | 84 | £24k | +7 | — | 4★ | 4★ | 178 / 66 | — |
| B. El Khannouss | Fas | OOS (CAM, LM, CM) | VfB Stuttgart | 21 | £14.6M | 76 | 84 | £28k | +8 | — | 3★ | 4★ | 180 / 70 | — |
| C. Chukwuemeka | İngiltere | OOS (CAM, CM) | Borussia Dortmund | 21 | £14.6M | 76 | 84 | £25k | +8 | — | 3★ | 4★ | 187 / 77 | — |
| C. Uche | Nijerya | OOS (ST, CAM, CM) | Crystal Palace | 22 | £14.6M | 76 | 84 | £25k | +8 | — | 3★ | 3★ | 190 / 80 | — |
| B. Gruda | Almanya | OOS (CAM, RM, CM) | Brighton & Hove Albion | 21 | £8.17M | 74 | 84 | £40k | +10 | — | 3★ | 4★ | 178 / 70 | — |
| Pablo Torre | İspanya | OOS (CAM, CM) | RCD Mallorca | 22 | £8.17M | 74 | 84 | £20k | +10 | — | 4★ | 4★ | 173 / 63 | — |
| Alvyn Sanches | İsviçre | OOS (CAM, CM, ST) | BSC Young Boys | 22 | £6.02M | 73 | 84 | £14k | +11 | — | 3★ | 4★ | 183 / 68 | — |
| J. Enciso | Paraguay | OOS (CAM, LM, RM, ST) | RC Strasbourg Alsace | 21 | £6.02M | 73 | 84 | £24k | +11 | — | 3★ | 3★ | 173 / 64 | — |
| Pablo Marín | İspanya | OOS (CM, CAM) | Real Sociedad | 21 | £6.02M | 73 | 84 | £17k | +11 | — | 3★ | 3★ | 178 / 71 | — |
| N. Pisilli | İtalya | OOS (CM, CAM) | Roma | 20 | £4.73M | 72 | 84 | £21k | +12 | — | 3★ | 2★ | 180 / 75 | Hidden Gem, High Growth |
| V. Carboni | Arjantin | OOS (CAM, ST, RM, CM) | Genoa | 20 | £4.73M | 72 | 84 | £13k | +12 | — | 3★ | 3★ | 185 / 78 | Hidden Gem, High Growth |
| I. Maza | Cezayir | OOS (CAM, CM) | Bayer 04 Leverkusen | 19 | £3.78M | 71 | 84 | £23k | +13 | — | 3★ | 4★ | 180 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| Luis Guilherme | Brezilya | OOS (RM, LM, CAM, RW) | West Ham United | 19 | £3.78M | 71 | 84 | £22k | +13 | — | 4★ | 4★ | 175 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Devine | İngiltere | OOS (CAM, CM) | Preston North End | 20 | £3.27M | 70 | 84 | £29k | +14 | — | 3★ | 3★ | 182 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| C. Rigg | İngiltere | OOS (CAM, CM) | Sunderland | 18 | £3.18M | 70 | 84 | £17k | +14 | — | 3★ | 3★ | 177 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| N. Weiper | Almanya | OOS (ST, CAM, CM) | 1. FSV Mainz 05 | 20 | £3.35M | 70 | 84 | £11k | +14 | — | 3★ | 3★ | 192 / 83 | Hidden Gem, Ucuz Cevher, High Growth |
| S. El Mala | Almanya | OOS (LM, CAM, LW) | 1. FC Köln | 18 | £2.67M | 68 | 84 | £7k | +16 | — | 4★ | 4★ | 187 / 77 | Hidden Gem, Ucuz Cevher, High Growth |
| S. Pafundi | İtalya | OOS (CAM, CM, ST) | Sampdoria | 19 | £2.67M | 68 | 84 | £5k | +16 | — | 3★ | 3★ | 166 / 64 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Manzambi | İsviçre | OOS (CAM, CM, CDM, ST) | SC Freiburg | 19 | £2.24M | 67 | 84 | £7k | +17 | — | 3★ | 4★ | 183 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| Unai Hernández | İspanya | OOS (LM, CM, CAM, LW) | Al Shabab | 20 | £1.89M | 66 | 84 | £8k | +18 | — | 3★ | 3★ | 171 / 65 | Hidden Gem, Ucuz Cevher, High Growth |
| M. Liberali | İtalya | OOS (RW, RM, CAM) | Catanzaro | 18 | £1.55M | 65 | 84 | £1k | +19 | — | 3★ | 3★ | 169 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| R. Bounida | Belçika | OOS (LW, CAM, LM) | Ajax | 19 | £1.38M | 64 | 84 | £3k | +20 | — | 4★ | 4★ | 179 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| T. Nyoni | İngiltere | OOS (CM, CAM) | Liverpool | 18 | £1.38M | 64 | 84 | £11k | +20 | — | 3★ | 3★ | 180 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| M. Baturina | Hırvatistan | OOS (CAM, CM) | Como | 22 | £18.5M | 78 | 83 | £61k | +5 | — | 4★ | 3★ | 172 / 68 | — |
| S. Steijn | Hollanda | OOS (CAM, CM) | Feyenoord | 23 | £18.1M | 78 | 83 | £14k | +5 | — | 3★ | 3★ | 173 / 59 | — |
| A. Hložek | Czechia | OOS (ST, RM, CAM, RW) | TSG 1899 Hoffenheim | 22 | £14.6M | 77 | 83 | £28k | +6 | — | 4★ | 3★ | 188 / 84 | — |
| Aimar Oroz | İspanya | OOS (CM, CAM, LM) | CA Osasuna | 23 | £14.2M | 77 | 83 | £25k | +6 | — | 3★ | 3★ | 177 / 72 | — |
| G. Rutter | Fransa | OOS (CAM, ST) | Brighton & Hove Albion | 23 | £14.2M | 77 | 83 | £58k | +6 | — | 5★ | 5★ | 182 / 83 | — |
| H. Diarra | Senegal | OOS (CM, CAM) | Sunderland | 21 | £14.6M | 77 | 83 | £34k | +6 | — | 2★ | 2★ | 178 / 75 | — |
| Gabri Veiga | İspanya | OOS (CAM, CM, LM) | FC Porto | 23 | £12.9M | 76 | 83 | £10k | +7 | — | 4★ | 4★ | 184 / 71 | — |
| S. Nanasi | İsveç | OOS (CAM, LM, CM) | RC Strasbourg Alsace | 23 | £12.9M | 76 | 83 | £34k | +7 | — | 3★ | 4★ | 178 / 71 | — |
| A. Schjelderup | Norveç | OOS (LW, CAM, LM) | SL Benfica | 21 | £10.8M | 75 | 83 | £12k | +8 | — | 3★ | 3★ | 176 / 69 | — |
| F. Ivanović | Hırvatistan | OOS (ST, CAM) | SL Benfica | 21 | £10.8M | 75 | 83 | £13k | +8 | — | 3★ | 3★ | 185 / 78 | — |
| Juanlu Sánchez | İspanya | OOS (RB, CAM, RM) | Sevilla FC | 21 | £10.3M | 75 | 83 | £16k | +8 | — | 3★ | 3★ | 186 / 70 | — |
| O. Hutchinson | İngiltere | OOS (CAM, RM, CM) | Nottingham Forest | 21 | £10.8M | 75 | 83 | £44k | +8 | — | 3★ | 3★ | 174 / 65 | — |
| A. Scott | İngiltere | OOS (CAM, CDM, CM) | AFC Bournemouth | 21 | £8.17M | 74 | 83 | £34k | +9 | — | 3★ | 3★ | 178 / 68 | — |
| C. Uzun | Türkiye | OOS (CAM, ST, CM) | Eintracht Frankfurt | 19 | £7.74M | 74 | 83 | £15k | +9 | — | 3★ | 4★ | 186 / 70 | Türk Yeteneği |
| G. Fabbian | İtalya | OOS (CM, CAM) | Bologna | 22 | £8.17M | 74 | 83 | £28k | +9 | — | 4★ | 3★ | 186 / 75 | — |
| M. Šín | Czechia | OOS (CAM, RM, CM) | AZ Alkmaar | 21 | £8.17M | 74 | 83 | £11k | +9 | — | 4★ | 3★ | 180 / 70 | — |
| N. Sadiki | Congo DR | OOS (CM, CDM, CAM) | Sunderland | 20 | £7.74M | 74 | 83 | £28k | +9 | — | 3★ | 2★ | 173 / 77 | — |
| N. O'Reilly | İngiltere | OOS (LB, CM, CAM) | Manchester City | 20 | £5.59M | 73 | 83 | £41k | +10 | — | 2★ | 3★ | 193 / 77 | — |
| G. Prestianni | Arjantin | OOS (RM, CAM, RW) | SL Benfica | 19 | £3.78M | 71 | 83 | £8k | +12 | Acrobat | 3★ | 4★ | 166 / 63 | Ucuz Cevher, High Growth |
| Marlon Gomes | Brezilya | OOS (CM, CAM, CDM) | Shakhtar Donetsk | 21 | £3.96M | 71 | 83 | £9k | +12 | — | 3★ | 3★ | 184 / 72 | Ucuz Cevher, High Growth |
| S. Lencina | Arjantin | OOS (RW, CAM, RM) | River Plate | 19 | £3.78M | 71 | 83 | £9k | +12 | — | 3★ | 3★ | 171 / 65 | Ucuz Cevher, High Growth |
| C. Ndour | İtalya | OOS (CM, CAM, CDM) | Fiorentina | 20 | £3.27M | 70 | 83 | £15k | +13 | — | 4★ | 3★ | 190 / 84 | Ucuz Cevher, High Growth |
| João Simões | Portekiz | OOS (CM, CAM, CDM) | Sporting CP | 18 | £2.75M | 69 | 83 | £5k | +14 | — | 3★ | 3★ | 175 / 71 | Ucuz Cevher, High Growth |
| M. Krattenmacher | Almanya | OOS (CAM, ST, CM) | Hertha BSC | 19 | £2.84M | 69 | 83 | £15k | +14 | — | 5★ | 3★ | 180 / 75 | Ucuz Cevher, High Growth |
| J. King | İngiltere | OOS (CM, CDM, CAM) | Fulham FC | 18 | £2.41M | 68 | 83 | £17k | +15 | — | 4★ | 3★ | 173 / 66 | Ucuz Cevher, High Growth |
| S. Andino | Arjantin | OOS (LM, LW, CAM) | Godoy Cruz | 19 | £2.49M | 68 | 83 | £3k | +15 | — | 3★ | 3★ | 174 / 66 | Ucuz Cevher, High Growth |
| I. Babadi | Hollanda | OOS (CAM, CM, LW) | Royal Antwerp FC | 20 | £2.32M | 67 | 83 | £6k | +16 | — | 4★ | 3★ | 178 / 68 | Ucuz Cevher, High Growth |
| D. Watson | Scotland | OOS (CM, CDM, CAM) | Kilmarnock | 20 | £1.89M | 66 | 83 | £2k | +17 | — | 3★ | 2★ | 175 / 68 | Ucuz Cevher, High Growth |
| Rodri Mendoza | İspanya | OOS (CM, RM, CAM) | Elche CF | 20 | £1.89M | 66 | 83 | £5k | +17 | — | 3★ | 3★ | 182 / 72 | Ucuz Cevher, High Growth |
| V. Tsukanov | Ukrayna | OOS (CM, CAM, RM) | Shakhtar Donetsk | 19 | £1.55M | 65 | 83 | £3k | +18 | — | 3★ | 2★ | 170 / 68 | Ucuz Cevher, High Growth |
| Hugo Pinilla | İspanya | OOS (RM, CAM, LM, RW) | Real Zaragoza | 19 | £1.12M | 62 | 83 | £2k | +21 | — | 3★ | 3★ | 185 / 70 | Ucuz Cevher, High Growth |
| L. Page | İngiltere | OOS (CM, CDM, CAM) | Leicester City | 16 | £860k | 61 | 83 | £3k | +22 | — | 3★ | 3★ | 173 / 67 | Ucuz Cevher, High Growth |
| F. Onyeka | Almanya | OOS (CAM, CM) | VfL Bochum 1848 | 18 | £666k | 60 | 83 | £5k | +23 | — | 4★ | 3★ | 186 / 72 | Ucuz Cevher, High Growth |
| F. Balogun | ABD | OOS (ST, CAM) | AS Monaco | 23 | £13.8M | 77 | 82 | £26k | +5 | — | 4★ | 3★ | 178 / 66 | — |
| F. Lemaréchal | Fransa | OOS (CAM, CM) | RC Strasbourg Alsace | 21 | £10.3M | 76 | 82 | £29k | +6 | — | 4★ | 3★ | 180 / 73 | — |
| Rômulo | Brezilya | OOS (ST, LW, CAM) | RB Leipzig | 23 | £10.3M | 76 | 82 | £36k | +6 | — | 3★ | 3★ | 193 / 80 | — |
| B. Bouanani | Cezayir | OOS (RW, CAM, RM) | VfB Stuttgart | 20 | £9.46M | 75 | 82 | £22k | +7 | — | 3★ | 3★ | 177 / 68 | — |
| C. Alcaraz | Arjantin | OOS (CAM, CM, ST) | Everton | 22 | £9.89M | 75 | 82 | £28k | +7 | — | 3★ | 4★ | 176 / 70 | — |
| Carlos Álvarez | İspanya | OOS (RM, CAM, RW) | Levante UD | 21 | £9.89M | 75 | 82 | £16k | +7 | — | 3★ | 3★ | 168 / 75 | — |
| F. Buonanotte | Arjantin | OOS (RM, CAM, RW) | Chelsea | 20 | £9.46M | 75 | 82 | £43k | +7 | — | 3★ | 3★ | 174 / 66 | — |
| L. Samardžić | Sırbistan | OOS (CM, CDM, CAM) | Atalanta | 23 | £9.46M | 75 | 82 | £37k | +7 | — | 3★ | 4★ | 184 / 79 | — |
| M. Al Juwair | Saudi Arabia | OOS (CM, CDM, CAM) | Al Qadsiah FC | 22 | £9.89M | 75 | 82 | £23k | +7 | — | 4★ | 3★ | 178 / 70 | — |
| S. Esposito | İtalya | OOS (ST, CAM) | Cagliari | 22 | £9.89M | 75 | 82 | £22k | +7 | — | 5★ | 4★ | 183 / 73 | — |
| Y. Asprilla | Kolombiya | OOS (RM, RW, CAM) | Girona FC | 21 | £9.89M | 75 | 82 | £18k | +7 | — | 3★ | 3★ | 175 / 75 | — |
| A. Velasco | Arjantin | OOS (LM, LW, CAM) | Boca Juniors | 22 | £8.17M | 74 | 82 | £13k | +8 | — | 4★ | 4★ | 167 / 63 | — |
| F. Rieder | İsviçre | OOS (CAM, CM, RM) | FC Augsburg | 23 | £8.17M | 74 | 82 | £22k | +8 | — | 3★ | 3★ | 179 / 74 | — |
| Fábio Carvalho | Portekiz | OOS (CAM, CM, RM) | Brentford | 22 | £8.17M | 74 | 82 | £40k | +8 | — | 4★ | 4★ | 170 / 62 | — |
| Hannibal | Tunisia | OOS (CM, CAM) | Burnley | 22 | £8.17M | 74 | 82 | £34k | +8 | — | 3★ | 3★ | 182 / 70 | — |
| J. Breum | Danimarka | OOS (CAM, LM, CM) | Go Ahead Eagles | 21 | £8.17M | 74 | 82 | £8k | +8 | — | 2★ | 3★ | 178 / 68 | — |
| L. Munteanu | Romanya | OOS (ST, CAM) | CFR Cluj | 23 | £8.17M | 74 | 82 | £6k | +8 | Acrobat | 3★ | 3★ | 184 / 80 | — |
| M. Röhl | Almanya | OOS (CAM, CM, CDM, ST) | Everton | 22 | £8.17M | 74 | 82 | £18k | +8 | — | 4★ | 3★ | 192 / 79 | — |
| Y. Musah | ABD | OOS (CM, CDM, RM, CAM) | Atalanta | 22 | £8.17M | 74 | 82 | £26k | +8 | — | 3★ | 4★ | 178 / 71 | — |
| A. Lescano | Arjantin | OOS (CM, CAM, RW) | Argentinos Juniors | 23 | £5.59M | 73 | 82 | £9k | +9 | — | 3★ | 3★ | 182 / 67 | — |
| C. Jander | Almanya | OOS (CM, CAM, CDM) | Southampton | 22 | £6.02M | 73 | 82 | £31k | +9 | — | 4★ | 3★ | 183 / 75 | — |
| H. Igamane | Fas | OOS (ST, LM, CAM) | Lille OSC | 22 | £6.02M | 73 | 82 | £18k | +9 | — | 4★ | 4★ | 181 / 77 | — |
| I. Gharbi | Tunisia | OOS (LM, CAM, LW) | FC Augsburg | 21 | £6.02M | 73 | 82 | £8k | +9 | — | 4★ | 3★ | 173 / 66 | — |
| K. Fitz-Jim | Hollanda | OOS (CM, CAM) | Ajax | 21 | £6.02M | 73 | 82 | £9k | +9 | — | 3★ | 3★ | 174 / 68 | — |
| M. Kjaergaard | Danimarka | OOS (CM, CDM, CAM) | FC Red Bull Salzburg | 22 | £6.02M | 73 | 82 | £12k | +9 | — | 3★ | 4★ | 192 / 77 | — |
| Peque | İspanya | OOS (CAM, LW, ST, CM) | Sevilla FC | 22 | £6.02M | 73 | 82 | £18k | +9 | — | 4★ | 3★ | 172 / 65 | — |
| Unai Gómez | İspanya | OOS (CAM, CM, LM) | Athletic Club | 22 | £6.02M | 73 | 82 | £22k | +9 | — | 3★ | 3★ | 183 / 74 | — |
| B. Dárdai | Macaristan | OOS (CAM, CM) | VfL Wolfsburg | 19 | £4.30M | 72 | 82 | £18k | +10 | — | 3★ | 3★ | 189 / 71 | — |
| L. Valente | Hollanda | OOS (CAM, CM) | Feyenoord | 21 | £4.73M | 72 | 82 | £8k | +10 | — | 3★ | 3★ | 189 / 78 | — |
| J. Recoba | Uruguay | OOS (LW, CAM, ST, LM) | UD Las Palmas | 21 | £3.61M | 71 | 82 | £4k | +11 | — | 3★ | 3★ | 177 / 75 | — |
| M. Yalcouyé | Mali | OOS (CM, RM, CAM, RW) | Swansea City | 19 | £3.44M | 71 | 82 | £28k | +11 | — | 2★ | 3★ | 169 / 69 | — |
| V. Froholdt | Danimarka | OOS (CM, CDM, CAM) | FC Porto | 19 | £3.44M | 71 | 82 | £5k | +11 | — | 4★ | 3★ | 180 / 74 | — |
| R. Esse | İngiltere | OOS (RW, CAM, LW, RM) | Crystal Palace | 20 | £3.27M | 70 | 82 | £27k | +12 | — | 2★ | 3★ | 178 / 65 | High Growth |
| U. Tohumcu | Almanya | OOS (CAM, CM) | TSG 1899 Hoffenheim | 20 | £3.27M | 70 | 82 | £12k | +12 | — | 4★ | 3★ | 175 / 71 | High Growth |
| J. Kałuziński | Polonya | OOS (CDM, CM, CAM) | Medipol Başakşehir FK | 22 | £2.75M | 69 | 82 | £7k | +13 | — | 3★ | 2★ | 184 / 74 | High Growth |
| T. Fukui | Japonya | OOS (CM, CAM, CDM) | FC Arouca | 20 | £2.84M | 69 | 82 | £3k | +13 | — | 3★ | 3★ | 172 / 65 | High Growth |
| M. Kömür | Almanya | OOS (CAM, CM) | FC Augsburg | 19 | £2.49M | 68 | 82 | £9k | +14 | — | 4★ | 3★ | 183 / 77 | High Growth |
| K. Wätjen | Almanya | OOS (CM, CAM, RM) | VfL Bochum 1848 | 19 | £2.06M | 67 | 82 | £9k | +15 | — | 3★ | 3★ | 184 / 72 | High Growth |
| Lucas Ferreira | Brezilya | OOS (RW, LM, CAM, RM) | Shakhtar Donetsk | 19 | £2.06M | 67 | 82 | £6k | +15 | — | 3★ | 3★ | 187 / 74 | High Growth |
| S. Idumbo | Belçika | OOS (CAM, LM, RM, CM) | AS Monaco | 20 | £2.15M | 67 | 82 | £8k | +15 | — | 3★ | 3★ | 171 / 61 | High Growth |
| Sandro Vidigal | Portekiz | OOS (LW, RW, CAM, LM) | Sporting Clube de Braga | 17 | £1.55M | 65 | 82 | £2k | +17 | — | 4★ | 3★ | 179 / 70 | High Growth |
| S. Pnevmonidis | Yunanistan | OOS (CAM, LW, ST, CM) | Olympiacos FC | 18 | £1.29M | 64 | 82 | £4k | +18 | — | 3★ | 4★ | 178 / 61 | High Growth |
| T. Parmo | Arjantin | OOS (CAM, CM) | Independiente | 17 | £1.29M | 64 | 82 | £2k | +18 | — | 3★ | 3★ | 171 / 68 | High Growth |
| K. Alajbegović | Bosnia and Herzegovina | OOS (LM, CAM, LW) | FC Red Bull Salzburg | 17 | £1.03M | 63 | 82 | £2k | +19 | — | 4★ | 3★ | 185 / 70 | High Growth |
| N. Darvich | Almanya | OOS (CAM, CM, RM) | VfB Stuttgart | 18 | £946k | 62 | 82 | £4k | +20 | — | 4★ | 4★ | 184 / 73 | High Growth |
| J. Obando | Kolombiya | OOS (CAM, CM) | Atlético Nacional | 18 | £666k | 60 | 82 | £3k | +22 | — | 3★ | 3★ | 175 / 70 | High Growth |
| P. Villalba | Paraguay | OOS (LM, LW, CAM) | Libertad | 16 | £559k | 58 | 82 | £2k | +24 | — | 3★ | 3★ | 178 / 70 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Ofansif Orta Saha (CAM / OOS))

- **C. Uzun** (Eintracht Frankfurt) — OVR 74, POT 83: Türk kadrosu için doğal hedef; düşük başlangıç OVR ile gizli cevher profili.
- **K. Yıldız** (Juventus) — OVR 79, POT 89: Türk kadrosu için doğal hedef; güçlü büyüme payı.
- **A. Güler** (Real Madrid) — OVR 81, POT 89: Türk kadrosu için doğal hedef.
- **P. Villalba** (Libertad) — OVR 58, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **F. Onyeka** (VfL Bochum 1848) — OVR 60, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **J. Obando** (Atlético Nacional) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 8. Sağ Kanat & Sağ Orta Saha (RM / RW)

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lamine Yamal | İspanya | RM / RW (RM, RW) | FC Barcelona | 17 | £126M | 89 | 95 | £86k | +6 | Dribbler, Crosser, Acrobat | 3★ | 5★ | 180 / 72 | — |
| D. Doué | Fransa | RM / RW (RW, LW, CM, RM) | Paris Saint-Germain | 20 | £71.8M | 85 | 91 | £86k | +6 | Dribbler, Acrobat | 4★ | 5★ | 181 / 79 | — |
| Endrick | Brezilya | RM / RW (ST, RW) | Real Madrid | 18 | £21.1M | 77 | 91 | £82k | +14 | — | 3★ | 4★ | 173 / 66 | High Growth |
| B. Saka | İngiltere | RM / RW (RW, RM) | Arsenal | 23 | £102M | 88 | 90 | £198k | +2 | Dribbler, Crosser | 4★ | 3★ | 178 / 65 | — |
| C. Palmer | İngiltere | RM / RW (CAM, RM, ST) | Chelsea | 23 | £93.7M | 87 | 90 | £159k | +3 | Dribbler, Playmaker , Complete midfielder | 3★ | 4★ | 185 / 76 | — |
| Nico Williams | İspanya | RM / RW (LM, RM, LW) | Athletic Club | 22 | £81.3M | 86 | 89 | £60k | +3 | Speedster, Dribbler, Acrobat | 5★ | 4★ | 181 / 67 | — |
| A. Güler | Türkiye | RM / RW (RM, CAM, RW) | Real Madrid | 20 | £48.6M | 81 | 89 | £108k | +8 | — | 3★ | 4★ | 175 / 70 | Türk Yeteneği |
| Estêvão | Brezilya | RM / RW (RM, CAM, RW) | Chelsea | 18 | £25.4M | 78 | 89 | £56k | +11 | Speedster, Acrobat | 2★ | 4★ | 176 / 70 | — |
| M. Olise | Fransa | RM / RW (RM, RW) | FC Bayern München | 23 | £75.7M | 86 | 88 | £82k | +2 | Dribbler, Acrobat | 2★ | 4★ | 184 / 73 | — |
| B. Barcola | Fransa | RM / RW (LW, RW, LM) | Paris Saint-Germain | 22 | £52.9M | 84 | 88 | £95k | +4 | Acrobat | 4★ | 4★ | 188 / 70 | — |
| R. Cherki | Fransa | RM / RW (RW, RM, CAM) | Manchester City | 21 | £45.1M | 81 | 88 | £86k | +7 | Dribbler | 5★ | 5★ | 177 / 71 | — |
| Yeremy Pino | İspanya | RM / RW (RM, LM, LW, RW) | Crystal Palace | 22 | £40.9M | 80 | 88 | £66k | +8 | — | 4★ | 3★ | 172 / 65 | — |
| F. Mastantuono | Arjantin | RM / RW (CAM, RW, ST) | Real Madrid | 17 | £18.9M | 77 | 88 | £59k | +11 | — | 3★ | 3★ | 177 / 71 | — |
| Geovany Quenda | Portekiz | RM / RW (RM, LM, LW, RW) | Sporting CP | 18 | £15.1M | 76 | 88 | £10k | +12 | — | 4★ | 4★ | 172 / 71 | High Growth |
| G. Read | Hollanda | RM / RW (RB, RM) | Feyenoord | 19 | £11.2M | 75 | 88 | £9k | +13 | — | 3★ | 3★ | 183 / 70 | High Growth |
| Savinho | Brezilya | RM / RW (RW, LW, RM) | Manchester City | 21 | £40.4M | 82 | 87 | £95k | +5 | Dribbler, Acrobat | 2★ | 4★ | 176 / 71 | — |
| A. Diao | Senegal | RM / RW (LM, RM, LW) | Como | 19 | £13.8M | 76 | 87 | £42k | +11 | Speedster | 4★ | 4★ | 185 / 72 | — |
| E. Nwaneri | İngiltere | RM / RW (RW, CM, RM) | Arsenal | 18 | £13.8M | 76 | 87 | £58k | +11 | — | 3★ | 3★ | 176 / 70 | — |
| J. Duranville | Belçika | RM / RW (RM, LM, ST, RW) | Borussia Dortmund | 19 | £4.73M | 72 | 87 | £17k | +15 | Dribbler, Acrobat | 3★ | 5★ | 170 / 67 | Hidden Gem, High Growth |
| K. Smit | Hollanda | RM / RW (CAM, CM, RM) | AZ Alkmaar | 19 | £4.73M | 72 | 87 | £9k | +15 | — | 4★ | 4★ | 180 / 66 | Hidden Gem, High Growth |
| Pablo García | İspanya | RM / RW (RM, ST, LM, RW) | Real Betis Balompié | 18 | £2.67M | 68 | 87 | £7k | +19 | — | 3★ | 3★ | 175 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| M. Greenwood | İngiltere | RM / RW (RM, CAM, RW) | Olympique de Marseille | 23 | £37.4M | 82 | 86 | £40k | +4 | Acrobat | 5★ | 4★ | 181 / 80 | — |
| M. Rogers | İngiltere | RM / RW (CAM, RM, LM, CM) | Aston Villa | 22 | £38.3M | 82 | 86 | £95k | +4 | — | 4★ | 4★ | 188 / 80 | — |
| G. Simeone | Arjantin | RM / RW (RM, ST, LM, RW) | Atlético Madrid | 22 | £34.0M | 81 | 86 | £54k | +5 | Speedster | 3★ | 3★ | 173 / 75 | — |
| K. Adeyemi | Almanya | RM / RW (RM, LW, CAM, RW) | Borussia Dortmund | 23 | £33.5M | 81 | 86 | £41k | +5 | Speedster, Acrobat | 4★ | 4★ | 180 / 77 | — |
| M. Akliouche | Fransa | RM / RW (RM, CAM, RW) | AS Monaco | 23 | £28.8M | 80 | 86 | £29k | +6 | — | 3★ | 4★ | 183 / 63 | — |
| T. Livramento | İngiltere | RM / RW (RB, LB, RM) | Newcastle United | 22 | £27.1M | 80 | 86 | £82k | +6 | — | 4★ | 3★ | 181 / 71 | — |
| Francisco Conceição | Portekiz | RM / RW (CAM, RM, RW, CM) | Juventus | 22 | £30.5M | 79 | 86 | £82k | +7 | Acrobat | 2★ | 4★ | 168 / 61 | — |
| Diego López | İspanya | RM / RW (LM, RM, LW) | Valencia CF | 23 | £26.7M | 78 | 86 | £29k | +8 | — | 4★ | 3★ | 172 / 63 | — |
| Tomás Araújo | Portekiz | RM / RW (CB, RB, RM) | SL Benfica | 23 | £24.9M | 78 | 86 | £15k | +8 | — | 2★ | 3★ | 187 / 81 | — |
| Asencio | İspanya | RM / RW (CB, RB, RM) | Real Madrid | 22 | £18.9M | 77 | 86 | £90k | +9 | — | 3★ | 2★ | 184 / 79 | — |
| T. Bischof | Almanya | RM / RW (CM, CDM, RM, CAM) | FC Bayern München | 20 | £14.2M | 76 | 86 | £31k | +10 | — | 3★ | 3★ | 176 / 66 | — |
| A. Gray | İngiltere | RM / RW (CDM, CB, RB, RM) | Tottenham Hotspur | 19 | £9.89M | 75 | 86 | £41k | +11 | — | 4★ | 2★ | 187 / 70 | — |
| L. Rodríguez | Uruguay | RM / RW (RW, RM, ST) | NEOM SC | 21 | £9.03M | 74 | 86 | £14k | +12 | — | 4★ | 3★ | 179 / 71 | High Growth |
| C. Talbi | Fas | RM / RW (RM, LM, RW) | Sunderland | 20 | £6.45M | 73 | 86 | £26k | +13 | Speedster | 4★ | 3★ | 175 / 64 | High Growth |
| J. Seys | Belçika | RM / RW (RB, LB, RM) | Club Brugge KV | 20 | £6.02M | 73 | 86 | £14k | +13 | — | 4★ | 2★ | 178 / 63 | High Growth |
| M. Carrizo | Arjantin | RM / RW (RM, CAM, ST, RW) | Vélez Sarsfield | 19 | £4.73M | 72 | 86 | £7k | +14 | — | 3★ | 3★ | 180 / 67 | Hidden Gem, High Growth |
| P. Wanner | Almanya | RM / RW (CAM, RW, CM) | PSV | 19 | £4.73M | 72 | 86 | £9k | +14 | — | 2★ | 4★ | 185 / 75 | Hidden Gem, High Growth |
| João Costa | Brezilya | RM / RW (RM, LM, LB, RB) | Al Ettifaq | 20 | £3.87M | 71 | 86 | £12k | +15 | — | 3★ | 3★ | 178 / 69 | Hidden Gem, Ucuz Cevher, High Growth |
| K. Karetsas | Yunanistan | RM / RW (CAM, RW, CM) | KRC Genk | 17 | £3.44M | 70 | 86 | £7k | +16 | — | 4★ | 3★ | 171 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| L. Karl | Almanya | RM / RW (CAM, RM, CM) | FC Bayern München | 17 | £1.29M | 63 | 86 | £5k | +23 | — | 3★ | 4★ | 168 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Doku | Belçika | RM / RW (LW, RW, LM) | Manchester City | 23 | £27.5M | 80 | 85 | £95k | +5 | Speedster, Dribbler, Acrobat | 3★ | 4★ | 173 / 66 | — |
| Amad | Côte d'Ivoire | RM / RW (CAM, RW, RM, CM) | Manchester United | 22 | £24.1M | 79 | 85 | £64k | +6 | Acrobat | 4★ | 4★ | 173 / 67 | — |
| J. Bakayoko | Belçika | RM / RW (RW, RM) | RB Leipzig | 22 | £24.5M | 78 | 85 | £40k | +7 | — | 3★ | 4★ | 179 / 76 | — |
| M. Soulé | Arjantin | RM / RW (CAM, RM, CM) | Roma | 22 | £24.5M | 78 | 85 | £39k | +7 | — | 4★ | 4★ | 176 / 69 | — |
| P. Nebel | Almanya | RM / RW (CAM, CM, RM) | 1. FSV Mainz 05 | 22 | £24.5M | 78 | 85 | £23k | +7 | Acrobat | 4★ | 3★ | 169 / 67 | — |
| J. Aramburu | Venezuela | RM / RW (RB, RM) | Real Sociedad | 22 | £19.4M | 77 | 85 | £26k | +8 | — | 3★ | 2★ | 176 / 71 | — |
| Wesley | Brezilya | RM / RW (RB, RM) | Roma | 21 | £19.4M | 77 | 85 | £28k | +8 | Acrobat | 3★ | 3★ | 178 / 75 | — |
| Y. Minteh | Gambia | RM / RW (RM, RW) | Brighton & Hove Albion | 20 | £19.8M | 77 | 85 | £48k | +8 | Speedster, Acrobat | 3★ | 4★ | 180 / 65 | — |
| Roger Fernandes | Portekiz | RM / RW (RM, LM, RW) | Al Ittihad | 19 | £13.8M | 76 | 85 | £22k | +9 | Acrobat | 4★ | 3★ | 166 / 65 | — |
| Martim Fernandes | Portekiz | RM / RW (RB, RM) | FC Porto | 19 | £9.89M | 75 | 85 | £8k | +10 | — | 2★ | 2★ | 181 / 73 | — |
| Jesús Rodríguez | İspanya | RM / RW (LM, RM, LW) | Como | 19 | £7.74M | 74 | 85 | £37k | +11 | — | 3★ | 3★ | 185 / 68 | — |
| S. Mouriño | Uruguay | RM / RW (CB, RB, RM) | Villarreal CF | 23 | £7.31M | 74 | 85 | £22k | +11 | — | 3★ | 2★ | 183 / 76 | — |
| T. Dibling | İngiltere | RM / RW (RM, RW, CAM) | Everton | 19 | £7.74M | 74 | 85 | £20k | +11 | — | 3★ | 3★ | 186 / 79 | — |
| K. Páez | Ekvador | RM / RW (CAM, RW, CM) | RC Strasbourg Alsace | 18 | £6.02M | 73 | 85 | £40k | +12 | — | 3★ | 4★ | 178 / 71 | High Growth |
| C. Kostoulas | Yunanistan | RM / RW (ST, CAM, RM) | Brighton & Hove Albion | 18 | £4.73M | 72 | 85 | £33k | +13 | — | 3★ | 3★ | 185 / 75 | Hidden Gem, High Growth |
| B. Gannon-Doak | Scotland | RM / RW (RM, RW) | AFC Bournemouth | 19 | £3.78M | 71 | 85 | £23k | +14 | — | 4★ | 4★ | 176 / 64 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Acheampong | İngiltere | RM / RW (RB, CB, CDM, RM) | Chelsea | 19 | £3.10M | 70 | 85 | £28k | +15 | — | 3★ | 2★ | 190 / 85 | Hidden Gem, Ucuz Cevher, High Growth |
| Antoñito Cordero | İspanya | RM / RW (LW, RW, LM) | KVC Westerlo | 18 | £3.01M | 69 | 85 | £28k | +16 | — | 3★ | 4★ | 178 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Subiabre | Arjantin | RM / RW (LW, RW, ST, LM) | River Plate | 18 | £3.01M | 69 | 85 | £6k | +16 | — | 3★ | 3★ | 171 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| T. Gomis | Fransa | RM / RW (LM, RM, ST, LW) | RB Leipzig | 18 | £2.67M | 68 | 85 | £11k | +17 | — | 3★ | 4★ | 183 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| A. Elanga | İsveç | RM / RW (RW, RM) | Newcastle United | 23 | £30.1M | 81 | 84 | £99k | +3 | Speedster | 5★ | 3★ | 178 / 70 | — |
| N. Madueke | İngiltere | RM / RW (RW, RM) | Arsenal | 23 | £25.8M | 80 | 84 | £99k | +4 | — | 3★ | 4★ | 182 / 75 | — |
| Arnau Martínez | İspanya | RM / RW (RB, RM, CB, RW) | Girona FC | 22 | £21.5M | 79 | 84 | £26k | +5 | — | 3★ | 2★ | 182 / 72 | — |
| M. Beier | Almanya | RM / RW (ST, RM, LM, RW) | Borussia Dortmund | 22 | £23.6M | 79 | 84 | £40k | +5 | — | 3★ | 4★ | 185 / 72 | — |
| M. Gusto | Fransa | RM / RW (RB, RM) | Chelsea | 22 | £21.5M | 79 | 84 | £77k | +5 | — | 3★ | 3★ | 178 / 74 | — |
| C. Bradley | Northern Ireland | RM / RW (RB, RM) | Liverpool | 21 | £18.1M | 78 | 84 | £52k | +6 | — | 3★ | 3★ | 181 / 75 | — |
| D. Bakwa | Fransa | RM / RW (RM, RW) | Nottingham Forest | 22 | £19.4M | 78 | 84 | £60k | +6 | — | 2★ | 4★ | 180 / 75 | — |
| H. Elliott | İngiltere | RM / RW (CAM, CM, RW) | Aston Villa | 22 | £19.4M | 78 | 84 | £65k | +6 | Acrobat | 3★ | 3★ | 168 / 64 | — |
| Eduardo Quaresma | Portekiz | RM / RW (CB, RB, RM) | Sporting CP | 23 | £16.8M | 77 | 84 | £14k | +7 | — | 3★ | 3★ | 184 / 79 | — |
| G. Konstantelias | Yunanistan | RM / RW (CAM, RW, CM) | PAOK | 22 | £18.5M | 77 | 84 | £24k | +7 | — | 4★ | 4★ | 178 / 66 | — |
| Carmona | İspanya | RM / RW (RB, RM, RW) | Sevilla FC | 23 | £13.8M | 76 | 84 | £21k | +8 | — | 3★ | 3★ | 183 / 80 | — |
| Raúl Moro | İspanya | RM / RW (LW, RW, LM) | Ajax | 22 | £14.6M | 76 | 84 | £15k | +8 | — | 3★ | 3★ | 169 / 67 | — |
| Yeremay | İspanya | RM / RW (LM, RM, LW) | RC Deportivo de La Coruña | 22 | £14.6M | 76 | 84 | £7k | +8 | Acrobat | 3★ | 4★ | 170 / 61 | — |
| M. Fernandez-Pardo | İspanya | RM / RW (LM, RM, LW) | Lille OSC | 20 | £10.8M | 75 | 84 | £16k | +9 | — | 3★ | 3★ | 188 / 77 | — |
| B. Gruda | Almanya | RM / RW (CAM, RM, CM) | Brighton & Hove Albion | 21 | £8.17M | 74 | 84 | £40k | +10 | — | 3★ | 4★ | 178 / 70 | — |
| N. Collins | Almanya | RM / RW (CB, RB, RM) | Eintracht Frankfurt | 21 | £7.74M | 74 | 84 | £15k | +10 | — | 3★ | 2★ | 191 / 84 | — |
| A. Khalaili | Israel | RM / RW (RM, RB, RW) | Union Saint-Gilloise | 20 | £5.59M | 73 | 84 | £11k | +11 | — | 4★ | 4★ | 183 / 77 | — |
| J. Enciso | Paraguay | RM / RW (CAM, LM, RM, ST) | RC Strasbourg Alsace | 21 | £6.02M | 73 | 84 | £24k | +11 | — | 3★ | 3★ | 173 / 64 | — |
| E. Baum | Almanya | RM / RW (RB, RM) | Eintracht Frankfurt | 19 | £4.73M | 72 | 84 | £12k | +12 | — | 3★ | 2★ | 180 / 73 | Hidden Gem, High Growth |
| I. Osman | Gana | RM / RW (LM, RM, LW) | AJ Auxerre | 20 | £4.73M | 72 | 84 | £33k | +12 | Speedster | 2★ | 3★ | 178 / 63 | Hidden Gem, High Growth |
| V. Carboni | Arjantin | RM / RW (CAM, ST, RM, CM) | Genoa | 20 | £4.73M | 72 | 84 | £13k | +12 | — | 3★ | 3★ | 185 / 78 | Hidden Gem, High Growth |
| K. Sabbe | Belçika | RM / RW (RB, LB, RM) | Club Brugge KV | 20 | £3.70M | 71 | 84 | £11k | +13 | — | 3★ | 2★ | 172 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| Luis Guilherme | Brezilya | RM / RW (RM, LM, CAM, RW) | West Ham United | 19 | £3.78M | 71 | 84 | £22k | +13 | — | 4★ | 4★ | 175 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| T. George | İngiltere | RM / RW (LM, RM, ST, LW) | Chelsea | 19 | £3.78M | 71 | 84 | £34k | +13 | — | 4★ | 4★ | 185 / 80 | Hidden Gem, Ucuz Cevher, High Growth |
| Pau Sans | İspanya | RM / RW (RM, LM, ST, RW) | Real Zaragoza | 20 | £3.27M | 70 | 84 | £4k | +14 | — | 3★ | 3★ | 177 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| Yang Min Hyeok | Korea Republic | RM / RW (RM, RW, LM) | Portsmouth | 19 | £3.27M | 70 | 84 | £27k | +14 | — | 3★ | 3★ | 171 / 61 | Hidden Gem, Ucuz Cevher, High Growth |
| E. Bajraktarević | Bosnia and Herzegovina | RM / RW (RW, RM) | PSV | 20 | £2.32M | 67 | 84 | £6k | +17 | — | 2★ | 4★ | 175 / 64 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Addai | Hollanda | RM / RW (RM, RW) | Como | 19 | £2.24M | 67 | 84 | £17k | +17 | — | 2★ | 4★ | 175 / 73 | Hidden Gem, Ucuz Cevher, High Growth |
| M. Liberali | İtalya | RM / RW (RW, RM, CAM) | Catanzaro | 18 | £1.55M | 65 | 84 | £1k | +19 | — | 3★ | 3★ | 169 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| B. Durdov | Hırvatistan | RM / RW (RW, RM) | Hajduk Split | 17 | £1.38M | 64 | 84 | £3k | +20 | — | 4★ | 3★ | 175 / 65 | Hidden Gem, Ucuz Cevher, High Growth |
| Dani Díaz | İspanya | RM / RW (RM, ST, RW) | Real Sociedad de Fútbol B | 19 | £1.29M | 63 | 84 | £1k | +21 | — | 3★ | 3★ | 165 / 58 | Hidden Gem, Ucuz Cevher, High Growth |
| F. Curtis | Scotland | RM / RW (LW, RW, LM) | Rangers FC | 18 | £1.29M | 63 | 84 | £8k | +21 | — | 3★ | 3★ | 180 / 66 | Hidden Gem, Ucuz Cevher, High Growth |
| S. Renders | Belçika | RM / RW (RB, RM) | Royal Antwerp FC | 17 | £1.03M | 62 | 84 | £2k | +22 | — | 3★ | 2★ | 176 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| Luis Henrique | Brezilya | RM / RW (RM, LM, RW) | Inter | 23 | £18.1M | 78 | 83 | £24k | +5 | — | 3★ | 3★ | 181 / 85 | — |
| A. Hložek | Czechia | RM / RW (ST, RM, CAM, RW) | TSG 1899 Hoffenheim | 22 | £14.6M | 77 | 83 | £28k | +6 | — | 4★ | 3★ | 188 / 84 | — |
| Bryan Zaragoza | İspanya | RM / RW (LM, LW, RM) | RC Celta | 23 | £14.2M | 77 | 83 | £39k | +6 | Acrobat | 4★ | 4★ | 164 / 60 | — |
| Diego Moreira | Belçika | RM / RW (LM, LB, RM) | RC Strasbourg Alsace | 20 | £14.2M | 77 | 83 | £31k | +6 | — | 3★ | 4★ | 179 / 73 | — |
| O. El Hilali | Fas | RM / RW (RB, CB, RM) | RCD Espanyol | 21 | £13.8M | 77 | 83 | £14k | +6 | — | 3★ | 3★ | 183 / 75 | — |
| Tiago Santos | Portekiz | RM / RW (RB, RM) | Lille OSC | 22 | £13.8M | 77 | 83 | £21k | +6 | — | 3★ | 3★ | 175 / 71 | — |
| A. Fatawu | Gana | RM / RW (RM, RW) | Leicester City | 21 | £12.9M | 76 | 83 | £27k | +7 | — | 4★ | 4★ | 177 / 73 | — |
| M. Cho | Fransa | RM / RW (LW, RW, ST, LM) | OGC Nice | 21 | £12.9M | 76 | 83 | £18k | +7 | — | 3★ | 3★ | 181 / 66 | — |
| S. Adingra | Côte d'Ivoire | RM / RW (RM, LM, RW) | Sunderland | 23 | £12.9M | 76 | 83 | £38k | +7 | — | 3★ | 3★ | 175 / 68 | — |
| Z. El Ouahdi | Fas | RM / RW (RB, RM, RW) | KRC Genk | 23 | £12.5M | 76 | 83 | £17k | +7 | — | 3★ | 3★ | 172 / 66 | — |
| B. Traoré | Côte d'Ivoire | RM / RW (LM, RM, LW) | FC Basel 1893 | 22 | £10.8M | 75 | 83 | £16k | +8 | Acrobat | 3★ | 4★ | 172 / 64 | — |
| J. Hinshelwood | İngiltere | RM / RW (CDM, RB, LB, RM) | Brighton & Hove Albion | 20 | £9.89M | 75 | 83 | £40k | +8 | — | 4★ | 3★ | 181 / 76 | — |
| Juanlu Sánchez | İspanya | RM / RW (RB, CAM, RM) | Sevilla FC | 21 | £10.3M | 75 | 83 | £16k | +8 | — | 3★ | 3★ | 186 / 70 | — |
| O. Hutchinson | İngiltere | RM / RW (CAM, RM, CM) | Nottingham Forest | 21 | £10.8M | 75 | 83 | £44k | +8 | — | 3★ | 3★ | 174 / 65 | — |
| W. Odobert | Fransa | RM / RW (LW, RW, LM) | Tottenham Hotspur | 20 | £10.8M | 75 | 83 | £51k | +8 | — | 4★ | 3★ | 182 / 75 | — |
| A. Zakharyan | Russia | RM / RW (RM, CM, LM, RW) | Real Sociedad | 22 | £8.17M | 74 | 83 | £22k | +9 | — | 4★ | 3★ | 182 / 73 | — |
| E. Zeballos | Arjantin | RM / RW (RM, RW, LW) | Boca Juniors | 23 | £8.17M | 74 | 83 | £13k | +9 | Acrobat | 3★ | 5★ | 175 / 68 | — |
| Gabriel Silva | Brezilya | RM / RW (LW, ST, RM, LM) | Santa Clara | 23 | £8.17M | 74 | 83 | £8k | +9 | Speedster | 3★ | 3★ | 177 / 69 | — |
| I. Akhomach | Fas | RM / RW (RM, RW, LW) | Villarreal CF | 21 | £8.17M | 74 | 83 | £19k | +9 | — | 4★ | 4★ | 175 / 70 | — |
| M. Rosenfelder | Almanya | RM / RW (CB, RB, RM) | SC Freiburg | 22 | £7.74M | 74 | 83 | £17k | +9 | — | 3★ | 3★ | 186 / 76 | — |
| M. Šín | Czechia | RM / RW (CAM, RM, CM) | AZ Alkmaar | 21 | £8.17M | 74 | 83 | £11k | +9 | — | 4★ | 3★ | 180 / 70 | — |
| W. Gnonto | İtalya | RM / RW (RM, LM, RW) | Leeds United | 21 | £8.17M | 74 | 83 | £28k | +9 | — | 4★ | 3★ | 169 / 72 | — |
| Óscar Aranda | İspanya | RM / RW (LM, ST, RM, LW) | Famalicão | 23 | £8.17M | 74 | 83 | £9k | +9 | — | 4★ | 4★ | 181 / 78 | — |
| C. Bonsu Baah | Gana | RM / RW (LM, RM, LW) | Al Qadsiah FC | 20 | £5.59M | 73 | 83 | £16k | +10 | — | 3★ | 4★ | 172 / 73 | — |
| Kaio César | Brezilya | RM / RW (RM, RW) | Al Hilal | 21 | £6.02M | 73 | 83 | £19k | +10 | Acrobat | 3★ | 5★ | 167 / 66 | — |
| Miguel Rodríguez | İspanya | RM / RW (RW, RM) | FC Utrecht | 22 | £6.02M | 73 | 83 | £9k | +10 | — | 3★ | 3★ | 178 / 73 | — |
| G. Diarra | Mali | RM / RW (LW, RW, LM) | Feyenoord | 22 | £4.73M | 72 | 83 | £9k | +11 | — | 3★ | 3★ | 183 / 74 | — |
| K. Nedeljković | Sırbistan | RM / RW (RB, RM) | RB Leipzig | 19 | £4.13M | 72 | 83 | £34k | +11 | — | 2★ | 2★ | 184 / 72 | Ucuz Cevher |
| Patati | Brezilya | RM / RW (RM, LM, RW) | AZ Alkmaar | 21 | £4.73M | 72 | 83 | £9k | +11 | — | 3★ | 4★ | 173 / 59 | — |
| G. Prestianni | Arjantin | RM / RW (RM, CAM, RW) | SL Benfica | 19 | £3.78M | 71 | 83 | £8k | +12 | Acrobat | 3★ | 4★ | 166 / 63 | Ucuz Cevher, High Growth |
| S. Lencina | Arjantin | RM / RW (RW, CAM, RM) | River Plate | 19 | £3.78M | 71 | 83 | £9k | +12 | — | 3★ | 3★ | 171 / 65 | Ucuz Cevher, High Growth |
| L. Koumas | Wales | RM / RW (RM, LM, RW) | Birmingham City | 19 | £2.84M | 69 | 83 | £23k | +14 | — | 4★ | 3★ | 182 / 68 | Ucuz Cevher, High Growth |
| M. Young | Hollanda | RM / RW (CB, RB, RM) | Sparta Rotterdam | 19 | £2.67M | 69 | 83 | £3k | +14 | — | 3★ | 2★ | 182 / 78 | Ucuz Cevher, High Growth |
| I. Mbaye | Fransa | RM / RW (RW, LW, RM) | Paris Saint-Germain | 17 | £2.41M | 68 | 83 | £15k | +15 | — | 3★ | 3★ | 176 / 65 | Ucuz Cevher, High Growth |
| N. Wurmbrand | Avusturya | RM / RW (RM, ST, RW) | SK Rapid | 19 | £2.49M | 68 | 83 | £5k | +15 | — | 4★ | 3★ | 172 / 75 | Ucuz Cevher, High Growth |
| Pedro Lima | Brezilya | RM / RW (RB, RM) | FC Porto | 19 | £2.32M | 68 | 83 | £15k | +15 | — | 2★ | 3★ | 178 / 57 | Ucuz Cevher, High Growth |
| Rodri Mendoza | İspanya | RM / RW (CM, RM, CAM) | Elche CF | 20 | £1.89M | 66 | 83 | £5k | +17 | — | 3★ | 3★ | 182 / 72 | Ucuz Cevher, High Growth |
| V. Tsukanov | Ukrayna | RM / RW (CM, CAM, RM) | Shakhtar Donetsk | 19 | £1.55M | 65 | 83 | £3k | +18 | — | 3★ | 2★ | 170 / 68 | Ucuz Cevher, High Growth |
| C. Donovan | Scotland | RM / RW (RB, CB, RM) | Celtic | 18 | £1.20M | 64 | 83 | £7k | +19 | — | 3★ | 3★ | 180 / 76 | Ucuz Cevher, High Growth |
| Toni Fernández | İspanya | RM / RW (RW, RM) | FC Barcelona | 16 | £1.29M | 64 | 83 | £9k | +19 | — | 2★ | 4★ | 176 / 75 | Ucuz Cevher, High Growth |
| Arturo | İspanya | RM / RW (RW, LW, RM) | UD Las Palmas | 18 | £1.12M | 63 | 83 | £1k | +20 | — | 3★ | 3★ | 176 / 69 | Ucuz Cevher, High Growth |
| Pablo López | İspanya | RM / RW (RW, LW, RM) | CD Mirandés | 19 | £1.12M | 63 | 83 | £5k | +20 | — | 3★ | 3★ | 175 / 65 | Ucuz Cevher, High Growth |
| Hugo Pinilla | İspanya | RM / RW (RM, CAM, LM, RW) | Real Zaragoza | 19 | £1.12M | 62 | 83 | £2k | +21 | — | 3★ | 3★ | 185 / 70 | Ucuz Cevher, High Growth |
| G. Doué | Côte d'Ivoire | RM / RW (RB, CB, RM) | RC Strasbourg Alsace | 22 | £12.9M | 77 | 82 | £34k | +5 | — | 3★ | 3★ | 187 / 84 | — |
| Yan Couto | Brezilya | RM / RW (RB, RM) | Borussia Dortmund | 23 | £12.9M | 77 | 82 | £29k | +5 | — | 3★ | 4★ | 168 / 60 | — |
| A. Hadj-Moussa | Cezayir | RM / RW (RW, RM) | Feyenoord | 23 | £10.3M | 76 | 82 | £13k | +6 | Dribbler, Acrobat | 3★ | 5★ | 176 / 72 | — |
| Hugo Álvarez | İspanya | RM / RW (LM, RM, LW) | RC Celta | 21 | £10.3M | 76 | 82 | £17k | +6 | — | 3★ | 3★ | 176 / 72 | — |
| M. Abline | Fransa | RM / RW (ST, RW, RM) | FC Nantes | 22 | £10.3M | 76 | 82 | £15k | +6 | — | 3★ | 3★ | 182 / 81 | — |
| B. Bouanani | Cezayir | RM / RW (RW, CAM, RM) | VfB Stuttgart | 20 | £9.46M | 75 | 82 | £22k | +7 | — | 3★ | 3★ | 177 / 68 | — |
| Carlos Álvarez | İspanya | RM / RW (RM, CAM, RW) | Levante UD | 21 | £9.89M | 75 | 82 | £16k | +7 | — | 3★ | 3★ | 168 / 75 | — |
| E. Nuamah | Gana | RM / RW (RM, RW) | Olympique Lyonnais | 21 | £9.89M | 75 | 82 | £12k | +7 | — | 3★ | 4★ | 178 / 71 | — |
| F. Buonanotte | Arjantin | RM / RW (RM, CAM, RW) | Chelsea | 20 | £9.46M | 75 | 82 | £43k | +7 | — | 3★ | 3★ | 174 / 66 | — |
| Francés | İspanya | RM / RW (CB, RB, LB, RM) | Girona FC | 22 | £9.03M | 75 | 82 | £20k | +7 | — | 4★ | 2★ | 181 / 70 | — |
| J. Rowe | İngiltere | RM / RW (LM, RM, LW) | Bologna | 22 | £9.89M | 75 | 82 | £30k | +7 | — | 4★ | 3★ | 178 / 73 | — |
| J. Steuckers | Belçika | RM / RW (RM, RW) | KRC Genk | 23 | £9.89M | 75 | 82 | £17k | +7 | — | 3★ | 3★ | 179 / 68 | — |
| Y. Asprilla | Kolombiya | RM / RW (RM, RW, CAM) | Girona FC | 21 | £9.89M | 75 | 82 | £18k | +7 | — | 3★ | 3★ | 175 / 75 | — |
| F. Rieder | İsviçre | RM / RW (CAM, CM, RM) | FC Augsburg | 23 | £8.17M | 74 | 82 | £22k | +8 | — | 3★ | 3★ | 179 / 74 | — |
| Fresneda | İspanya | RM / RW (RB, RM, LB) | Sporting CP | 20 | £7.74M | 74 | 82 | £9k | +8 | — | 4★ | 3★ | 181 / 79 | — |
| Fábio Carvalho | Portekiz | RM / RW (CAM, CM, RM) | Brentford | 22 | £8.17M | 74 | 82 | £40k | +8 | — | 4★ | 4★ | 170 / 62 | — |
| M. Kvistgaarden | Danimarka | RM / RW (ST, LW, RW, LM) | Norwich City | 23 | £8.17M | 74 | 82 | £25k | +8 | — | 3★ | 3★ | 175 / 68 | — |
| Robert Navarro | İspanya | RM / RW (RM, LM, RW) | Athletic Club | 23 | £8.17M | 74 | 82 | £24k | +8 | — | 3★ | 4★ | 178 / 65 | — |
| Y. Musah | ABD | RM / RW (CM, CDM, RM, CAM) | Atalanta | 22 | £8.17M | 74 | 82 | £26k | +8 | — | 3★ | 4★ | 178 / 71 | — |
| A. Lescano | Arjantin | RM / RW (CM, CAM, RW) | Argentinos Juniors | 23 | £5.59M | 73 | 82 | £9k | +9 | — | 3★ | 3★ | 182 / 67 | — |
| Andrés García | İspanya | RM / RW (RB, RM) | Aston Villa | 22 | £5.59M | 73 | 82 | £46k | +9 | — | 4★ | 3★ | 183 / 82 | — |
| Fer López | İspanya | RM / RW (RW, RM) | Wolverhampton Wanderers | 21 | £6.02M | 73 | 82 | £31k | +9 | — | 2★ | 3★ | 186 / 76 | — |
| M. Zanotti | İtalya | RM / RW (RB, RM) | FC Lugano | 22 | £5.59M | 73 | 82 | £8k | +9 | — | 3★ | 3★ | 173 / 71 | — |
| Pubill | İspanya | RM / RW (RB, RM) | Atlético Madrid | 22 | £5.59M | 73 | 82 | £29k | +9 | — | 3★ | 2★ | 190 / 86 | — |
| Ângelo | Brezilya | RM / RW (RM, LM, RW) | Al Nassr | 20 | £5.59M | 73 | 82 | £19k | +9 | Acrobat | 2★ | 5★ | 180 / 78 | — |
| L. Koleosho | İtalya | RM / RW (LM, RM, LW) | RCD Espanyol | 20 | £4.30M | 72 | 82 | £23k | +10 | Speedster | 4★ | 3★ | 175 / 67 | — |
| O. Bobb | Norveç | RM / RW (RW, LW, RM) | Manchester City | 21 | £4.73M | 72 | 82 | £44k | +10 | — | 3★ | 4★ | 174 / 70 | — |
| Rodrigo Gomes | Portekiz | RM / RW (RW, LW, RM) | Wolverhampton Wanderers | 21 | £4.73M | 72 | 82 | £28k | +10 | — | 3★ | 3★ | 175 / 67 | — |
| Wagner Pina | Cabo Verde | RM / RW (RM, RB) | Trabzonspor | 22 | £4.73M | 72 | 82 | £24k | +10 | — | 2★ | 3★ | 180 / 72 | — |
| E. Mayenda | İspanya | RM / RW (ST, RM, LM, RW) | Sunderland | 20 | £3.53M | 71 | 82 | £24k | +11 | — | 2★ | 2★ | 180 / 75 | — |
| L. Angulo | Kolombiya | RM / RW (LM, RM, LW) | Talleres | 21 | £3.61M | 71 | 82 | £6k | +11 | — | 4★ | 3★ | 174 / 65 | — |
| M. Yalcouyé | Mali | RM / RW (CM, RM, CAM, RW) | Swansea City | 19 | £3.44M | 71 | 82 | £28k | +11 | — | 2★ | 3★ | 169 / 69 | — |
| Mella | İspanya | RM / RW (RM, LM, RW) | RC Deportivo de La Coruña | 20 | £3.53M | 71 | 82 | £3k | +11 | Speedster | 4★ | 4★ | 169 / 65 | — |
| C. Irié | Burkina Faso | RM / RW (RM, ST, RW) | SC Freiburg | 20 | £3.27M | 70 | 82 | £10k | +12 | — | 2★ | 3★ | 185 / 78 | High Growth |
| M. Abaldo | Uruguay | RM / RW (RW, RM) | Independiente | 21 | £3.35M | 70 | 82 | £6k | +12 | — | 3★ | 3★ | 172 / 60 | High Growth |
| R. Esse | İngiltere | RM / RW (RW, CAM, LW, RM) | Crystal Palace | 20 | £3.27M | 70 | 82 | £27k | +12 | — | 2★ | 3★ | 178 / 65 | High Growth |
| William Gomes | Brezilya | RM / RW (LW, RW, LM) | FC Porto | 19 | £3.27M | 70 | 82 | £5k | +12 | — | 3★ | 3★ | 171 / 66 | High Growth |
| L. Høgsberg | Danimarka | RM / RW (CB, RB, LB, RM) | RC Strasbourg Alsace | 19 | £2.67M | 69 | 82 | £13k | +13 | — | 3★ | 2★ | 187 / 70 | High Growth |
| R. Bardghji | İsveç | RM / RW (RM, RW) | FC Barcelona | 19 | £2.84M | 69 | 82 | £21k | +13 | — | 4★ | 4★ | 173 / 70 | High Growth |
| Jan Virgili | İspanya | RM / RW (LW, RW, ST, LM) | RCD Mallorca | 18 | £2.41M | 68 | 82 | £9k | +14 | — | 3★ | 4★ | 177 / 68 | High Growth |
| P. Diallo | Senegal | RM / RW (LM, LW, RM) | Norwich City | 21 | £2.58M | 68 | 82 | £10k | +14 | — | 2★ | 3★ | 182 / 67 | High Growth |
| S. Egeli | Norveç | RM / RW (RM, LM, RW) | Ipswich Town | 19 | £2.49M | 68 | 82 | £15k | +14 | — | 3★ | 3★ | 180 / 70 | High Growth |
| T. Watson | İngiltere | RM / RW (LM, RM, LW) | Brighton & Hove Albion | 19 | £2.49M | 68 | 82 | £20k | +14 | — | 3★ | 3★ | 190 / 77 | High Growth |
| Z. Gruber | Macaristan | RM / RW (ST, RW, RM) | Ferencvárosi Torna Club | 20 | £2.49M | 68 | 82 | £8k | +14 | — | 3★ | 2★ | 180 / 73 | High Growth |
| C. Campbell | ABD | RM / RW (RM, RW) | Borussia Dortmund | 19 | £2.06M | 67 | 82 | £9k | +15 | — | 3★ | 4★ | 170 / 68 | High Growth |
| K. Wätjen | Almanya | RM / RW (CM, CAM, RM) | VfL Bochum 1848 | 19 | £2.06M | 67 | 82 | £9k | +15 | — | 3★ | 3★ | 184 / 72 | High Growth |
| Lucas Ferreira | Brezilya | RM / RW (RW, LM, CAM, RM) | Shakhtar Donetsk | 19 | £2.06M | 67 | 82 | £6k | +15 | — | 3★ | 3★ | 187 / 74 | High Growth |
| N. Irankunda | Avustralya | RM / RW (RM, ST, LM, RW) | Watford | 19 | £2.06M | 67 | 82 | £9k | +15 | Acrobat | 3★ | 3★ | 175 / 74 | High Growth |
| S. Idumbo | Belçika | RM / RW (CAM, LM, RM, CM) | AS Monaco | 20 | £2.15M | 67 | 82 | £8k | +15 | — | 3★ | 3★ | 171 / 61 | High Growth |
| B. Burrowes | İngiltere | RM / RW (RM, ST, RW) | Aston Villa | 17 | £1.55M | 65 | 82 | £10k | +17 | — | 3★ | 3★ | 179 / 75 | High Growth |
| M. Ponomarenko | Ukrayna | RM / RW (ST, RW, LW) | Dynamo Kyiv | 19 | £1.63M | 65 | 82 | £4k | +17 | — | 4★ | 2★ | 188 / 89 | High Growth |
| S. Campbell | South Africa | RM / RW (LW, RW, LM) | Club Brugge KV | 19 | £1.55M | 65 | 82 | £5k | +17 | — | 3★ | 3★ | 178 / 65 | High Growth |
| S. Fini | İtalya | RM / RW (RM, LM, ST, RW) | Genoa | 19 | £1.55M | 65 | 82 | £4k | +17 | — | 3★ | 3★ | 178 / 73 | High Growth |
| Sandro Vidigal | Portekiz | RM / RW (LW, RW, CAM, LM) | Sporting Clube de Braga | 17 | £1.55M | 65 | 82 | £2k | +17 | — | 4★ | 3★ | 179 / 70 | High Growth |
| E. Dijkstra | Hollanda | RM / RW (RB, LB, RM) | AZ Alkmaar | 18 | £1.20M | 64 | 82 | £3k | +18 | — | 4★ | 3★ | 173 / 67 | High Growth |
| L. Jovanović | Sırbistan | RM / RW (RM, LM, RW) | VfB Stuttgart | 18 | £1.29M | 64 | 82 | £5k | +18 | — | 3★ | 3★ | 184 / 76 | High Growth |
| A. Garcia | İngiltere | RM / RW (LB, RW, LW, RM) | Reading FC | 17 | £946k | 63 | 82 | £0k | +19 | — | 2★ | 3★ | 180 / 67 | High Growth |
| N. Darvich | Almanya | RM / RW (CAM, CM, RM) | VfB Stuttgart | 18 | £946k | 62 | 82 | £4k | +20 | — | 4★ | 4★ | 184 / 73 | High Growth |
| T. Sanusi | İngiltere | RM / RW (LW, RW, LM) | FC Lorient | 18 | £860k | 61 | 82 | £10k | +21 | — | 3★ | 4★ | 178 / 63 | High Growth |
| J. von der Hitz | Almanya | RM / RW (RM, RB, RW) | 1. FC Nürnberg | 18 | £666k | 60 | 82 | £1k | +22 | — | 4★ | 3★ | 177 / 70 | High Growth |
| A. Tatu | Avustralya | RM / RW (LM, RM, LW) | Adelaide United | 17 | £452k | 57 | 82 | £0k | +25 | — | 4★ | 2★ | 175 / 69 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Sağ Kanat & Sağ Orta Saha (RM / RW))

- **A. Güler** (Real Madrid) — OVR 81, POT 89: Türk kadrosu için doğal hedef.
- **A. Tatu** (Adelaide United) — OVR 57, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **J. von der Hitz** (1. FC Nürnberg) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **T. Sanusi** (FC Lorient) — OVR 61, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **S. Renders** (Royal Antwerp FC) — OVR 62, POT 84: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **L. Karl** (FC Bayern München) — OVR 63, POT 86: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 9. Sol Kanat & Sol Orta Saha (LM / LW)

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J. Musiala | Almanya | LM / LW (CAM, LM, CM, ST) | FC Bayern München | 22 | £115M | 88 | 92 | £95k | +4 | Dribbler, Acrobat, Clinical finisher, Complete … | 4★ | 5★ | 184 / 72 | — |
| D. Doué | Fransa | LM / LW (RW, LW, CM, RM) | Paris Saint-Germain | 20 | £71.8M | 85 | 91 | £86k | +6 | Dribbler, Acrobat | 4★ | 5★ | 181 / 79 | — |
| Nico Williams | İspanya | LM / LW (LM, RM, LW) | Athletic Club | 22 | £81.3M | 86 | 89 | £60k | +3 | Speedster, Dribbler, Acrobat | 5★ | 4★ | 181 / 67 | — |
| Nuno Mendes | Portekiz | LM / LW (LB, LM) | Paris Saint-Germain | 23 | £74.0M | 86 | 89 | £95k | +3 | Speedster, Acrobat | 4★ | 3★ | 180 / 70 | — |
| Álex Baena | İspanya | LM / LW (LM, ST, LW) | Atlético Madrid | 23 | £54.6M | 84 | 89 | £71k | +5 | — | 4★ | 3★ | 174 / 70 | — |
| P. Hincapié | Ekvador | LM / LW (CB, LB, LM) | Arsenal | 23 | £44.7M | 83 | 89 | £70k | +6 | — | 2★ | 3★ | 184 / 77 | — |
| K. Yıldız | Türkiye | LM / LW (CAM, LM, LW, CM) | Juventus | 20 | £33.1M | 79 | 89 | £69k | +10 | — | 5★ | 4★ | 185 / 75 | Türk Yeteneği |
| Rodrigo Mora | Portekiz | LM / LW (CAM, LW, CM, ST) | FC Porto | 18 | £15.1M | 76 | 89 | £8k | +13 | — | 4★ | 4★ | 168 / 56 | High Growth |
| B. Barcola | Fransa | LM / LW (LW, RW, LM) | Paris Saint-Germain | 22 | £52.9M | 84 | 88 | £95k | +4 | Acrobat | 4★ | 4★ | 188 / 70 | — |
| Yeremy Pino | İspanya | LM / LW (RM, LM, LW, RW) | Crystal Palace | 22 | £40.9M | 80 | 88 | £66k | +8 | — | 4★ | 3★ | 172 / 65 | — |
| Álvaro Carreras | İspanya | LM / LW (LB, LM) | Real Madrid | 22 | £38.7M | 80 | 88 | £112k | +8 | — | 4★ | 3★ | 186 / 78 | — |
| A. Nusa | Norveç | LM / LW (LM, CAM, LW) | RB Leipzig | 20 | £15.5M | 76 | 88 | £28k | +12 | Acrobat | 4★ | 4★ | 183 / 77 | High Growth |
| Geovany Quenda | Portekiz | LM / LW (RM, LM, LW, RW) | Sporting CP | 18 | £15.1M | 76 | 88 | £10k | +12 | — | 4★ | 4★ | 172 / 71 | High Growth |
| R. Ngumoha | İngiltere | LM / LW (LM, LW) | Liverpool | 16 | £2.84M | 68 | 88 | £15k | +20 | Speedster | 3★ | 3★ | 170 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Gvardiol | Hırvatistan | LM / LW (LB, CB, LM) | Manchester City | 23 | £46.0M | 84 | 87 | £112k | +3 | — | 5★ | 3★ | 185 / 80 | — |
| X. Simons | Hollanda | LM / LW (CAM, LM, ST) | Tottenham Hotspur | 22 | £50.3M | 84 | 87 | £108k | +3 | Dribbler, Acrobat | 3★ | 4★ | 179 / 58 | — |
| Balde | İspanya | LM / LW (LB, LM) | FC Barcelona | 21 | £42.6M | 83 | 87 | £69k | +4 | Speedster | 4★ | 3★ | 175 / 69 | — |
| M. Tillman | ABD | LM / LW (CAM, LW, CM) | Bayer 04 Leverkusen | 23 | £39.6M | 82 | 87 | £69k | +5 | — | 3★ | 4★ | 187 / 71 | — |
| Savinho | Brezilya | LM / LW (RW, LW, RM) | Manchester City | 21 | £40.4M | 82 | 87 | £95k | +5 | Dribbler, Acrobat | 2★ | 4★ | 176 / 71 | — |
| C. Tzolis | Yunanistan | LM / LW (LM, LW) | Club Brugge KV | 23 | £36.5M | 80 | 87 | £28k | +7 | — | 4★ | 4★ | 179 / 73 | — |
| Fermín | İspanya | LM / LW (CAM, CM, LW, ST) | FC Barcelona | 22 | £37.0M | 80 | 87 | £69k | +7 | — | 4★ | 3★ | 174 / 64 | — |
| A. Diao | Senegal | LM / LW (LM, RM, LW) | Como | 19 | £13.8M | 76 | 87 | £42k | +11 | Speedster | 4★ | 4★ | 185 / 72 | — |
| J. Duranville | Belçika | LM / LW (RM, LM, ST, RW) | Borussia Dortmund | 19 | £4.73M | 72 | 87 | £17k | +15 | Dribbler, Acrobat | 3★ | 5★ | 170 / 67 | Hidden Gem, High Growth |
| Pablo García | İspanya | LM / LW (RM, ST, LM, RW) | Real Betis Balompié | 18 | £2.67M | 68 | 87 | £7k | +19 | — | 3★ | 3★ | 175 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| M. Kerkez | Macaristan | LM / LW (LB, LM) | Liverpool | 21 | £35.7M | 82 | 86 | £70k | +4 | — | 3★ | 3★ | 180 / 71 | — |
| M. Rogers | İngiltere | LM / LW (CAM, RM, LM, CM) | Aston Villa | 22 | £38.3M | 82 | 86 | £95k | +4 | — | 4★ | 4★ | 188 / 80 | — |
| G. Simeone | Arjantin | LM / LW (RM, ST, LM, RW) | Atlético Madrid | 22 | £34.0M | 81 | 86 | £54k | +5 | Speedster | 3★ | 3★ | 173 / 75 | — |
| K. Adeyemi | Almanya | LM / LW (RM, LW, CAM, RW) | Borussia Dortmund | 23 | £33.5M | 81 | 86 | £41k | +5 | Speedster, Acrobat | 4★ | 4★ | 180 / 77 | — |
| Moleiro | İspanya | LM / LW (LM, CAM, LW) | Villarreal CF | 21 | £30.5M | 79 | 86 | £28k | +7 | — | 4★ | 4★ | 171 / 68 | — |
| Diego López | İspanya | LM / LW (LM, RM, LW) | Valencia CF | 23 | £26.7M | 78 | 86 | £29k | +8 | — | 4★ | 3★ | 172 / 63 | — |
| M. Fofana | Belçika | LM / LW (LM, LW) | Olympique Lyonnais | 20 | £26.7M | 78 | 86 | £15k | +8 | — | 5★ | 4★ | 170 / 60 | — |
| M. Tel | Fransa | LM / LW (ST, LW, CAM) | Tottenham Hotspur | 20 | £20.2M | 77 | 86 | £58k | +9 | — | 4★ | 4★ | 183 / 77 | — |
| J. Bahoya | Fransa | LM / LW (LM, CAM, LW) | Eintracht Frankfurt | 20 | £10.8M | 75 | 86 | £18k | +11 | Speedster | 3★ | 4★ | 180 / 76 | — |
| C. Echeverri | Arjantin | LM / LW (CAM, CM, LW) | Bayer 04 Leverkusen | 19 | £8.60M | 74 | 86 | £46k | +12 | Acrobat | 3★ | 3★ | 170 / 65 | High Growth |
| C. Talbi | Fas | LM / LW (RM, LM, RW) | Sunderland | 20 | £6.45M | 73 | 86 | £26k | +13 | Speedster | 4★ | 3★ | 175 / 64 | High Growth |
| L. Sauer | Slovakia | LM / LW (LW, CAM, LM) | Feyenoord | 19 | £4.73M | 72 | 86 | £8k | +14 | — | 3★ | 4★ | 184 / 74 | Hidden Gem, High Growth |
| M. Moore | İngiltere | LM / LW (LW, LM) | Rangers FC | 17 | £4.73M | 72 | 86 | £28k | +14 | — | 4★ | 3★ | 180 / 75 | Hidden Gem, High Growth |
| João Costa | Brezilya | LM / LW (RM, LM, LB, RB) | Al Ettifaq | 20 | £3.87M | 71 | 86 | £12k | +15 | — | 3★ | 3★ | 178 / 69 | Hidden Gem, Ucuz Cevher, High Growth |
| Miguel Gutiérrez | İspanya | LM / LW (LB, LM) | Napoli | 23 | £29.7M | 81 | 85 | £72k | +4 | — | 3★ | 2★ | 180 / 73 | — |
| J. Doku | Belçika | LM / LW (LW, RW, LM) | Manchester City | 23 | £27.5M | 80 | 85 | £95k | +5 | Speedster, Dribbler, Acrobat | 3★ | 4★ | 173 / 66 | — |
| Fábio Silva | Portekiz | LM / LW (ST, LW) | Borussia Dortmund | 22 | £24.5M | 79 | 85 | £40k | +6 | — | 3★ | 4★ | 185 / 75 | — |
| J. Gittens | İngiltere | LM / LW (LM, LW) | Chelsea | 20 | £24.1M | 78 | 85 | £63k | +7 | Speedster, Dribbler, Acrobat | 4★ | 4★ | 179 / 77 | — |
| N. Brown | Almanya | LM / LW (LB, LM) | Eintracht Frankfurt | 22 | £19.4M | 77 | 85 | £22k | +8 | — | 3★ | 4★ | 180 / 64 | — |
| E. Ben Seghir | Fas | LM / LW (LM, CAM, LW) | Bayer 04 Leverkusen | 20 | £14.2M | 76 | 85 | £37k | +9 | — | 3★ | 4★ | 178 / 72 | — |
| O. Gloukh | Israel | LM / LW (CAM, LW, CM) | Ajax | 21 | £14.6M | 76 | 85 | £12k | +9 | — | 4★ | 4★ | 171 / 68 | — |
| Roger Fernandes | Portekiz | LM / LW (RM, LM, RW) | Al Ittihad | 19 | £13.8M | 76 | 85 | £22k | +9 | Acrobat | 4★ | 3★ | 166 / 65 | — |
| C. Harder | Danimarka | LM / LW (ST, CAM, LW, CM) | RB Leipzig | 20 | £8.17M | 74 | 85 | £28k | +11 | — | 3★ | 3★ | 185 / 71 | — |
| Jesús Rodríguez | İspanya | LM / LW (LM, RM, LW) | Como | 19 | £7.74M | 74 | 85 | £37k | +11 | — | 3★ | 3★ | 185 / 68 | — |
| M. Godts | Belçika | LM / LW (LW, LM) | Ajax | 20 | £8.17M | 74 | 85 | £11k | +11 | — | 3★ | 4★ | 176 / 70 | — |
| B. Touré | Côte d'Ivoire | LM / LW (LM, LW, CAM) | TSG 1899 Hoffenheim | 19 | £3.27M | 70 | 85 | £11k | +15 | Speedster | 2★ | 4★ | 175 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| Adrián Liso | İspanya | LM / LW (LM, ST, LW) | Getafe CF | 20 | £3.18M | 69 | 85 | £4k | +16 | — | 3★ | 3★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| Antoñito Cordero | İspanya | LM / LW (LW, RW, LM) | KVC Westerlo | 18 | £3.01M | 69 | 85 | £28k | +16 | — | 3★ | 4★ | 178 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Subiabre | Arjantin | LM / LW (LW, RW, ST, LM) | River Plate | 18 | £3.01M | 69 | 85 | £6k | +16 | — | 3★ | 3★ | 171 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| T. Gomis | Fransa | LM / LW (LM, RM, ST, LW) | RB Leipzig | 18 | £2.67M | 68 | 85 | £11k | +17 | — | 3★ | 4★ | 183 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| D. León | Paraguay | LM / LW (LB, LM) | Manchester United | 18 | £1.55M | 64 | 85 | £9k | +21 | — | 2★ | 2★ | 177 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Lerma | Ekvador | LM / LW (LM, CAM, CM, LW) | Independiente del Valle | 17 | £1.55M | 64 | 85 | £3k | +21 | — | 3★ | 4★ | 176 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Maatsen | Hollanda | LM / LW (LB, LM) | Aston Villa | 23 | £21.1M | 79 | 84 | £73k | +5 | — | 2★ | 3★ | 178 / 68 | — |
| M. Beier | Almanya | LM / LW (ST, RM, LM, RW) | Borussia Dortmund | 22 | £23.6M | 79 | 84 | £40k | +5 | — | 3★ | 4★ | 185 / 72 | — |
| H. Haraldsson | Iceland | LM / LW (CAM, LM, CM) | Lille OSC | 22 | £19.4M | 78 | 84 | £24k | +6 | — | 4★ | 3★ | 178 / 71 | — |
| Lucas Beraldo | Brezilya | LM / LW (CB, LB, LM) | Paris Saint-Germain | 21 | £17.6M | 78 | 84 | £42k | +6 | — | 2★ | 2★ | 182 / 78 | — |
| A. Garnacho | Arjantin | LM / LW (CAM, LW, LM, CM) | Chelsea | 21 | £18.5M | 77 | 84 | £60k | +7 | — | 4★ | 3★ | 180 / 72 | — |
| B. El Khannouss | Fas | LM / LW (CAM, LM, CM) | VfB Stuttgart | 21 | £14.6M | 76 | 84 | £28k | +8 | — | 3★ | 4★ | 180 / 70 | — |
| C. Summerville | Hollanda | LM / LW (LM, LW) | West Ham United | 23 | £14.2M | 76 | 84 | £42k | +8 | — | 3★ | 3★ | 169 / 64 | — |
| Raúl Moro | İspanya | LM / LW (LW, RW, LM) | Ajax | 22 | £14.6M | 76 | 84 | £15k | +8 | — | 3★ | 3★ | 169 / 67 | — |
| Yeremay | İspanya | LM / LW (LM, RM, LW) | RC Deportivo de La Coruña | 22 | £14.6M | 76 | 84 | £7k | +8 | Acrobat | 3★ | 4★ | 170 / 61 | — |
| C. Mawissa | Fransa | LM / LW (CB, LB, LM) | AS Monaco | 20 | £9.89M | 75 | 84 | £16k | +9 | — | 5★ | 2★ | 184 / 77 | — |
| M. Fernandez-Pardo | İspanya | LM / LW (LM, RM, LW) | Lille OSC | 20 | £10.8M | 75 | 84 | £16k | +9 | — | 3★ | 3★ | 188 / 77 | — |
| Y. Cathline | Fransa | LM / LW (LW, LM) | FC Utrecht | 22 | £10.8M | 75 | 84 | £10k | +9 | — | 2★ | 3★ | 176 / 68 | — |
| P. Dorgu | Danimarka | LM / LW (LB, LM) | Manchester United | 20 | £7.74M | 74 | 84 | £35k | +10 | — | 2★ | 2★ | 185 / 70 | — |
| R. van Bommel | Hollanda | LM / LW (LW, LM) | PSV | 20 | £8.17M | 74 | 84 | £13k | +10 | — | 2★ | 3★ | 192 / 83 | — |
| J. Enciso | Paraguay | LM / LW (CAM, LM, RM, ST) | RC Strasbourg Alsace | 21 | £6.02M | 73 | 84 | £24k | +11 | — | 3★ | 3★ | 173 / 64 | — |
| I. Osman | Gana | LM / LW (LM, RM, LW) | AJ Auxerre | 20 | £4.73M | 72 | 84 | £33k | +12 | Speedster | 2★ | 3★ | 178 / 63 | Hidden Gem, High Growth |
| S. Mbangula | Belçika | LM / LW (LM, LW) | SV Werder Bremen | 21 | £5.16M | 72 | 84 | £13k | +12 | — | 3★ | 3★ | 179 / 65 | Hidden Gem, High Growth |
| Luis Guilherme | Brezilya | LM / LW (RM, LM, CAM, RW) | West Ham United | 19 | £3.78M | 71 | 84 | £22k | +13 | — | 4★ | 4★ | 175 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| T. George | İngiltere | LM / LW (LM, RM, ST, LW) | Chelsea | 19 | £3.78M | 71 | 84 | £34k | +13 | — | 4★ | 4★ | 185 / 80 | Hidden Gem, Ucuz Cevher, High Growth |
| Pau Sans | İspanya | LM / LW (RM, LM, ST, RW) | Real Zaragoza | 20 | £3.27M | 70 | 84 | £4k | +14 | — | 3★ | 3★ | 177 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| Y. Medina | Ekvador | LM / LW (LB, LW, LM) | KRC Genk | 20 | £3.18M | 70 | 84 | £9k | +14 | Speedster | 2★ | 3★ | 175 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| Yang Min Hyeok | Korea Republic | LM / LW (RM, RW, LM) | Portsmouth | 19 | £3.27M | 70 | 84 | £27k | +14 | — | 3★ | 3★ | 171 / 61 | Hidden Gem, Ucuz Cevher, High Growth |
| S. El Mala | Almanya | LM / LW (LM, CAM, LW) | 1. FC Köln | 18 | £2.67M | 68 | 84 | £7k | +16 | — | 4★ | 4★ | 187 / 77 | Hidden Gem, Ucuz Cevher, High Growth |
| Unai Hernández | İspanya | LM / LW (LM, CM, CAM, LW) | Al Shabab | 20 | £1.89M | 66 | 84 | £8k | +18 | — | 3★ | 3★ | 171 / 65 | Hidden Gem, Ucuz Cevher, High Growth |
| R. Bounida | Belçika | LM / LW (LW, CAM, LM) | Ajax | 19 | £1.38M | 64 | 84 | £3k | +20 | — | 4★ | 4★ | 179 / 62 | Hidden Gem, Ucuz Cevher, High Growth |
| F. Curtis | Scotland | LM / LW (LW, RW, LM) | Rangers FC | 18 | £1.29M | 63 | 84 | £8k | +21 | — | 3★ | 3★ | 180 / 66 | Hidden Gem, Ucuz Cevher, High Growth |
| K. Schade | Almanya | LM / LW (LM, LW) | Brentford | 23 | £18.1M | 78 | 83 | £51k | +5 | Speedster | 4★ | 3★ | 185 / 74 | — |
| Luis Henrique | Brezilya | LM / LW (RM, LM, RW) | Inter | 23 | £18.1M | 78 | 83 | £24k | +5 | — | 3★ | 3★ | 181 / 85 | — |
| Abde | Fas | LM / LW (LM, LW) | Real Betis Balompié | 23 | £14.2M | 77 | 83 | £22k | +6 | — | 3★ | 4★ | 177 / 72 | — |
| Aimar Oroz | İspanya | LM / LW (CM, CAM, LM) | CA Osasuna | 23 | £14.2M | 77 | 83 | £25k | +6 | — | 3★ | 3★ | 177 / 72 | — |
| Barrenetxea | İspanya | LM / LW (LM, LW) | Real Sociedad | 23 | £14.2M | 77 | 83 | £28k | +6 | — | 4★ | 3★ | 175 / 74 | — |
| Bryan Zaragoza | İspanya | LM / LW (LM, LW, RM) | RC Celta | 23 | £14.2M | 77 | 83 | £39k | +6 | Acrobat | 4★ | 4★ | 164 / 60 | — |
| Diego Moreira | Belçika | LM / LW (LM, LB, RM) | RC Strasbourg Alsace | 20 | £14.2M | 77 | 83 | £31k | +6 | — | 3★ | 4★ | 179 / 73 | — |
| Q. Hartman | Hollanda | LM / LW (LB, LM) | Burnley | 23 | £13.3M | 77 | 83 | £39k | +6 | — | 3★ | 3★ | 183 / 77 | — |
| Gabri Veiga | İspanya | LM / LW (CAM, CM, LM) | FC Porto | 23 | £12.9M | 76 | 83 | £10k | +7 | — | 4★ | 4★ | 184 / 71 | — |
| M. Cho | Fransa | LM / LW (LW, RW, ST, LM) | OGC Nice | 21 | £12.9M | 76 | 83 | £18k | +7 | — | 3★ | 3★ | 181 / 66 | — |
| S. Adingra | Côte d'Ivoire | LM / LW (RM, LM, RW) | Sunderland | 23 | £12.9M | 76 | 83 | £38k | +7 | — | 3★ | 3★ | 175 / 68 | — |
| S. Nanasi | İsveç | LM / LW (CAM, LM, CM) | RC Strasbourg Alsace | 23 | £12.9M | 76 | 83 | £34k | +7 | — | 3★ | 4★ | 178 / 71 | — |
| A. Schjelderup | Norveç | LM / LW (LW, CAM, LM) | SL Benfica | 21 | £10.8M | 75 | 83 | £12k | +8 | — | 3★ | 3★ | 176 / 69 | — |
| B. Traoré | Côte d'Ivoire | LM / LW (LM, RM, LW) | FC Basel 1893 | 22 | £10.8M | 75 | 83 | £16k | +8 | Acrobat | 3★ | 4★ | 172 / 64 | — |
| M. Ruggeri | İtalya | LM / LW (LM, LB) | Atlético Madrid | 22 | £10.8M | 75 | 83 | £36k | +8 | — | 3★ | 3★ | 187 / 69 | — |
| V. Barco | Arjantin | LM / LW (LB, LM, CM) | RC Strasbourg Alsace | 20 | £10.3M | 75 | 83 | £26k | +8 | — | 3★ | 3★ | 170 / 66 | — |
| W. Odobert | Fransa | LM / LW (LW, RW, LM) | Tottenham Hotspur | 20 | £10.8M | 75 | 83 | £51k | +8 | — | 4★ | 3★ | 182 / 75 | — |
| A. Zakharyan | Russia | LM / LW (RM, CM, LM, RW) | Real Sociedad | 22 | £8.17M | 74 | 83 | £22k | +9 | — | 4★ | 3★ | 182 / 73 | — |
| E. Zeballos | Arjantin | LM / LW (RM, RW, LW) | Boca Juniors | 23 | £8.17M | 74 | 83 | £13k | +9 | Acrobat | 3★ | 5★ | 175 / 68 | — |
| Gabriel Silva | Brezilya | LM / LW (LW, ST, RM, LM) | Santa Clara | 23 | £8.17M | 74 | 83 | £8k | +9 | Speedster | 3★ | 3★ | 177 / 69 | — |
| I. Akhomach | Fas | LM / LW (RM, RW, LW) | Villarreal CF | 21 | £8.17M | 74 | 83 | £19k | +9 | — | 4★ | 4★ | 175 / 70 | — |
| W. Gnonto | İtalya | LM / LW (RM, LM, RW) | Leeds United | 21 | £8.17M | 74 | 83 | £28k | +9 | — | 4★ | 3★ | 169 / 72 | — |
| Óscar Aranda | İspanya | LM / LW (LM, ST, RM, LW) | Famalicão | 23 | £8.17M | 74 | 83 | £9k | +9 | — | 4★ | 4★ | 181 / 78 | — |
| B. Domínguez | Arjantin | LM / LW (LM, LW) | Bologna | 21 | £6.02M | 73 | 83 | £22k | +10 | — | 3★ | 4★ | 172 / 68 | — |
| C. Bonsu Baah | Gana | LM / LW (LM, RM, LW) | Al Qadsiah FC | 20 | £5.59M | 73 | 83 | £16k | +10 | — | 3★ | 4★ | 172 / 73 | — |
| G. Diarra | Mali | LM / LW (LW, RW, LM) | Feyenoord | 22 | £4.73M | 72 | 83 | £9k | +11 | — | 3★ | 3★ | 183 / 74 | — |
| Patati | Brezilya | LM / LW (RM, LM, RW) | AZ Alkmaar | 21 | £4.73M | 72 | 83 | £9k | +11 | — | 3★ | 4★ | 173 / 59 | — |
| I. Jensen | Danimarka | LM / LW (LM, LW) | AZ Alkmaar | 21 | £3.35M | 70 | 83 | £7k | +13 | — | 3★ | 3★ | 185 / 84 | Ucuz Cevher, High Growth |
| L. Koumas | Wales | LM / LW (RM, LM, RW) | Birmingham City | 19 | £2.84M | 69 | 83 | £23k | +14 | — | 4★ | 3★ | 182 / 68 | Ucuz Cevher, High Growth |
| Y. Özcan | Türkiye | LM / LW (CB, LB, LM) | RSC Anderlecht | 19 | £2.67M | 69 | 83 | £23k | +14 | — | 2★ | 2★ | 185 / 75 | Türk Yeteneği, Ucuz Cevher, High Growth |
| H. Amass | İngiltere | LM / LW (LB, LM) | Sheffield Wednesday | 18 | £2.32M | 68 | 83 | £16k | +15 | — | 3★ | 2★ | 178 / 75 | Ucuz Cevher, High Growth |
| I. Mbaye | Fransa | LM / LW (RW, LW, RM) | Paris Saint-Germain | 17 | £2.41M | 68 | 83 | £15k | +15 | — | 3★ | 3★ | 176 / 65 | Ucuz Cevher, High Growth |
| S. Andino | Arjantin | LM / LW (LM, LW, CAM) | Godoy Cruz | 19 | £2.49M | 68 | 83 | £3k | +15 | — | 3★ | 3★ | 174 / 66 | Ucuz Cevher, High Growth |
| I. Babadi | Hollanda | LM / LW (CAM, CM, LW) | Royal Antwerp FC | 20 | £2.32M | 67 | 83 | £6k | +16 | — | 4★ | 3★ | 178 / 68 | Ucuz Cevher, High Growth |
| N. Adedeji-Sternberg | Belçika | LM / LW (LM, LW) | KRC Genk | 20 | £2.32M | 67 | 83 | £7k | +16 | — | 3★ | 3★ | 183 / 68 | Ucuz Cevher, High Growth |
| Arturo | İspanya | LM / LW (RW, LW, RM) | UD Las Palmas | 18 | £1.12M | 63 | 83 | £1k | +20 | — | 3★ | 3★ | 176 / 69 | Ucuz Cevher, High Growth |
| Pablo López | İspanya | LM / LW (RW, LW, RM) | CD Mirandés | 19 | £1.12M | 63 | 83 | £5k | +20 | — | 3★ | 3★ | 175 / 65 | Ucuz Cevher, High Growth |
| Hugo Pinilla | İspanya | LM / LW (RM, CAM, LM, RW) | Real Zaragoza | 19 | £1.12M | 62 | 83 | £2k | +21 | — | 3★ | 3★ | 185 / 70 | Ucuz Cevher, High Growth |
| D. Svensson | İsveç | LM / LW (LB, CM, LM) | Borussia Dortmund | 23 | £12.9M | 77 | 82 | £29k | +5 | — | 4★ | 2★ | 178 / 72 | — |
| Hugo Álvarez | İspanya | LM / LW (LM, RM, LW) | RC Celta | 21 | £10.3M | 76 | 82 | £17k | +6 | — | 3★ | 3★ | 176 / 72 | — |
| Q. Merlin | Fransa | LM / LW (LB, LM) | Stade Rennais FC | 23 | £9.46M | 76 | 82 | £18k | +6 | — | 2★ | 3★ | 174 / 68 | — |
| Rômulo | Brezilya | LM / LW (ST, LW, CAM) | RB Leipzig | 23 | £10.3M | 76 | 82 | £36k | +6 | — | 3★ | 3★ | 193 / 80 | — |
| Tiago Tomás | Portekiz | LM / LW (LW, LM, ST) | VfB Stuttgart | 23 | £10.3M | 76 | 82 | £28k | +6 | — | 3★ | 4★ | 180 / 78 | — |
| Ansu Fati | İspanya | LM / LW (LM, LW) | AS Monaco | 22 | £9.89M | 75 | 82 | £48k | +7 | — | 4★ | 4★ | 178 / 66 | — |
| E. Diouf | Senegal | LM / LW (LB, LM) | West Ham United | 20 | £9.03M | 75 | 82 | £32k | +7 | — | 2★ | 3★ | 183 / 75 | — |
| J. Rowe | İngiltere | LM / LW (LM, RM, LW) | Bologna | 22 | £9.89M | 75 | 82 | £30k | +7 | — | 4★ | 3★ | 178 / 73 | — |
| A. Velasco | Arjantin | LM / LW (LM, LW, CAM) | Boca Juniors | 22 | £8.17M | 74 | 82 | £13k | +8 | — | 4★ | 4★ | 167 / 63 | — |
| Gerard Martín | İspanya | LM / LW (LB, CB, LM) | FC Barcelona | 23 | £7.74M | 74 | 82 | £42k | +8 | — | 3★ | 3★ | 186 / 76 | — |
| J. Breum | Danimarka | LM / LW (CAM, LM, CM) | Go Ahead Eagles | 21 | £8.17M | 74 | 82 | £8k | +8 | — | 2★ | 3★ | 178 / 68 | — |
| L. Ullrich | Almanya | LM / LW (LB, LM) | Borussia Mönchengladbach | 21 | £7.74M | 74 | 82 | £15k | +8 | — | 2★ | 2★ | 180 / 73 | — |
| M. Kvistgaarden | Danimarka | LM / LW (ST, LW, RW, LM) | Norwich City | 23 | £8.17M | 74 | 82 | £25k | +8 | — | 3★ | 3★ | 175 / 68 | — |
| Robert Navarro | İspanya | LM / LW (RM, LM, RW) | Athletic Club | 23 | £8.17M | 74 | 82 | £24k | +8 | — | 3★ | 4★ | 178 / 65 | — |
| S. Iling-Junior | İngiltere | LM / LW (LM, LB, LW) | West Bromwich Albion | 21 | £8.17M | 74 | 82 | £46k | +8 | — | 4★ | 3★ | 182 / 75 | — |
| T. Fernández | Arjantin | LM / LW (LM, LW) | Vélez Sarsfield | 21 | £8.17M | 74 | 82 | £9k | +8 | — | 2★ | 3★ | 175 / 68 | — |
| A. Boiro | Senegal | LM / LW (LB, LM) | Athletic Club | 23 | £5.59M | 73 | 82 | £21k | +9 | — | 3★ | 3★ | 183 / 76 | — |
| H. Igamane | Fas | LM / LW (ST, LM, CAM) | Lille OSC | 22 | £6.02M | 73 | 82 | £18k | +9 | — | 4★ | 4★ | 181 / 77 | — |
| I. Gharbi | Tunisia | LM / LW (LM, CAM, LW) | FC Augsburg | 21 | £6.02M | 73 | 82 | £8k | +9 | — | 4★ | 3★ | 173 / 66 | — |
| J. Ondrejka | İsveç | LM / LW (LM, LW) | Parma | 22 | £6.02M | 73 | 82 | £13k | +9 | — | 4★ | 4★ | 180 / 70 | — |
| K. Paredes | ABD | LM / LW (LW, LM, LB) | VfL Wolfsburg | 22 | £6.02M | 73 | 82 | £26k | +9 | — | 3★ | 4★ | 175 / 61 | — |
| Peque | İspanya | LM / LW (CAM, LW, ST, CM) | Sevilla FC | 22 | £6.02M | 73 | 82 | £18k | +9 | — | 4★ | 3★ | 172 / 65 | — |
| S. Dahl | İsveç | LM / LW (LB, LM) | SL Benfica | 22 | £5.59M | 73 | 82 | £10k | +9 | — | 3★ | 3★ | 171 / 68 | — |
| Unai Gómez | İspanya | LM / LW (CAM, CM, LM) | Athletic Club | 22 | £6.02M | 73 | 82 | £22k | +9 | — | 3★ | 3★ | 183 / 74 | — |
| Ângelo | Brezilya | LM / LW (RM, LM, RW) | Al Nassr | 20 | £5.59M | 73 | 82 | £19k | +9 | Acrobat | 2★ | 5★ | 180 / 78 | — |
| L. Koleosho | İtalya | LM / LW (LM, RM, LW) | RCD Espanyol | 20 | £4.30M | 72 | 82 | £23k | +10 | Speedster | 4★ | 3★ | 175 / 67 | — |
| O. Bobb | Norveç | LM / LW (RW, LW, RM) | Manchester City | 21 | £4.73M | 72 | 82 | £44k | +10 | — | 3★ | 4★ | 174 / 70 | — |
| Rodrigo Gomes | Portekiz | LM / LW (RW, LW, RM) | Wolverhampton Wanderers | 21 | £4.73M | 72 | 82 | £28k | +10 | — | 3★ | 3★ | 175 / 67 | — |
| Álex Valle | İspanya | LM / LW (LB, LM) | Como | 21 | £4.30M | 72 | 82 | £30k | +10 | — | 3★ | 3★ | 183 / 57 | — |
| E. Mayenda | İspanya | LM / LW (ST, RM, LM, RW) | Sunderland | 20 | £3.53M | 71 | 82 | £24k | +11 | — | 2★ | 2★ | 180 / 75 | — |
| J. Recoba | Uruguay | LM / LW (LW, CAM, ST, LM) | UD Las Palmas | 21 | £3.61M | 71 | 82 | £4k | +11 | — | 3★ | 3★ | 177 / 75 | — |
| K. Sano | Japonya | LM / LW (CDM, LM, CM) | NEC Nijmegen | 21 | £3.44M | 71 | 82 | £5k | +11 | — | 3★ | 3★ | 176 / 66 | — |
| L. Angulo | Kolombiya | LM / LW (LM, RM, LW) | Talleres | 21 | £3.61M | 71 | 82 | £6k | +11 | — | 4★ | 3★ | 174 / 65 | — |
| L. Mincarelli | Fransa | LM / LW (LB, LM) | Montpellier HSC | 21 | £3.44M | 71 | 82 | £3k | +11 | — | 3★ | 2★ | 180 / 65 | — |
| M. Del Blanco | Arjantin | LM / LW (LB, CM, LM) | Club Atlético Unión | 21 | £3.44M | 71 | 82 | £5k | +11 | — | 3★ | 3★ | 170 / 68 | — |
| Mella | İspanya | LM / LW (RM, LM, RW) | RC Deportivo de La Coruña | 20 | £3.53M | 71 | 82 | £3k | +11 | Speedster | 4★ | 4★ | 169 / 65 | — |
| Wesley | Brezilya | LM / LW (LW, LM) | Al Nassr | 20 | £3.53M | 71 | 82 | £16k | +11 | — | 4★ | 4★ | 180 / 70 | — |
| Eguinaldo | Brezilya | LM / LW (LM, LW, ST) | Shakhtar Donetsk | 20 | £3.27M | 70 | 82 | £8k | +12 | — | 4★ | 3★ | 175 / 69 | High Growth |
| J. Belocian | Fransa | LM / LW (CB, LB, LM) | Bayer 04 Leverkusen | 20 | £3.10M | 70 | 82 | £21k | +12 | — | 3★ | 2★ | 182 / 73 | High Growth |
| L. Leroux | Fransa | LM / LW (CM, LB, LM) | FC Nantes | 19 | £3.27M | 70 | 82 | £7k | +12 | — | 2★ | 3★ | 184 / 75 | High Growth |
| Newerton | Brezilya | LM / LW (LW, LM) | Shakhtar Donetsk | 20 | £3.27M | 70 | 82 | £9k | +12 | — | 3★ | 4★ | 167 / 60 | High Growth |
| R. Esse | İngiltere | LM / LW (RW, CAM, LW, RM) | Crystal Palace | 20 | £3.27M | 70 | 82 | £27k | +12 | — | 2★ | 3★ | 178 / 65 | High Growth |
| William Gomes | Brezilya | LM / LW (LW, RW, LM) | FC Porto | 19 | £3.27M | 70 | 82 | £5k | +12 | — | 3★ | 3★ | 171 / 66 | High Growth |
| Š. Hrgović | Hırvatistan | LM / LW (LB, RB, LM) | Hajduk Split | 21 | £3.27M | 70 | 82 | £9k | +12 | — | 3★ | 2★ | 173 / 69 | High Growth |
| Héctor Fort | İspanya | LM / LW (RB, LB, LM) | Elche CF | 18 | £2.32M | 68 | 82 | £16k | +14 | — | 3★ | 3★ | 185 / 78 | High Growth |
| Jan Virgili | İspanya | LM / LW (LW, RW, ST, LM) | RCD Mallorca | 18 | £2.41M | 68 | 82 | £9k | +14 | — | 3★ | 4★ | 177 / 68 | High Growth |
| P. Diallo | Senegal | LM / LW (LM, LW, RM) | Norwich City | 21 | £2.58M | 68 | 82 | £10k | +14 | — | 2★ | 3★ | 182 / 67 | High Growth |
| S. Egeli | Norveç | LM / LW (RM, LM, RW) | Ipswich Town | 19 | £2.49M | 68 | 82 | £15k | +14 | — | 3★ | 3★ | 180 / 70 | High Growth |
| T. Watson | İngiltere | LM / LW (LM, RM, LW) | Brighton & Hove Albion | 19 | £2.49M | 68 | 82 | £20k | +14 | — | 3★ | 3★ | 190 / 77 | High Growth |
| Álvaro Rodríguez | Uruguay | LM / LW (ST, LW, LM) | Elche CF | 20 | £2.49M | 68 | 82 | £8k | +14 | — | 3★ | 3★ | 193 / 81 | High Growth |
| Lucas Ferreira | Brezilya | LM / LW (RW, LM, CAM, RM) | Shakhtar Donetsk | 19 | £2.06M | 67 | 82 | £6k | +15 | — | 3★ | 3★ | 187 / 74 | High Growth |
| M. Cvetković | Sırbistan | LM / LW (ST, LW) | RSC Anderlecht | 18 | £2.06M | 67 | 82 | £8k | +15 | — | 3★ | 3★ | 175 / 75 | High Growth |
| N. Irankunda | Avustralya | LM / LW (RM, ST, LM, RW) | Watford | 19 | £2.06M | 67 | 82 | £9k | +15 | Acrobat | 3★ | 3★ | 175 / 74 | High Growth |
| S. Idumbo | Belçika | LM / LW (CAM, LM, RM, CM) | AS Monaco | 20 | £2.15M | 67 | 82 | £8k | +15 | — | 3★ | 3★ | 171 / 61 | High Growth |
| M. Ponomarenko | Ukrayna | LM / LW (ST, RW, LW) | Dynamo Kyiv | 19 | £1.63M | 65 | 82 | £4k | +17 | — | 4★ | 2★ | 188 / 89 | High Growth |
| S. Campbell | South Africa | LM / LW (LW, RW, LM) | Club Brugge KV | 19 | £1.55M | 65 | 82 | £5k | +17 | — | 3★ | 3★ | 178 / 65 | High Growth |
| S. Fini | İtalya | LM / LW (RM, LM, ST, RW) | Genoa | 19 | £1.55M | 65 | 82 | £4k | +17 | — | 3★ | 3★ | 178 / 73 | High Growth |
| Sandro Vidigal | Portekiz | LM / LW (LW, RW, CAM, LM) | Sporting Clube de Braga | 17 | £1.55M | 65 | 82 | £2k | +17 | — | 4★ | 3★ | 179 / 70 | High Growth |
| L. Jovanović | Sırbistan | LM / LW (RM, LM, RW) | VfB Stuttgart | 18 | £1.29M | 64 | 82 | £5k | +18 | — | 3★ | 3★ | 184 / 76 | High Growth |
| S. Pnevmonidis | Yunanistan | LM / LW (CAM, LW, ST, CM) | Olympiacos FC | 18 | £1.29M | 64 | 82 | £4k | +18 | — | 3★ | 4★ | 178 / 61 | High Growth |
| A. Garcia | İngiltere | LM / LW (LB, RW, LW, RM) | Reading FC | 17 | £946k | 63 | 82 | £0k | +19 | — | 2★ | 3★ | 180 / 67 | High Growth |
| K. Alajbegović | Bosnia and Herzegovina | LM / LW (LM, CAM, LW) | FC Red Bull Salzburg | 17 | £1.03M | 63 | 82 | £2k | +19 | — | 4★ | 3★ | 185 / 70 | High Growth |
| Alex Marchal | İspanya | LM / LW (LW, LM) | Real Sociedad de Fútbol B | 17 | £946k | 62 | 82 | £1k | +20 | — | 3★ | 3★ | 176 / 62 | High Growth |
| L. Jetten | Hollanda | LM / LW (LB, LM) | Ajax | 18 | £946k | 62 | 82 | £2k | +20 | — | 3★ | 2★ | 166 / 61 | High Growth |
| O. Stange | Almanya | LM / LW (ST, LM) | SV Elversberg | 18 | £946k | 62 | 82 | £3k | +20 | — | 3★ | 3★ | 187 / 82 | High Growth |
| T. Sanusi | İngiltere | LM / LW (LW, RW, LM) | FC Lorient | 18 | £860k | 61 | 82 | £10k | +21 | — | 3★ | 4★ | 178 / 63 | High Growth |
| P. Villalba | Paraguay | LM / LW (LM, LW, CAM) | Libertad | 16 | £559k | 58 | 82 | £2k | +24 | — | 3★ | 3★ | 178 / 70 | High Growth |
| A. Tatu | Avustralya | LM / LW (LM, RM, LW) | Adelaide United | 17 | £452k | 57 | 82 | £0k | +25 | — | 4★ | 2★ | 175 / 69 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Sol Kanat & Sol Orta Saha (LM / LW))

- **Y. Özcan** (RSC Anderlecht) — OVR 69, POT 83: Türk kadrosu için doğal hedef; düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **K. Yıldız** (Juventus) — OVR 79, POT 89: Türk kadrosu için doğal hedef; güçlü büyüme payı.
- **A. Tatu** (Adelaide United) — OVR 57, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **P. Villalba** (Libertad) — OVR 58, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **T. Sanusi** (FC Lorient) — OVR 61, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **Hugo Pinilla** (Real Zaragoza) — OVR 62, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## 10. Santraforlar (ST / CF / SNT)

| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F. Wirtz | Almanya | SNT / CF (CAM, ST, CM) | Liverpool | 22 | £129M | 89 | 93 | £163k | +4 | Dribbler, Playmaker , Crosser, Acrobat, Complet… | 4★ | 4★ | 177 / 71 | — |
| J. Musiala | Almanya | SNT / CF (CAM, LM, CM, ST) | FC Bayern München | 22 | £115M | 88 | 92 | £95k | +4 | Dribbler, Acrobat, Clinical finisher, Complete … | 4★ | 5★ | 184 / 72 | — |
| Endrick | Brezilya | SNT / CF (ST, RW) | Real Madrid | 18 | £21.1M | 77 | 91 | £82k | +14 | — | 3★ | 4★ | 173 / 66 | High Growth |
| C. Palmer | İngiltere | SNT / CF (CAM, RM, ST) | Chelsea | 23 | £93.7M | 87 | 90 | £159k | +3 | Dribbler, Playmaker , Complete midfielder | 3★ | 4★ | 185 / 76 | — |
| Álex Baena | İspanya | SNT / CF (LM, ST, LW) | Atlético Madrid | 23 | £54.6M | 84 | 89 | £71k | +5 | — | 4★ | 3★ | 174 / 70 | — |
| Rodrigo Mora | Portekiz | SNT / CF (CAM, LW, CM, ST) | FC Porto | 18 | £15.1M | 76 | 89 | £8k | +13 | — | 4★ | 4★ | 168 / 56 | High Growth |
| H. Ekitiké | Fransa | SNT / CF (ST, CAM) | Liverpool | 23 | £47.7M | 83 | 88 | £103k | +5 | — | 3★ | 4★ | 189 / 70 | — |
| B. Šeško | Slovenia | SNT / CF (ST) | Manchester United | 22 | £40.9M | 80 | 88 | £72k | +8 | Aerial threat | 4★ | 4★ | 195 / 86 | — |
| F. Mastantuono | Arjantin | SNT / CF (CAM, RW, ST) | Real Madrid | 17 | £18.9M | 77 | 88 | £59k | +11 | — | 3★ | 3★ | 177 / 71 | — |
| X. Simons | Hollanda | SNT / CF (CAM, LM, ST) | Tottenham Hotspur | 22 | £50.3M | 84 | 87 | £108k | +3 | Dribbler, Acrobat | 3★ | 4★ | 179 / 58 | — |
| Fermín | İspanya | SNT / CF (CAM, CM, LW, ST) | FC Barcelona | 22 | £37.0M | 80 | 87 | £69k | +7 | — | 4★ | 3★ | 174 / 64 | — |
| J. Duranville | Belçika | SNT / CF (RM, LM, ST, RW) | Borussia Dortmund | 19 | £4.73M | 72 | 87 | £17k | +15 | Dribbler, Acrobat | 3★ | 5★ | 170 / 67 | Hidden Gem, High Growth |
| Pablo García | İspanya | SNT / CF (RM, ST, LM, RW) | Real Betis Balompié | 18 | £2.67M | 68 | 87 | £7k | +19 | — | 3★ | 3★ | 175 / 67 | Hidden Gem, Ucuz Cevher, High Growth |
| F. Camarda | İtalya | SNT / CF (ST) | Lecce | 17 | £1.98M | 65 | 87 | £6k | +22 | — | 3★ | 3★ | 184 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| G. Simeone | Arjantin | SNT / CF (RM, ST, LM, RW) | Atlético Madrid | 22 | £34.0M | 81 | 86 | £54k | +5 | Speedster | 3★ | 3★ | 173 / 75 | — |
| J. Durán | Kolombiya | SNT / CF (ST) | Fenerbahçe SK | 21 | £31.0M | 79 | 86 | £33k | +7 | — | 2★ | 3★ | 187 / 70 | — |
| Samu | İspanya | SNT / CF (ST) | FC Porto | 21 | £31.0M | 79 | 86 | £12k | +7 | Strength | 3★ | 3★ | 193 / 90 | — |
| M. Tel | Fransa | SNT / CF (ST, LW, CAM) | Tottenham Hotspur | 20 | £20.2M | 77 | 86 | £58k | +9 | — | 4★ | 4★ | 183 / 77 | — |
| Y. Bonny | Fransa | SNT / CF (ST, CAM) | Inter | 21 | £14.6M | 76 | 86 | £20k | +10 | — | 3★ | 4★ | 189 / 86 | — |
| L. Rodríguez | Uruguay | SNT / CF (RW, RM, ST) | NEOM SC | 21 | £9.03M | 74 | 86 | £14k | +12 | — | 4★ | 3★ | 179 / 71 | High Growth |
| M. Carrizo | Arjantin | SNT / CF (RM, CAM, ST, RW) | Vélez Sarsfield | 19 | £4.73M | 72 | 86 | £7k | +14 | — | 3★ | 3★ | 180 / 67 | Hidden Gem, High Growth |
| S. Nypan | Norveç | SNT / CF (CM, CAM, ST) | Middlesbrough | 18 | £3.01M | 69 | 86 | £25k | +17 | — | 4★ | 4★ | 183 / 70 | Hidden Gem, Ucuz Cevher, High Growth |
| Fábio Silva | Portekiz | SNT / CF (ST, LW) | Borussia Dortmund | 22 | £24.5M | 79 | 85 | £40k | +6 | — | 3★ | 4★ | 185 / 75 | — |
| Marcos Leonardo | Brezilya | SNT / CF (ST, CAM, CM) | Al Hilal | 22 | £24.5M | 79 | 85 | £38k | +6 | — | 4★ | 4★ | 175 / 72 | — |
| L. Delap | İngiltere | SNT / CF (ST) | Chelsea | 22 | £24.9M | 78 | 85 | £82k | +7 | — | 5★ | 3★ | 186 / 90 | — |
| M. Biereth | Danimarka | SNT / CF (ST) | AS Monaco | 22 | £24.9M | 78 | 85 | £28k | +7 | — | 3★ | 3★ | 187 / 78 | — |
| T. Barry | Fransa | SNT / CF (ST) | Everton | 22 | £20.6M | 77 | 85 | £33k | +8 | — | 4★ | 3★ | 195 / 82 | — |
| C. Harder | Danimarka | SNT / CF (ST, CAM, LW, CM) | RB Leipzig | 20 | £8.17M | 74 | 85 | £28k | +11 | — | 3★ | 3★ | 185 / 71 | — |
| E. Kroupi | Fransa | SNT / CF (ST) | AFC Bournemouth | 19 | £7.74M | 74 | 85 | £35k | +11 | — | 3★ | 3★ | 179 / 70 | — |
| C. Kostoulas | Yunanistan | SNT / CF (ST, CAM, RM) | Brighton & Hove Albion | 18 | £4.73M | 72 | 85 | £33k | +13 | — | 3★ | 3★ | 185 / 75 | Hidden Gem, High Growth |
| K. Konaté | Côte d'Ivoire | SNT / CF (ST) | FC Red Bull Salzburg | 21 | £5.16M | 72 | 85 | £10k | +13 | — | 4★ | 3★ | 178 / 68 | Hidden Gem, High Growth |
| R. Vermant | Belçika | SNT / CF (ST) | Club Brugge KV | 21 | £5.16M | 72 | 85 | £15k | +13 | — | 3★ | 3★ | 184 / 76 | Hidden Gem, High Growth |
| Adrián Liso | İspanya | SNT / CF (LM, ST, LW) | Getafe CF | 20 | £3.18M | 69 | 85 | £4k | +16 | — | 3★ | 3★ | 182 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| I. Subiabre | Arjantin | SNT / CF (LW, RW, ST, LM) | River Plate | 18 | £3.01M | 69 | 85 | £6k | +16 | — | 3★ | 3★ | 171 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| T. Gomis | Fransa | SNT / CF (LM, RM, ST, LW) | RB Leipzig | 18 | £2.67M | 68 | 85 | £11k | +17 | — | 3★ | 4★ | 183 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| João Pedro | Brezilya | SNT / CF (ST, CAM) | Chelsea | 23 | £23.2M | 79 | 84 | £90k | +5 | — | 4★ | 4★ | 188 / 82 | — |
| M. Beier | Almanya | SNT / CF (ST, RM, LM, RW) | Borussia Dortmund | 22 | £23.6M | 79 | 84 | £40k | +5 | — | 3★ | 4★ | 185 / 72 | — |
| N. Woltemade | Almanya | SNT / CF (ST, CAM) | Newcastle United | 23 | £23.2M | 79 | 84 | £90k | +5 | Aerial threat | 3★ | 4★ | 199 / 90 | — |
| C. Uche | Nijerya | SNT / CF (ST, CAM, CM) | Crystal Palace | 22 | £14.6M | 76 | 84 | £25k | +8 | — | 3★ | 3★ | 190 / 80 | — |
| R. Pepi | ABD | SNT / CF (ST) | PSV | 22 | £14.6M | 76 | 84 | £17k | +8 | — | 3★ | 3★ | 185 / 74 | — |
| S. Castro | Arjantin | SNT / CF (ST) | Bologna | 20 | £14.2M | 76 | 84 | £30k | +8 | — | 4★ | 4★ | 182 / 76 | — |
| Alvyn Sanches | İsviçre | SNT / CF (CAM, CM, ST) | BSC Young Boys | 22 | £6.02M | 73 | 84 | £14k | +11 | — | 3★ | 4★ | 183 / 68 | — |
| J. Enciso | Paraguay | SNT / CF (CAM, LM, RM, ST) | RC Strasbourg Alsace | 21 | £6.02M | 73 | 84 | £24k | +11 | — | 3★ | 3★ | 173 / 64 | — |
| F. Esposito | İtalya | SNT / CF (ST) | Inter | 20 | £4.73M | 72 | 84 | £15k | +12 | — | 3★ | 3★ | 191 / 76 | Hidden Gem, High Growth |
| V. Carboni | Arjantin | SNT / CF (CAM, ST, RM, CM) | Genoa | 20 | £4.73M | 72 | 84 | £13k | +12 | — | 3★ | 3★ | 185 / 78 | Hidden Gem, High Growth |
| Marc Guiu | İspanya | SNT / CF (ST) | Chelsea | 19 | £3.87M | 71 | 84 | £39k | +13 | — | 4★ | 3★ | 187 / 82 | Hidden Gem, Ucuz Cevher, High Growth |
| T. George | İngiltere | SNT / CF (LM, RM, ST, LW) | Chelsea | 19 | £3.78M | 71 | 84 | £34k | +13 | — | 4★ | 4★ | 185 / 80 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Domina | Arjantin | SNT / CF (ST) | Club Atlético Unión | 19 | £3.27M | 70 | 84 | £5k | +14 | — | 3★ | 4★ | 171 / 72 | Hidden Gem, Ucuz Cevher, High Growth |
| N. Weiper | Almanya | SNT / CF (ST, CAM, CM) | 1. FSV Mainz 05 | 20 | £3.35M | 70 | 84 | £11k | +14 | — | 3★ | 3★ | 192 / 83 | Hidden Gem, Ucuz Cevher, High Growth |
| Pau Sans | İspanya | SNT / CF (RM, LM, ST, RW) | Real Zaragoza | 20 | £3.27M | 70 | 84 | £4k | +14 | — | 3★ | 3★ | 177 / 71 | Hidden Gem, Ucuz Cevher, High Growth |
| C. Kofane | Kamerun | SNT / CF (ST) | Bayer 04 Leverkusen | 18 | £2.67M | 68 | 84 | £17k | +16 | — | 3★ | 3★ | 189 / 68 | Hidden Gem, Ucuz Cevher, High Growth |
| S. Pafundi | İtalya | SNT / CF (CAM, CM, ST) | Sampdoria | 19 | £2.67M | 68 | 84 | £5k | +16 | — | 3★ | 3★ | 166 / 64 | Hidden Gem, Ucuz Cevher, High Growth |
| J. Manzambi | İsviçre | SNT / CF (CAM, CM, CDM, ST) | SC Freiburg | 19 | £2.24M | 67 | 84 | £7k | +17 | — | 3★ | 4★ | 183 / 75 | Hidden Gem, Ucuz Cevher, High Growth |
| C. Obi | Danimarka | SNT / CF (ST) | Manchester United | 17 | £1.55M | 65 | 84 | £10k | +19 | — | 4★ | 2★ | 188 / 81 | Hidden Gem, Ucuz Cevher, High Growth |
| Dani Díaz | İspanya | SNT / CF (RM, ST, RW) | Real Sociedad de Fútbol B | 19 | £1.29M | 63 | 84 | £1k | +21 | — | 3★ | 3★ | 165 / 58 | Hidden Gem, Ucuz Cevher, High Growth |
| E. Emegha | Hollanda | SNT / CF (ST) | RC Strasbourg Alsace | 22 | £18.9M | 78 | 83 | £43k | +5 | Aerial threat | 5★ | 3★ | 195 / 82 | — |
| A. Hložek | Czechia | SNT / CF (ST, RM, CAM, RW) | TSG 1899 Hoffenheim | 22 | £14.6M | 77 | 83 | £28k | +6 | — | 4★ | 3★ | 188 / 84 | — |
| B. Brobbey | Hollanda | SNT / CF (ST) | Sunderland | 23 | £14.6M | 77 | 83 | £45k | +6 | Strength | 4★ | 3★ | 180 / 78 | — |
| G. Rutter | Fransa | SNT / CF (CAM, ST) | Brighton & Hove Albion | 23 | £14.2M | 77 | 83 | £58k | +6 | — | 5★ | 5★ | 182 / 83 | — |
| M. Cho | Fransa | SNT / CF (LW, RW, ST, LM) | OGC Nice | 21 | £12.9M | 76 | 83 | £18k | +7 | — | 3★ | 3★ | 181 / 66 | — |
| R. Højlund | Danimarka | SNT / CF (ST) | Napoli | 22 | £13.3M | 76 | 83 | £54k | +7 | — | 3★ | 3★ | 191 / 79 | — |
| F. Ivanović | Hırvatistan | SNT / CF (ST, CAM) | SL Benfica | 21 | £10.8M | 75 | 83 | £13k | +8 | — | 3★ | 3★ | 185 / 78 | — |
| L. Stassin | Belçika | SNT / CF (ST) | AS Saint-Étienne | 20 | £10.8M | 75 | 83 | £7k | +8 | — | 3★ | 2★ | 183 / 71 | — |
| C. Uzun | Türkiye | SNT / CF (CAM, ST, CM) | Eintracht Frankfurt | 19 | £7.74M | 74 | 83 | £15k | +9 | — | 3★ | 4★ | 186 / 70 | Türk Yeteneği |
| Gabriel Silva | Brezilya | SNT / CF (LW, ST, RM, LM) | Santa Clara | 23 | £8.17M | 74 | 83 | £8k | +9 | Speedster | 3★ | 3★ | 177 / 69 | — |
| J. Panichelli | Arjantin | SNT / CF (ST) | RC Strasbourg Alsace | 22 | £8.17M | 74 | 83 | £33k | +9 | — | 3★ | 3★ | 190 / 82 | — |
| O. Óskarsson | Iceland | SNT / CF (ST) | Real Sociedad | 20 | £8.17M | 74 | 83 | £22k | +9 | — | 3★ | 2★ | 186 / 76 | — |
| Óscar Aranda | İspanya | SNT / CF (LM, ST, RM, LW) | Famalicão | 23 | £8.17M | 74 | 83 | £9k | +9 | — | 4★ | 4★ | 181 / 78 | — |
| M. Frigan | Hırvatistan | SNT / CF (ST) | Parma | 22 | £6.02M | 73 | 83 | £14k | +10 | — | 4★ | 2★ | 185 / 78 | — |
| M. Meerdink | Hollanda | SNT / CF (ST) | AZ Alkmaar | 21 | £6.02M | 73 | 83 | £11k | +10 | — | 3★ | 4★ | 183 / 68 | — |
| Kauã Elias | Brezilya | SNT / CF (ST) | Shakhtar Donetsk | 19 | £3.87M | 71 | 83 | £9k | +12 | — | 3★ | 4★ | 181 / 71 | Ucuz Cevher, High Growth |
| I. Gueye | Senegal | SNT / CF (ST) | Udinese | 18 | £3.18M | 70 | 83 | £6k | +13 | — | 3★ | 3★ | 185 / 66 | Ucuz Cevher, High Growth |
| M. Meïté | Fransa | SNT / CF (ST) | Stade Rennais FC | 17 | £3.18M | 70 | 83 | £8k | +13 | — | 3★ | 3★ | 192 / 80 | Ucuz Cevher, High Growth |
| M. Krattenmacher | Almanya | SNT / CF (CAM, ST, CM) | Hertha BSC | 19 | £2.84M | 69 | 83 | £15k | +14 | — | 5★ | 3★ | 180 / 75 | Ucuz Cevher, High Growth |
| N. Tresoldi | Almanya | SNT / CF (ST) | Club Brugge KV | 20 | £2.92M | 69 | 83 | £10k | +14 | — | 3★ | 3★ | 183 / 77 | Ucuz Cevher, High Growth |
| Carlos Espí | İspanya | SNT / CF (ST) | Levante UD | 19 | £2.49M | 68 | 83 | £9k | +15 | Aerial threat | 3★ | 3★ | 194 / 80 | Ucuz Cevher, High Growth |
| N. Wurmbrand | Avusturya | SNT / CF (RM, ST, RW) | SK Rapid | 19 | £2.49M | 68 | 83 | £5k | +15 | — | 4★ | 3★ | 172 / 75 | Ucuz Cevher, High Growth |
| Thalys | Brezilya | SNT / CF (ST) | UD Almería | 20 | £2.49M | 68 | 83 | £3k | +15 | — | 3★ | 2★ | 184 / 72 | Ucuz Cevher, High Growth |
| M. Melia | Republic of Ireland | SNT / CF (ST) | St Patrick's Athletic FC | 17 | £1.29M | 64 | 83 | £0k | +19 | — | 4★ | 2★ | 186 / 78 | Ucuz Cevher, High Growth |
| A. Stepanov | Ukrayna | SNT / CF (ST) | 1. FC Nürnberg | 17 | £1.12M | 63 | 83 | £8k | +20 | — | 3★ | 2★ | 192 / 88 | Ucuz Cevher, High Growth |
| K. Furo | Belçika | SNT / CF (ST) | Club Brugge KV | 18 | £1.12M | 63 | 83 | £4k | +20 | — | 4★ | 2★ | 190 / 80 | Ucuz Cevher, High Growth |
| A. Kalimuendo | Fransa | SNT / CF (ST) | Nottingham Forest | 23 | £17.6M | 78 | 82 | £66k | +4 | — | 3★ | 3★ | 178 / 79 | — |
| F. Balogun | ABD | SNT / CF (ST, CAM) | AS Monaco | 23 | £13.8M | 77 | 82 | £26k | +5 | — | 4★ | 3★ | 178 / 66 | — |
| M. Abline | Fransa | SNT / CF (ST, RW, RM) | FC Nantes | 22 | £10.3M | 76 | 82 | £15k | +6 | — | 3★ | 3★ | 182 / 81 | — |
| Rômulo | Brezilya | SNT / CF (ST, LW, CAM) | RB Leipzig | 23 | £10.3M | 76 | 82 | £36k | +6 | — | 3★ | 3★ | 193 / 80 | — |
| Tiago Tomás | Portekiz | SNT / CF (LW, LM, ST) | VfB Stuttgart | 23 | £10.3M | 76 | 82 | £28k | +6 | — | 3★ | 4★ | 180 / 78 | — |
| C. Alcaraz | Arjantin | SNT / CF (CAM, CM, ST) | Everton | 22 | £9.89M | 75 | 82 | £28k | +7 | — | 3★ | 4★ | 176 / 70 | — |
| E. Wahi | Fransa | SNT / CF (ST) | Eintracht Frankfurt | 22 | £9.89M | 75 | 82 | £23k | +7 | — | 4★ | 4★ | 181 / 77 | — |
| S. Esposito | İtalya | SNT / CF (ST, CAM) | Cagliari | 22 | £9.89M | 75 | 82 | £22k | +7 | — | 5★ | 4★ | 183 / 73 | — |
| L. Munteanu | Romanya | SNT / CF (ST, CAM) | CFR Cluj | 23 | £8.17M | 74 | 82 | £6k | +8 | Acrobat | 3★ | 3★ | 184 / 80 | — |
| M. Kvistgaarden | Danimarka | SNT / CF (ST, LW, RW, LM) | Norwich City | 23 | £8.17M | 74 | 82 | £25k | +8 | — | 3★ | 3★ | 175 / 68 | — |
| M. Röhl | Almanya | SNT / CF (CAM, CM, CDM, ST) | Everton | 22 | £8.17M | 74 | 82 | £18k | +8 | — | 4★ | 3★ | 192 / 79 | — |
| E. Ferguson | Republic of Ireland | SNT / CF (ST) | Roma | 20 | £5.59M | 73 | 82 | £40k | +9 | — | 3★ | 3★ | 188 / 78 | — |
| H. Igamane | Fas | SNT / CF (ST, LM, CAM) | Lille OSC | 22 | £6.02M | 73 | 82 | £18k | +9 | — | 4★ | 4★ | 181 / 77 | — |
| Peque | İspanya | SNT / CF (CAM, LW, ST, CM) | Sevilla FC | 22 | £6.02M | 73 | 82 | £18k | +9 | — | 4★ | 3★ | 172 / 65 | — |
| G. Ilenikhena | Nijerya | SNT / CF (ST) | AS Monaco | 18 | £4.30M | 72 | 82 | £14k | +10 | — | 3★ | 3★ | 185 / 76 | — |
| O. Diakité | Côte d'Ivoire | SNT / CF (ST) | Cercle Brugge KSV | 21 | £4.73M | 72 | 82 | £5k | +10 | — | 3★ | 2★ | 182 / 75 | — |
| E. Mayenda | İspanya | SNT / CF (ST, RM, LM, RW) | Sunderland | 20 | £3.53M | 71 | 82 | £24k | +11 | — | 2★ | 2★ | 180 / 75 | — |
| J. Recoba | Uruguay | SNT / CF (LW, CAM, ST, LM) | UD Las Palmas | 21 | £3.61M | 71 | 82 | £4k | +11 | — | 3★ | 3★ | 177 / 75 | — |
| C. Irié | Burkina Faso | SNT / CF (RM, ST, RW) | SC Freiburg | 20 | £3.27M | 70 | 82 | £10k | +12 | — | 2★ | 3★ | 185 / 78 | High Growth |
| Eguinaldo | Brezilya | SNT / CF (LM, LW, ST) | Shakhtar Donetsk | 20 | £3.27M | 70 | 82 | £8k | +12 | — | 4★ | 3★ | 175 / 69 | High Growth |
| Gonzalo | İspanya | SNT / CF (ST) | Real Madrid | 21 | £3.01M | 69 | 82 | £43k | +13 | — | 4★ | 3★ | 182 / 82 | High Growth |
| A. Ruberto | Arjantin | SNT / CF (ST) | River Plate | 19 | £2.49M | 68 | 82 | £6k | +14 | — | 3★ | 2★ | 183 / 80 | High Growth |
| Jan Virgili | İspanya | SNT / CF (LW, RW, ST, LM) | RCD Mallorca | 18 | £2.41M | 68 | 82 | £9k | +14 | — | 3★ | 4★ | 177 / 68 | High Growth |
| Z. Gruber | Macaristan | SNT / CF (ST, RW, RM) | Ferencvárosi Torna Club | 20 | £2.49M | 68 | 82 | £8k | +14 | — | 3★ | 2★ | 180 / 73 | High Growth |
| Álvaro Rodríguez | Uruguay | SNT / CF (ST, LW, LM) | Elche CF | 20 | £2.49M | 68 | 82 | £8k | +14 | — | 3★ | 3★ | 193 / 81 | High Growth |
| M. Cvetković | Sırbistan | SNT / CF (ST, LW) | RSC Anderlecht | 18 | £2.06M | 67 | 82 | £8k | +15 | — | 3★ | 3★ | 175 / 75 | High Growth |
| N. Irankunda | Avustralya | SNT / CF (RM, ST, LM, RW) | Watford | 19 | £2.06M | 67 | 82 | £9k | +15 | Acrobat | 3★ | 3★ | 175 / 74 | High Growth |
| Nacho Ferri | İspanya | SNT / CF (ST) | KVC Westerlo | 20 | £2.15M | 67 | 82 | £4k | +15 | — | 3★ | 2★ | 192 / 80 | High Growth |
| B. Burrowes | İngiltere | SNT / CF (RM, ST, RW) | Aston Villa | 17 | £1.55M | 65 | 82 | £10k | +17 | — | 3★ | 3★ | 179 / 75 | High Growth |
| M. Ponomarenko | Ukrayna | SNT / CF (ST, RW, LW) | Dynamo Kyiv | 19 | £1.63M | 65 | 82 | £4k | +17 | — | 4★ | 2★ | 188 / 89 | High Growth |
| S. Fini | İtalya | SNT / CF (RM, LM, ST, RW) | Genoa | 19 | £1.55M | 65 | 82 | £4k | +17 | — | 3★ | 3★ | 178 / 73 | High Growth |
| R. Vaz | Fransa | SNT / CF (ST) | Olympique de Marseille | 18 | £1.29M | 64 | 82 | £6k | +18 | — | 3★ | 3★ | 186 / 75 | High Growth |
| S. Pnevmonidis | Yunanistan | SNT / CF (CAM, LW, ST, CM) | Olympiacos FC | 18 | £1.29M | 64 | 82 | £4k | +18 | — | 3★ | 4★ | 178 / 61 | High Growth |
| D. Konadu | Hollanda | SNT / CF (ST) | Ajax | 19 | £1.12M | 63 | 82 | £3k | +19 | — | 3★ | 2★ | 190 / 77 | High Growth |
| J. Wilson | Scotland | SNT / CF (ST) | Hearts | 18 | £1.03M | 63 | 82 | £2k | +19 | — | 3★ | 2★ | 170 / 70 | High Growth |
| O. Stange | Almanya | SNT / CF (ST, LM) | SV Elversberg | 18 | £946k | 62 | 82 | £3k | +20 | — | 3★ | 3★ | 187 / 82 | High Growth |
| J. Kusi-Asare | İsveç | SNT / CF (ST) | Fulham FC | 17 | £666k | 60 | 82 | £4k | +22 | — | 3★ | 2★ | 196 / 84 | High Growth |
| I. Tyjon | İngiltere | SNT / CF (ST) | Blackburn Rovers | 17 | £452k | 57 | 82 | £3k | +25 | — | 3★ | 2★ | 181 / 71 | High Growth |

### Hidden Gems & Turkish Talents Recommendation (Santraforlar (ST / CF / SNT))

- **C. Uzun** (Eintracht Frankfurt) — OVR 74, POT 83: Türk kadrosu için doğal hedef; düşük başlangıç OVR ile gizli cevher profili.
- **I. Tyjon** (Blackburn Rovers) — OVR 57, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **J. Kusi-Asare** (Fulham FC) — OVR 60, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **O. Stange** (SV Elversberg) — OVR 62, POT 82: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **Dani Díaz** (Real Sociedad de Fútbol B) — OVR 63, POT 84: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.
- **K. Furo** (Club Brugge KV) — OVR 63, POT 83: düşük piyasa değeri; güçlü büyüme payı; düşük başlangıç OVR ile gizli cevher profili.

## Bonus: Overall Top 11 Wonderkid XI (veri setine göre)

Formasyon: **4-3-3** (geniş). Her slotta **birincil mevki** (`player_positions` içinde virgülden önceki kod) kullanılır; böylece örn. `CM, CDM` oyuncuları CDM değil CM hattında değerlendirilir. Seçim: en yüksek POT (eşitlikte OVR); aynı oyuncu iki kez kullanılmaz.

| Pozisyon | Oyuncu | Takım | OVR | POT |
|---|---|---|---|---|
| KL | L. Chevalier | Paris Saint-Germain | 83 | 88 |
| D(Sağ) | G. Read | Feyenoord | 75 | 88 |
| D(M) #1 | W. Pacho | Paris Saint-Germain | 86 | 89 |
| D(M) #2 | P. Hincapié | Arsenal | 83 | 89 |
| D(Sol) | Nuno Mendes | Paris Saint-Germain | 86 | 89 |
| DOS | M. Caicedo | Chelsea | 87 | 89 |
| OS(M) #1 | Pedri | FC Barcelona | 89 | 93 |
| OS(M) #2 | João Neves | Paris Saint-Germain | 85 | 90 |
| RM/RW | Lamine Yamal | FC Barcelona | 89 | 95 |
| LM/LW | Nico Williams | Athletic Club | 86 | 89 |
| SNT | Endrick | Real Madrid | 77 | 91 |

## Bonus: Budget Wonderkid Team (~£50M)

Aşağıdaki kadro, filtrelenmiş havuzdan **düşük `value_eur`** ve **yüksek `potential - overall`** skoruna göre otomatik seçilmiştir; transfer ücretleri oyun içi pazarlıkla değişir.

| Rol | Oyuncu | Takım | Değer (£) | OVR | POT |
|---|---|---|---|---|---|
| KL | L. Brughmans | KRC Genk | £538k | 59 | 82 |
| RB | J. von der Hitz | 1. FC Nürnberg | £666k | 60 | 82 |
| CB | J. Orozco Chiquete | Serbest Oyuncu | — | 73 | 83 |
| CB | A. Natali | AZ Alkmaar | £624k | 60 | 82 |
| LB | L. Jakirović | Dinamo Zagreb | £838k | 61 | 82 |
| CDM | B. Mamuzah Lum | Hertha BSC | £645k | 60 | 82 |
| CM | F. Onyeka | VfL Bochum 1848 | £666k | 60 | 83 |
| CAM | P. Villalba | Libertad | £559k | 58 | 82 |
| RM | A. Tatu | Adelaide United | £452k | 57 | 82 |
| LM | T. Sanusi | FC Lorient | £860k | 61 | 82 |
| ST | I. Tyjon | Blackburn Rovers | £452k | 57 | 82 |

- **Yaklaşık toplam değer (liste fiyatı, £):** £6.3M
