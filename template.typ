// ==============================================================================
// SOFTWARE ENGINEERING MAANG MASTERCLASS - TYPST TEMPLATE (v0.15+ COMPATIBLE)
// 500 Ders • 50 Bölüm • Çift Dilli (TR & EN) • Java 25 & Spring Boot
// ==============================================================================

#let setup_book(title: "", author: "Antigravity & MAANG Software Engineering Guild", body) = {
  set document(title: title, author: author)
  set text(font: ("Avenir Next", "Helvetica Neue", "Arial"), size: 9pt, lang: "tr")
  set page(
    paper: "a4",
    margin: (x: 1.8cm, top: 2.2cm, bottom: 2.2cm),
    header: context {
      let cur_page = counter(page).get().first()
      if cur_page > 2 [
        #text(size: 8pt, fill: rgb("64748b"))[
          #grid(
            columns: (1fr, 1fr),
            [MAANG Software Engineering • 500 Lessons Masterclass],
            [#align(right)[Aptala Anlatır Gibi Yazılım Mühendisliği]]
          )
        ]
        #v(-2pt)
        #line(length: 100%, stroke: 0.5pt + rgb("e2e8f0"))
      ]
    },
    footer: context {
      let cur_page = counter(page).get().first()
      if cur_page > 2 [
        #line(length: 100%, stroke: 0.5pt + rgb("e2e8f0"))
        #v(2pt)
        #text(size: 8pt, fill: rgb("64748b"))[
          #grid(
            columns: (1fr, 1fr),
            [Clean Code • Clean Arch • Java 25 & Spring Boot 3+ • Distributed Systems],
            [#align(right)[Sayfa / Page #counter(page).display()]]
          )
        ]
      ]
    }
  )
  set par(justify: true, leading: 0.58em)
  body
}

#let diagram_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("030712"), // Deep Midnight
    stroke: (left: 4.5pt + rgb("6366f1"), rest: 0.5pt + rgb("1e1b4b")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("818cf8"), size: 9.5pt)[⚡ Mimari Akış ve Süreç Şeması]],
        [#align(right)[#text(weight: "bold", fill: rgb("a5b4fc"), size: 9.5pt)[⚡ Process & Architecture Schematic]]]
      )
      #v(3pt)
      #body
    ]
  )
  v(4pt)
}

#let eli5_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("eff6ff"), // Soft Blue
    stroke: (left: 4.5pt + rgb("2563eb"), rest: 0.5pt + rgb("bfdbfe")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("1e40af"), size: 9.5pt)[💡 Aptala Anlatım (ELI5 Metaforu)]],
        [#align(right)[#text(weight: "bold", fill: rgb("1d4ed8"), size: 9.5pt)[💡 ELI5 Real-Life Metaphor]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let deep_dive_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("f8fafc"), // Slate
    stroke: (left: 4.5pt + rgb("0d9488"), rest: 0.5pt + rgb("ccfbf1")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("115e59"), size: 9.5pt)[🔍 MAANG Seviyesi Teknik Derinlik]],
        [#align(right)[#text(weight: "bold", fill: rgb("0f766e"), size: 9.5pt)[🔍 MAANG Technical Deep-Dive]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let java25_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("faf5ff"), // Light Violet
    stroke: (left: 4.5pt + rgb("9333ea"), rest: 0.5pt + rgb("e9d5ff")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("6b21a8"), size: 9.5pt)[☕ Modern Java 25 & Spring Boot Uygulaması]],
        [#align(right)[#text(weight: "bold", fill: rgb("7e22ce"), size: 9.5pt)[☕ Java 25 & Spring Boot Implementation]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let warning_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("fff1f2"), // Rose
    stroke: (left: 4.5pt + rgb("e11d48"), rest: 0.5pt + rgb("fecdd3")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("9f1239"), size: 9.5pt)[⚠️ Mülakat Tuzağı ve Mimari Anti-Pattern]],
        [#align(right)[#text(weight: "bold", fill: rgb("be123c"), size: 9.5pt)[⚠️ Interview Trap & Anti-Pattern]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let takeaways_box(takeaways) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("f0fdf4"), // Emerald
    stroke: (left: 4.5pt + rgb("16a34a"), rest: 0.5pt + rgb("bbf7d0")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("15803d"), size: 9.5pt)[🎯 Mülakatta Hatırlanacak Altın Kurallar]],
        [#align(right)[#text(weight: "bold", fill: rgb("166534"), size: 9.5pt)[🎯 Key Architectural Takeaways]]]
      )
      #v(4pt)
      #for item in takeaways [
        #grid(
          columns: (1fr, 1fr),
          gutter: 10pt,
          [#text(size: 8pt)[• #item.at(0)]],
          [#text(size: 8pt, fill: rgb("475569"))[• #item.at(1)]]
        )
        #v(2pt)
      ]
    ]
  )
  v(4pt)
}

#let lesson_header(lesson_num, title_tr, title_en, module_name_tr, module_name_en) = {
  v(3pt)
  rect(
    width: 100%,
    fill: rgb("0f172a"), // Slate 900
    radius: 7pt,
    inset: (x: 12pt, y: 10pt),
    [
      #grid(
        columns: (auto, 1fr),
        gutter: 12pt,
        [
          #circle(radius: 17pt, fill: rgb("4f46e5"))[
            #align(center + horizon)[#text(weight: "bold", fill: white, size: 11pt)[#lesson_num]]
          ]
        ],
        [
          #text(size: 7.5pt, fill: rgb("818cf8"), weight: "bold")[
            BÖLÜM: #upper(module_name_tr)  |  MODULE: #upper(module_name_en)
          ]
          #v(2pt)
          #text(size: 12pt, fill: white, weight: "bold")[#title_tr]
          #v(2pt)
          #text(size: 10pt, fill: rgb("38bdf8"), weight: "medium")[#title_en]
        ]
      )
    ]
  )
  v(5pt)
}

#let module_cover(module_num, title_tr, title_en, desc_tr, desc_en) = {
  pagebreak()
  v(20pt)
  align(center)[
    #rect(
      width: 100%,
      fill: rgb("020617"),
      radius: 10pt,
      inset: (x: 20pt, y: 24pt),
      [
        #text(size: 12pt, fill: rgb("818cf8"), weight: "bold")[BÖLÜM #module_num / MODULE #module_num]
        #v(6pt)
        #text(size: 18pt, fill: white, weight: "bold")[#title_tr]
        #v(4pt)
        #text(size: 14pt, fill: rgb("94a3b8"), weight: "medium")[#title_en]
        #v(12pt)
        #line(length: 60%, stroke: 1.5pt + rgb("4f46e5"))
        #v(12pt)
        #grid(
          columns: (1fr, 1fr),
          gutter: 16pt,
          [
            #align(left)[
              #text(size: 9pt, fill: rgb("cbd5e1"))[#desc_tr]
            ]
          ],
          [
            #align(left)[
              #text(size: 9pt, fill: rgb("94a3b8"))[#desc_en]
            ]
          ]
        )
      ]
    )
  ]
  v(16pt)
}

#let book_front_cover() = {
  set page(header: none, footer: none, margin: 0pt)
  rect(
    width: 100%,
    height: 100%,
    fill: rgb("030712"), // Midnight Indigo Obsidian
    inset: (x: 3.2cm, y: 3.2cm),
    [
      #v(20pt)
      #rect(fill: rgb("1e1b4b"), radius: 4pt, inset: (x: 10pt, y: 6pt))[
        #text(size: 9.5pt, fill: rgb("c7d2fe"), weight: "bold")[MAANG SOFTWARE ENGINEERING MASTERCLASS • BILINGUAL EDITION]
      ]
      #v(16pt)
      #text(size: 32pt, fill: white, weight: "bold")[
        Aptala Anlatır Gibi\ Yazılım Mühendisliği
      ]
      #v(8pt)
      #text(size: 18pt, fill: rgb("818cf8"), weight: "medium")[
        Software Engineering for MAANG Interviews: 500 Lessons & 50 Modules
      ]
      #v(12pt)
      #text(size: 11pt, fill: rgb("94a3b8"))[
        50 Bölüm • 500 Ders • Mimari ASCII Şemaları • Modern Java 25 LTS & Spring Boot 3+ • Çift Dilli (TR & EN)
      ]
      #v(24pt)
      #line(length: 100%, stroke: 2pt + rgb("4f46e5"))
      #v(24pt)
      #grid(
        columns: (1fr, 1fr, 1fr),
        gutter: 12pt,
        [
          #rect(fill: rgb("0f172a"), radius: 6pt, inset: 10pt, width: 100%)[
            #text(weight: "bold", fill: white, size: 9.5pt)[🏛️ Clean Architecture & DDD]\
            #v(2pt)
            #text(size: 8pt, fill: rgb("94a3b8"))[SOLID, Tasarım Kalıpları, Bounded Contexts, Hexagonal Ports & Adapters]
          ]
        ],
        [
          #rect(fill: rgb("0f172a"), radius: 6pt, inset: 10pt, width: 100%)[
            #text(weight: "bold", fill: white, size: 9.5pt)[☕ Java 25 & Spring Boot 3]\
            #v(2pt)
            #text(size: 8pt, fill: rgb("94a3b8"))[Virtual Threads, Pattern Matching, Spring Data JPA, Security, Cloud Native]
          ]
        ],
        [
          #rect(fill: rgb("0f172a"), radius: 6pt, inset: 10pt, width: 100%)[
            #text(weight: "bold", fill: white, size: 9.5pt)[🌐 Dağıtık Sistemler & MAANG]\
            #v(2pt)
            #text(size: 8pt, fill: rgb("94a3b8"))[Kafka, Sharding, Saga Pattern, Observability, Staff+ Sistem Tasarımı]
          ]
        ]
      )
      #v(40pt)
      #align(bottom)[
        #text(size: 9pt, fill: rgb("64748b"))[
          Yayın Sürümü: 1.0.0 • 500 Derslik Mega Müfredat • 2026
        ]
      ]
    ]
  )
}
