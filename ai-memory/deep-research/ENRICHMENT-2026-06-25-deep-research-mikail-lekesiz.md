# AI Hafıza Envanteri — Derin Araştırma Zenginleştirme & Doğrulama

> **Üreten:** Perplexity Computer (Claude) — Derin Araştırma modu
> **Tarih:** 25 Haziran 2026 (Europe/Paris)
> **Amaç:** `lekesiz/mikail` reposundaki AI hafıza envanterlerini, halka açık resmi kaynaklar + kullanıcının kendi Google Drive arşivi ile **doğrulamak, düzeltmek ve genişletmek**.
> **Kaynak katmanları:** (1) Resmi/açık web kaynakları (INSEE/recherche-entreprises API, DGEFP, Caisse des Dépôts/Mon Compte Formation, GitHub API, Wikidata, vb.) — her satırda URL'li. (2) Kullanıcının Google Drive birinci el belgeleri — `[Drive-CV]` / `[Drive-Tek]` ile işaretli.
>
> **Güven notasyonu:** **Yüksek [CV]** = resmi kaynak veya ≥2 bağımsız kaynak · **Orta [Tek]** = tek kaynak/self-source · **Düşük [?]** = sınırlı/çelişkili · **Doğrulanamadı [?]** = halka açık kanıt bulunamadı · **[Çürütüldü]** = aksi kanıtlandı · **[Drive-CV/Tek]** = kullanıcının kendi belgesi.
>
> **Hassas veri:** Kişisel e-posta, telefon, doğum tarihi, IBAN, API anahtarları, sunucu IP'leri **\*\*\*MASKED\*\*\***.

---

## 0. Yönetici Özeti

Bu zenginleştirme çalışması, repodaki envanterlerin **en güçlü iddialarını resmi kaynaklarla doğrularken**, bazı önemli iddiaları **düzeltmekte veya çürütmektedir**. Üç kritik bulgu:

1. **Netz Informatique kurumsal kimliği güçlü biçimde doğrulandı** (SIREN/SIRET/adres/OF kaydı/MCF kataloğu) — ancak repoda "Yüksek [CV]" olarak geçen bazı finansal/operasyonel rakamlar (2025 ciro ~1,27M €, EDOF ~1.451 dosya, QualiRépar no 1056) **halka açık kaynakla doğrulanamadı** ve düşürülmelidir.
2. **Repodaki belirsiz [?] alanlar netleşti:** İngiltere şirketinin adı kullanıcının Drive arşivinde **CortexAI** olarak bulundu; Reflektif Bilişim A.Ş.'nin kuruluş tarihi (16 Mart 2026), sermayesi ve ekibi Drive'da detaylandı.
3. **İki repo iddiası çürütüldü/düzeltilmeli:** Wikidata **Q140131918 mevcut değil**; **`github.com/lekesiz/reflektif`** public repo olarak doğrulanamadı (bunun yerine `Reflektif.net_sorular` ve `reflektif-web` adlı public repolar var).

---

## 1. Yeni Bulgular ve Doğrulama Tablosu (Ana Özet)

| Repo iddiası | Sonuç | Kanıt | Kaynak | Güven |
|---|---|---|---|---|
| Mikail Lekesiz, Haguenau merkezli girişimci/CEO | ✅ Doğrulandı | Resmi şirket kaydı NETZ başkanı = Mikail LEKESIZ; LinkedIn "PDG chez Netz Informatique et Reflektif" | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [LinkedIn](https://www.linkedin.com/in/mikail-lekesiz) | Yüksek [CV] |
| Netz Informatique SIREN 818 347 346 | ✅ Doğrulandı | SIREN/SIRET/adres/APE/durum resmi API + Societe + Le Figaro uyumlu | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| Netz organisme de formation / Qualiopi | ✅ Doğrulandı | DGEFP listesinde NDA 44670671567; Actions de formations + Bilans de compétences sertifikalı | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Netz SIRET 81834734600020 EDOF/MCF aktif | ✅ Doğrulandı | MCF kataloğunda 18 RS referanslı eğitim + Drive'da 2022–2026 ~30 EDOF dossier export'u | [Caisse des Dépôts API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100); Drive `Export_Tous les dossiers_81834734600020_*` | Yüksek [CV] / [Drive-CV] |
| Netz 2022 ciro ~404k € | ✅ Doğrulandı | Resmi API 404.272 €, net sonuç 8.882 € | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346), [Numbers.finance](https://numbers.finance/entreprise/netz-informatique-818347346) | Yüksek [CV] |
| Netz **2025 ciro ~1,27M €** | ⚠️ Doğrulanamadı | Açık resmi kaynakta 2025 rakamı yok; en güncel doğrulanmış veri 2022 | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Düşük [?] |
| **EDOF/WEDOF ~1.451 dosya** | ⚠️ Doğrulanamadı | Açık MCF kataloğu yalnızca 18 eğitim kaydı gösteriyor; dosya hacmi kamu verisiyle doğrulanamaz (iç metrik) | [Caisse des Dépôts API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100) | Düşük [?] |
| **QualiRépar etiketi no 1056** | ⚠️ Kısmen | Reparea NETZ'i "QualiRépar agréé" listeliyor; "1056" numarası resmi annuaire'de doğrulanamadı | [Reparea](https://reparea.fr/annuaire-reparateurs/netz-informatique-haguenau), [Label QualiRépar](https://www.label-qualirepar.fr/annuaires/) | Orta [Tek] / no: [?] |
| Reflektif.net canlı, AI kariyer platformu | ✅ Doğrulandı | Site 200; RIASEC + Big Five + Values + AI + 920+ meslek | [Reflektif](https://reflektif.net), [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| **Reflektif Bilişim A.Ş. (Türkiye tüzel)** | 🔶 Drive'da detaylı, resmi sicil [?] | Drive: A.Ş. kuruluş 16 Mart 2026, %100 Mikail, 1M TL sermaye. Site öğrenci koşulları unvanı beyan ediyor. TR Ticaret Sicili/MERSİS doğrulaması bulunamadı | Drive `REFLEKTIF-BILGI-TABANI.md`; [Reflektif Öğrenci Koşulları](https://ogrenci.reflektif.net/terms) | [Drive-CV] / resmi: [?] |
| **İngiltere şirketi (repoda isimsiz [?])** | 🆕 İsim tespit edildi | Drive: Mikail'in 3. şirketi = **CortexAI (İngiltere)** | Drive `REFLEKTIF-BILGI-TABANI.md` | [Drive-Tek] |
| **Wikidata Q140131918** | ❌ Çürütüldü | EntityData "No entity with ID" 404 döndü; entity mevcut değil | [Wikidata EntityData](https://www.wikidata.org/wiki/Special:EntityData/Q140131918.json) | Yüksek [CV] |
| **`github.com/lekesiz/reflektif`** | ⚠️ Doğrulanamadı | Public repo listesinde yok (403/404); bunun yerine `Reflektif.net_sorular`, `reflektif-web` var | [GitHub repos API](https://api.github.com/users/lekesiz/repos) | Düşük [?] |
| `github.com/lekesiz/mikail` | ✅ Doğrulandı | Public, 25/06/2026 oluşturuldu, AI memory dosyaları içeriyor | [lekesiz/mikail](https://github.com/lekesiz/mikail) | Yüksek [CV] |
| GitHub profili `lekesiz` | ✅ Doğrulandı + genişletildi | 264 public repo, ad "Mikail LEKESIZ", şirket Netz Informatique, lokasyon Strasbourg, bio "devops engineer", hesap 2014'ten beri | [GitHub Users API](https://api.github.com/users/lekesiz) | Yüksek [CV] |
| Strasbourg Üni. LP DWCA 2025/2026 | 🔶 Dolaylı | Public `lekesiz/unistra` reposu var; resmi üniversite kaydı doğrulanamadı | [lekesiz/unistra](https://github.com/lekesiz/unistra) | Düşük [?] |

---

## 2. Netz Informatique — Resmi Kurumsal Doğrulama

| Alan | Doğrulanan bilgi | Kaynak | Güven |
|---|---|---|---|
| Tüzel ad | NETZ INFORMATIQUE | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Yüksek [CV] |
| SIREN | 818 347 346 | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Yüksek [CV] |
| SIRET siège | 818 347 346 00020 | [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| Kuruluş | Resmi API 10/02/2016; Societe RCS 23/02/2016 | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Yüksek [CV] |
| Adres | 1 A Route de Schweighouse, 67500 Haguenau | [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346) | Yüksek [CV] |
| Hukuki form | SAS/SASU (nature juridique 5710) | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Yüksek [CV] |
| APE/NAF | 85.59B "Autres enseignements" (API'de 85.59H da görünüyor) | [Le Figaro Entreprises](https://entreprises.lefigaro.fr/netz-informatique-67/entreprise-818347346) | Yüksek [CV] |
| Yönetici | Mikail LEKESIZ, Président de SAS (doğum bilgisi MASKED) | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Yüksek [CV] |
| Durum | Aktif (etat_administratif: A, date_fermeture: null) | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Yüksek [CV] |
| Etablissement | 2 toplam / 1 açık (eski SIRET ...00012 kapalı) | [Societe.com](https://www.societe.com/societe/netz-informatique-818347346.html) | Yüksek [CV] |
| 2022 finansal | Ciro 404.272 €, net sonuç 8.882 € | [Numbers.finance](https://numbers.finance/entreprise/netz-informatique-818347346) | Yüksek [CV] |
| 2025 finansal | Halka açık kaynakta doğrulanamadı | [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=818347346) | Doğrulanamadı [?] |

> ⚠️ **Düzeltme:** NETZ sitesindeki "35 ans d'expérience" türü ifadeler şirketin 2016 kuruluşuyla çelişmez; bunlar kurumsal yaş değil deneyim/uzmanlık beyanıdır ([NETZ](https://www.netzinformatique.fr)).

### 2.1 Organisme de Formation / Qualiopi (DGEFP resmi kaydı)

| Alan | Bilgi | Kaynak | Güven |
|---|---|---|---|
| NDA | 44670671567 | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| OF SIRET | 81834734600020 | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Sertifikasyon kategorileri | Actions de formations ✅ · Bilans de compétences ✅ · VAE ❌ · Apprentissage ❌ | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Son deklarasyon | 13/04/2026 (dönem 01/01/2025–31/12/2025) | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Uzmanlık alanları | 326 Informatique/réseaux · 415 Orientation/insertion professionnelle | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |
| Stagiaire / formateur | 404 stagiaire · 2 formateur (2025 beyanı) | [DGEFP OpenData](https://dgefp.opendatasoft.com/explore/dataset/liste-publique-des-of-v2/table/) | Yüksek [CV] |

> **Not:** DGEFP'in resmi "Apprentissage = false" kaydı, repodaki "10+ çıraklık sözleşmesi (l'Opcommerce)" iddiasıyla görünürde çelişir. OF kaydı çıraklık *eğitimi vermeyi* yansıtır; şirketin *çırak istihdam etmesi* ayrı bir şeydir. Bu ayrım repoda netleştirilmeli — l'Opcommerce çıraklık dosyaları halka açık doğrulanamadı [?].

### 2.2 Mon Compte Formation Kataloğu (18 RS referanslı eğitim)

SIRET 81834734600020 altında 25/06/2026 extract'inde **18 eğitim**, tümü RS referanslı (Tosa/DigComp ailesi), Bas-Rhin/Grand Est ([Caisse des Dépôts API](https://opendata.caissedesdepots.fr/api/explore/v2.1/catalog/datasets/moncompteformation_catalogueformation/records?where=siret%3D%2281834734600020%22&limit=100)):

| Eğitim | Sertifikasyon | RS kodu |
|---|---|---|
| PowerPoint percutant | Présentations PowerPoint (Tosa) | RS6961 |
| Office VBA otomasyon | Automatiser Office avec VBA (Tosa) | RS6963 |
| Python otomasyon | Programmer/automatiser avec Python (Tosa) | RS6962 |
| DigComp | DigComp (Tosa) | RS6893 |
| WordPress | Sites web WordPress (Tosa) | RS6965 |
| Excel | Microsoft Excel (Tosa) | RS7256 |
| AutoCAD/InDesign/Word/Photoshop/Access/Illustrator/Outlook/M365 | Tosa RS ailesi | RS6955/6957/6964/6959/7096/6956/6958/6960 |

> ⚠️ Açık katalogda NETZ adına doğrudan **"bilan de compétences" MCF teklifi doğrulanamadı**, ancak DGEFP listesi bu kategoride sertifikalı olduğunu doğruluyor.

---

## 3. Reflektif — Doğrulama + Drive Zenginleştirmesi

### 3.1 Halka açık web (reflektif.net)

| Alan | Bulgu | Kaynak | Güven |
|---|---|---|---|
| Site durumu | Canlı (200); www.reflektif.net'e yönleniyor | [Reflektif](https://reflektif.net) | Yüksek [CV] |
| Konumlandırma | RIASEC + Big Five + Professional Values + AI analiz | [Reflektif](https://reflektif.net) | Orta [Tek] |
| Test yapısı | RIASEC 30s · Big Five 50s · Values 30s · "Living Tests" AI görüşmesi | [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| Katalog | 920+ meslek, kişiselleştirilmiş Top 30 eşleştirme | [Reflektif](https://reflektif.net) | Orta [Tek] |
| Dil | TR / FR / EN | [Reflektif Business](https://www.reflektif.net/business) | Orta [Tek] |
| Fiyat | Discovery 0 € · Expert Guidance 199 € | [Reflektif Pricing](https://www.reflektif.net/pricing) | Orta [Tek] |
| Veri sorumlusu | NETZ Informatique SASU / SIREN 818 347 346; AI raporları Google Gemini ile | [Reflektif Privacy](https://reflektif.net/privacy) | Orta [Tek] |
| Wikidata Q140131918 | ❌ Mevcut değil (404) | [Wikidata EntityData](https://www.wikidata.org/wiki/Special:EntityData/Q140131918.json) | Yüksek [CV] |
| Wikipedia | TR/FR/EN'de bağımsız madde/taslak yok | [TR Wikipedia API](https://tr.wikipedia.org/w/api.php?action=query&list=search&srsearch=Reflektif&format=json) | Yüksek [CV] |

> **Önemli nüans:** Fransa tarafında veri sorumlusu **NETZ Informatique**; Türkiye tarafında öğrenci koşulları **REFLEKTİF BİLİŞİM A.Ş.** beyan ediyor. İki tüzel yapının ilişkisi (Fr operasyon ↔ Tr A.Ş.) repoda açıkça not edilmeli.

### 3.2 Drive arşivinden genişletilmiş profil ([Drive-CV] — kullanıcının kendi belgeleri)

Kaynak: `REFLEKTIF-BILGI-TABANI.md` (Pangea Agoras, 18 Haz 2026), `Reflektif_Fizibilite_Raporu.md` (Net&Work, Mayıs 2026), `01_Dossier_Presentation_REFLEKTIF.pdf`.

- **Tüzel/finansal:** Anlaşma 8 Mart 2026 · A.Ş. kuruluş 16 Mart 2026 · %100 Mikail Lekesiz · sermaye 1.000.000 TL (10.000 hisse) · hedef değerleme 10M € · aylık burn rate ~296.900 TL · finansman: şahsi gelir + Netz Informatique + CortexAI.
- **Ofis:** Zaim Teknopark (İstanbul Sabahattin Zaim Üniversitesi) + Kağıthane paylaşımlı ofis.
- **Tech stack (planlanan):** Vercel + Supabase + AWS S3. (Not: canlı site HTTP başlığında `railway-hikari` görüldü — deployment Railway olabilir [Tek].)
- **Çift modlu motor:** Mod A (pragmatik kariyer) + Mod B (varoluşsal/fıtrat) — Drive belgesi "Türkiye'de Mod B sunan tek platform" diyor.
- **Çekirdek ekip:** Mikail Lekesiz (Kurucu/GM/Teknik Lider) · Halil Kılıç (Operasyon) · Şeyma Lekesiz (Netz'te görevli) · Sudenur Tekce (Teknopark köprüsü) · Nihat Bey (muhasebe).
- **Yeni ürün hattı:** **Reflektif İK** — kurumsal İK pazarına yönelik (Net&Work fizibilite raporu Mayıs 2026).
- **Aktif proje:** İZÜ × Reflektif pilotu (zaim.reflektif.net, 30 soruluk test, ~41 bölüm eşleştirme), 20 Temmuz – 10 Ağustos 2026.

---

## 4. Web Varlıkları Durumu (25/06/2026, hepsi canlı 200)

| Varlık | Amaç | Teknoloji ipuçları | Kaynak |
|---|---|---|---|
| netzinformatique.fr | IT, dépannage, cybersécurité, IA, cloud, web/SEO, formation | Vercel; React/Vite SPA | [NETZ](https://www.netzinformatique.fr) |
| formation-haguenau.fr | Bilişim eğitimleri (programlama, WordPress, Python/Django, AI) | nginx, PHP/Plesk, WordPress, Elementor | [Formation Haguenau](https://formation-haguenau.fr/) |
| bilancompetence.ai | "Bilan de compétences nouvelle génération", IA + CPF | Cloudflare, Express, React/Vite | [bilancompetence.ai](https://bilancompetence.ai/) |
| mikail.net | Kişisel portföy (teknoloji lideri/girişimci) | nginx, PHP/Plesk, WordPress + React | [mikail.net](https://mikail.net/) |
| haguenau.pro | Haguenau yerel işletme dizini | Vercel, Next.js, React | [Haguenau.PRO](https://haguenau.pro/) |
| boutique-haguenau.fr | Türk/oryantal online épicerie (1000+ ürün) | nginx, WordPress, WooCommerce | [Boutique Haguenau](https://boutique-haguenau.fr/) |
| reflektif.net | Kariyer rehberliği + psikometri + AI | railway-hikari; React/Vite | [Reflektif](https://reflektif.net) |

---

## 5. GitHub Varlığı (lekesiz)

| Alan | Bulgu | Kaynak | Güven |
|---|---|---|---|
| Profil | ad "Mikail LEKESIZ", şirket Netz Informatique, lokasyon Strasbourg, bio "devops engineer" | [GitHub Users API](https://api.github.com/users/lekesiz) | Yüksek [CV] |
| Public repo | 264 repo + 2 gist; hesap 2014-08-05'ten beri, son güncelleme 2026-06-21 | [GitHub Users API](https://api.github.com/users/lekesiz) | Yüksek [CV] |
| `lekesiz/mikail` | Public, 25/06/2026, AI memory dosyaları | [lekesiz/mikail](https://github.com/lekesiz/mikail) | Yüksek [CV] |
| `lekesiz/reflektif` | Doğrulanamadı (403/404); bunun yerine `Reflektif.net_sorular`, `reflektif-web` var | [GitHub repos API](https://api.github.com/users/lekesiz/repos) | Düşük [?] |
| Teknoloji | JavaScript, HTML, Python, TypeScript, PHP; örnekler `netzinformatique`, `mikail-ai`, `MonOPCO-v3`, `ai-web-content-analyzer` | [GitHub repos API](https://api.github.com/users/lekesiz/repos) | Yüksek [CV] |

---

## 6. Sektörel Bağlam (2025/2026 — projelere stratejik değer)

| Konu | Güncel bağlam | Etki | Kaynak |
|---|---|---|---|
| Bilan de compétences | Maks. 24 saat, 3 fazlı (ön/araştırma/sonuç) süreç; CPF finansmanı | Reflektif/bilancompetence.ai resmi 3 faza bağlanmalı | [Service-Public.fr](https://www.service-public.gouv.fr/particuliers/vosdroits/F3087), [Mon Compte Formation](https://www.moncompteformation.gouv.fr/espace-public/tout-savoir-sur-le-bilan-de-competences) |
| BdC finansman gerilimi (2025) | Sektör finansman kısıtları konusunda "alarm" verdi | Kalite kanıtı/6 ay takip rekabet avantajı | [Centre Inffo](https://www.centre-inffo.fr/site-centre-inffo/actualites-centre-inffo/le-quotidien-de-la-formation-actualite-formation-professionnelle-apprentissage/articles-2025/financement-du-bilan-de-competences-les-acteurs-poussent-un-cri-dalarme) |
| Qualiopi RNQ | 7 kriter / 32 gösterge (22 ortak + 10 özel); 18 ay gözetim, 3 yıl yenileme | NETZ kalite dokümantasyonu güncel tutulmalı | [Ministère du Travail RNQ](https://travail-emploi.gouv.fr/referentiel-national-qualite-guide-de-lecture-qualiopi) |
| France Compétences RS | 21/01/2026 vademecum yayınlandı; RS = transversal yetkinlik, RNCP'den farklı (seviye vermez) | "certificateur" ↔ "préparation" ayrımı net olmalı | [FC Vademecum 2026](https://www.francecompetences.fr/app/uploads/2026/01/20260121_FC_Vademecum.pdf) |
| QualiRépar / Bonus Réparation | AGEC yasası; faturadan doğrudan indirim (örn. dizüstü onarımı min 150 €'da 50 € bonus) | NETZ repair için çevre + satın alma gücü argümanı | [AFNOR QualiRépar](https://certification.afnor.org/environnement/label-qualirepar), [ecosystem](https://www.ecosystem.eco/reparer/equipement/ordinateur-portable) |
| OPCO ATLAS 2026 | Yeni finansman kriterleri 01/01/2026'dan; dosya eğitim başlamadan verilmeli | NETZ/MonOPCO için "avant démarrage" uyarısı kritik | [OPCO Atlas 2026](https://www.opco-atlas.fr/actualites/decouvrez-les-nouveaux-criteres-de-financement-2026.html) |
| l'Opcommerce alternance | Çıraklık finansmanı OPCO + France Compétences coût contrat üzerinden | NETZ çıraklık iddiası şirket özelinde doğrulanamadı [?] | [l'Opcommerce](https://www.lopcommerce.com/entreprise/recruter-un-collaborateur/contrats-en-alternance/) |

---

## 7. Repo Envanterleri İçin Önerilen Düzeltmeler

Mevcut `ai-memory/*.md` envanterlerinde şu alanlar **güncellenmelidir**:

1. **2025 ciro ~1,27M €** → "Yüksek [CV]"den **"Düşük [?] — halka açık kaynakla doğrulanmadı"a** indir. Doğrulanmış son rakam: 2022 = 404.272 €.
2. **EDOF/WEDOF ~1.451 dosya** → **[?]** olarak işaretle (iç metrik; açık katalog 18 eğitim gösteriyor). Drive'da 2022–2026 dossier export'larının varlığı operasyonun sürekliliğini destekliyor ama dosya sayısı bağımsız doğrulanamaz.
3. **QualiRépar no 1056** → "varlık: Orta [Tek] (Reparea); numara 1056: [?]".
4. **İngiltere şirketi [?]** → **"CortexAI (İngiltere) [Drive-Tek]"** olarak isimlendir; tüzel detay hâlâ doğrulanmalı.
5. **Reflektif Bilişim A.Ş.** → Drive detaylarını ekle (16 Mart 2026 kuruluş, 1M TL sermaye, %100 Mikail) ama "resmi TR sicil doğrulaması: [?]" notunu koru.
6. **Wikidata Q140131918** → **[Çürütüldü]** — entity mevcut değil, kaldır veya "yanlış/eski id" işaretle.
7. **github.com/lekesiz/reflektif** → "doğrulanamadı [?]"; bunun yerine `Reflektif.net_sorular` ve `reflektif-web` public repolarını listele.
8. **Apprentissage** → DGEFP kaydı "Apprentissage = false"; OF olarak çıraklık eğitimi vermek ile çırak istihdam etmek ayrımını netleştir.

---

## 8. İzleme / Sonraki Doğrulama Önerileri

| # | Doğrulama | Kaynak |
|---|---|---|
| 1 | 2023–2025 NETZ ciro/bilan — INPI/RNE/Kbis | [Registre national des entreprises](https://registre.entreprises.gouv.fr) |
| 2 | QualiRépar "no 1056" — resmi annuaire/certificate id | [Label QualiRépar](https://www.label-qualirepar.fr/annuaires/) |
| 3 | Reflektif Bilişim A.Ş. — TR Ticaret Sicili Gazetesi/MERSİS | [MERSİS](https://mersis.ticaret.gov.tr) |
| 4 | CortexAI (UK) — Companies House kaydı | https://find-and-update.company-information.service.gov.uk |
| 5 | `lekesiz/reflektif` — private/renamed mı? owner hesabından | [GitHub repos API](https://api.github.com/users/lekesiz/repos) |
| 6 | LP DWCA 2025/2026 — üniversite kaydı/öğrenci belgesi | [Université de Strasbourg](https://www.unistra.fr) |

---

## 9. Kaynak Katmanları ve Sınırlar

- **Web kaynakları:** Resmi Fransız şirket/eğitim API'leri (recherche-entreprises, DGEFP, Caisse des Dépôts/MCF), GitHub API, Wikidata API, AFNOR/ecosystem, France Compétences, OPCO ATLAS, l'Opcommerce, Centre Inffo — tümü erişilebilir ve URL'li.
- **Drive kaynakları:** Kullanıcının kendi belgeleri (`REFLEKTIF-BILGI-TABANI.md`, `Reflektif_Fizibilite_Raporu.md`, EDOF export'ları, Reflektif sunum/rapor PDF'leri). Bunlar birinci el ama self-source'dur — resmi sicil doğrulaması gerektiren iddialar [Drive-Tek] olarak işaretlendi.
- **Gmail:** Bu oturumda Gmail arama connector'ı token propagasyon hatası nedeniyle erişilemedi; e-posta kaynaklı doğrulama yapılamadı (Drive ve web bunu büyük ölçüde telafi etti).
- **Hassas veri:** Doğum tarihi, kişisel e-posta, IBAN, API anahtarları, sunucu IP'leri \*\*\*MASKED\*\*\* tutulmuştur.

---

*Üretim: Perplexity Computer — Derin Araştırma, 25 Haziran 2026. Bu doküman, kullanıcının (Mikail Lekesiz) nihai kontrolünden geçmeden resmi kayıt olarak kullanılmamalıdır.*
