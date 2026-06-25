# Mikail Lekesiz AI Memory Deep Research — Doğrulama ve Zenginleştirme Raporu

**Araştırma tarihi:** 25 Haziran 2026, Europe/Paris.  
**Kapsam:** NETZ Informatique, Reflektif, web varlıkları, GitHub, kişisel/profesyonel dijital iz ve 2025/2026 sektörel bağlam.  
**Güven notasyonu:** **Yüksek [CV]** = resmi kaynak veya birden fazla bağımsız kaynakla çapraz doğrulama; **Orta [Tek]** = tek kaynak, dizin veya şirketin kendi beyanı; **Düşük [?]** = erişim sınırlı, çelişkili veya yalnızca dolaylı kanıt; **Doğrulanamadı [?]** = halka açık doğrulanabilir kaynak bulunamadı.  
**Hassas veri politikası:** Kişisel e-posta, telefon, doğum tarihi/ayı ve özel hesap/izin bilgileri rapora alınmadı veya **MASKED** olarak işlendi.

## 0. Yönetici özeti

NETZ Informatique’in SIREN **818 347 346** ile Haguenau merkezli, aktif bir **SAS/SASU** olduğu resmi Fransız şirket API’si ve Societe.com/Le Figaro gibi açık şirket dizinleriyle doğrulandı; şirketin açık finansal göstergelerinde en güvenilir doğrulanmış rakam **2022 ciro 404.272 €** ve **2022 net sonuç 8.882 €** olarak görünüyor ([recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html), [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346)).  
NETZ Informatique’in resmi DGEFP “liste publique des organismes de formation” kaydında **Actions de formations** ve **Bilans de compétences** kapsamlarında sertifikalı olduğu, NDA numarasının **44670671567** olduğu ve 2025 deklarasyon döneminde **404 stagiaire** ile **2 formateur** bildirdiği doğrulandı ([DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/)).  
Mon Compte Formation açık katalog verisinde NETZ Informatique SIRET **81834734600020** için **18 aktif/indekslenmiş RS referanslı eğitim** bulundu; buna karşılık aynı açık katalog sorgusunda NETZ adına doğrudan “bilan de compétences” teklifi doğrulanamadı ([Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100), [data.gouv.fr MCF dataset](https://www.data.gouv.fr/datasets/moncompteformation-loffre-de-formation)).  
Reflektif.net canlıdır ve RIASEC, Big Five, değerler testi, yapay zekâ analizi ve 920+ meslek eşleştirme üzerine konumlanmıştır; gizlilik sayfası veri sorumlusu olarak NETZ Informatique’i gösterirken öğrenci alt alanındaki kullanım koşulları REFLEKTİF BİLİŞİM A.Ş. beyanı içerdiğinden Türkiye tüzel bağlantısı resmi sicil ile henüz doğrulanamadı ([Reflektif](https://reflektif.net), [Reflektif Privacy](https://reflektif.net/privacy), [Reflektif Öğrenci Koşulları](https://ogrenci.reflektif.net/terms)).  
Wikidata **Q140131918** iddiası, ilgili EntityData isteğinin “No entity with ID Q140131918 was found” dönmesi nedeniyle mevcut anda çürütülmüş kabul edilmelidir; Wikipedia’da da Reflektif platformu için bağımsız madde/taslak bulunamadı ([Wikidata EntityData](https://www.wikidata.org/wiki/Special:EntityData/Q140131918.json), [Türkçe Wikipedia API](https://tr.wikipedia.org/w/api.php?action=query&list=search&srsearch=Reflektif&format=json), [Fransızca Wikipedia API](https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=Reflektif&format=json), [İngilizce Wikipedia API](https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Reflektif&format=json)).  
GitHub profili **lekesiz** için GitHub API’si **264 public repo**, profil adı **Mikail LEKESIZ**, şirket **Netz Informatique**, lokasyon **Strasbourg** ve bio **devops engineer** verilerini döndürdü; `lekesiz/mikail` public repo doğrulandı, ancak `lekesiz/reflektif` repo’su halka açık API/web erişiminde doğrulanamadı veya erişim kısıtı/404 ile karşılaşıldı ([GitHub profile](https://github.com/lekesiz), [GitHub Users API](https://api.github.com/users/lekesiz), [lekesiz/mikail](https://github.com/lekesiz/mikail)).

## 1. Yeni Bulgular ve Doğrulama Tablosu

| Repo iddiası / konu | Araştırma sonucu | Kanıt özeti | Kaynak | Güven |
|---|---:|---|---|---|
| Mikail Lekesiz Haguenau merkezli girişimci/CEO | **Doğrulandı** | Resmi şirket kaydı NETZ başkanı olarak Mikail LEKESIZ’i gösteriyor; LinkedIn arama sonucu CEO/PDG profilini destekliyor. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [LinkedIn profili](https://www.linkedin.com/in/mikail-lekesiz) | Yüksek [CV] |
| NETZ Informatique SIREN 818 347 346 | **Doğrulandı** | SIREN, SIRET, adres, APE/NAF ve aktif durum resmi API ve Societe/Le Figaro ile uyumlu. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html), [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346) | Yüksek [CV] |
| NETZ 2025 ciro ~1,27M € | **Doğrulanamadı** | Açık resmi/yarı resmi kaynaklarda bu araştırmada 2025 ciro rakamı bulunmadı; doğrulanmış en son finansal veri 2022’ye ait. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Numbers.finance](https://numbers.finance/entreprise/netz-informatique-818347346) | Düşük [?] |
| NETZ 2022 ciro ~404k € | **Doğrulandı** | Resmi API 404.272 €, Numbers.finance 404 k€ olarak gösteriyor. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Numbers.finance](https://numbers.finance/entreprise/netz-informatique-818347346) | Yüksek [CV] |
| NETZ Qualiopi / organisme de formation | **Doğrulandı** | DGEFP açık listesinde Actions de formations ve Bilans de compétences sertifikasyonları işaretli. | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| QualiRépar etiketi no 1056 | **Kısmen doğrulandı / no doğrulanamadı** | Reparea NETZ’i QualiRépar onaylı tamirci olarak listeliyor; “1056” numarası için resmi dizin kanıtı bulunamadı. | [Reparea NETZ sayfası](https://reparea.fr/annuaire-reparateurs/netz-informatique-haguenau), [AFNOR QualiRépar açıklaması](https://certification.afnor.org/environnement/label-qualirepar) | Orta [Tek] / Düşük [?] |
| EDOF/WEDOF ~1.451 dosya | **Doğrulanamadı** | Açık Mon Compte Formation katalog verisi 18 eğitim kaydı gösteriyor; dosya/adet performans metriği kamuya açık veriyle doğrulanamadı. | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Düşük [?] |
| Reflektif.net canlı ve AI kariyer rehberliği platformu | **Doğrulandı** | Site 200 döndü; içerik RIASEC, Big Five, Values, AI analiz ve 920+ meslek katalogunu anlatıyor. | [Reflektif](https://reflektif.net), [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| Reflektif Bilişim A.Ş. Türkiye tüzel bağlantısı | **Belirsiz** | Öğrenci koşulları bu unvanı beyan ediyor; Ticaret Sicili/MERSİS tarafında bağımsız kayıt doğrulanamadı. | [Reflektif Öğrenci Koşulları](https://ogrenci.reflektif.net/terms), [TOBB Ticaret Sicili](https://www.ticaretsicil.gov.tr), [MERSİS](https://mersis.ticaret.gov.tr) | Düşük [?] |
| Wikidata Q140131918 | **Çürütüldü / mevcut değil** | EntityData isteği 404 ve “No entity with ID” yanıtı verdi. | [Wikidata EntityData](https://www.wikidata.org/wiki/Special:EntityData/Q140131918.json) | Yüksek [CV] |
| `github.com/lekesiz/reflektif` | **Doğrulanamadı** | Halka açık repo listesinde `reflektif` adı yok; erişim denemelerinde 403/404 görüldü; `Reflektif.net_sorular` ve `reflektif-web` adları public listede var. | [GitHub repos API](https://api.github.com/users/lekesiz/repos), [lekesiz/reflektif](https://github.com/lekesiz/reflektif) | Düşük [?] |
| `github.com/lekesiz/mikail` | **Doğrulandı** | Public repo, 25 Haziran 2026’da oluşturulmuş ve AI memory dosyaları içeriyor. | [lekesiz/mikail](https://github.com/lekesiz/mikail), [GitHub repo API](https://api.github.com/repos/lekesiz/mikail) | Yüksek [CV] |
| Strasbourg Üniversitesi LP DWCA 2025/2026 | **Kısmen / dolaylı** | Public GitHub’da `unistra` repo’su var; resmi üniversite kayıt kaynağı bu araştırmada bulunmadı. | [GitHub repos API](https://api.github.com/users/lekesiz/repos), [lekesiz/unistra](https://github.com/lekesiz/unistra) | Düşük [?] |

## 2. NETZ Informatique kurumsal doğrulama

### 2.1 Resmi ve açık şirket verileri

| Alan | Doğrulanan bilgi | Kaynak | Güven |
|---|---|---|---|
| Tüzel ad | NETZ INFORMATIQUE | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| SIREN | 818 347 346 | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346) | Yüksek [CV] |
| SIRET siège | 818 347 346 00020 | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| Kuruluş / immatriculation | Resmi API’de 10/02/2016; Societe.com RCS tarihi olarak 23/02/2016 gösteriyor. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| Adres | 1 A Route de Schweighouse, 67500 Haguenau | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346) | Yüksek [CV] |
| Hukuki form | SAS/SASU; resmi API nature juridique kodu 5710. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| APE/NAF | 85.59B “Autres enseignements”; resmi API’de NAF 2025 alanı 85.59H olarak da görünüyor. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346) | Yüksek [CV] |
| Sermaye | Societe.com 100 € sermaye gösteriyor; bazı özkaynak/ilan metinlerinde geçmiş ilanlarda farklı sermaye beyanı görülebildiği için güncel sermaye için Kbis/RNE önerilir. | [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html), [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346) | Orta [Tek] |
| Yönetici | Mikail LEKESIZ, Président de SAS; doğum bilgisi **MASKED**. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| Durum | Aktif; resmi API’de `etat_administratif: A`, `date_fermeture: null`. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Yüksek [CV] |
| Etablissement sayısı | 2 toplam, 1 açık; eski SIRET 81834734600012 kapalı görünüyor. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| Çalışan dilimi | Resmi API `tranche_effectif_salarie: 02` ve yıl 2023 döndürdü; bu kod raporda aralığa çevrilmeden korunmuştur. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Orta [Tek] |
| 2022 finansal göstergeler | Ciro 404.272 €, net sonuç 8.882 €; Numbers.finance aynı ciroyu 404 k€ olarak yuvarlıyor. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Numbers.finance](https://numbers.finance/entreprise/netz-informatique-818347346) | Yüksek [CV] |
| 2025 finansal göstergeler | Halka açık resmi kaynakta doğrulanmadı. | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Doğrulanamadı [?] |
| Pappers / Infogreffe görünürlüğü | Arama sonuçlarında doğrudan NETZ Pappers sayfası bulunamadı; Infogreffe için doğrudan doğrulanabilir kayıt sayfası yerine genel Infogreffe sayfaları çıktı. | [Pappers](https://www.pappers.fr), [Infogreffe](https://infogreffe.org/web/guest) | Düşük [?] |

### 2.2 Organisme de formation, Qualiopi ve DataDock/EDOF izi

| Alan | Doğrulanan bilgi | Kaynak | Güven |
|---|---|---|---|
| NDA | 44670671567 | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| OF SIRET | 81834734600020 | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Sertifikasyon kategorileri | Actions de formations = true; Bilans de compétences = true; VAE = false; Apprentissage = false. | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Son deklarasyon | 13/04/2026; beyan dönemi 01/01/2025–31/12/2025. | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Eğitim uzmanlıkları | 326 “Informatique, traitement de l'information, réseaux de transmission des données” ve 415 “Développement des capacités d'orientation, d'insertion ou de réinsertion sociales et professionnelles”. | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Stagiaire / formateur | 404 stagiaire ve 2 formateur bildirimi. | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Qualiopi ticari beyan | FranceNum ve NETZ sitesi/Formation Haguenau, Qualiopi sertifikalı eğitim ve bilan de compétences iddiası içeriyor; resmi DGEFP kaydı bunu kategori düzeyinde destekliyor. | [France Num](https://www.francenum.gouv.fr/activateurs/netz-informatique), [NETZ Informatique](https://www.netzinformatique.fr), [formation-haguenau.fr](https://formation-haguenau.fr/) | Orta [Tek] / Yüksek [CV] |
| DataDock | Araştırmada NETZ için güncel bağımsız DataDock kaydı doğrulanamadı; 2022 sonrası kamu finansmanı için pratik ana doğrulama Qualiopi/DGEFP listesi üzerinden yapılmalıdır. | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Doğrulanamadı [?] |

### 2.3 QualiRépar doğrulaması

| Alan | Bulgu | Kaynak | Güven |
|---|---|---|---|
| NETZ’in QualiRépar varlığı | Reparea sayfası NETZ Informatique’i “Réparateur agréé QualiRépar à Haguenau” olarak listeliyor. | [Reparea NETZ sayfası](https://reparea.fr/annuaire-reparateurs/netz-informatique-haguenau) | Orta [Tek] |
| Label no 1056 | Resmi QualiRépar/ecosystem annuaire üzerinde “1056” numarası halka açık biçimde doğrulanamadı. | [Label QualiRépar annuaires](https://www.label-qualirepar.fr/annuaires/), [Reparea NETZ sayfası](https://reparea.fr/annuaire-reparateurs/netz-informatique-haguenau) | Doğrulanamadı [?] |
| Program bağlamı | AFNOR, QualiRépar’ın AGEC yasasıyla ilişkili olduğunu, 15/12/2022’den beri bonus réparation indirimi için kullanılabildiğini ve etiketin 3 yıl geçerli olup 18 ayda takip denetimi gerektirdiğini açıklıyor. | [AFNOR QualiRépar](https://certification.afnor.org/environnement/label-qualirepar) | Yüksek [CV] |
| Bilgisayar onarım bonusu | Ecosystem dizininde taşınabilir bilgisayar onarımı için minimum 150 € onarımda 50 € bonus bilgisi yer alıyor. | [ecosystem ordinateur portable](https://www.ecosystem.eco/reparer/equipement/ordinateur-portable) | Orta [Tek] |

## 3. Mon Compte Formation / EDOF varlığı

Açık Mon Compte Formation katalog verisi, NETZ Informatique’in **SIRET 81834734600020** altında 25/06/2026 tarihli extract’te **18 eğitim kaydı** gösteriyor; tüm kayıtlar **RS** referanslıdır ve Bas-Rhin / Grand Est bölgesi ile ilişkilidir ([Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100), [data.gouv.fr MCF dataset](https://www.data.gouv.fr/datasets/moncompteformation-loffre-de-formation)).

| Katalog başlığı | Sertifikasyon | RS / kod | Kaynak | Güven |
|---|---|---:|---|---|
| Créer des présentations percutantes avec PowerPoint - Netz Informatique | Développer des présentations visuelles et dynamiques avec PowerPoint (Tosa) | RS6961 | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Yüksek [CV] |
| Automatiser les processus Office avec VBA - Netz Informatique | Automatiser des processus dans les applications Microsoft Office avec VBA (Tosa) | RS6963 | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Yüksek [CV] |
| Développer des solutions d'automatisation avec Python - Netz Informatique | Programmer et automatiser des tâches avec Python (Tosa) | RS6962 | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Yüksek [CV] |
| Certification DigComp / niveaux Opérationnel, Avancé, Expert | DigComp (Tosa) | RS6893 | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Yüksek [CV] |
| Créer et gérer un site web professionnel avec WordPress - Netz Informatique | Créer et gérer des sites web avec WordPress (Tosa) | RS6965 | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Yüksek [CV] |
| Formation Microsoft Excel - Préparation à la certification Tosa | Exploiter les fonctionnalités de Microsoft Excel (Tosa) | RS7256 | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Yüksek [CV] |
| AutoCAD, InDesign, Word, Photoshop, Access, Illustrator, Outlook, Microsoft 365 eğitimleri | Tosa RS sertifikasyon ailesi | RS6955/6957/6964/6959/7096/6956/6958/6960 | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Yüksek [CV] |
| Bilan de compétences MCF teklifi | Açık katalog sorgusunda NETZ adına doğrudan bilan de compétences kaydı doğrulanamadı; DGEFP listesi NETZ’in bu kategori için sertifikalı olduğunu doğruluyor. | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100), [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Orta [Tek] / Düşük [?] |

## 4. Reflektif / reflektif.net

| Alan | Bulgu | Kaynak | Güven |
|---|---|---|---|
| Site durumu | `https://reflektif.net` 200 ile erişilebilir ve `https://www.reflektif.net` final URL’sine yönleniyor. | [Reflektif](https://reflektif.net) | Yüksek [CV] |
| Konumlandırma | Platform kariyer rehberliği ekosistemi olarak RIASEC, Big Five, Professional Values ve yapay zekâ analizini birleştiriyor. | [Reflektif](https://reflektif.net) | Orta [Tek] |
| Hedef kitle | Öğrenciler/gençler, yetişkin beceri bilanı, işveren/recruitment ve erişilebilirlik modülleri hedefleniyor. | [Reflektif](https://reflektif.net), [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| Katalog | Reflektif site içeriği 920+ meslek referansı ve kişiselleştirilmiş Top 30 eşleştirme beyan ediyor. | [Reflektif](https://reflektif.net), [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| Test yapısı | Business sayfasında RIASEC 30 soru, Big Five 50 soru, Values 30 soru ve Living Tests AI görüşmesi anlatılıyor. | [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| Dil desteği | Business sayfası platformun Türkçe, Fransızca ve İngilizce kullanılabildiğini belirtiyor. | [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| Fiyat sayfası | Pricing sayfası Discovery 0 € ve Expert Guidance 199 € planlarını gösteriyor. | [Reflektif Pricing](https://www.reflektif.net/pricing) | Orta [Tek] |
| Veri sorumlusu | Privacy sayfası veri sorumlusu olarak NETZ Informatique SASU/SIREN 818 347 346’yı gösteriyor ve Google Gemini ile AI rapor üretimini açıklıyor. | [Reflektif Privacy](https://reflektif.net/privacy) | Orta [Tek] |
| Türkiye tüzel beyanı | Öğrenci kullanım koşulları platformun REFLEKTİF BİLİŞİM A.Ş. tarafından yayınlandığını söylüyor; resmi sicil doğrulaması bulunamadı. | [Reflektif Öğrenci Koşulları](https://ogrenci.reflektif.net/terms), [TOBB Ticaret Sicili](https://www.ticaretsicil.gov.tr), [MERSİS](https://mersis.ticaret.gov.tr) | Düşük [?] |
| Wikidata | Q140131918 mevcut değil; EntityData 404 döndü. | [Wikidata EntityData](https://www.wikidata.org/wiki/Special:EntityData/Q140131918.json) | Yüksek [CV] |
| Wikipedia | TR/FR/EN Wikipedia aramalarında platforma ilişkin bağımsız madde/taslak bulunmadı; TR sonuçları “reflektif” kelimesinin genel kullanımlarına gidiyor. | [Türkçe Wikipedia API](https://tr.wikipedia.org/w/api.php?action=query&list=search&srsearch=Reflektif&format=json), [Fransızca Wikipedia API](https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=Reflektif&format=json), [İngilizce Wikipedia API](https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Reflektif&format=json) | Yüksek [CV] |

**Repo için önerilen hafıza notu:** Reflektif, doğrulanabilir kamu verisi bakımından şu anda esasen self-source ve canlı site kanıtına dayanır; Fransız tarafında veri sorumlusu NETZ Informatique olarak, Türkiye tarafında ise yalnızca platform içi koşullar düzeyinde REFLEKTİF BİLİŞİM A.Ş. olarak görünmektedir ([Reflektif Privacy](https://reflektif.net/privacy), [Reflektif Öğrenci Koşulları](https://ogrenci.reflektif.net/terms)).

## 5. Web varlıkları durumu

| Varlık | Canlılık / erişim | İçerik ve amaç özeti | Teknoloji ipuçları | Kaynak | Güven |
|---|---|---|---|---|---|
| netzinformatique.fr | 200 / canlı | Haguenau merkezli IT, dépannage, maintenance, cybersécurité, IA, cloud, web/SEO ve formation hizmetleri. | Vercel; React/Vite SPA olası. | [NETZ Informatique](https://www.netzinformatique.fr) | Orta [Tek] |
| formation-haguenau.fr | 200 / canlı | Bilişim eğitimleri; programlama, WordPress/Shopify, Python/Django/Flask, Java, C#, JS, SQL, GitHub, cloud ve AI araçları menüleri. | nginx, PHP/Plesk, WordPress, Elementor, Site Kit. | [Formation Haguenau](https://formation-haguenau.fr/) | Orta [Tek] |
| bilancompetence.ai | 200 / canlı | “Bilan de compétences nouvelle génération”, IA destekli kariyer/bilan akışı ve CPF finansmanı beyanı. | Cloudflare, Express, React/Vite olası. | [bilancompetence.ai](https://bilancompetence.ai/) | Orta [Tek] |
| mikail.net | 200 / canlı | Mikail Lekesiz kişisel portföyü; teknoloji lideri, girişimci, Netz ve Reflektif anlatısı. | nginx, PHP/Plesk, WordPress/Site Kit ve React olası. | [mikail.net](https://mikail.net/) | Orta [Tek] |
| haguenau.pro | 200 / canlı | Haguenau yerel işletme/profesyonel dizini; müşteri yorumları ve profil görünürlüğü vaadi. | Vercel, Next.js, React. | [Haguenau.PRO](https://haguenau.pro/) | Orta [Tek] |
| boutique-haguenau.fr | 200 / canlı | Türk ve oryantal online épicerie; 1000+ ürün ve Fransa geneli teslimat beyanı. | nginx, PHP/Plesk, WordPress, WooCommerce, Site Kit. | [Boutique Haguenau](https://boutique-haguenau.fr/) | Orta [Tek] |
| reflektif.net | 200 / canlı | Bilimsel kariyer rehberliği, psikometrik testler, AI analiz ve 900+/920+ meslek eşleştirmesi. | railway-hikari; React/Vite olası. | [Reflektif](https://reflektif.net) | Orta [Tek] |

**Dikkat edilmesi gereken tutarsızlık:** NETZ sitesindeki “35 ans d’expérience” gibi ifadeler şirketin 2016 kuruluş tarihiyle doğrudan aynı kategori değildir; bu tür metinler kurumsal tarih değil, deneyim/uzmanlık beyanı olarak **[Tek]** notuyla saklanmalıdır ([NETZ Informatique](https://www.netzinformatique.fr), [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346)).

## 6. GitHub varlığı

| Alan | Bulgu | Kaynak | Güven |
|---|---|---|---|
| Profil | `lekesiz`, görünen ad Mikail LEKESIZ, şirket Netz Informatique, lokasyon Strasbourg, bio “devops engineer”. | [GitHub profile](https://github.com/lekesiz), [GitHub Users API](https://api.github.com/users/lekesiz) | Yüksek [CV] |
| Public repo sayısı | GitHub API 264 public repo ve 2 public gist döndürdü. | [GitHub Users API](https://api.github.com/users/lekesiz) | Yüksek [CV] |
| Profil oluşturma / güncelleme | API `created_at: 2014-08-05`, `updated_at: 2026-06-21` döndürdü. | [GitHub Users API](https://api.github.com/users/lekesiz) | Yüksek [CV] |
| `lekesiz/mikail` | Public; 25/06/2026’da oluşturulmuş, 25/06/2026’da push/update edilmiş, AI memory dosyaları içeriyor. | [lekesiz/mikail](https://github.com/lekesiz/mikail), [GitHub repo API](https://api.github.com/repos/lekesiz/mikail) | Yüksek [CV] |
| `lekesiz/reflektif` | Public repo olarak doğrulanamadı; erişim 403/404 ve public repo listesinde tam ad bulunmadı. | [lekesiz/reflektif](https://github.com/lekesiz/reflektif), [GitHub repos API](https://api.github.com/users/lekesiz/repos) | Düşük [?] |
| Reflektif benzeri public repo adları | Public repo listesinde `Reflektif.net_sorular` ve `reflektif-web` adları bulundu; içerik detayı bu raporda ayrıca klonlanmadı. | [GitHub repos API](https://api.github.com/users/lekesiz/repos) | Orta [Tek] |
| Teknoloji ipuçları | Son dönem public repolarda JavaScript, HTML, Python, TypeScript ve PHP görünüyor; örnekler `netzinformatique`, `mikail-ai`, `MonOPCO-v3`, `ai-web-content-analyzer`. | [GitHub repos API](https://api.github.com/users/lekesiz/repos), [lekesiz/netzinformatique](https://github.com/lekesiz/netzinformatique), [lekesiz/mikail-ai](https://github.com/lekesiz/mikail-ai) | Yüksek [CV] |
| Eğitimle dolaylı bağlantı | `lekesiz/unistra` public repo’su var; LP DWCA kaydını tek başına resmi biçimde kanıtlamaz. | [lekesiz/unistra](https://github.com/lekesiz/unistra), [GitHub repos API](https://api.github.com/users/lekesiz/repos) | Düşük [?] |

**Hassasiyet notu:** GitHub API’de e-posta ve bazı yetki/plan alanları görünebildi; repo hafızasına yalnızca public profil alanları alınmalı, kişisel e-posta **MASKED** tutulmalıdır ([GitHub Users API](https://api.github.com/users/lekesiz)).

## 7. Mikail Lekesiz kişisel/profesyonel dijital iz

| Kanal | Bulgu | Kaynak | Güven |
|---|---|---|---|
| LinkedIn kişi profili | Arama sonucu Mikail Lekesiz’i “PDG chez Netz Informatique et Reflektif” olarak gösteriyor; açık erişim fetch robot kısıtı nedeniyle sınırlı. | [LinkedIn profili](https://www.linkedin.com/in/mikail-lekesiz) | Orta [Tek] |
| LinkedIn şirket profili | NETZ Informatique şirket sayfası IT services/consulting, 2-10 çalışan, 2016 kuruluş ve Haguenau adresi gibi bilgiler gösteriyor; erişim robot kısıtlı. | [LinkedIn NETZ Informatique](https://fr.linkedin.com/company/netz-informatique) | Orta [Tek] |
| FranceNum | NETZ, France Num “Activateur” olarak listeleniyor; sayfa NETZ’i Mikail Lekesiz tarafından 2016’da Haguenau’da kurulan dijital hizmet/formation sağlayıcısı olarak tanıtıyor. | [France Num](https://www.francenum.gouv.fr/activateurs/netz-informatique) | Orta [Tek] |
| Kişisel portföy | mikail.net, Mikail Lekesiz’i teknoloji lideri/girişimci olarak konumlandırıyor ve Netz/Reflektif projelerini anlatıyor. | [mikail.net](https://mikail.net/) | Orta [Tek] |
| Yerel basın / iş dünyası | Bu araştırmada Haguenau yerel basınında bağımsız haber doğrulanamadı. | [France Num](https://www.francenum.gouv.fr/activateurs/netz-informatique) | Doğrulanamadı [?] |
| France Compétences/RS başvuruları | NETZ’in kendi adına certificateur olarak RS kaydı veya başvuru kaydı bu araştırmada doğrulanmadı; MCF katalogundaki kayıtlar Tosa/DigComp gibi RS referanslı sertifikasyonlara hazırlanma teklifleri olarak görünür. | [Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100), [France Compétences](https://www.francecompetences.fr) | Düşük [?] |

## 8. Sektörel bağlam ve stratejik değer

### 8.1 Bilan de compétences pazarı ve düzenleme bağlamı

| Konu | Güncel bağlam | Mikail/NETZ projelerine etkisi | Kaynak | Güven |
|---|---|---|---|---|
| Tanım ve amaç | Bilan de compétences, mesleki ve kişisel yetkinlikleri analiz ederek mesleki/eğitim projesi tanımlamaya yarar. | Reflektif ve bilancompetence.ai, psikometri + AI ile bu resmi çerçeveyi dijitalleştiren ürün hattı olarak konumlanabilir. | [Service-Public.fr](https://www.service-public.gouv.fr/particuliers/vosdroits/F3087), [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-public/tout-savoir-sur-le-bilan-de-competences) | Yüksek [CV] |
| Süre ve yapı | Resmi kaynaklar bilan de compétences süresini en fazla 24 saat ve üç fazlı süreç olarak açıklar: ön faz, araştırma/inceleme fazı, sonuç fazı. | NETZ’in AI destekli süreçlerini resmi üç faza açıkça bağlamak güvenilirliği artırır. | [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-public/tout-savoir-sur-le-bilan-de-competences), [Service-Public.fr](https://www.service-public.gouv.fr/particuliers/vosdroits/F3087) | Yüksek [CV] |
| CPF finansmanı | 2026 kaynaklarında CPF mobilizasyonu, koşullar ve katılım payı gibi kısıtlar öne çıkıyor. | “100% CPF” ifadeleri güncel istisna/katılım payı koşullarıyla uyumlu ve dikkatli yazılmalı. | [Service-Public.fr](https://www.service-public.gouv.fr/particuliers/vosdroits/F3087), [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-public/tout-savoir-sur-le-bilan-de-competences) | Yüksek [CV] |
| Pazar gerilimi | 2025’te bilan de compétences finansmanında olası kısıtlamalar ve kalite/fiyat heterojenliği üzerine sektör endişeleri raporlandı. | NETZ için kalite kanıtı, sonuç ölçümü, 6 ay takip ve metodoloji şeffaflığı rekabet avantajı olur. | [Centre Inffo](https://www.centre-inffo.fr/site-centre-inffo/actualites-centre-inffo/le-quotidien-de-la-formation-actualite-formation-professionnelle-apprentissage/articles-2025/financement-du-bilan-de-competences-les-acteurs-poussent-un-cri-dalarme) | Orta [Tek] |

### 8.2 Qualiopi 7 kriter / 32 gösterge

| Konu | Güncel bağlam | Mikail/NETZ projelerine etkisi | Kaynak | Güven |
|---|---|---|---|---|
| Qualiopi zorunluluğu | Kamu veya mutualisé fonlarla finanse edilen formation, bilan de compétences, VAE ve apprentissage faaliyetlerinde Qualiopi 01/01/2022’den beri kilit kalite şartıdır. | NETZ’in DGEFP kaydındaki sertifikasyonları CPF/OPCO iletişiminde ana güven unsuru olmalıdır. | [Ministère du Travail Qualiopi](https://travail-emploi.gouv.fr/qualiopi-marque-de-certification-qualite-des-prestataires-de-formation), [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| RNQ yapısı | Resmi rehber RNQ’nun 7 kriterden ve 22 ortak + 10 özel gösterge olmak üzere 32 göstergeden oluştuğunu belirtir. | Reflektif/bilancompetence.ai için erişilebilirlik, hedef uyumu, değerlendirme, iyileştirme ve paydaş geri bildirimi izlenebilir hale getirilmeli. | [Ministère du Travail RNQ guide](https://travail-emploi.gouv.fr/referentiel-national-qualite-guide-de-lecture-qualiopi) | Yüksek [CV] |
| Denetim döngüsü | Qualiopi sertifikasyonunda ilk denetim, yaklaşık 18 ayda gözetim ve 3 yılda yenileme çerçevesi bulunur. | NETZ’in kalite dokümantasyonu ve göstergeleri sürekli güncel tutulmalı. | [Ministère du Travail Qualiopi](https://travail-emploi.gouv.fr/qualiopi-marque-de-certification-qualite-des-prestataires-de-formation) | Yüksek [CV] |

### 8.3 France Compétences / Répertoire Spécifique (RS)

| Konu | Güncel bağlam | Mikail/NETZ projelerine etkisi | Kaynak | Güven |
|---|---|---|---|---|
| RS mantığı | France Compétences 2026 vademecum’u RS’yi mesleklere tamamlayıcı/transversal yetkinlikleri belgeleyen sertifikasyon repertuarı olarak açıklar; RNCP’den farklı olarak devletçe tanınan seviye vermez. | NETZ’in MCF eğitimleri Tosa/DigComp RS kodlarına bağlı olduğundan “certificateur” ve “préparation à certification” ayrımı net tutulmalı. | [France Compétences Vademecum 2026](https://www.francecompetences.fr/app/uploads/2026/01/20260121_FC_Vademecum.pdf), [France Compétences CP](https://www.francecompetences.fr/app/uploads/2026/02/CP_Publication-vademecum-21-janvier-2026-VF.pdf) | Yüksek [CV] |
| 2026 doktrin | 21/01/2026 vademecum’u RNCP/RS kayıt prosedürleri, kriterler, ön inceleme, karar aşaması ve reddedilme durumları için güncel referans olarak yayımlandı. | NETZ gelecekte kendi RS sertifikasyonu düşünürse, referentiel de compétences ve iş piyasası kanıtı şartları önceden tasarlanmalı. | [France Compétences CP](https://www.francecompetences.fr/app/uploads/2026/02/CP_Publication-vademecum-21-janvier-2026-VF.pdf), [Centre Inffo France Compétences](https://www.centre-inffo.fr/site-droit-formation/actualites-droit/france-competences-decision-denregistrement-aux-repertoires-nationaux) | Yüksek [CV] |

### 8.4 QualiRépar / Bonus Réparation

| Konu | Güncel bağlam | Mikail/NETZ projelerine etkisi | Kaynak | Güven |
|---|---|---|---|---|
| Program amacı | QualiRépar, AGEC yasası kapsamında elektrikli/elektronik cihazların kullanım ömrünü uzatmayı ve onarımı teşvik etmeyi hedefler. | NETZ’in PC/Mac repair faaliyetleri için çevresel ve satın alma gücü argümanı oluşturur. | [AFNOR QualiRépar](https://certification.afnor.org/environnement/label-qualirepar) | Yüksek [CV] |
| Bonus işleyişi | Bonus réparation etiketli ağdaki onarımda faturadan doğrudan indirim olarak uygulanır. | Web ve mağaza iletişiminde “bonus uygulanabilirliği” ürün/kategori/alt limit şartlarıyla birlikte verilmelidir. | [AFNOR QualiRépar](https://certification.afnor.org/environnement/label-qualirepar), [Label QualiRépar](https://www.label-qualirepar.fr/particulier/bonusreparation.html) | Yüksek [CV] |
| NETZ için kanıt düzeyi | NETZ’in QualiRépar varlığı Reparea ile destekleniyor; resmi numara/label id için ek belge gerekli. | Repo’da “QualiRépar varlığı: Orta [Tek]; no 1056: [?]” olarak saklanmalı. | [Reparea NETZ sayfası](https://reparea.fr/annuaire-reparateurs/netz-informatique-haguenau) | Orta [Tek] |

### 8.5 OPCO ATLAS ve l’Opcommerce finansmanı

| Konu | Güncel bağlam | Mikail/NETZ projelerine etkisi | Kaynak | Güven |
|---|---|---|---|---|
| OPCO ATLAS 2026 | Atlas 2026 kriterleri, şube önceliklerine göre actions éligibles, prise en charge ve finansman modalitelerinin değişebileceğini duyurdu. | NETZ’in IT/AI/cyber eğitimleri için her müşteri branşına göre kriter kontrolü yapılmalı. | [OPCO Atlas 2026 kriterleri](https://www.opco-atlas.fr/actualites/decouvrez-les-nouveaux-criteres-de-financement-2026.html) | Yüksek [CV] |
| Atlas bureaux d’études | Bureaux d’études/ingénieurs/conseils sayfası 2026 kriterlerinin 01/01/2026’dan beri fon mevcudiyetine bağlı uygulanacağını ve dosyaların eğitim başlamadan önce verilmesi gerektiğini belirtir. | MonOPCO/OPCO danışmanlığı için “avant démarrage” uyarısı kritik olmalı. | [OPCO Atlas branche BETIC](https://www.opco-atlas.fr/criteres-financement/bureaux-detudes-techniques-ingenieurs-et-conseils) | Yüksek [CV] |
| l’Opcommerce alternance | l’Opcommerce, alternance finansmanının OPCO’lara emanet edildiğini ve contrat d’apprentissage desteğinin France Compétences tarafından referanslanan yıllık coût contrat üzerinden yapıldığını açıklar. | NETZ çıraklık/alternance bağlamı iddiası için şirket özelinde sözleşme kanıtı yok; yalnızca sektörel finansman çerçevesi doğrulandı. | [l’Opcommerce alternance](https://www.lopcommerce.com/entreprise/recruter-un-collaborateur/contrats-en-alternance/) | Yüksek [CV] |
| 2026 apprentissage yardımı | l’Opcommerce 2026’da devletin apprentissage istihdam yardımlarını belirli koşullarla sürdürdüğünü duyurdu. | Çıraklık iletişiminde tarih, seviye ve şirket büyüklüğü koşulları net verilmeli. | [l’Opcommerce apprentissage 2026](https://www.lopcommerce.com/l-opcommerce/actualites/apprentissage-quelles-aides-pour-les-employeurs-en-2026/) | Yüksek [CV] |
| NETZ’in l’Opcommerce dosyası | NETZ’e özel l’Opcommerce çıraklık dosyası bu araştırmada halka açık kaynakla doğrulanamadı. | Repo’da “l’Opcommerce çıraklık: [?]” olarak tutulmalı. | [l’Opcommerce alternance](https://www.lopcommerce.com/entreprise/recruter-un-collaborateur/contrats-en-alternance/) | Doğrulanamadı [?] |

## 9. Repo için önerilen AI Hafıza Envanteri güncelleme blokları

### 9.1 Yüksek güvenli [CV] bloklar

- **[CV] NETZ Informatique**: SIREN 818 347 346, SIRET siège 81834734600020, aktif SAS/SASU, adres 1 A Route de Schweighouse, 67500 Haguenau, APE/NAF 85.59B, kuruluş/immatriculation Şubat 2016, dirigeant Mikail LEKESIZ, siège aktif; kanıt resmi API + Societe/Le Figaro ile çapraz doğrulandı ([recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html), [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346)).
- **[CV] NETZ finansal veri**: Halka açık doğrulanmış finansal rakam olarak 2022 ciro 404.272 € ve net sonuç 8.882 € kullanılmalı; 2025 ciro iddiası kamu kaynağıyla doğrulanmadı ([recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Numbers.finance](https://numbers.finance/entreprise/netz-informatique-818347346)).
- **[CV] NETZ organisme de formation / Qualiopi**: NDA 44670671567; Actions de formations ve Bilans de compétences sertifikasyon kategorileri; 2025 beyan döneminde 404 stagiaire ve 2 formateur ([DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/)).
- **[CV] Mon Compte Formation katalog**: SIRET 81834734600020 altında 18 RS referanslı eğitim kaydı; başlıklar Tosa/DigComp/Office/WordPress/Python/AutoCAD/Adobe/M365 ekseninde yoğunlaşıyor ([Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100)).
- **[CV] GitHub**: `lekesiz` profilinde 264 public repo; `lekesiz/mikail` public ve AI memory envanter dosyaları içeriyor ([GitHub Users API](https://api.github.com/users/lekesiz), [lekesiz/mikail](https://github.com/lekesiz/mikail)).

### 9.2 Orta güvenli [Tek] bloklar

- **[Tek] Reflektif**: Reflektif.net canlı; RIASEC, Big Five, Professional Values, AI debrief, 920+ careers ve TR/FR/EN dil desteği beyan ediyor; bu bilgiler platformun kendi sayfalarından geldiği için self-source notuyla saklanmalı ([Reflektif](https://reflektif.net), [Reflektif Business](https://www.reflektif.net/business)).
- **[Tek] Web varlıkları**: netzinformatique.fr, formation-haguenau.fr, bilancompetence.ai, mikail.net, haguenau.pro, boutique-haguenau.fr ve reflektif.net 25/06/2026 itibarıyla canlı; teknoloji ipuçları HTTP başlıkları ve HTML meta/generator alanlarından türetildi ([NETZ Informatique](https://www.netzinformatique.fr), [Formation Haguenau](https://formation-haguenau.fr/), [bilancompetence.ai](https://bilancompetence.ai/), [mikail.net](https://mikail.net/), [Haguenau.PRO](https://haguenau.pro/), [Boutique Haguenau](https://boutique-haguenau.fr/), [Reflektif](https://reflektif.net)).
- **[Tek] QualiRépar varlığı**: NETZ Reparea’da QualiRépar onaylı tamirci olarak görünüyor; resmi label numarası ayrıca belgelenmeli ([Reparea NETZ sayfası](https://reparea.fr/annuaire-reparateurs/netz-informatique-haguenau)).

### 9.3 Belirsiz / çürütülen [?] bloklar

- **[?] 2025 ciro ~1,27M €**: Kamuya açık resmi kaynakla doğrulanamadı; repo’da kesin rakam gibi kullanılmamalı ([recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346)).
- **[?] EDOF/WEDOF ~1.451 dosya**: Mon Compte Formation açık katalogu yalnızca 18 eğitim kaydı doğruladı; dosya hacmi kamu verisiyle doğrulanmadı ([Caisse des Dépôts OpenData API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100)).
- **[?] Reflektif Bilişim A.Ş.**: Yalnızca Reflektif öğrenci koşullarında beyan edildi; resmi Türkiye sicil kaydı bulunamadı ([Reflektif Öğrenci Koşulları](https://ogrenci.reflektif.net/terms), [TOBB Ticaret Sicili](https://www.ticaretsicil.gov.tr), [MERSİS](https://mersis.ticaret.gov.tr)).
- **[Çürütüldü] Wikidata Q140131918**: İlgili entity mevcut değil; repo’daki Wikidata iddiası kaldırılmalı veya “eski/yanlış id” olarak işaretlenmeli ([Wikidata EntityData](https://www.wikidata.org/wiki/Special:EntityData/Q140131918.json)).
- **[?] `lekesiz/reflektif` repo**: Public repo olarak doğrulanamadı; bunun yerine public listede `Reflektif.net_sorular` ve `reflektif-web` adları bulundu ([GitHub repos API](https://api.github.com/users/lekesiz/repos), [lekesiz/reflektif](https://github.com/lekesiz/reflektif)).

## 10. İzleme ve sonraki doğrulama önerileri

| Öncelik | Yapılacak doğrulama | Neden önemli | Önerilen kaynak | Güven hedefi |
|---|---|---|---|---|
| 1 | 2023/2024/2025 NETZ bilan ve CA rakamlarını INPI/RNE/Kbis veya resmi comptes annuels üzerinden kontrol etmek. | 2025 ~1,27M € iddiası şu anda kamu kaynağıyla desteklenmiyor. | [Registre national des entreprises](https://registre.entreprises.gouv.fr), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| 2 | QualiRépar resmi annuaire ekran görüntüsü veya certificate id ile “no 1056” doğrulamak. | Label no iddiası repo’da netleştirilmeli. | [Label QualiRépar annuaires](https://www.label-qualirepar.fr/annuaires/), [ecosystem](https://www.ecosystem.eco/reparer/) | Yüksek [CV] |
| 3 | Reflektif Bilişim A.Ş. için Ticaret Sicili Gazetesi/MERSİS ilanı bulmak. | Türkiye tüzel bağlantısı şu anda self-source seviyesinde. | [TOBB Ticaret Sicili](https://www.ticaretsicil.gov.tr), [MERSİS](https://mersis.ticaret.gov.tr) | Yüksek [CV] |
| 4 | `lekesiz/reflektif` repo adının private/renamed/organization kısıtı mı olduğunu GitHub owner hesabından doğrulamak. | Repo hafızasında yanlış public repo iddiası oluşmamalı. | [GitHub repos API](https://api.github.com/users/lekesiz/repos), [lekesiz/reflektif](https://github.com/lekesiz/reflektif) | Yüksek [CV] |
| 5 | LP DWCA 2025/2026 eğitim iddiası için üniversite kaydı, öğrenci belgesi veya public portfolio sayfası bulmak. | Eğitim iddiası şu anda public kaynakta resmi doğrulanmadı. | [Université de Strasbourg](https://www.unistra.fr), [lekesiz/unistra](https://github.com/lekesiz/unistra) | Orta/Yüksek |

---

**Kısa sonuç:** NETZ Informatique’in kurumsal, OF/Qualiopi ve MCF eğitim kataloğu boyutları güçlü biçimde doğrulandı; Reflektif’in ürün ve canlılık bilgisi doğrulandı ancak tüzel yapı/Wikidata/GitHub repo iddialarında düzeltme gerekiyor. Repo’daki AI hafıza envanterlerinde 2025 ciro, EDOF dosya sayısı, QualiRépar no 1056, Reflektif Bilişim A.Ş., Wikidata Q140131918 ve `lekesiz/reflektif` alanları **[?]** veya **çürütüldü** olarak güncellenmelidir.
