#!/usr/bin/env python3
"""
Scrape mikail.net blog listing pages and emit a Markdown inventory.
No external dependencies beyond Python stdlib.
"""
import re
import html
import urllib.request
import urllib.error
from pathlib import Path

BASE = "https://mikail.net/blog/page/{page}/"
OUT = Path(__file__).parent.parent / "external-sources" / "mikail.net-blog-inventory.md"


def fetch(page: int) -> str:
    url = BASE.format(page=page)
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return ""
        raise


def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return text.strip()


def parse_listing(html_text: str):
    posts = []
    # Each post is a <li class="wp-block-post ..."> ... </li>
    for block in re.findall(r'<li class="wp-block-post[^"]*"[^>]*>(.*?)</li>', html_text, re.S | re.I):
        title_match = re.search(r'<h\d[^>]*class="wp-block-post-title[^"]*"[^>]*>.*?<a[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>.*?</h\d>', block, re.S | re.I)
        if not title_match:
            continue
        link, title = title_match.groups()
        title = clean(title)
        date = None
        dt_match = re.search(r'<time[^>]*datetime=["\'](\d{4}-\d{2}-\d{2})', block)
        if dt_match:
            date = dt_match.group(1)
        posts.append({"title": title, "link": link, "date": date})
    return posts


def main():
    all_posts = []
    for page in range(1, 40):
        html = fetch(page)
        if not html:
            break
        posts = parse_listing(html)
        if not posts:
            break
        all_posts.extend(posts)

    # Deduplicate by link
    seen = set()
    unique = []
    for p in all_posts:
        if p["link"] in seen:
            continue
        seen.add(p["link"])
        unique.append(p)

    # Group by year-month
    grouped = {}
    for p in unique:
        ym = p["date"][:7] if p["date"] else "Tarihsiz"
        grouped.setdefault(ym, []).append(p)

    dates = [p["date"] for p in unique if p["date"]]

    lines = [
        "# mikail.net Blog Yazıları Envanteri",
        "",
        "> **Kaynak:** https://mikail.net/blog/ ve sayfalama sayfaları  ",
        "> **Tarama tarihi:** 2026-06-25  ",
        "> **Amaç:** Blog içeriğinin temalarını, yoğunluklarını ve zaman çizelgesini görünür kılmak.  ",
        "",
        "---",
        "",
        "## Özet İstatistikler",
        "",
        f"| Metrik | Değer |",
        "|---|---|",
        f"| Toplam yazı | {len(unique)} |",
        f"| İlk yazı | {min(dates) if dates else '—'} |",
        f"| Son yazı | {max(dates) if dates else '—'} |",
        "",
        "---",
        "",
        "## Ana Temalar",
        "",
        "| Tema | Açıklama |",
        "|---|---|",
        "| **360° Hakikat / Karar Motoru** | V4.x–V8.0 arası sürümler; epistemoloji, ontoloji, abduktif/dedüktif sentez, karar verme çerçeveleri |",
        "| **Reflektif & Kariyer** | Psikometri, fıtrat/istidat/şâkile, kariyer seçimi, eğitim sistemi, yetkinlik değerlendirme |",
        "| **AI & Teknoloji** | LLM'ler, otonom ajanlar (Auto-GPT, BabyAGI, CrewAI, AutoGen, LangChain), sesli asistanlar, Claude Code, MLOps |",
        "| **Felsefe & İnsan** | Heidegger, Sokrates, Kant, İbn Arabî, Gazali, Farabi, İslam tasavvufu, ahlak, özgürlük, modernite eleştirisi |",
        "| **Sistem & Toplum** | Pangea-Agoras, küresel krizler, eğitim politikaları, AB fonları, Türkiye'de yetkinlik değerlendirme |",
        "| **Teknik Rehber** | Laravel Nova, Puppeteer, web scraping, Python, n8n, veri aktarımı, siber güvenlik araçları |",
        "",
        "---",
        "",
        "## Kronolojik Envanter",
        "",
    ]

    for ym in sorted(grouped.keys(), reverse=True):
        if ym == "Tarihsiz":
            lines.append("### Tarihsiz")
        else:
            lines.append(f"### {ym}")
        lines.append("")
        for p in sorted(grouped[ym], key=lambda x: x["date"] or "", reverse=True):
            date_part = f" ({p['date']})" if p["date"] else ""
            lines.append(f"- [{p['title']}]({p['link']}){date_part}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Çapraz Doğrulama Notları",
        "",
        "- Blog, teknik içerikleri felsefi/insani bir çerçeveye oturtan uzun form yazılar barındırır.",
        "- '360 Derece Hakikat Araştırma ve Karar Motoru' serisi en yoğun tekrar eden çerçevedir.",
        "- Reflektif.net ile ilgili yazılar, platformun sadece bir ürün değil, aynı zamanda bir dünya görüşü olduğunu gösterir.",
        "",
        "*Çıkarım: Kimi Code CLI · 2026-06-25 · Tüm bağlantılar https://mikail.net adresinden kamuya açık olarak alınmıştır.*",
        "",
    ])

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(unique)} posts to {OUT}")


if __name__ == "__main__":
    main()
