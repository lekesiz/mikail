# Çok Dilli İçerik — Yerel İnceleme Checklist

> Bu dosya, AI yardımıyla çevrilen içeriklerin anadili konuşanlar tarafından gözden geçirilmesi için bir rehberdir.

---

## İnceleme Durumu

| Dil | Dosyalar | Durum | İnceleyen | Notlar |
|---|---|---|---|---|
| 🇨🇳 Mandarin Çincesi | `BIO-zh` · `AI-MEMORY-zh` | ⏳ Bekliyor | — | — |
| 🇮🇳 Hintçe | `BIO-hi` · `AI-MEMORY-hi` | ⏳ Bekliyor | — | — |
| 🇸🇦 Arapça | `BIO-ar` · `AI-MEMORY-ar` | ⏳ Bekliyor | — | — |
| 🇧🇩 Bengalce | `BIO-bn` · `AI-MEMORY-bn` | ⏳ Bekliyor | — | — |
| 🇷🇺 Rusça | `BIO-ru` · `AI-MEMORY-ru` | ⏳ Bekliyor | — | — |
| 🇵🇰 Urduca | `BIO-ur` · `AI-MEMORY-ur` | ⏳ Bekliyor | — | — |

**Yüksek güvenli diller** (İngilizce, Fransızca, Türkçe) ve **yüksek-orta güvenli diller** (İspanyolca, Portekizce) bu listede yok; bunlar ön incelemeden geçirilmiş kabul edilir.

---

## İnceleyene Talimatlar

Her dosya için aşağıdaki kontrolleri yap:

### 1. Doğruluk (Accuracy)
- [ ] Şirket isimleri doğru yazılmış mı?
  - Netz Informatique
  - Reflektif Bilişim A.Ş.
  - CORTEX AI LTD
- [ ] Sayısal veriler doğru mu?
  - SIREN: 818 347 346
  - Companies House no: 16176249
  - Reflektif sermaye: 1.000.000 TL
  - Reflektif kullanıcı sayısı: 1000+
  - TUSAŞ çağrı kodu: USI-J0650-0213-35
- [ ] Psikometrik yüzdeler doğru aktarılmış mı?
  - RIASEC: Araştırmacı 96%, Sanatsal 92%, Girişimci 88%
  - Big Five: Açıklık 100%, Sorumluluk 100%

### 2. Doğal Akıcılık (Fluency)
- [ ] Cümleler o dilin doğal yapısına uygun mu?
- [ ] Teknik terimler o pazarda yaygın kullanılan karşılıklara sahip mi?
- [ ] Ticari/marka terimler (örneğin "bilan de compétence") doğru bırakılmış mı?

### 3. Kültürel Uyum (Cultural Fit)
- [ ] Dini/kültürel ifadeler (Kur'an, Osmanlı belgeleri vb.) o topluma uygun şekilde aktarılmış mı?
- [ ] Aile bilgileri korumacı ve saygılı bir dille ifade edilmiş mi?
- [ ] Coğrafi referanslar (Haguenau, Strasbourg, İstanbul, Tekirdağ) doğru telaffuz/edilme şekliyle yazılmış mı?

### 4. Format ve Bütünlük
- [ ] Markdown başlık yapısı bozulmamış mı?
- [ ] Tüm tablolar doğru hizalanmış mı?
- [ ] Bağlantılar çalışıyor mu?
- [ ] "Translation quality" notu güncellenmeli mi?

---

## İnceleme Sonrası Adımlar

1. İnceleme tamamlandıktan sonra düzeltmeleri doğrudan ilgili dosyaya uygula.
2. Bu tablodaki **Durum** sütununu "✅ Tamamlandı" olarak güncelle.
3. **İnceleyen** ve **Notlar** sütunlarını doldur.
4. Commit mesajı örneği:
   ```bash
   git add multilingual/
   git commit -m "Review Chinese (zh) bio and AI memory summary"
   git push origin main
   ```

---

## Hızlı Başvuru — Temel Kavramların Çevirileri

| Kavram | İngilizce | Fransızca | Türkçe |
|---|---|---|---|
| Visionary Systems Architect | Visionary Systems Architect | Architecte de Systèmes Visionnaire | Vizyoner Sistem Mimarı |
| Structured Revolutionary | Structured Revolutionary | Révolutionnaire Structuré | Yapılandırılmış Devrimci |
| Solo technical founder | Solo technical founder | Fondateur technique solo | Solo teknik kurucu |
| AI-augmented psychometrics | AI-augmented psychometrics | Psychométrie augmentée par l'IA | AI destekli psikometri |
| Career-discovery platform | Career-discovery platform | Plateforme d'orientation | Kariyer keşif platformu |

---

*Son güncelleme: 2026-06-25*
