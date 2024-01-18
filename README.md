# Projekta darbs

Mans izveidotais projekta darbs ir **automatizēts pieteikums RTU sporta centra trenežieru zālei.**

Kā programmu palaiž, tā atver interneta pārlūku "**Google Chrome**", un atver RTU sporta centra mājaslapu. Tā sāk ar sīkdatņu apstiprināšanu, pagaida 1 sekundi un tad ieiet mājaslapas izvēlnes sadaļā, atrod un uzklikšķina uz sadaļas "_Ieiet_", kas pārceļ uz ORTUS login lapu, un automātiski ievada manus ORTUS datus, tad tos arī apstiprina. Kad ir apstiprināti mani dati un pārvests atpakaļ uz galveno lapu, programma uzgaida 1 sekundi, vēlreiz uzklikšina uz lapas izvēlnes sadaļas, atrod un šoreiz uzklišķina "_Pieteikties nodarbībām_" sadaļu. Atveras kalendārs ar iknedēļas notikumiem un aktivitātēm. Programma vēlreiz uzgaida sekundi, atrod un uzklišķina uz ikdienas režīma kalendārā, sakarā ar to, ka pagaidām spēj pieteikt aktivitātes tajā dienā, kad kods tiek palaists. Tad programma atrod un izvēlas tieši to trenežieru zāli un laiku, kuru esmu atvēlējis es. Atveras jauna lapa ar pogu "_Pieteikties nodarbībai_", kuru programma atrod un nospiež, tālāk parādās apstiprināšanas logs, kurā programma arī izvēlas opciju "Jā". Tālāk lapa pārceļ uz maksājuma vietni, un sakarā ar to, ka RTU sporta centra mājaslapā nauda glabājās kontā kā virtuālā nauda, programmai atliek tikai uzspiest uz "_Apmaksāt_", un tā ir veiksmīgi izpildījusi savu uzdevumu. Kad uzdevums izpildiīts, pārlūku var izslēgt, vai arī piespiest jebkuru pogu terminālī, kas pateiks programmai, ka darbs jābeidz.

## Izmantotās bibliotēkas

Galvenā izmantotā bibliotēka ir **_"Selenium"_**, kas ļauj programmēšanas valodai "Python" strādāt ar interneta pārlūku "Google Chrome".

**_"webdriver"_** modulis ļauj man vadīt interneta pārlūku "Google Chrome", izmantojot programmēšanas valodu "Python".

**_"Service"_** modulis tiek izmantots, lai konfigurētu un vadītu "Google Chrome" parlūka vadību un sniedz iespēju norādīt konkrētus uzstādījumus un pakalpojumus, kas saistīti ar šo pārlūku, kas ļauj man izpildīt savu uzdevumu.

**_"By"_** modulis nodrošinās mehānismus, lai varu atrast elementus HTML lapā, ar kuriem pēc tam varu automatizēt manu uzdevumu.

**_"time"_** bibliotēka, ļauj man apstādināt programmas tālāku darbību, lai programma paspēj atrast nepieciešamos elementus un nenobrūk.

## Programmatūras izmantošanas metodes

Programmatūras rezultāts ir ierobežots, jo veic tikai vienu uzdevumu, bet to var pilnveidot, ievadot terminālī, kurā dienā vēlies veikt pieteikumu un kurā trenežieru zālē, laikā, kā arī lietojot bibliotēku "Selenium", var izveidot ko līdzīgu, kas daudziem cilvēkiem palīdzēs ātrāk izpildīt ikdienas uzdevumu, automatizējot kādu procesu, kā šis un daudzus citus.

