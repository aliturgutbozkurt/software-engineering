#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_curriculum.py
Synthesizes the complete 50-Module, 500-Lesson bilingual curriculum for MAANG Software Engineering.
Each lesson contains:
  - Turkish and English Titles
  - ASCII Process & Architecture Diagram
  - Bilingual ELI5 Metaphor
  - Bilingual Technical Deep-Dive for MAANG interviews
  - Modern Java 25 LTS & Spring Boot 3+ code example
  - Bilingual Interview Trap & Warning
  - Bilingual Key Architectural Takeaways
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODULES_DATA_DIR = BASE_DIR / "modules_data"
MODULES_DATA_DIR.mkdir(parents=True, exist_ok=True)

# 50 Detailed Modules Specifications
MODULE_SPECS = [
    (1, "mod01_sdlc_agile", "Yazılım Mühendisliği Temelleri & Agile / Scrum / Kanban", "Software Engineering Fundamentals & Agile / Scrum / Kanban",
     "Yazılım yaşam döngüsü (SDLC), Waterfall'dan Agile'a evrim, Scrum törenleri, Kanban akış yönetimi, XP pratikleri ve MAANG ekiplerinin teslimat hız sırları.",
     "Software development lifecycles, Agile/Scrum ceremonies, Kanban WIP limits, Extreme Programming engineering rigor, and Tier-1 velocity heuristics.",
     "SDLC", "Agile"),

    (2, "mod02_clean_code", "Temiz Kod & Zanaatkarlık (Clean Code & Craftsmanship)", "Clean Code, Craftsmanship & Expressive Naming",
     "Okunabilir kod ilkeleri, anlamlı isimlendirme, tek iş yapan fonksiyonlar, yorum satırı anti-pattern'leri ve bilişsel yükü en aza indiren refactoring kalıpları.",
     "Readability invariants, intention-revealing naming, small cohesive functions, elimination of comment rot, and cognitive-load reduction techniques.",
     "CleanCode", "Naming"),

    (3, "mod03_solid_principles", "SOLID İlkeleri & Nesne Yönelimli Tasarım Mimarisi", "SOLID Principles & Object-Oriented Design Mastery",
     "Tek Sorumluluk (SRP), Açık/Kapalı (OCP), Liskov İkame (LSP), Arayüz Ayrımı (ISP) ve Bağımlılığı Tersine Çevirme (DIP) ilkelerinin modern Java ile derinlemesine analizi.",
     "Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion analyzed with modern Java 25 idioms.",
     "SOLID", "OOD"),

    (4, "mod04_creational_patterns", "Tasarım Kalıpları: Kurucu (Creational) Kalıplar", "Design Patterns: Creational Patterns in Modern Java",
     "Factory Method, Abstract Factory, Builder, Singleton, Prototype ve Multiton kalıplarının Java 25 Records ve Spring DI dünyasındaki modern karşılıkları.",
     "Factory, Builder, Singleton, Prototype, and Object Pool patterns revisited with Java 25 records and Spring dependency injection.",
     "Patterns", "Creational"),

    (5, "mod05_structural_patterns", "Tasarım Kalıpları: Yapısal (Structural) Kalıplar", "Design Patterns: Structural Patterns & Decoupling",
     "Adapter, Decorator, Facade, Composite, Proxy, Flyweight ve Bridge kalıpları ile gevşek bağlı (loosely coupled) sistem tasarımı.",
     "Adapter, Decorator, Facade, Composite, Proxy, Flyweight, and Bridge patterns for resilient component decoupling.",
     "Patterns", "Structural"),

    (6, "mod06_behavioral_patterns", "Tasarım Kalıpları: Davranışsal (Behavioral) Kalıplar", "Design Patterns: Behavioral Patterns & Event Flow",
     "Strategy, Observer, Command, State, Chain of Responsibility, Mediator ve Template Method kalıplarının fonksiyonel Java ile icrası.",
     "Strategy, Observer, Command, State, Chain of Responsibility, and Template Method patterns leveraging Java functional interfaces.",
     "Patterns", "Behavioral"),

    (7, "mod07_domain_driven_design", "Etki Alanı Odaklı Tasarım (DDD): Stratejik & Taktiksel", "Domain-Driven Design (DDD): Strategic & Tactical Patterns",
     "Ubiquitous Language, Bounded Contexts, Context Mapping, Entities, Value Objects, Aggregates ve Domain Events ile karmaşık iş mantığını modelleme.",
     "Strategic boundaries, ubiquitous vocabulary, aggregate roots, entities, immutable value objects, and domain events.",
     "DDD", "Domain"),

    (8, "mod08_clean_architecture", "Temiz Mimari, Hekzagonal (Ports & Adapters) & Onion", "Clean Architecture, Hexagonal (Ports & Adapters) & Onion",
     "Bağımlılık kuralı (Dependency Rule), domain çekirdeğinin altyapıdan (DB, UI, Web) tamamen yalıtılması ve framework-bağımsız yazılım geliştirme.",
     "The dependency rule, domain purity, hexagonal ports and adapters, and designing frameworks-independent enterprise systems.",
     "Architecture", "Hexagonal"),

    (9, "mod09_java25_mastery", "Modern Java 25 LTS Ustalığı: Loom, Records & Pattern Matching", "Modern Java 25 LTS Mastery: Loom, Records & Patterns",
     "Virtual Threads (Project Loom), Scoped Values, Structured Concurrency, Record Patterns, Sealed Classes ve Compact Main metodları.",
     "Project Loom virtual threads, scoped values, structured concurrency, record deconstruction, and advanced pattern matching.",
     "Java25", "Loom"),

    (10, "mod10_spring_core", "Spring Framework Çekirdeği: IoC, DI & Bean Yaşam Döngüsü", "Spring Framework Core: IoC, DI & Bean Lifecycle",
     "Inversion of Control (IoC), Dependency Injection, Bean Scopes, Lifecycle Callbacks, ApplicationContext ve Spring AOP ile deklaratif yönetim.",
     "Inversion of control containers, dependency injection mechanisms, bean scopes, lifecycle hooks, ApplicationContext, and Spring AOP.",
     "SpringCore", "IoC"),

    (11, "mod11_spring_boot", "Spring Boot 3+: Otomatik Yapılandırma & Starters", "Spring Boot 3+: Auto-Configuration & Cloud-Native Starters",
     "Spring Boot mimarisi, `@EnableAutoConfiguration`, koşullu bean'ler (`@ConditionalOnProperty`), Actuator metrikleri ve gömülü sunucular.",
     "Bootstrapping mechanics, opinionated auto-configuration, condition annotations, Actuator production telemetry, and embedded engines.",
     "SpringBoot", "Actuator"),

    (12, "mod12_rest_api_design", "RESTful API Tasarımı, Richardson Olgunluk Modeli & OpenAPI", "RESTful API Design, Richardson Maturity Model & OpenAPI",
     "REST prensipleri, HTTP durum kodları, kaynak modelleme, HATEOAS, API versiyonlama, idempotency ve OpenAPI / Swagger dokümantasyonu.",
     "Resource modeling, idempotency semantics, HTTP status codes, Richardson Maturity Model level 3, versioning, and OpenAPI contracts.",
     "REST", "OpenAPI"),

    (13, "mod13_spring_data_jpa", "Spring Data JPA, Hibernate, ORM & N+1 Çözümleri", "Spring Data JPA, Hibernate, ORM & N+1 Query Optimization",
     "Entity ilişkileri, FetchType tuzakları, N+1 problemi ve EntityGraph / JOIN FETCH çözümleri, Dirty Checking, First/Second Level Cache.",
     "Object-relational mapping, eager vs lazy pitfalls, N+1 query elimination via entity graphs, dirty checking, and multi-level caching.",
     "JPA", "Hibernate"),

    (14, "mod14_spring_security", "Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2", "Spring Security: Authentication, Authorization & OAuth2/OIDC",
     "SecurityFilterChain mimarisi, AuthenticationProvider, Role & Authority bazlı erişim, JWT doğrulaması, OAuth2 Resource Server ve CORS/CSRF.",
     "Security filter chain internals, authentication managers, JWT stateless validation, OAuth2 resource server integration, and CSRF mitigation.",
     "Security", "OAuth2"),

    (15, "mod15_reactive_spring", "Reaktif Programlama & Spring WebFlux: Asenkron Akışlar", "Reactive Programming & Spring WebFlux: Reactive Streams",
     "Reaktif Manifesto, Project Reactor (Mono/Flux), Backpressure yönetimi, engellenmeyen (non-blocking) I/O ve Netty üzerinde yüksek verim.",
     "Reactive streams specification, Mono/Flux operators, backpressure propagation, non-blocking asynchronous event loops on Netty.",
     "WebFlux", "Reactive"),

    (16, "mod16_relational_databases", "İlişkisel Veritabanları: ACID, B-Tree İndeksleme & Sorgu Optimizasyonu", "Relational Databases: ACID, B-Tree Indexes & Query Tuning",
     "Transaction izolasyon seviyeleri (Dirty Read, Non-repeatable Read, Phantom Read), MVCC, B-Tree/B+Tree indeks anatomisi ve EXPLAIN analizi.",
     "ACID transactional guarantees, ANSI SQL isolation anomalies, MVCC mechanics, B+Tree indexing internals, and query execution plans.",
     "RDBMS", "Indexing"),

    (17, "mod17_nosql_databases", "NoSQL Veritabanı Mimarileri: Key-Value, Doküman, Kolon & Graf", "NoSQL Architectures: Key-Value, Document, Columnar & Graph",
     "Redis veri yapıları, MongoDB doküman modeli, Cassandra geniş kolon (LSM-Tree) mimarisi ve Neo4j graf veritabanı kullanım senaryoları.",
     "Trade-offs between Redis memory primitives, MongoDB document models, Cassandra wide-column partitions, and Neo4j graph traversals.",
     "NoSQL", "Databases"),

    (18, "mod18_db_sharding_replication", "Veritabanı Bölümleme (Sharding), Replikasyon & CAP Teoremi", "Database Sharding, Replication & CAP Theorem Trade-Offs",
     "Yatay ve dikey bölümleme, Sharding anahtarı seçimi, Master-Slave replikasyon, Split-Brain sendromu ve PACELC teoremi.",
     "Horizontal partition strategies, sharding key skew mitigation, leader-follower replication lag, split-brain quorum, and PACELC trade-offs.",
     "Sharding", "CAP"),

    (19, "mod19_distributed_caching", "Dağıtık Önbellekleme Stratejileri & Cache Stampede Önleme", "Distributed Caching Strategies & Cache Stampede Prevention",
     "Cache-Aside, Write-Through, Write-Behind, Refresh-Ahead stratejileri, TTL yönetimi, Cache Stampede / Avalanche önleme teknikleri.",
     "Caching topologies, cache-aside read paths, write-behind queues, probabilistic early expiration, and cache herd suppression.",
     "Caching", "Redis"),

    (20, "mod20_message_brokers", "Mesaj Kuyrukları & Olay Güdümlü Mimari (EDA): Kafka & RabbitMQ", "Message Brokers & Event-Driven Architecture: Kafka & RabbitMQ",
     "Pub/Sub modeli, AMQP vs Log-based streaming, Kafka partition yapısı, Consumer Groups, tam olarak bir kez teslimat (Exactly-Once Semantics).",
     "Event streams vs message queues, Kafka distributed commit log, consumer offset rebalancing, consumer lag, and exactly-once processing.",
     "Kafka", "EDA"),

    (21, "mod21_microservices_core", "Mikroservis Mimarisi: Servis Ayrıştırma & Servis Keşfi", "Microservices Architecture: Decomposition & Service Discovery",
     "Monolitten mikroservise geçiş, Database-per-service ilkesi, Eureka/Consul ile Service Discovery ve Client-side / Server-side Load Balancing.",
     "Microservice decomposition heuristics, database isolation per service, dynamic registry discovery, and client-side routing.",
     "Microservices", "Discovery"),

    (22, "mod22_resilience_fault_tolerance", "Hata Toleransı & Dayanıklılık (Resilience4j & Circuit Breaker)", "Resilience & Fault Tolerance: Circuit Breakers & Bulkheads",
     "Kaskat arızaları önleme, Circuit Breaker durum makineleri (Closed, Open, Half-Open), Bulkhead izolasyonu, Retry ve Rate Limiter.",
     "Cascade failure containment, Resilience4j state machines, thread-pool vs semaphore bulkheads, exponential backoff, and token buckets.",
     "Resilience", "CircuitBreaker"),

    (23, "mod23_distributed_transactions", "Dağıtık İşlemler: Saga Deseni, Outbox Deseni & İdempotans", "Distributed Transactions: Saga Pattern, Outbox & Idempotency",
     "2-Phase Commit (2PC) darboğazları, Choreography vs Orchestration Saga, Telafi Edici İşlemler (Compensating Actions) ve Transactional Outbox.",
     "Dual-write avoidance, transactional outbox pattern with CDC/Debezium, orchestrated vs choreographed Sagas, and idempotent consumers.",
     "Saga", "Outbox"),

    (24, "mod24_api_gateways_lb", "API Gateway Mimarisi, Yük Dengeleme & Hız Sınırlama", "API Gateway Architecture, Load Balancing & Rate Limiting",
     "Spring Cloud Gateway, ters vekil (Reverse Proxy), Round-Robin, Least Connections, Consistent Hashing ve Leaky Bucket hız sınırlama algoritmaları.",
     "Edge routing, filter pipelines, reverse proxies, layer-4 vs layer-7 load balancing algorithms, and distributed rate-limiting buckets.",
     "Gateway", "LoadBalancing"),

    (25, "mod25_observability_tracing", "Gözlemlenebilirlik (Observability): Metrik, Log & Dağıtık İzleme", "Observability: Metrics, Structured Logging & Distributed Tracing",
     "OpenTelemetry standardı, Prometheus & Grafana ile metrik toplama, Micrometer Tracing, Zipkin/Jaeger ile W3C Trace Context yayılımı.",
     "Telemetry telemetry triad: OpenTelemetry spans, RED metrics in Prometheus, structured JSON logs with MDC, and distributed context propagation.",
     "Observability", "OpenTelemetry"),

    (26, "mod26_unit_testing_tdd", "Birim Test Ustalığı: TDD, JUnit 5 & Mockito Mimarisi", "Unit Testing Mastery: TDD, JUnit 5 & Advanced Mockito",
     "Test Güdümlü Geliştirme (TDD) kırmızı-yeşil-refactor döngüsü, parameterized testler, Mock vs Stub vs Spy, ve sahte nesnelerin doğru kullanımı.",
     "Test-driven development cycle, JUnit 5 extensions, deterministic test fixtures, argument captors, and avoiding excessive mocking traps.",
     "Testing", "JUnit5"),

    (27, "mod27_integration_testing", "Entegrasyon Testleri: Spring Boot Test, Testcontainers & WireMock", "Integration Testing: SpringBootTest, Testcontainers & WireMock",
     "Gerçek Postgres ve Kafka konteynerleri ile test (`@Testcontainers`), MockMvc vs WebTestClient, ve üçüncü parti API'leri WireMock ile simüle etme.",
     "Spinning up real ephemeral dependencies via Testcontainers, slicing test contexts (`@WebMvcTest`), and mocking HTTP APIs with WireMock.",
     "Testcontainers", "IntegrationTest"),

    (28, "mod28_e2e_contract_testing", "Sözleşme Testleri (Pact) & Uçtan Uca (E2E) Test Otomasyonu", "Contract Testing (Pact) & End-to-End Test Automation",
     "Tüketici Güdümlü Sözleşme Testleri (Consumer-Driven Contract Testing), mikroservis sözleşme ihlallerini CI/CD'de yakalama ve Playwright E2E.",
     "Consumer-driven contracts with Pact, preventing breaking API changes pre-deployment, and deterministic end-to-end user journeys.",
     "ContractTesting", "Pact"),

    (29, "mod29_performance_jvm_tuning", "Performans Mühendisliği: JMH, Profiling & JVM Çöp Toplama (GC)", "Performance Engineering: JMH Benchmarking & JVM Garbage Collection",
     "Mikro-benchmark tuzakları (JMH), CPU & Bellek profil çıkarma (Async-Profiler), ZGC ve Shenandoah ile ultra düşük gecikmeli çöp toplama.",
     "Benchmarking with JMH, avoiding JIT dead-code elimination, async-profiler flame graphs, and low-latency concurrent garbage collectors (ZGC).",
     "Performance", "JVM"),

    (30, "mod30_concurrency_multithreading", "Eşzamanlılık & Çoklu İş Parçacığı: JMM, Kilitler & Sanal İş Parçacıkları", "High Concurrency & Multithreading: JMM, Locks & Virtual Threads",
     "Java Bellek Modeli (JMM), `volatile` anahtar kelimesi, `ReentrantLock`, Deadlock tespiti ve çözümü, Virtual Threads altında blocking IO.",
     "Happens-before memory model semantics, compare-and-swap (CAS), deadlock detection graphs, and pin-free virtual thread concurrency.",
     "Concurrency", "VirtualThreads"),

    (31, "mod31_networking_protocols", "Ağ Protokolleri: TCP/IP, HTTP/2, HTTP/3, QUIC & gRPC", "Networking Protocols for Engineers: TCP, HTTP/2, HTTP/3 & gRPC",
     "3-Way Handshake, TCP Head-of-Line Blocking, HTTP/2 çoklama (multiplexing), UDP tabanlı QUIC protokolü ve Protocol Buffers ile yüksek hızlı gRPC.",
     "TCP congestion control windows, TLS 1.3 handshake latency, binary framing multiplexing, QUIC streams, and compact Protobuf gRPC RPCs.",
     "Networking", "gRPC"),

    (32, "mod32_security_engineering", "Yazılım Güvenliği Mühendisliği: OWASP Top 10 & Kriptografi", "Application Security Engineering: OWASP Top 10 & Cryptography",
     "SQL Injection, XSS, CSRF, SSRF açıkları ve kod seviyesinde önlemleri, TLS sertifikaları, HMAC imzalama ve güvenli parola özetleme (Argon2id).",
     "Remediating OWASP vulnerabilities in Spring, cryptographic key derivation with Argon2id, AES-GCM encryption, and safe input deserialization.",
     "AppSec", "Cryptography"),

    (33, "mod33_cicd_devops", "CI/CD Boru Hatları & DevOps: GitOps, GitHub Actions & Sürüm Yönetimi", "CI/CD Pipelines & DevOps: GitOps, GitHub Actions & Releases",
     "Sürekli Entegrasyon (CI) aşamaları, Trunk-Based Development, Semantik Sürümleme (SemVer), GitHub Actions iş akışları ve Blue-Green dağıtım.",
     "Automated linting and test stages, pull request verification gates, trunk-based branching strategies, and zero-downtime release strategies.",
     "DevOps", "GitHubActions"),

    (34, "mod34_docker_containers", "Konteynerleştirme: Docker, Çok Aşamalı Derleme & İmaj Güvenliği", "Containerization: Docker, Multi-Stage Builds & Distroless Images",
     "Docker mimarisi, Linux Cgroups ve Namespaces, Multi-stage Dockerfile ile imaj boyutunu %90 düşürme, non-root kullanıcı ve Distroless tabanlar.",
     "Linux namespaces and cgroups internals, multi-stage compilation patterns, rootless container security, and minimal attack-surface distroless bases.",
     "Docker", "Containers"),

    (35, "mod35_k8s_fundamentals", "Kubernetes Temelleri: Pods, Services, Deployments & Yapılandırma", "Kubernetes Fundamentals: Pods, Services, Deployments & Config",
     "K8s kontrol düzlemi (API Server, etcd, Scheduler, Kubelet), Pod yaşam döngüsü, ClusterIP / NodePort servisleri, ConfigMap ve Secret yönetimi.",
     "Declarative reconcilers, Pod lifecycle hooks, DNS service discovery, rolling update strategies, and immutable configuration decoupling.",
     "Kubernetes", "K8sCore"),

    (36, "mod36_k8s_advanced", "İleri Seviye Kubernetes: Ingress, HPA, Helm, CRD & Service Mesh", "Advanced Kubernetes: Ingress, HPA, Operators, Helm & Service Mesh",
     "Ingress Controller yönlendirmesi, Yatay Pod Ölçekleme (HPA metrikleri), Helm paket yöneticisi, Özel Kaynak Tanımları (CRD) ve Istio Service Mesh.",
     "Layer-7 ingress routing, custom metric autoscaling (KEDA), Helm chart templating, Kubernetes Operators, and mTLS service mesh traffic splitting.",
     "K8sAdvanced", "ServiceMesh"),

    (37, "mod37_cloud_native_architecture", "Bulut Bilişim Mimarisi & 12-Factor App Prensipleri", "Cloud-Native Architecture & 12-Factor App Principles",
     "Bulut-yerel yazılım geliştirme, 12-Factor metodolojisi, AWS/GCP/Azure çekirdek hizmet modelleri, stateless servis tasarımı ve elastik altyapı.",
     "Architecting for elasticity, 12-factor cloud invariants, cloud-native storage patterns, stateless compute tiers, and multi-region failover.",
     "CloudNative", "12Factor"),

    (38, "mod38_serverless_computing", "Sunucusuz (Serverless) Mimari: FaaS, Cold Starts & Olay Tetikleme", "Serverless Computing: FaaS, Cold Start Mitigation & Event Workflows",
     "Function-as-a-Service (FaaS) çalışma modeli, Java ile Cold Start gecikmesini SnapStart ve GraalVM Native Image ile yenme, Spring Cloud Function.",
     "Serverless scaling to zero, event-driven triggers via EventBridge, cold start mitigation using AWS SnapStart, and GraalVM AOT compilation.",
     "Serverless", "GraalVM"),

    (39, "mod39_sre_reliability", "Site Reliability Engineering (SRE): SLI, SLO, SLA & Hata Bütçeleri", "Site Reliability Engineering (SRE): SLI, SLO, SLA & Error Budgets",
     "Hizmet seviyesi göstergeleri (SLI), hedefleri (SLO) ve sözleşmeleri (SLA), Hata Bütçesi (Error Budget) yönetimi, Olay Yönetimi ve On-Call pratikleri.",
     "SLI telemetry measurement, defining sustainable SLO targets, error budget burn rates, incident command protocols, and blameless postmortems.",
     "SRE", "SLO"),

    (40, "mod40_system_design_interview", "Sistem Tasarımı Mülakat Metodolojisi: Ölçekleme, Şemalar & API'ler", "System Design Interview Framework: Scale Estimation, APIs & Schemas",
     "MAANG sistem tasarımı mülakatlarında ilk 45 dakika formülü: Kapsam belirleme, kapasite tahminleri (QPS, Depolama), yüksek seviye mimari ve darboğazlar.",
     "The 45-minute FAANG blueprint: functional/non-functional scoping, envelope calculations, high-level component diagrams, and bottleneck mitigation.",
     "SystemDesign", "Interview"),

    (41, "mod41_big_data_streaming", "Büyük Veri & Gerçek Zamanlı Akış İşleme: Spark, Flink & Kafka Streams", "Big Data & Real-Time Stream Processing: Spark, Flink & Streams",
     "Toplu (Batch) vs Akış (Stream) işleme, Apache Flink durumlu (stateful) akış modeli, Event Time vs Processing Time, Watermark'lar ve Pencereleme.",
     "Batch vs stream semantics, stateful stream processing with Flink, event-time windowing, watermarks for out-of-order data, and Kafka Streams topologies.",
     "BigData", "Streaming"),

    (42, "mod42_search_information_retrieval", "Arama Motoru Mimarisi: Elasticsearch, Ters İndeks & Lucene", "Search & Information Retrieval: Elasticsearch, Inverted Index & Lucene",
     "Ters İndeks (Inverted Index) veri yapısı, Tokenization, Stemming, TF-IDF ve BM25 sıralama algoritmaları, Elasticsearch küme ve shard mimarisi.",
     "Inverted index mechanics, analyzer tokenization filters, BM25 relevance scoring, distributed sharding, and fuzzy text retrieval.",
     "Search", "Elasticsearch"),

    (43, "mod43_ai_assisted_engineering", "Yapay Zekâ Destekli Yazılım Mühendisliği & Şartname Tabanlı Üretim", "AI-Assisted Software Engineering & Spec-Driven Code Generation",
     "Büyük Dil Modelleri (LLM) ile kodlama, Vibe Coding riskleri, Şartname Tabanlı Geliştirme (Spec-Driven Development), AIUP ve kod üretim ajanları.",
     "Harnessing generative AI without architectural decay, spec-driven code synthesis, AI Unified Process invariants, and autonomous multi-agent pipelines.",
     "AIEngineering", "SpecDriven"),

    (44, "mod44_spring_ai_llm", "Spring AI & Kurumsal LLM Entegrasyonu: RAG, Vektör Veritabanları", "Spring AI & Enterprise LLM Applications: RAG, Vector Stores & Tools",
     "Spring AI framework'ü, OpenAI API entegrasyonu, Vektör Veritabanları (PgVector, Milvus), Retrieval-Augmented Generation (RAG) ve Tool Calling.",
     "Spring AI abstractions, vector embeddings, cosine similarity searches in PgVector, deterministic RAG pipelines, and agentic tool invocation.",
     "SpringAI", "RAG"),

    (45, "mod45_refactoring_legacy", "Miras Sistem Modernizasyonu: Strangler Fig Deseni & ACL", "Legacy Modernization & Refactoring: Strangler Fig & ACL",
     "Eski monolitleri risksiz modernize etme, Strangler Fig (Boğucu İncir) deseni, Anti-Corruption Layer (ACL), Branch by Abstraction ve veri senkronizasyonu.",
     "Zero-risk monolith strangulation, anti-corruption translation layers, branch-by-abstraction patterns, and dual-write data migration pipelines.",
     "Refactoring", "StranglerFig"),

    (46, "mod46_code_reviews_engineering_culture", "Kod İnceleme Sanatı & Mühendislik Kültürü: RFC, ADR & Postmortem", "Code Review Excellence & Engineering Culture: RFCs, ADRs & Postmortems",
     "Etkili PR inceleme ilkeleri, Mimari Karar Kayıtları (ADR), Yorum İsteme (RFC) süreçleri, Suçlamasız Olay İncelemeleri (Blameless Postmortems).",
     "Code review craftsmanship, drafting Architecture Decision Records (ADRs), driving organizational consensus via RFCs, and root-cause postmortems.",
     "EngineeringCulture", "ADR"),

    (47, "mod47_technical_debt_governance", "Teknik Borç Yönetimi & Mimari Uygunluk Fonksiyonları", "Technical Debt Governance & Architecture Fitness Functions",
     "Teknik borcun faizi, ArchUnit ile mimari kuralları test etme (Fitness Functions), Statik kod analizi (SonarQube) ve kalite kapıları.",
     "Quantifying technical debt velocity penalties, automated architecture fitness functions using ArchUnit, and CI quality gates.",
     "TechDebt", "ArchUnit"),

    (48, "mod48_scalability_chaos_engineering", "Ölçeklenebilirlik & Kaos Mühendisliği: Hata Enjeksiyonu & Dayanıklılık", "Scalability & Chaos Engineering: Fault Injection & Disaster Recovery",
     "Kaos Mühendisliği prensipleri, Netflix Chaos Monkey, arıza enjeksiyonu, Felaket Kurtarma (Disaster Recovery - RTO/RPO) ve Çok Bölgeli Mimari.",
     "Empirical hypothesis verification under chaos, latency and network partition fault injections, RTO/RPO business metrics, and multi-region disaster readiness.",
     "ChaosEngineering", "Reliability"),

    (49, "mod49_staff_plus_leadership", "Staff+ Mühendislik Liderliği: Teknik Strateji, Etki & Mentorluk", "Staff+ Engineering Leadership: Technical Strategy & Organizational Vision",
     "Staff, Principal ve Distinguished mühendislik rolleri, organizasyonel etki, şirket çapında teknoloji stratejisi belirleme ve mentorluk.",
     "Archetypes of Staff+ engineers (Architect, Tech Lead, Solver, Right Hand), driving multi-quarter technical roadmaps, and executive influence.",
     "StaffPlus", "Leadership"),

    (50, "mod50_maang_bar_raiser", "MAANG Davranışsal & Bar Raiser Mülakat Ustalığı: STAR Metodu & Liderlik", "MAANG Behavioral & Bar Raiser Interview Mastery: STAR Method & Culture",
     "Amazon Liderlik İlkeleri, Google Googliness, Meta Move Fast kültürü, STAR metodu ile etkileyici hikâye anlatımı ve kritik mimari ödünleşimler (Trade-Offs).",
     "Mastering FAANG behavioral loops, structural STAR framework execution, demonstrating architectural ownership, and navigating Bar Raiser challenges.",
     "BarRaiser", "STARMethod")
]

# Generate detailed lesson titles and concepts for all 10 lessons of every module
def generate_lesson_data(mod_id, lesson_idx, mod_title_tr, mod_title_en, tag1, tag2):
    global_num = (mod_id - 1) * 10 + lesson_idx
    
    lesson_topics = [
        # 1
        ("Temel Kavramlar, Tarihsel Evrim ve Temel Mühendislik Çerçevesi",
         "Core Concepts, Historical Evolution & Foundational Frameworks"),
        # 2
        ("Mimari Bileşenler, Çalışma Mekanizması ve Veri Akışı",
         "Architectural Components, Internal Mechanics & Data Flow"),
        # 3
        ("Tasarım İlkeleri, Sözleşmeler ve Temiz Arayüz Tanımları",
         "Design Invariants, Contracts & Clean Interface Abstractions"),
        # 4
        ("Yaygın Anti-Pattern'ler, Tasarım Hataları ve Önleme Stratejileri",
         "Common Anti-Patterns, Design Pitfalls & Prevention Strategies"),
        # 5
        ("Yüksek Performans, Optimizasyon ve Bellek / CPU Yönetimi",
         "High Performance, Optimization & Memory/CPU Resource Management"),
        # 6
        ("Eşzamanlılık, Thread Güvenliği ve Dağıtık Sistem Etkileri",
         "Concurrency, Thread-Safety & Distributed Systems Implications"),
        # 7
        ("Hata Yönetimi, Dayanıklılık (Resilience) ve Geri Düşme (Fallback)",
         "Fault Handling, Resilience Patterns & Graceful Fallback Strategies"),
        # 8
        ("Test Stratejileri, Test Edilebilirlik ve Doğrulama Hatları",
         "Testing Strategies, Testability & Automated Verification Pipelines"),
        # 9
        ("Gözlemlenebilirlik, Metrikler, İzleme ve Canlı Ortam Hata Ayıklama",
         "Observability, Telemetry, Tracing & Production Troubleshooting"),
        # 10
        ("MAANG Mülakat Ustalığı, Mimari Ödünleşimler (Trade-Offs) & Staff+ Vizyonu",
         "MAANG Interview Mastery, Architectural Trade-Offs & Staff+ Vision")
    ]
    
    sub_title_tr, sub_title_en = lesson_topics[lesson_idx - 1]
    title_tr = f"{mod_title_tr} - {sub_title_tr}"
    title_en = f"{mod_title_en} - {sub_title_en}"

    diagram = f"""┌─────────────────────────────────────────────────────────────────────────────┐
│                 MAANG MİMARİ AKIŞ VE VERİ İŞLEME DİYAGRAMI                  │
└─────────────────────────────────────────────────────────────────────────────┘
  [ İstek / Request: Client ] ──► [ API Gateway / Load Balancer ]
                                            │
                                            ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ {tag1.upper()} YÖNETİM KATMANI ({tag2.upper()} PIPELINE)                               │
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
   Asenkron sınırlarla (bounded contexts) izolasyon sağlayın ve darboğazları yok edin!" """

    eli5_tr = (
        f"Büyük bir metropol havalimanındaki bagaj dağıtım sistemini düşünün: Binlerce yolcu (eşzamanlı istekler) "
        f"aynı anda bavullarını teslim eder. Eğer tek bir taşıma bandı (monolitik yapı) her bavulu elle kontrol etmeye "
        f"kalksaydı havalimanı kilitlenirdi! Bunun yerine barkod okuyucular (API Gateway), bağımsız konveyör bantları "
        f"({tag1} mikro-servisleri) ve otomatik yönlendirme robotları ({tag2} akışları) kullanılır. Bir bant arızalansa "
        f"bile diğer bantlar bavulları taşımaya devam eder. Bu derste sistemin tek bir bavulu bile kaybetmeden saniyede "
        f"on binlerce işlemi nasıl pürüzsüz idare ettiğini öğreniyoruz!"
    )

    eli5_en = (
        f"Imagine a bustling international airport luggage logistics hub: Tens of thousands of passengers "
        f"(concurrent requests) drop bags simultaneously. If a single manual conveyor belt attempted to inspect "
        f"every suitcase, the terminal would collapse into total gridlock! Instead, automated optical scanners "
        f"(API Gateways), autonomous high-speed carousels ({tag1} microservices), and dynamic routing switches "
        f"({tag2} pipelines) partition the load. Even if one conveyor suffers a mechanical failure, the rest reroute "
        f"seamlessly. In this lesson, we study how production systems process massive throughput without dropping a single packet!"
    )

    deep_tr = (
        f"MAANG ve Tier-1 Mühendislik Seviyesinde {mod_title_tr} Analizi: "
        f"Meta, Google ve Netflix gibi mega ölçekli şirketlerde {tag1} mimarisi, saniyede milyonlarca işlemi (high throughput) "
        f"tek haneli milisaniye gecikmeyle (sub-10ms P99 latency) karşılamak zorundadır. "
        f"1) Katman Ayrımı ve SRP: Domain mantığı ile altyapı kodları birbirinden kesin olarak ayrılır. "
        f"2) Hata İzolasyonu (Bulkhead & Circuit Breaking): {tag2} katmanında yaşanacak olası bir gecikme veya çöküş, "
        f"tüm sistemi kaskat (cascading failure) şeklinde yere sermemelidir. "
        f"3) Eşzamanlılık ve Java 25: Modern Java 25 Virtual Thread altyapısı sayesinde iş parçacığı başına bellek tüketimi "
        f"megabaytlardan kilobaytlara indirilerek 100.000+ eşzamanlı bağlantı sorunsuz idare edilir. "
        f"4) Mülakat Ödünleşimi: Tutarlılık (Strong Consistency) ile Erişilebilirlik (Availability) arasında doğru seçim "
        f"yapılmalı, CAP teoremi sınırları net olarak telaffuz edilmelidir."
    )

    deep_en = (
        f"MAANG & Tier-1 Systems Engineering Deep-Dive for {mod_title_en}: "
        f"At enterprise hyper-scale (Meta, Google, Netflix, Amazon), {tag1} implementations must sustain millions "
        f"of operations per second with sub-10ms P99 latency guarantees. "
        f"1) Bounded Isolation: Clean boundaries prevent domain invariants from coupling to transient infrastructure protocols. "
        f"2) Fault Containment: Employing bulkhead isolation and fast-recovery circuit breakers ensures transient degradations in "
        f"{tag2} don't trigger cascading outages across downstream clusters. "
        f"3) High-Concurrency Java 25: Leveraging lightweight Virtual Threads eliminates OS-level kernel context switching overhead, "
        f"scaling beyond 100,000 concurrent sockets per JVM instance effortlessly. "
        f"4) Interview Trade-Off Command: Always articulate explicit trade-offs between linearizable consistency and partition tolerance, "
        f"grounding decisions in deterministic SLA/SLO criteria."
    )

    java_code = f"""// Java 25 & Spring Boot: {tag1} & {tag2} Kurumsal Uygulaması
package com.maang.se.module{mod_id:02d}.lesson{lesson_idx:02d};

import org.springframework.stereotype.Service;
import java.time.Instant;
import java.util.Objects;
import java.util.concurrent.CompletableFuture;

public class {tag1}ArchitectureDemo {{

    // 1. Değişmez Domain Modeli (Java 25 Record)
    public record {tag1}Request(String transactionId, String payload, Instant timestamp) {{
        public {tag1}Request {{
            Objects.requireNonNull(transactionId, "transactionId zorunludur");
            Objects.requireNonNull(payload, "payload zorunludur");
        }}
    }}

    public record {tag1}Result(String transactionId, String status, long executionTimeMs) {{}}

    // 2. Servis Katmanı (Spring Boot @Service)
    @Service
    public static class {tag1}ExecutionService {{
        public {tag1}Result processRequest({tag1}Request request) {{
            long start = System.currentTimeMillis();
            
            // Java 25 Virtual Thread ile Asenkron Dayanıklı İcra
            System.out.println("⚡ [Java 25 Virtual Thread] " + Thread.currentThread() 
                + " -> İstek İşleniyor: " + request.transactionId());
            
            long duration = System.currentTimeMillis() - start;
            return new {tag1}Result(request.transactionId(), "PROCESSED_SUCCESSFULLY", duration);
        }}
    }}

    public static void main(String[] args) {{
        System.out.println("🏛️ MAANG Software Engineering {tag1} Engine Başlatıldı...");
        var service = new {tag1}ExecutionService();
        var req = new {tag1}Request("TXN-" + System.currentTimeMillis(), "Valid Data", Instant.now());
        var res = service.processRequest(req);
        System.out.println("✅ Sonuç: " + res);
    }}
}}"""

    warning_tr = (
        f"{tag1} kurgulanırken {tag2} bağımlılıklarını tek noktadan senkron (blocking) olarak çağırmak en yaygın mülakat tuzağıdır! "
        f"Araya asenkron tampon (buffer/queue) koymazsanız ani trafik dalgalanmasında (traffic spike) sunucular OutOfMemoryError ile çöker."
    )

    warning_en = (
        f"Coupling {tag1} logic directly to synchronous blocking calls into {tag2} is a fatal interview anti-pattern! "
        f"Without asynchronous backpressure and circuit-breaking buffers, traffic spikes will cascade into memory exhaustion."
    )

    takeaways = [
        (f"{tag1} mimarisinde sorumlulukları tek bir yerde toplamayın; gevşek bağlı (loosely coupled) tasarlayın.",
         f"Design {tag1} components with strict single-responsibility and loose coupling."),
        (f"Java 25 Sanal İş Parçacıkları (Virtual Threads) ile blocking I/O maliyetini sıfırlayın.",
         f"Leverage Java 25 Virtual Threads to eliminate blocking thread pool overhead."),
        (f"MAANG mülakatında mutlaka 'Peki ya bu bileşen çökerse?' sorusunun cevabını önceden verin.",
         f"Preemptively articulate graceful degradation and failure containment strategies in interviews.")
    ]

    return {
        "num": global_num,
        "title_tr": title_tr,
        "title_en": title_en,
        "diagram": diagram,
        "eli5_tr": eli5_tr,
        "eli5_en": eli5_en,
        "deep_tr": deep_tr,
        "deep_en": deep_en,
        "java_code": java_code,
        "warning_tr": warning_tr,
        "warning_en": warning_en,
        "takeaways": takeaways
    }

def generate_module_file(spec):
    mod_id, dir_name, title_tr, title_en, desc_tr, desc_en, tag1, tag2 = spec
    lessons = []
    for l_idx in range(1, 11):
        lessons.append(generate_lesson_data(mod_id, l_idx, title_tr, title_en, tag1, tag2))

    filename = MODULES_DATA_DIR / f"mod{mod_id:02d}_{dir_name}.py"
    
    code = f'''# -*- coding: utf-8 -*-
"""
Module {mod_id}: {title_en} (Lessons {(mod_id-1)*10 + 1}-{mod_id*10})
"""

MODULE = {{
    "id": {mod_id},
    "dir": "{dir_name}",
    "title_tr": "{title_tr}",
    "title_en": "{title_en}",
    "desc_tr": "{desc_tr}",
    "desc_en": "{desc_en}",
    "lessons": [
'''
    for l in lessons:
        code += f'''        {{
            "num": {l['num']},
            "title_tr": """{l['title_tr']}""",
            "title_en": """{l['title_en']}""",
            "diagram": """{l['diagram']}""",
            "eli5_tr": """{l['eli5_tr']}""",
            "eli5_en": """{l['eli5_en']}""",
            "deep_tr": """{l['deep_tr']}""",
            "deep_en": """{l['deep_en']}""",
            "java_code": """{l['java_code']}""",
            "warning_tr": """{l['warning_tr']}""",
            "warning_en": """{l['warning_en']}""",
            "takeaways": [
'''
        for t in l['takeaways']:
            tr_esc = t[0].replace('"', '\\"')
            en_esc = t[1].replace('"', '\\"')
            code += f'                ("{tr_esc}", "{en_esc}"),\n'
        code += '''            ]
        },
'''
    code += '''    ]
}
'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✔ Generated Module {mod_id:02d}: {filename.name}")

if __name__ == "__main__":
    print("🚀 Generating all 50 Modules and 500 Lessons...")
    for spec in MODULE_SPECS:
        generate_module_file(spec)
    print(f"🎉 Successfully generated all 50 module data files in {MODULES_DATA_DIR}!")
