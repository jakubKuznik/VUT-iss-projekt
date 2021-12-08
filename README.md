# VUT-iss-projekt


# <p align="center">ISS/VSG Projekt 2021/22</p>
<p align="center">Honza Černocký, Honza Brukner a Honza Švec, ÚPGM FIT VUT</br>
November 17, 2021</p>

## 1 Úvod

Často se stane, že dostaneme signál zarušený nějakými artefakty a je potřeba jej vyfiltrovat. Pro tento projekt
jsme pro Vás připravili signály ze známé databáze TIMIT, kam se ale “zatoulaly” čtyři harmonicky vztažené
cosinusovky. Vašı́m úkolem je signál analyzovat, najı́t, na kterých frekvencı́ch cosinusovky jsou, navrhnout filtr
nebo filtry pro čištěnı́ signálu a pak signál vyčistit.
Projekt je individuálnı́ a je možno řešit v Python-u, Matlab-u, Octave, jazyce C nebo v libovolném jiném
programovacı́m jazyce. Je možné použı́t libovolné knihovny. Projekt se nezaměřuje na “krásu programovánı́”,
nenı́ tedy nutné mı́t vše úhledně zabalené do okomentovaných funkcı́, ošetřené všechny chybové stavy, atd. Důležitý
je výsledek. Kód musı́ prokazatelně produkovat výsledky obsažené ve Vašem protokolu.
V zadánı́ se občas vyskytujı́ funkce, či jiné části kódu, jako nápovědy. Tyto ukázky jsou v Python-u s použitı́m
knihovny numpy (přesněji import numpy as np).

## 2 Vstup

Váš osobnı́ signál máte v souboru https://www.fit.vutbr.cz/study/courses/ISS/public/proj2021-22/signals/
xlogin00.wav, kde ”xlogin00” je login pro studenty FIT, přı́padně šestimı́stné čı́slo studenta pro studenty FSI.
Váš login nebo čı́slo studenta musı́te vypsat, adresář nenı́ možné vylistovat (nerad bych dával světu spam-list
všech studentů ISS/VSG). 


## 3 Odevzdání projektu

bude probı́hat do informačnı́ho systému WIS (studenty FSI prosı́m o zaslánı́ řešenı́ emailem) ve dvou souborech:
### 1. xlogin00.pdf nebo xlogin00_e.pdf (kde “xlogin00” je Váš login či čı́slo studenta) je protokol s řešenı́m.
• V záhlavı́ prosı́m uveďte své jméno, přı́jmenı́ a login.
• Pak budou následovat odpovědi na jednotlivé otázky — obrázky, numerické hodnoty, komentáře.
• U každé otázky uveďte stručný postup - může se jednat o kousek okomentovaného kódu, komentovanou
rovnici nebo text. Nenı́ nutné kopı́rovat do protokolu celý zdrojový kód. Nenı́ nutné opisovat zadánı́ či
teorii, soustřeďte se přı́mo na řešenı́. Je-li v zadánı́ “zobrazte”, znamená to, že výsledek chceme vidět
v protokolu.
• Pokud využijete zdroje mimo standardnı́ch materiálů (přednášky, cvičenı́ a studijnı́ etapa projektu ISS),
prosı́m uveďte, odkud jste čerpali (např. dokumentace numpy, Matlab, scipy, . . . ).
• Protokol je možné psát v libovolném systému (Latex, MS-Word, Libre Office, . . . ), můžete jej psát i
čitelně rukou, dolepit do něj obrázky a pak oskenovat.
• Protokol může být česky, slovensky nebo anglicky. Budete-i psát anglicky, prosı́me, abyste nazvali
výsledný soubor xlogin00_e.pdf. Za angličtinu v protokolu nenı́ žádné zvýhodněnı́ ani penalizace,
sloužı́ nám jen pro výběr opravujı́cı́ch.

### 2. xlogin00.tar.gz je komprimovaný archiv obsahujı́cı́ následujı́cı́ adresáře:
• /src - Vaše zdrojové kódy – může se jednat o jeden soubor (např. moje_reseni.py), o vı́ce souborů
či skriptů nebo o celou adresářovou strukturu.
• /audio - audio soubory – ve formátu WAV, na vzorkovacı́ frekvenci 16 kHz, bitová šı́řka 16 bitů, bez
komprese.
### 3. Projekt je samostatná práce, proto budou Vaše zdrojové kódy křı́žově korelovány a v přı́padě silné podob-
nosti budou vyvozeny přı́slušné závěry.
### 4. Silná korelace s kódy ze studijnı́ etapy projektu, z Python notebooků studijnı́ podpory a z přı́kladů Katky
Žmolı́kové 1 je v pořádku, nemusı́te tedy měnit názvy proměnných, přepisovat komentáře, atd.

## 3 Standardnı́ zadánı́
Úspěšné řešenı́ těchto bodů zadánı́ vede k plnému počtu bodů za projekt, tedy 18ti.

### 4.1 Základy – 1 bod
Načtěte vstupnı́ signál, určete a napište jeho délku ve vzorcı́ch a v sekundách, určete a napište jeho minimálnı́ a
maximálnı́ hodnotu a zobrazte jej se slušnou časovou osou v sekundách.

### 4.2 Předzpracovánı́ a rámce 1 bod
Načtený signál ustředněte (odečtěte střednı́ hodnotu) a normalizujte do dynamického rozsahu -1 až 1 dělenı́m
maximem absolutnı́ hodnoty. Signál rozdělte na úseky (rámce) o délce 1024 vzorků s překrytı́m 512 vzorků, rámce
uložte jako sloupce matice. Vyberte ”pěkný” rámec s periodickým charakterem (znělý) a zobrazte jej se slušnou
časovou osou v sekundách.

### 4.3 DFT – 2 body
Implementujte vlastnı́ funkci pro výpočet diskrétnı́ Fourierovy transformace pro N=1024 vzorků. Snažte se pra-
covat ”vektorově”, tedy s minimálnı́m počtem cyklů. Transformace by měla být realizována jako násobenı́ matice
bázı́ s vektorem signálu. Spusťte Vaši funkci na vybraném rámci, zobrazte modul DFT pro frekvence od 0 do F 2 s
se slušnou frekvenčnı́ osou v Hz. Porovnejte Váš výsledek s knihovnı́ implementacı́ FFT (např. np.fft.fft) -
graficky a budete-li chtı́t, pomocı́ funkce na přibližné porovnánı́, např. np.allclose.

### 4.4 Spektrogram – 1 bod
Pro celý signál vypočtěte a zobrazte “logaritmický výkonový spektrogram” tedy obrázek s časem v sekundách
na x-ové ose a s frekvencı́ v Hz na y-ové ose (opět do poloviny vzorkovacı́ frekvence). Použijte opět délku okna
1024 vzorků a překrytı́ 512 vzorků. Hodnoty jednotlivých koeficientů DFT upravte pomocı́ P [k] = 10 log 10 |X[k]| 2 .
Můžete využı́t knihovnı́ funkci, ale rádi bychom, aby časová a frekvenčnı́ osa měly správné hodnoty. Pro hodnotu
koeficientu můžete dle libosti použı́t stupeň šedi nebo barvu.

### 4.5 Určenı́ rušivých frekvencı́ – 2 body
Na spektrogramu budou jasně viditelné rušivé komponenty. Určete jejich frekvence f 1 , f 2 , f 3 , f 4 v Hz. Ověřte, že
jsou 4 rušivé cosinusovky harmonicky vztažené, tedy že f 2 , f 3 a f 4 jsou násobky té nejnižšı́ frekvence. Na určenı́
frekvencı́ si můžete napsat funkci nebo je odečı́st “ručně” ze spektrogramu či jednoho spektra.
Hint: při odečı́tánı́ z jednoho spektra si dejte pozor na to, abyste rušivou frekvenci nezaměnili za součást
spektra řeči.

### Generovánı́ signálu – 3 body
Vygenerujte signál se směsı́ 4 cosinusovek na frekvencı́ch f 1 , f 2 , f 3 , f 4 , o stejné délce jako původnı́ signál. Uložte
jej do souboru audio/4cos.wav. Zobrazte jeho spektrogram. Poslechem a srovnánı́m spektrogramů ověřte, že
jste frekvence určili a signál vygenerovali správně.

### Čisticı́ filtr – 3 body
Navrhněte filtr nebo sadu filtrů typu pásmová zádrž pro čištěnı́ signálu — musı́ potlačovat frekvence f 1 , f 2 , f 3 ,
f 4 . Můžete postupovat jednou ze třı́ alternativ:

#### 1. výroba filtru v z-rovině:
dělejte filtr tak, aby měl 4 nulové body “sedı́cı́” na jednotkové kružnici,
vypočı́táte je pomocı́ konverze frekvence v Hz na normované kruhové frekvence ω k = 2π F f k s a pak takto:
n k = e jω k . Doplňte k nim ještě 4 dalšı́ komplexně sdružené nulové body (např. np.conj) a pak nulové body
převeďte na koeficienty filtru (např. np.poly). Měli byste dostat FIR filtr s 9-ti koeficienty. Pokud postup nespletete, bude vyrobený filtr dobře potlačovat rušenı́, ale také zkreslovat signál. To nenı́ důvod ke strženı́
bodů, ale zkuste vysvětlit, proč tomu tak je.

#### 2. návrh filtru ze spektra:
nejprve si ”vymodelujte” požadovanou frekvenčnı́ charakteristiku filtru H[k]
(např. na 1024 bodech): doporučujeme pracovat pouze na 513 bodech od H[0] do H[512], naplnit je
jedničkami a pak najı́t indexy koeficientů, které je třeba vynulovat. Indexy zjistı́te pomocı́ převodu z f 1 ,
f 2 , f 3 , f 4 , přı́padně se dá spektrum nebo spektrogram zobrazit s frekvenčnı́ osou s indexy koeficientů a
odečı́st je přı́mo. Pozor, pak musı́te doplnit druhou polovinu spektra, tedy vzı́t body H[1 . . . 511], otočit
jejich pořadı́ (např. np.fliplr) a přilepit za body H[0 . . . 512]. Teoreticky byste je měli ještě i komplexně
sdružit, ale jsou to jen nuly nebo jedničky, nenı́ to potřeba. Pak vyrobı́te impulsnı́ odezvu filtru pomoci
inverznı́ FFT. Pozor, jejı́ výstup je ještě nutné přerovnat tak, aby bylo maximum impulsnı́ odezvy uprostřed
(např. np.fftshift), jinak to nefunguje.

#### 3. návrh 4 pásmových zádržı́:
vyhledejte si a použijte funkce pro návrh filtrů a vyrobte 4 pásmové zádrže
(band-stop filters) se závěrnými pásmy (stop-bands) okolo frekvencı́ f 1 , f 2 , f 3 , f 4 . Doporučujeme např.
scipy.signal.buttord a scipy.signal.butter nebo scipy.signal.ellipord a scipy.signal.ellip.
Při návrhu filtrů je dobré nedefinovat je úplně “ostré” (dostanete je pak šı́leně dlouhé), ale s rozumnou šı́řı́
závěrného pásma, třeba 30 Hz, a s rozumnou šı́řı́ přechodů do propustého pásma, třeba 50 Hz na každé
straně. Zvlněnı́ (ripple) v propustném pásmu nastavte třeba na 3 dB a potlačenı́ v závěrném pásmu (stop-
band attenuation) třeba na -40 dB. Pozor na normovánı́ frekvencı́, návrhové funkce v Pythonu a Matlabu
normujı́ frekvence pomocı́ Nyquistovy frekvence F 2 s a ne pomocı́ vzorkovacı́ frekvence F s !

#### 4. jakýkoliv jiný způsob návrhu filtru vedoucı́ ke kýženému výsledku je vı́tán.


Uveďte koeficienty filtru nebo filtrů a zobrazte jeho/jejich impulsnı́ odezvy. Pokud jsou nekonečné, omezte je na
délku vhodnou pro zobrazenı́.

### 4.8 Nulové body a póly – 2 body
Vypočtěte nulové body a póly navrženého filtru nebo filtrů a zobrazte je v komplexnı́ rovině. Zde budou ve
výhodě uživatelé Matlabu či Octave, kteřı́ využijı́ funkce zplane. Pythonisté si ji budou muset naprogramovat
(asi 5 řádků, využijte np.roots) nebo vygooglit již hotovou.

### 4.9 Frekvenčnı́ charakteristika – 2 body
Vypočtěte frekvenčnı́ charakteristiku filtru/filtrů a zobrazte ji/je se slušnou frekvenčnı́ osou v Hz. Ověřte, že filtr
potlačuje rušivý signál na správných frekvencı́ch.

### 4.10 Filtrace – 1 bod
Proveďte filtraci signálu pomocı́ Vámi navrženého filtru / filtrů. Zkontrolujte, zda je výsledný signál ve slušném
dynamickém rozsahu od -1 do +1, pokud nenı́, upravte. Uložte výsledek jako audio/clean aaa.wav, kde “aaa” je
zkratka použité metody návrhu filtru (“z” pro z-rovinu, “spec” pro převod filtru ze spektrálnı́ oblasti a “bandstop”
pro pásmové zádrže). Ověřte poslechem, zda došlo k vyčištěnı́ signálu. Výsledek okomentujte.

## 5 Bonusové úkoly
Za tyto úkoly nejsou body, ale bude Vás také hřát pocit skutečného porozuměnı́ signálům. Autor/ka nejlepšı́ho
řešenı́ dostane láhev kvalitnı́ho francouzského červeného vı́na.

### 5.1 Přesné určenı́ frekvence
Určete frekvencı́ rušivých signálů s přesnostı́ na 1 Hz. Běžná FFT to nedokáže, protože 16000/1024=15.6 Hz.
Můžete

• zkusit nadvzorkovánı́ spektra s interpolacı́ pomocı́ kardinálnı́ho sinu (pozor, Matlab i Python ho definujı́
jako sin(πx)/πx). Matlab navı́c obsahuje šikovnou funkci interp, která vše udělá za Vás.
• hodilo by se ale zprůměrovat spektra přes všechny rámce. Pozor, rozhodně průměrujte absolutnı́ hodnoty,
ne původnı́ komplexnı́ koeficienty.
• nebo můžete frekvenci určit nahrubo (FFT) a pak generovat komplexnı́ exponenciály s krokem 1 Hz okolo
té nahrubo určené a dı́vat se, která je nejpodobnějšı́. Podobnost určujte na celém signálu.

### 5.2 Přesné určenı́ amplitudy
Určete přesně amplitudy všech 4 cosinusovek.
• Vezměte absolutnı́ hodnotu přı́slušného koeficientu, dělte počtem vzorků FFT a násobte dvěma (viz teorie
jak vypočı́tat z DFT parametry diskrétnı́ cosinusovky).
• opět bude asi potřeba průměrovat přes vı́ce rámců, aby se výsledek zpřesnil. Opět absolutnı́ hodnoty, ne
komplexnı́ koeficienty.
• Spektrum řeči může určenı́ amplitud rušivého signálu nabourat - bude lepšı́ amplitudy určovat na začátku
a na konci nahrávky, kde je ticho (řečaři tomu řı́kajı́ voice activity detection – VAD – tady ji můžete udělat
od oka).

### 5.3 Určenı́ počátečnı́ch fázı́ cosinusovek
To jsme doposud ignorovali, tak to zkuste. Referenčnı́ pro určenı́ fázı́ je nultý rámec ležı́cı́ od času 0.
• ještě lepšı́ by ale bylo fáze počı́tat přes všechny rámce, jenže ony se nám posouvajı́: pro každý dalšı́ tam
bude změna fáze o −ω k 512, kde ω k je normovaná kruhová frekvence dané cosinusovky. O tyto fáze by to
tedy chtělo fáze spočı́tané FFTčkem korigovat (tedy vždy přičı́st rω k 512), kde r je čı́slo rámce.
• před průměrovánı́m je také potřeba vypočtené hodnoty zarovnat do intervalu od −π do +π. Stackoverflow
radı́ např. toto: phases = (phases + np.pi) % (2 * np.pi) - np.pi
• bude-li vypočtená fáze blı́zko −π nebo +π a mezi těmito dvěma hodnotami bude “přeblikávat” kvůli num-
erickým nepřesnostem, může to při průměrovánı́ způsobit problém. Zkuste s tı́m něco udělat.
• Pro korekci rozhodně doporučujeme přesně vypočı́tané hodnoty frekvence s těmi “hrubými FFTčkovými” se
Vám korekce asi brzy rozjedou. . . .

### 5.4 Odečet rušivého signálu
Vygenerujte podle přesných frekvencı́, amplitud a fázı́ rušivý signál (můžete srovnat s tı́m přibližným ze cvičenı́ 6) a
odečtěte ho od vstupnı́ho. Výsledek zobrazte v jednom obrázku s původnı́m. Výsledek dejte do audio/bonus.wav,
poslechněte si jej, prohlédněte a okomentujte, jak to dopadlo.
