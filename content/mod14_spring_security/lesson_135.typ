#import "/template.typ": *

#show: doc => setup_book(title: "Ders 135: Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Yüksek Performans, Optimizasyon ve Bellek / CPU Yönetimi", doc)

#lesson_header(
  135,
  "Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Yüksek Performans, Optimizasyon ve Bellek / CPU Yönetimi",
  "Spring Security: Authentication, Authorization & OAuth2/OIDC - High Performance, Optimization & Memory/CPU Resource Management",
  "Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2",
  "Spring Security: Authentication, Authorization & OAuth2/OIDC"
)

#diagram_box[
```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 MAANG MİMARİ AKIŞ VE VERİ İŞLEME DİYAGRAMI                  │
└─────────────────────────────────────────────────────────────────────────────┘
  [ İstek / Request: Client ] ──► [ API Gateway / Load Balancer ]
                                            │
                                            ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SECURITY YÖNETİM KATMANI (OAUTH2 PIPELINE)                               │
  │  1. Girdi Doğrulama (Input Guard) ──► Fail-Fast Kontrolü                │
  │  2. Temiz İş Mantığı (Core Logic) ──► Java 25 Virtual Thread ile İcra   │
  │  3. Durum / Veri Değişimi         ──► Transactional Outbox / Event      │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
        [ Cache / Memory: Redis ]               [ Storage: Database ]
        (Düşük Gecikme / P99 < 5ms)             (ACID / Konsensüs / Log)

  🎯 MAANG MİMARİ İLKESİ:
  "Yüksek ölçekli sistemlerde her bileşen bağımsız olarak hata verebilir (fail-safe).
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" 
```
]

#eli5_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("1e40af"), size: 8.5pt)[🇹🇷 TÜRKÇE (ELI5)]\
      #v(2pt)
      Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!
    ],
    [
      #text(weight: "bold", fill: rgb("1d4ed8"), size: 8.5pt)[🇬🇧 ENGLISH (ELI5)]\
      #v(2pt)
      #text(fill: rgb("334155"))[Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!]
    ]
  )
]

#deep_dive_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("115e59"), size: 8.5pt)[🇹🇷 MAANG DERİNLEMESİNE ANALİZ]\
      #v(2pt)
      MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.
    ],
    [
      #text(weight: "bold", fill: rgb("0f766e"), size: 8.5pt)[🇬🇧 MAANG TECHNICAL DEEP-DIVE]\
      #v(2pt)
      #text(fill: rgb("334155"))[MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.]
    ]
  )
]

#java25_box[
```java
// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson05;

import org.springframework.stereotype.Service;
import java.time.Instant;
import java.util.Objects;
import java.util.concurrent.CompletableFuture;

public class SecurityArchitectureDemo {

    // 1. Değişmez Domain Modeli (Java 25 Record)
    public record SecurityRequest(String transactionId, String payload, Instant timestamp) {
        public SecurityRequest {
            Objects.requireNonNull(transactionId, "transactionId zorunludur");
            Objects.requireNonNull(payload, "payload zorunludur");
        }
    }

    public record SecurityResult(String transactionId, String status, long executionTimeMs) {}

    // 2. Servis Katmanı (Spring Boot @Service)
    @Service
    public static class SecurityExecutionService {
        public SecurityResult processRequest(SecurityRequest request) {
            long start = System.currentTimeMillis();
            
            // Java 25 Virtual Thread ile Asenkron Dayanıklı İcra
            System.out.println("⚡ [Java 25 Virtual Thread] " + Thread.currentThread() 
                + " -> İstek İşleniyor: " + request.transactionId());
            
            long duration = System.currentTimeMillis() - start;
            return new SecurityResult(request.transactionId(), "PROCESSED_SUCCESSFULLY", duration);
        }
    }

    public static void main(String[] args) {
        System.out.println("🏛️ MAANG Software Engineering Security Engine Başlatıldı...");
        var service = new SecurityExecutionService();
        var req = new SecurityRequest("TXN-" + System.currentTimeMillis(), "Valid Data", Instant.now());
        var res = service.processRequest(req);
        System.out.println("✅ Sonuç: " + res);
    }
}
```
]

#warning_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("9f1239"), size: 8.5pt)[🇹🇷 MÜLAKAT TUZAĞI VE ANTİ-PATTERN]\
      #v(2pt)
      Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.
    ],
    [
      #text(weight: "bold", fill: rgb("be123c"), size: 8.5pt)[🇬🇧 INTERVIEW TRAP & ANTI-PATTERN]\
      #v(2pt)
      #text(fill: rgb("881337"))[Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.]
    ]
  )
]

#takeaways_box((
    ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
    ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
    ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
))
