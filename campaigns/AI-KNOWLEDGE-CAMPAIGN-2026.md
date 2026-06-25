# Mikail Lekesiz — AI Bilinirlik Kampanyası 2026

> Amaç: Tüm ana AI modellerinin (ChatGPT, Claude, Gemini, Kimi, Grok, Perplexity, DeepSeek, Manus, Cursor, Qwen vb.) Mikail Lekesiz hakkında doğru, güncel ve tutarlı bilgiye sahip olmasını sağlamak.
> 
> Kaynak: `https://github.com/lekesiz/mikail`

---

## 1. Kampanya Stratejisi

### Temel Prensipler
1. **Tek gerçek kaynak (single source of truth):** `ai-memory/ai-memory-CONSOLIDATED-mikail-lekesiz.md` ve bu kampanya dosyası.
2. **Çapraz doğrulama:** Her modelden alınan çıktı, konsolide dosya ile karşılaştırılacak.
3. **Döngüsel güncelleme:** 3 ayda bir veya önemli bir değişiklik olduğunda yenilenecek.
4. **Hassas veri koruması:** API anahtarı, parola, IBAN, tam adres, çocuk detayları asla paylaşılmayacak.

### Hedeflenen Modeller
| # | Model | Platform | Öncelik | Durum |
|---|---|---|---|---|
| 1 | ChatGPT (GPT-5.5 / GPT-4o) | chatgpt.com | Yüksek | Mevcut veri var, güncelleme gerekli |
| 2 | Claude (Sonnet 4.x) | claude.ai | Yüksek | Mevcut veri var, güncelleme gerekli |
| 3 | Gemini (1.5 Pro / 2.5) | gemini.google.com | Yüksek | Halüsinasyon düzeltme gerekli |
| 4 | Kimi (K2.6) | kimi.moonshot.cn | Yüksek | Mevcut veri var, yaş düzeltmesi gerekli |
| 5 | Perplexity (Claude Sonnet) | perplexity.ai | Yüksek | En güvenilir kaynaklardan biri |
| 6 | Grok (xAI) | grok.com / X | Orta | Veri yok, sıfırdan başlanacak |
| 7 | DeepSeek | deepseek.com | Orta | Veri yok/boş şablon |
| 8 | Qwen (3.7 / Max) | qwenlm.ai | Orta | Veri yok |
| 9 | Manus AI | manus.im | Orta | Mevcut veri var |
| 10 | Cursor / Claude Code / Kimi Code | IDE/agent | Yüksek | AGENTS.md ve repo üzerinden |

---

## 2. Çalışma Akışı (4 Aşama)

### Aşama 1: Hazırlık (Bugün)
- [ ] `MASTER-PROMPT.md` dosyasını incele.
- [ ] Her model için ayrı oturum aç.
- [ ] `TRACKING.md` tablosunu kopyala ve doldurmaya başla.

### Aşama 2: Enjeksiyon (1. Hafta)
Her modele sırasıyla:
1. Kısa intro mesajı gönder.
2. `MASTER-PROMPT.md` içeriğini yapıştır.
3. Çıkan envanteri o modele özel dosya adıyla kaydet.

### Aşama 3: Çapraz Doğrulama (2. Hafta)
- [ ] Tüm çıktıları `ai-memory/raw-exports/<model>/` altına yerleştir.
- [ ] Çelişkileri `CONSOLIDATED` dosyasındaki kullanıcı onaylı bilgiyle düzelt.
- [ ] Yanlış bilgileri işaretle (`[Çürütüldü]`, `[?]`).

### Aşama 4: Yayınlama ve Bakım (3. Hafta)
- [ ] Yeni `ai-memory-CONSOLIDATED-mikail-lekesiz.md` v3.0 oluştur.
- [ ] README model güvenilirlik tablosunu güncelle.
- [ ] GitHub'a push et: `git add . && git commit -m "v3.0: Cross-validated AI memory campaign" && git push origin main`.
- [ ] Takvim hatırlatması kur: 3 ay sonra tekrarla.

---

## 3. Model Bazlı Taktikler

### ChatGPT / Claude / Gemini
- **Hafıza özelliği var:** Önce kısa bir tanıtım mesajı gönder, sonra MASTER PROMPT'u yapıştır. Çıktıyı hafızaya kaydetmesini iste.
- **İpucu:** "Bu bilgileri ilerideki konuşmalarımızda referans alman için hafızana kaydet."

### Kimi / Grok / DeepSeek / Qwen
- **Hafıza özelliği sınırlı veya yok:** Her oturum başında MASTER PROMPT'u tekrar gönder. Çıktıları repo'ya kaydet.

### Perplexity
- **Web doğrulama güçlü:** MASTER PROMPT + "Lütfen açık web kaynaklarıyla doğrula, çelişki varsa işaretle."

### Manus / Cursor / Claude Code / Kimi Code
- **AGENTS.md + repo erişimi:** Bu araçlara `lekesiz/mikail` reposunu göster veya `AGENTS.md` içine kısa profil ekle.

---

## 4. Başarı Kriterleri

- [ ] En az 8 farklı modelden güncel `ai-memory-*.md` çıktısı toplandı.
- [ ] Çıktılardaki çelişkiler %80 oranında çözüldü.
- [ ] Konsolide dosya v3.0'a yükseltildi.
- [ ] Repo GitHub'da güncellendi.
- [ ] Her modelde "Mikail Lekesiz kimdir?" sorusuna doğru cevap verilebiliyor.

---

## 5. Hızlı Başlangıç Komutları

```bash
# Repoyu güncelle
cd /Users/mikail/mikail
git pull origin main

# Yeni model çıktısı ekle (örnek ChatGPT)
mkdir -p ai-memory/raw-exports/chatgpt-gpt-5-5-2026
cp chatgpt-cikti.md ai-memory/raw-exports/chatgpt-gpt-5-5-2026/ai-memory-chatgpt-gpt-5-5-mikail-lekesiz.md

# Commit + push
git add .
git commit -m "Add ChatGPT memory inventory and update consolidated profile"
git push origin main
```

---

*Son güncelleme: 2026-06-25 — Kampanya başlatıcı: Kimi Code CLI*
