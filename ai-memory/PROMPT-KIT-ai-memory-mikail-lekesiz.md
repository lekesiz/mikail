# AI Hafıza Envanteri — Optimize Edilmiş Prompt Seti
### Mikail Lekesiz için Taşınabilir Çalışma Paketi

İki bölüm: **BÖLÜM A** orijinal görevi 10 aşamalı optimize ana prompt'a dönüştürür; **BÖLÜM B** farklı AI modellerinden bilgi toplamak için 10 bağımsız profesyonel prompt verir.

> Kullanım: Önce BÖLÜM B'deki 10 prompt ile her AI modelinden çıktı topla → bunları bana getir → ben çapraz doğrulayıp tek master envanterde birleştiririm.

---

## BÖLÜM A — Optimize Edilmiş Ana Prompt (10 Aşamalı)

`[MODEL_ADI]` kısmını kullandığın modelle değiştir.

ROL: Mikail Lekesiz hakkında eriştiğin tüm hafıza/konuşma/dosya/bağlamı analiz eden titiz bir veri analistisin.

AŞAMA 1 — KAPSAM DENETİMİ: Neye gerçekten erişiyorsun? Hangi bilgi doğrudan verildi, hangisi çıkarım? Sadece gerçekten eriştiğini kullan.

AŞAMA 2 — KESİN KURALLAR: (1) Uydurma yok. (2) Emin olmadığını işaretle. (3) Diğer AI'ların bildiğini tahmin etme. (4) Her bilgiye güven seviyesi (Yüksek/Orta/Düşük). (5) Hassas veriyi maskele (API/parola/IBAN/kimlik/adres/IP). (6) Kimlik-şirket-proje karıştırma.

AŞAMA 3 — METADATA + KİMLİK ÖZETİ: Metadata tablosu + 5-10 cümle kimlik özeti + güven seviyesi.

AŞAMA 4 — KİŞİSEL + PROFESYONEL PROFİL: Tablolarla; her satıra güven.

AŞAMA 5 — ŞİRKETLER: Her şirket için ayrı tablo (Ülke/Şehir/Rol/Faaliyet/Web/Projeler/Güven). Kontrol: Netz Informatique, İngiltere AI şirketi, Formation Haguenau, Netz Blog, Informatique Haguenau, Service Apple, Recup Donnee, Aide Informatique AI.

AŞAMA 6 — PROJELER + ALTYAPI: Her proje (Tür/Amaç/Teknoloji/Durum/Rol/Risk/Sonraki Adım/Güven). Sonra teknik altyapı tablosu (hassas maskeli).

AŞAMA 7 — EĞİTİM + HUKUKİ/FİNANSAL: Eğitim/sertifika tablosu; hukuki (SFR vb.) ve finansal konular özet; gayrimenkul maskeli.

AŞAMA 8 — AİLE + İÇERİK + HEDEFLER: Aile (korumacı), içerik/yayın projeleri, stratejik hedefler tablosu.

AŞAMA 9 — ÇALIŞMA TARZI + DOMAINLER + TEKNOLOJİ + RİSKLER: Tercih analizi, domain tablosu, teknoloji tablosu, belirsizlik tablosu.

AŞAMA 10 — KATEGORİK ÖZET + PORTRE + SINIRLAR + SONUÇ: Özet tablosu, 300-600 kelime analitik portre, hafıza sınırları notu, sonuç.

ÇIKTI: Profesyonel Markdown, 20 bölümlük şablon. Dosya adı: ai-memory-[MODEL_ADI]-mikail-lekesiz.md. GitHub erişimin varsa github.com/lekesiz/mikail reposunda ai-memory/ klasörüne commit et: "Add AI memory inventory from [MODEL_ADI]". Erişimin yoksa tam içeriği ver.

SON KONTROL: Halüsinasyon yok mu? Hassas veri maskeli mi? Belirsizler işaretli mi? Güven seviyeleri var mı? Model adı + tarih var mı?

---

## BÖLÜM B — 10 Bağımsız Veri Çıkarma Prompt'u

Her prompt'un başına ekle: "Sadece gerçekten eriştiğin bilgileri kullan. Uydurma. Emin olmadığını işaretle. Her maddeye Güven Seviyesi (Yüksek/Orta/Düşük) ekle. Hassas veriyi maskele."

### Prompt 1 — Kişisel & Kimlik
Mikail Lekesiz hakkında KİŞİSEL bilgileri çıkar: ad-soyad, şehir/ülke(ler), diller, yaşam tarzı, ilgi alanları, uzun vadeli kişisel hedefler. Aileyi özet/korumacı yaz. Çıktı: tablo (Bilgi | Detay | Güven | Not).

### Prompt 2 — Profesyonel Profil
PROFESYONEL kimliği çıkar: ana meslek, bilişim/teknik servis geçmişi, yöneticilik/kurucu rolü, AI yaklaşımı, yazılım ilgisi, eğitim/danışmanlık, girişimcilik, risk/teknoloji takip tarzı. Çıktı: tablo (Alan | Detay | Güven).

### Prompt 3 — Şirketler
TÜM şirket/marka/organizasyonları listele (Ülke/Şehir/Rol/Faaliyet/Web/Projeler/Güven). Kontrol: Netz Informatique, İngiltere AI şirketi, Formation Haguenau, Netz Blog, Informatique Haguenau, Service Apple, Recup Donnee, Aide Informatique AI.

### Prompt 4 — Projeler (en kapsamlı)
TÜM projeleri detaylandır (Tür/Amaç/Teknoloji/Durum/Rol/Risk/Sonraki Adım/Güven). Ara: AI bilan de compétence, France Compétences/RS, Netz web yeniden tasarım, fatura.fr/Crater, sesle bilgisayar kontrol, Netz Asistan, AI ürün verisi çıkarma, fiyat karşılaştırma, Netz Blog otomasyon, Kur'an kitabı, Osmanlı belge çeviri, mikail.net, bilancompetence.ai, kod analiz ajanı, terminal CLI asistanı, reflektif.net, NavigAItor.

### Prompt 5 — Teknik Altyapı & Stack
Altyapı/cihaz/teknoloji tercihleri (bilgisayar/OS/sunucu/domain/framework/dil/AI araçları/veritabanı/hosting/Docker/Nginx). API anahtarı/parola/IP YAZMA. Çıktı: tablo (Kategori | Bilgi | Güven).

### Prompt 6 — Eğitim & Sertifika
Eğitim/sertifika/yetkinlik (üniversite, uzaktan eğitim, LP DWCA, sertifika, eğitmenlik, deneyim, AI/yazılım yetkinliği). Çıktı: tablo (Alan | Detay | Tarih | Güven). Tarih bilmiyorsan "belirsiz".

### Prompt 7 — Hukuki & Finansal
DİKKATLİ/ÖZET: Hukuki (SFR, sözleşme, dava/başvuru); Finansal (vergi, muhasebe, kredi, kira geliri, analiz); Gayrimenkul (özet). Banka/IBAN/adres/tutar maskeli. Her başlık: bilgi + hassasiyet + güven + doğrulanması gereken.

### Prompt 8 — Aile & İçerik/Yayın
(A) Aile/eğitim bağlamı (KORUMACI): Kur'an dersi, yaşa uygun içerik, Fransızca desteği, aktiviteler. (B) İçerik projeleri: Kur'an kitabı, İslami metin editörlüğü, Netz Blog otomasyon, SEO, bilan içerikleri, CGV/hukuki metin, Osmanlı belge. Her biri: amaç/dil/kitle/standart/durum/güven.

### Prompt 9 — Hedefler & Çalışma Tarzı
(A) Stratejik hedefler tablosu (Hedef | Açıklama | Zaman | Güven): Fransa büyüme, Türkiye yazılım, İngiltere açılım, AI eğitim ürünleri, bilan platformlaşma, SEO, AI ekosistemi, kişisel marka. (B) Çalışma tarzı: cevap formatı, dil, adım adım, teknik detay, proje yönetimi, karar alma, AI beklentisi, kısa/detay, ton.

### Prompt 10 — Domainler + Belirsizlikler + Kategorik Özet
(1) Domain/dijital varlık tablosu (Domain | Amaç | Proje | Durum | Güven). (2) Belirsizlikler tablosu (Konu | Neden | Doğrulama Bilgisi | Öncelik). (3) Kategorik özet tablosu (Kategori | Özet | Güven). Bilmediğini "Bilgi yok" işaretle.

---

## Geri Getirme Talimatı
1. Her AI modelinde BÖLÜM B'deki 10 prompt'u sor. 2. Çıktıları model adıyla etiketle. 3. Bana yapıştır. 4. Ben çapraz doğrulayıp master `ai-memory-...-mikail-lekesiz.md` üretip repoya yüklerim.
