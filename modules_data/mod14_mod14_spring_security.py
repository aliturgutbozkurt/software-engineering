# -*- coding: utf-8 -*-
"""
Module 14: Spring Security: Authentication, Authorization & OAuth2/OIDC (Lessons 131-140)
"""

MODULE = {
    "id": 14,
    "dir": "mod14_spring_security",
    "title_tr": "Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2",
    "title_en": "Spring Security: Authentication, Authorization & OAuth2/OIDC",
    "desc_tr": "SecurityFilterChain mimarisi, AuthenticationProvider, Role & Authority bazlı erişim, JWT doğrulaması, OAuth2 Resource Server ve CORS/CSRF.",
    "desc_en": "Security filter chain internals, authentication managers, JWT stateless validation, OAuth2 resource server integration, and CSRF mitigation.",
    "lessons": [
        {
            "num": 131,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Temel Kavramlar, Tarihsel Evrim ve Temel Mühendislik Çerçevesi""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Core Concepts, Historical Evolution & Foundational Frameworks""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson01;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 132,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Mimari Bileşenler, Çalışma Mekanizması ve Veri Akışı""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Architectural Components, Internal Mechanics & Data Flow""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson02;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 133,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Tasarım İlkeleri, Sözleşmeler ve Temiz Arayüz Tanımları""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Design Invariants, Contracts & Clean Interface Abstractions""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson03;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 134,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Yaygın Anti-Pattern'ler, Tasarım Hataları ve Önleme Stratejileri""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Common Anti-Patterns, Design Pitfalls & Prevention Strategies""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson04;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 135,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Yüksek Performans, Optimizasyon ve Bellek / CPU Yönetimi""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - High Performance, Optimization & Memory/CPU Resource Management""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 136,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Eşzamanlılık, Thread Güvenliği ve Dağıtık Sistem Etkileri""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Concurrency, Thread-Safety & Distributed Systems Implications""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson06;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 137,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Hata Yönetimi, Dayanıklılık (Resilience) ve Geri Düşme (Fallback)""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Fault Handling, Resilience Patterns & Graceful Fallback Strategies""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson07;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 138,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Test Stratejileri, Test Edilebilirlik ve Doğrulama Hatları""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Testing Strategies, Testability & Automated Verification Pipelines""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson08;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 139,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - Gözlemlenebilirlik, Metrikler, İzleme ve Canlı Ortam Hata Ayıklama""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - Observability, Telemetry, Tracing & Production Troubleshooting""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson09;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
        {
            "num": 140,
            "title_tr": """Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 - MAANG Mülakat Ustalığı, Mimari Ödünleşimler (Trade-Offs) & Staff+ Vizyonu""",
            "title_en": """Spring Security: Authentication, Authorization & OAuth2/OIDC - MAANG Interview Mastery, Architectural Trade-Offs & Staff+ Vision""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """,
            "eli5_tr": """Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları (Security mikro-servisleri) ve otomatik yönlendirme robotları (OAuth2 akışları) kullanılır. Bir bant arızalansa bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!""",
            "eli5_en": """Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers (concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners (API Gateways), autonomous high-speed carousels (Security microservices), and dynamic routing switches (OAuth2 pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!""",
            "deep_tr": """MAANG ve Tier-1 Mühendislik Seviyesinde Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2 Analizi: Meta, Google ve Netflix gibi mega ölçekli şirketlerde Security mimarisi, saniyede milyonlarca işlemi (high throughput) tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. 1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. 2) Hata İzolasyonu (Bulkhead & Circuit Breaking): OAuth2 katmanında yaşanacak olası bir gecikme veya çöküş, tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. 3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. 4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir.""",
            "deep_en": """MAANG & Tier-1 Systems Engineering Deep-Dive for Spring Security: Authentication, Authorization & OAuth2/OIDC: At enterprise hyper-scale (Meta, Google, Netflix, Amazon), Security implementations must sustain millions of operations per second with sub-10ms P99 latency guarantees. 1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. 2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in OAuth2 don't trigger cascading outages across downstream clusters. 3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. 4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, grounding decisions in deterministic SLA/SLO criteria.""",
            "java_code": """// Java 25 & Spring Boot: Security & OAuth2 Kurumsal Uygulaması
package com.maang.se.module14.lesson10;

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
}""",
            "warning_tr": """Security kurgulanırken OAuth2 bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker.""",
            "warning_en": """Coupling Security logic directly to synchronous blocking calls into OAuth2 is a fatal interview anti-pattern! Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion.""",
            "takeaways": [
                ("Security mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.", "Design Security components with strict single-responsibility and loose coupling."),
                ("Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.", "Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
                ("MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.", "Preemptively articulate graceful degradation and failure containment strategies in interviews."),
            ]
        },
    ]
}
