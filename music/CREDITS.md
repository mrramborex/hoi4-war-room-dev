# TOBS Music Credits — Full Historical Recordings

## Library of Congress — National Jukebox Data Package

**Suggested credit:** Library of Congress, National Jukebox.

Official source and rights statement: https://data.labs.loc.gov/jukebox/
Dataset documentation: https://data.labs.loc.gov/jukebox/README.html
Official per-file manifest and MD5 checksum evidence: https://data.labs.loc.gov/jukebox/manifest.html

The dataset includes complete historical recordings from 1900–1922 that the Library of Congress regards as public domain in the United States. The files were retrieved from the Library's official dataset, and MD5 checksums were matched to its file manifest. Do not substitute different recordings or restorations without validating their rights separately.

### WRS Victory Ballroom — United States

| Complete historic recording | LOC catalog item | File |
| --- | --- | --- |
| 'Joe Turner Blues' Medley | https://www.loc.gov/item/jukebox-19795/ | `audio/tobs-full-joe-turner-blues.mp3` |
| 12th Street Rag | https://www.loc.gov/item/jukebox-38191/ | `audio/tobs-full-12th-street-rag.mp3` |
| A Classical Spasm | https://www.loc.gov/item/jukebox-20378/ | `audio/tobs-full-classical-spasm.mp3` |
| A Rag-Time Episode | https://www.loc.gov/item/jukebox-129854/ | `audio/tobs-full-rag-time-episode.mp3` |
| After You've Gone | https://www.loc.gov/item/jukebox-313413/ | `audio/tobs-full-after-youve-gone.mp3` |

The full-length recordings replaced five short Citizen DJ excerpt files on 2026-11-15. All seven original synthetic station test clips were removed before this update.

Import sources and validation: `music/loc-full-recordings.json`, `music/import_loc_full.py`, `.github/workflows/import-loc-full.yml`.

**Rights rule:** Only recordings with documented public-domain status or an explicit free-use license permitting intended website redistribution are eligible. Other researched recordings remain outside the playable radio until they meet that gate.

## International repertoire — LOC National Jukebox Batch 1

Ten additional complete historical MP3 recordings imported on 2026-11-15, validated against individual official Library of Congress MD5 file checksums. They date from 1900–1922 and are drawn from the same public-domain-designated National Jukebox data package. Source and checksum index: https://data.labs.loc.gov/jukebox/manifest.html. **These recordings were made on Victor records in the United States**, and the station selections reflect language and musical repertoire, not original national radio broadcasts.

### United Kingdom

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| A Bowl of Roses | [LOC 131863](https://www.loc.gov/item/jukebox-131863/) | Marguerite Dunlap; music Robert Coningsby Clarke, lyrics W.E. Henley | `audio/tobs-international-131863.mp3` |
| A Child's Song | [LOC 259778](https://www.loc.gov/item/jukebox-259778/) | John McCormack; lyrics Thomas Moore, music Charles Marshall | `audio/tobs-international-259778.mp3` |

### France

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| Adieu, notre petite table | [LOC 127011](https://www.loc.gov/item/jukebox-127011/) | Geraldine Farrar; Jules Massenet | `audio/tobs-international-127011.mp3` |
| Air de Lia | [LOC 129652](https://www.loc.gov/item/jukebox-129652/) | Jeanne Gerville-Réache; Claude Debussy | `audio/tobs-international-129652.mp3` |

### Germany

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| Aus der Jugendzeit | [LOC 213054](https://www.loc.gov/item/jukebox-213054/) | Emil Muench; Robert Radecke | `audio/tobs-international-213054.mp3` |
| Bärbchen | [LOC 127819](https://www.loc.gov/item/jukebox-127819/) | Ernestine Schumann-Heink; Hans Hermann | `audio/tobs-international-127819.mp3` |

### Italy

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| A tanto amor | [LOC 28011](https://www.loc.gov/item/jukebox-28011/) | Giuseppe De Luca; Gaetano Donizetti | `audio/tobs-international-28011.mp3` |
| Abbietta zingara | [LOC 187534](https://www.loc.gov/item/jukebox-187534/) | Marcel Journet; Giuseppe Verdi | `audio/tobs-international-187534.mp3` |

### Soviet Union (historical pre-Soviet Russian repertoire)

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| Eugene Onegin — Aria | [LOC 122060](https://www.loc.gov/item/jukebox-122060/) | Albert G. Janpolski; Pyotr Ilyich Tchaikovsky (pre-Soviet historical Russian repertoire) | `audio/tobs-international-122060.mp3` |
| Douchechka devitza | [LOC 16142](https://www.loc.gov/item/jukebox-16142/) | Nina Dimitrieff; Alexander Dargomyzhsky (pre-Soviet historical Russian repertoire) | `audio/tobs-international-16142.mp3` |

Japan is deliberately not included yet: no suitable Japanese-language music was found within this particular LOC dataset. Our public-domain/free-use gate still applies to other sources.

## Sakura Denpa — Japan (82.6 MHz)

Two complete historical Japanese performances, sourced as **original OGG files** from Wikimedia Commons and checked against the Commons original-file SHA1 and file size during import. Commons explicitly identifies the underlying compositions/lyrics, performances and historical Japanese sound-recording rights as public domain (including U.S. pre-1926 sound-recording eligibility). These files were uploaded to Commons from online historical transfers; do not replace them with later commercial remasters without fresh rights verification.

| Performance | Date | Historical credits | Source | Local file |
| --- | --- | --- | --- | --- |
| Gunkan kōshinkyoku (Warship March) | 1913 | Fumiko Nōsho; Tokichi Setoguchi; Hiraku Toriyama | https://commons.wikimedia.org/wiki/File:Gunkan_k%C5%8Dshinkyoku_(1913).ogg | `audio/tobs-japan-gunkan-1913.ogg` |
| Teki wa Ikuman | Before 1913 | Nōsho Benjirō; Sakunosuke Koyama; Yamada Bimyō | https://commons.wikimedia.org/wiki/File:Teki_wa_Ikuman_(N%C5%8Dsho_Benjir%C5%8D).ogg | `audio/tobs-japan-teki-wa-ikuman.ogg` |

The Japanese playlist currently has two historical **military** pieces, not a balanced representation of civilian music; expand with verified traditional and popular repertoire when eligible recordings are found. Source identities and validation procedure: `music/japan-recordings-batch-1.json`, `music/import_japan_recordings.py`.

## Phase 23C.4 — Major-Power Expansion (10 full-length recordings)

Source: [Library of Congress National Jukebox 1900–1922 dataset](https://data.labs.loc.gov/jukebox/). Rights statement: https://data.labs.loc.gov/jukebox/README.html . Every MP3 was independently verified against its exact MD5 at https://data.labs.loc.gov/jukebox/manifest.html before import.

### United Kingdom

| Complete performance | LOC item | Historical credits | Local file |
| --- | --- | --- | --- |
| A Farewell | [259782](https://www.loc.gov/item/jukebox-259782/) | John McCormack; Charles Kingsley and Samuel Liddle | `audio/tobs-major-batch2-259782.mp3` |
| A Little Bit of Heaven | [12879](https://www.loc.gov/item/jukebox-12879/) | Charles Harrison; Ernest R. Ball and J. Keirn Brennan | `audio/tobs-major-batch2-12879.mp3` |

### France

| Complete performance | LOC item | Historical credits | Local file |
| --- | --- | --- | --- |
| Ah! fuyez, douce image | [131294](https://www.loc.gov/item/jukebox-131294/) | Enrico Caruso; Jules Massenet | `audio/tobs-major-batch2-131294.mp3` |
| Au fond du temple saint | [131400](https://www.loc.gov/item/jukebox-131400/) | Edmond Clément and Marcel Journet; Georges Bizet | `audio/tobs-major-batch2-131400.mp3` |

### Germany

| Complete performance | LOC item | Historical credits | Local file |
| --- | --- | --- | --- |
| Der Tannenbaum | [122801](https://www.loc.gov/item/jukebox-122801/) | Emil Muench; traditional song, Joachim August Zarnack lyrics | `audio/tobs-major-batch2-122801.mp3` |
| Der Tod und das Mädchen | [125293](https://www.loc.gov/item/jukebox-125293/) | Ernestine Schumann-Heink; Franz Schubert and Matthias Claudius | `audio/tobs-major-batch2-125293.mp3` |

### Italy

| Complete performance | LOC item | Historical credits | Local file |
| --- | --- | --- | --- |
| Addio del passato | [134548](https://www.loc.gov/item/jukebox-134548/) | Lucrezia Bori; Giuseppe Verdi | `audio/tobs-major-batch2-134548.mp3` |
| Ah! non credea mirarti | [24085](https://www.loc.gov/item/jukebox-24085/) | Amelita Galli-Curci; Vincenzo Bellini | `audio/tobs-major-batch2-24085.mp3` |

### Soviet Union

| Complete performance | LOC item | Historical credits | Local file |
| --- | --- | --- | --- |
| Oi kasala mene mati | [16147](https://www.loc.gov/item/jukebox-16147/) | Nina Dimitrieff; Russian/Ukrainian traditional repertoire as described by LOC | `audio/tobs-major-batch2-16147.mp3` |
| Song of the Volga Boatmen | [41296](https://www.loc.gov/item/jukebox-41296/) | Emilio de Gogorza; traditional Russian repertoire, Edward Bromberg arrangement | `audio/tobs-major-batch2-41296.mp3` |

**Historical context:** Source performances are earlier than 1923 and were not genuine wartime national-radio transmissions. Station curation is based on musical or language relevance. The Soviet Union station includes pre-Soviet Russian repertoire; do not describe the originals as Soviet-era recordings. Japanese selections remain unchanged.

## Phase 23C.5 — Rejected prototypes

Six newly synthesized WWII-era-inspired instrumentals were **rejected after listening review** because they sounded artificial compared with authentic archival music. All six were removed from the development playlists and media files on 2026-11-15. This section is a historical note, not playable-music credits. Prefer credible original historical performances with documented public-domain or free-use rights; do not restore these recordings.

## Phase 23C.7 — Poland: Polskie Echo (89.5 MHz)

**Ulan (Pieśń Narodowa)** — Original Polish/Russian folk-song performance, 1916-03-30. Performed by tenor Jakov M. Medvedieff with King's Orchestra, Edward T. King conducting. This is real archival audio, not an AI-generated tune, and **not a WWII-era recording**. Recording originally made in the United States; assigned to Poland for Polish-language folk repertoire.

- Official Library of Congress catalog: https://www.loc.gov/item/jukebox-17105/
- Rights: https://www.loc.gov/collections/national-jukebox/about-this-collection/rights-and-access/
- Complete MP3 from LOC dataset: https://data.labs.loc.gov/jukebox/audio/jukebox-17105_1.mp3
- Official MD5 verified: `528e0097e369e015186ecd03a41d8367` (https://data.labs.loc.gov/jukebox/manifest.html)
- TOBS file: `audio/tobs-poland-ulan-1916.mp3`

No synthetic music was reintroduced. Authentic 1936–1945 recordings still require item-level verification of recording and underlying work rights before adding to public audio.

## Phase 23C.8 — British historical songs (two full original 1914 performances)

These are two different complete original recordings of *It's a Long, Long Way to Tipperary* (1914). This is **WWI-associated music, not WWII-era recordings**, but historically authentic songs. Both pre-1923 recordings were validated against [LOC official MD5 hashes](https://data.labs.loc.gov/jukebox/manifest.html) and the [LOC public-domain dataset rights statement](https://data.labs.loc.gov/jukebox/README.html).

| Original performer | Recording date | LOC item | Original checksum (MD5) | TOBS file |
| --- | --- | --- | --- | --- |
| Harry Macdonough, William F. Hooley, John McCormack and Reinald Werrenrath; Jack Judge and Harry Williams | 1914-11-23 | [jukebox-11634](https://www.loc.gov/item/jukebox-11634/) | `6c19d14dda3babf8961e35e3eb20e315` | `audio/tobs-uk-tipperary-11634.mp3` |
| American Quartet (Billy Murray, Steve Porter, Robert D. Armour and William F. Hooley); Jack Judge and Harry Williams | 1914-09-15 | [jukebox-11094](https://www.loc.gov/item/jukebox-11094/) | `5879894a21f61b11ebf50439a070b540` | `audio/tobs-uk-tipperary-11094.mp3` |

The eight MP3s in the user's personal WW2 Music.rar archive were not copied to the public GitHub repo. They remain accessible through the browser-local personal file picker, without any upload.

## Phase 23C.9 — French, German, Austrian historical recordings

All three are genuine pre-1923 recordings obtained as complete MP3s from the Library of Congress National Jukebox. Each source MP3 matched the exact entry in the [LOC dataset MD5 manifest](https://data.labs.loc.gov/jukebox/manifest.html). No WWII-era master is claimed; region assignment is based on the composition or repertoire, not the place of recording.

| TOBS station | Historic composition and recording | Date | Performers and composer | LOC catalog and original MD5 |
| --- | --- | --- | --- | --- |
| France | La Marseillaise — Emilio de Gogorza and Carlos Francisco | 1905-01-10 | Emilio de Gogorza and Carlos Francisco, baritones; Claude Joseph Rouget de Lisle, composer | [LOC 121062](https://www.loc.gov/item/jukebox-121062/), `b1a53d7652a77e750d2a5345c255a0a2` |
| Germany | Deutschland über alles — Carl Schlegel | 1914-11-10 | Carl Schlegel, baritone; Walter B. Rogers, conductor; Joseph Haydn, composer | [LOC 187660](https://www.loc.gov/item/jukebox-187660/), `b1b0e6542a9bdf9a5ba2c3161de7dcab` |
| Austria | Brüderlein fein — Frida Bennèche | 1916-08-02 | Frida Bennèche, soprano; King's Orchestra; Edward T. King, conductor; Joseph Drechsler, composer; Ferdinand Raimund, playwright | [LOC 19147](https://www.loc.gov/item/jukebox-19147/), `8f8e101854e99b41ecf1b021102acc0b` |

Both the 1914 German national song and the French anthem are used as period historical documentation, not endorsement of any political ideology. Austrian *Brüderlein fein* is part of a Viennese theatrical tradition, but was recorded in the United States. The source recordings are pre-WWII; no user-provided private audio has been published.

## Phase 23C.10 — Northern Europe, Mexico, and Poland (nine authentic recordings)

All nine complete original recordings are from the [Library of Congress National Jukebox dataset](https://data.labs.loc.gov/jukebox/) and **matched their individual official MD5 checksums** in the [LOC manifest](https://data.labs.loc.gov/jukebox/manifest.html). These are recordings from **1906–1916**, not WWII-era performances or actual period national broadcasts. Station assignments are based on cultural repertoire/language/ensemble, never on the location of the studio. The Danish-language selection *Fritz og Lise* is a performance of a French-composed Offenbach work; it is explicitly **Danish-language programming**, not native Danish composition.

| Station | Recording | Original date | Original performance credits | LOC source and MD5 |
| --- | --- | --- | --- | --- |
| Sweden | Drick ur ditt glas | 1906-07-12 | Joel Mossberg (baritone); Carl Michael Bellman (composer) | [LOC 123353](https://www.loc.gov/item/jukebox-123353/), `b272e29b39c295e2176891490bc179bf` |
| Sweden | Hell dig, du höga Nord! | 1916-03-03 | Aage Wang-Holm (tenor); King's Orchestra; Bernhard Henrik Crusell (composer) | [LOC 16725](https://www.loc.gov/item/jukebox-16725/), `ea5c5fbe89201f20de39e7bca2f179f7` |
| Norway | Hun er sød, hun er blid | 1913-10-08 | Carsten Woll (tenor), Fred Bachman (piano); Halfdan Kjerulf (composer) | [LOC 133882](https://www.loc.gov/item/jukebox-133882/), `463f5ccf021e4bf3889c7634b582bef0` |
| Norway | Sæterjentens søndag | 1913-10-09 | Carsten Woll (tenor), Fred Bachman (piano); Ole Bull (composer) | [LOC 133885](https://www.loc.gov/item/jukebox-133885/), `816d1264a2db0900a9a88f0581e63814` |
| Finland | Taivas on sininen ja valkoinen | 1916-06-27 | Elli Suokas (soprano), King's Orchestra; Edward T. King (conductor) | [LOC 18368](https://www.loc.gov/item/jukebox-18368/), `fa13b52aa461c1921efa4bfee8dbfda8` |
| Finland | Ei taivahan alla | 1916-06-27 | Elli Suokas (soprano), King's Orchestra; Edward T. King (conductor) | [LOC 18369](https://www.loc.gov/item/jukebox-18369/), `403b5fc593c7a23e6b088f27f53ecb5d` |
| Denmark | Fritz og Lise | 1906-12-06 | Gudrun Carlson (soprano), Johannes Herskind; Jacques Offenbach (composer) | [LOC 124182](https://www.loc.gov/item/jukebox-124182/), `1550e45e48f71724355d2586d6423ed9` |
| Mexico | Adela | 1914-12-01 | Banda Rodríguez; Walter B. Rogers (conductor); E. Navarro (composer) | [LOC 258926](https://www.loc.gov/item/jukebox-258926/), `f8513e7856f71bdcabc98137daec5498` |
| Poland | Krakowiak | 1911-07-20 | Rybowiak Orchestra; A. E. Brunner (composer) | [LOC 130659](https://www.loc.gov/item/jukebox-130659/), `6da5c7bd15f864e0e2a296e1310f2411` |

All nine MP3s are in `audio/tobs-minors-batch4-[item-id].mp3`; the machine-readable source table is `music/minor-batch4-sources.json`. Authentic 1936–1945 songs are still under research due to rights restrictions; no rejected synthetic instrumentals or commercially restricted uploads were added.

## Phase 23C.11 — Argentina, Brazil, Greece, and Mexico (5 original complete recordings)

All five historic master files were included in the [LOC National Jukebox downloadable dataset](https://data.labs.loc.gov/jukebox/), dated before 1923 and matched to the item's official MD5 recording checksum. **These recordings are not WWII-era recordings.** Station assignment reflects musical or regional repertoire, not where the performances were recorded.

| TOBS station | Historical performance | Original record date | Credits | Original source / MD5 |
| --- | --- | --- | --- | --- |
| Argentina | Mi ricurita — tango | 1915-11-30 | Victor Orchestra, Edward T. King (conductor); Osmán Pérez Freire (composer) | [LOC 15618](https://www.loc.gov/item/jukebox-15618/), `46e3b1c896e45ac31e217cee08340bf0` |
| Brazil | A madrugada exul | 1908-05-04 | Roxy King (soprano), Victor Orchestra; Leopoldo Miguez (Brazilian composer) | [LOC 126387](https://www.loc.gov/item/jukebox-126387/), `ea5e0e834609f1d5fe892103a6be1ff2` |
| Greece | Estudiantina waltz | 1916 | Athenian Mandolin Quartet; Émile Waldteufel / Paul Lacome (composer credit per LOC) | [LOC 16628](https://www.loc.gov/item/jukebox-16628/), `bf39cfaa93f0fcefa49cba5dcd2a72ac` |
| Greece | Spanish rhapsody | 1916 | Athenian Mandolin Quartet; Simone Salvetti (composer per LOC) | [LOC 16627](https://www.loc.gov/item/jukebox-16627/), `782dae0e613ad38101516529b0c1c44b` |
| Mexico | Alejandra | 1910s | Banda Rodríguez, Victor Band; E. Navarro (composer) | [LOC 12663](https://www.loc.gov/item/jukebox-12663/), `fd8e54e799e2e4893aca1e9f754a4ee4` |

**Context:** The Athenian Mandolin Quartet's two recordings are European repertoire performed by a historically Greek ensemble—not traditional Greek songs. *Mi ricurita* is catalogued by LOC as an Argentine-targeted tango performed by the Victor Orchestra in the United States. *A madrugada exul* is music by Brazilian composer Leopoldo Miguez, performed in Portuguese. *Alejandra* is Mexican band repertoire, not a newly synthesized recording. See `music/minor-batch5-sources.json` for the item-level rationale. No copyrighted user-uploaded MP3s were publicly hosted.

## Phase 23C.12 — Spain, Argentina, Mexico (four genuine archived recordings)

All four complete, original pre-1923 recordings were retrieved from the [LOC National Jukebox downloadable dataset](https://data.labs.loc.gov/jukebox/) and passed exact [archive MD5 checksums](https://data.labs.loc.gov/jukebox/manifest.html). These are **not WWII-era recordings** or national radio broadcast tapes. Country assignment reflects composer, music tradition, or language, not studio geography.

| TOBS station | Performance | Recorded | Historical credits | LOC source and validated MD5 |
| --- | --- | --- | --- | --- |
| Spain | La paloma | 1903-05-17 | Zélie de Lussan (soprano), Sebastián Yradier (Spanish composer) | [LOC 117554](https://www.loc.gov/item/jukebox-117554/), `0c68b476a84a0410645c5941b0d6ca73` |
| Spain | Meus amores | 1906-07-02 | Eladio A. Chao (baritone) | [LOC 123293](https://www.loc.gov/item/jukebox-123293/), `5ddf4760b2baed048074b1861e37fe12` |
| Argentina | El amanecer | 1915-10-15 | Victor Orchestra, Edward T. King (conductor); Roberto Firpo (Argentine tango composer) | [LOC 189361](https://www.loc.gov/item/jukebox-189361/), `6af204d92a91790e02c7bda7af95dfab` |
| Mexico | Over the Waves (Sobre las olas) | 1915-10-06 | Pietro Deiro (accordion), Juventino Rosas (Mexican composer) | [LOC 13857](https://www.loc.gov/item/jukebox-13857/), `ab4fa987a01265e03b3d95dfbbac2770` |

*La paloma* is Spanish by composition (Sebastián Yradier); *Meus amores* is a Galician-language vocal. *El amanecer* is a tango by Argentine composer Roberto Firpo. *Over the Waves* is by Mexican composer Juventino Rosas but performed by accordionist Pietro Deiro; it is not a Mexican traditional band recording. No synthetic music or rights-uncleared 1940s commercial audio was imported.

## Phase 23C.13 — Three additional original historical songs

This batch contains **actual historical recordings**, not WWII-era performances. Three complete MP3 files passed their original Library of Congress package MD5 validation. The planned [1915 National Airs of the Allies (LOC 12768)](https://www.loc.gov/item/jukebox-12768/), including Belgian *La Brabançonne*, was **excluded** because the official downloaded LOC dataset did not include its full audio; Belgium remains silent rather than receive an unverified substitute.

| TOBS station | Historical performance | Original recording date | Credits and country rationale | Official LOC item and MD5 |
| --- | --- | --- | --- | --- |
| Argentina | El Choclo — Tango | 1916-04-14 | Hurtado Brothers Royal Marimba Band of Guatemala; Ángel Gregorio Villoldo, Argentine composer; Early instrumental recording of Argentine tango composed by Ángel Villoldo, performed by Guatemalan ensemble in 1916; not an Argentine radio master. | [LOC 17295](https://www.loc.gov/item/jukebox-17295/), `b5575e2c546b1671177bc60525b80069` |
| Mexico | Chaqueteros | 1914-12-16 | Banda Rodríguez; Walter B. Rogers, conductor; J. M. Garza, composer; LOC catalog identifies Spanish (Mexico) Mexican popular band repertoire. | [LOC 11850](https://www.loc.gov/item/jukebox-11850/), `4e75a0cac50c99c8cb2521b1e213bace` |
| Mexico | La Golondrina | 1906-06-27 | Emilio de Gogorza and Carlos Francisco, baritones; Narciso Serradell, Mexican composer; Spanish-language historical rendition of original Mexican composition. | [LOC 249295](https://www.loc.gov/item/jukebox-249295/), `5d523d1576a239f31f315b689d7f4e21` |

Original audio verified from the [LOC National Jukebox pre-1923 dataset](https://data.labs.loc.gov/jukebox/) and [published manifest](https://data.labs.loc.gov/jukebox/manifest.html). No user-provided restricted tracks or rejected synthetic audio uploaded.

## Phase 23C.14 — Five countries added via verified Commons archival source pages

Six actual human musical performances have been added to the TOBS playlists using directly allowlisted `upload.wikimedia.org` sound-file URLs. **Important technical limitation:** importing local Ogg copies was blocked by HTTP 429 rate limits on the GitHub Actions runner. Unlike the previous LOC batches, the downloaded bytes were **not independently hashed** on GitHub; the public audio manifest points only to the exact canonical Wikimedia Commons files, as verified against their source pages. Live browser playback still needs user testing. No public GitHub-hosted media was added in this batch.

| Station | Recording | Original date/length | Attribution | Commons source and rights evidence |
| --- | --- | --- | --- | --- |
| Canada | O Canada — Victor Military Band (recorded 1915, issued c.1916) | 1915-12-09 | Victor Military Band; Calixa Lavallée | [Commons original and license](https://commons.wikimedia.org/wiki/File:O_Canada_instrumental_1916.ogg) |
| Australia | Advance Australia Fair — original 1915 recording | 1915-02-25 | Historic Australian performance; archival source lacks independently confirmed performer | [Commons original and license](https://commons.wikimedia.org/wiki/File:Advance_Australia_Fair_(1915).ogg) |
| Netherlands | Het Wilhelmus — first recording (1899) | 1899 | Historical Dutch anthem performance; performer not reliably identified in source | [Commons original and license](https://commons.wikimedia.org/wiki/File:Het_Wilhelmus_(first_recording_1899).ogg) |
| Netherlands | Wilhelmus — Henri Dons (1920) | 1920 | Henri Dons (singer) | [Commons original and license](https://commons.wikimedia.org/wiki/File:Henri_Dons_-_Wilhelmus.ogg) |
| Estonia | Mu isamaa, mu õnn ja rõõm — instrumental (1914) | 1914 | Puhkpillide Orkester (historic band, per Commons) | [Commons original and license](https://commons.wikimedia.org/wiki/File:Estonian_National_Anthem_(first_instrumental_recording).oga) |
| Belgium | La Brabançonne — United States Navy Band (circa 2003) | c.2003 | United States Navy Band; François Van Campenhout (composer) | [Commons original and license](https://commons.wikimedia.org/wiki/File:La_Braban%C3%A7onne.oga) |

**Period accuracy:** Canada's *O Canada* is the Victor Military Band original recorded December 1915, issued circa 1916; Australia's 1915 *Advance Australia Fair* is a very short original historical recording (~39 seconds); the Netherlands performances are from 1899 and around 1920; Estonia's original 1914 instrumental is ~35 seconds. The **Belgian U.S. Navy Band performance is from approximately 2003**, of a much older anthem. It's a real band, but **not a WWI or WWII historical recording**. Short historical pieces count toward playlist entries but are not full-length modern pop songs. No synthetic music or the user's separately supplied commercial MP3s has been distributed.

**Import issue:** The automation `music/import_commons_batch8.py` and `.github/workflows/import-commons-batch8.yml` are retained for future verified local import when Wikimedia's GitHub-hosted download rate limit clears. Keep remote sources allowlisted only, and don't count the failed workflow as a successful hosted binary import.

## Phase 23C.15 — Twelve additional northern European historic performances

All twelve are genuine **original recordings from 1906–1916**, retrieved as complete files from the [Library of Congress National Jukebox downloadable archive](https://data.labs.loc.gov/jukebox/) and checked against the [official original master MD5s](https://data.labs.loc.gov/jukebox/manifest.html). They are **not original WWII-period recordings** and were not necessarily recorded in their assigned countries; programming reflects repertoire, language, ensemble or composer.

| Country | Title | Original date | Performer/composer information | LOC source and confirmed MD5 |
| --- | --- | --- | --- | --- |
| Sweden | Aktenskapsfragan | 1916-06-01 | Lundberg, Oscar, Vocalist -- Bass Vocal | King, Edward T., Conductor | King's Orchestra, Musical Group | Fröding, Gustaf, Author | [LOC 17981](https://www.loc.gov/item/jukebox-17981/), `084a67dc5ee2b98cbcb117a4c7511ca6` |
| Sweden | Kung Carl XII | 1916-05-05 | Westermark, Otto, Composer | King, Edward T., Conductor | Wang-Holm, Aage, Vocalist -- Tenor Vocal | King's Orchestra, Musical Group | [LOC 16730](https://www.loc.gov/item/jukebox-16730/), `e9ca6953372d7c63ab24b64dbbc93cd6` |
| Sweden | Lifdrabanten och kung Erik | 1916-05-05 | King, Edward T., Conductor | King's Orchestra, Musical Group | Wang-Holm, Aage, Vocalist -- Tenor Vocal | Lindblad, Otto, Composer | [LOC 17593](https://www.loc.gov/item/jukebox-17593/), `7db13f31e6fe9ffb67877ce32c8973e3` |
| Norway | Det Norske flag | 1906-07-17 | Ibsen, L. M., Composer | Rören, Hjalmar E., Vocalist -- Baritone Vocal | [LOC 123367](https://www.loc.gov/item/jukebox-123367/), `599b2226f144556c3c1b85566976fb39` |
| Norway | Eg veit ei liti gjenta | 1913-10-09 | Elling, Catharinus, Lyricist | Woll, Carsten, Vocalist -- Tenor Vocal | Elling, Catharinus, Composer | Bachman, Fred, Instrumentalist -- Piano | [LOC 133883](https://www.loc.gov/item/jukebox-133883/), `2f6325b83d45997d578ba7df94a1d758` |
| Norway | Kom med visor | 1914-05-05 | Sinding, Christian, Composer | Hammer, Rolf, Vocalist -- Tenor Vocal | Pike, Katherine, Instrumentalist -- Piano | [LOC 135074](https://www.loc.gov/item/jukebox-135074/), `e28a8c9c49ad5151ee8b9bd102a4313d` |
| Denmark | Legende | 1906-12-06 | Offenbach, Jacques, Composer | Carlson, Gudrun, Vocalist -- Soprano Vocal | Herskind, Johannes, Vocalist | [LOC 124178](https://www.loc.gov/item/jukebox-124178/), `7a7b5af3e32209ac560843b625522cfe` |
| Denmark | Gobble duet | 1906-12-06 | Audran, Edmond, Composer | Carlson, Gudrun, Vocalist -- Soprano Vocal | Herskind, Johannes, Vocalist | [LOC 124176](https://www.loc.gov/item/jukebox-124176/), `9fba81fb74085262bb5ecbf68b93e2c1` |
| Poland | Mazur | 1911-07-17 | Rybowiak Orchestra, Musical Group | Hensel, R., Composer | [LOC 130630](https://www.loc.gov/item/jukebox-130630/), `cb2ff9557951f32b2bc7f95863e9ec19` |
| Poland | Polonez Pozegnanie Ojczyzny | 1911-07-20 | Rybowiak Orchestra, Musical Group | Oginski, Michel, Composer | [LOC 130665](https://www.loc.gov/item/jukebox-130665/), `bb3b13520a85582417710b0a3e34ec78` |
| Poland | Polonez Kosciuszkowski | 1915-10-21 | Wroński, Tadeusz, Vocalist -- Baritone Vocal | King, Edward T., Conductor | King's Orchestra, Musical Group | [LOC 15249](https://www.loc.gov/item/jukebox-15249/), `2831e83068a104d2c345b461ce617a06` |
| Austria | Chorus of priests : Grand Isis! | 1913-04-04 | Metropolitan Opera Male Chorus, Vocal Group | Victor Orchestra, Musical Group | Mozart, Wolfgang Amadeus, Composer | [LOC 133032](https://www.loc.gov/item/jukebox-133032/), `d6f5349deb7f01d5f3722743f4532612` |

The Danish-language stage recordings are works by Offenbach and Audran, not Danish-composed songs. The Austrian station receives a U.S. performance of an opera excerpt by Austrian composer Mozart. These are listed by their genuine origins and source dates. The remote Commons recordings from C.14 remain linked rather than locally stored; the 12 new LOC master MP3s **are locally hosted in development**. No user MP3s or synth-generated audio have been uploaded.
