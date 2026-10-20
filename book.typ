#import "/template.typ": *

#show: doc => setup_book(
  title: "Aptala Anlatır Gibi MAANG Yazılım Mühendisliği El Kitabı",
  author: "Antigravity & MAANG Software Engineering Guild",
  doc
)

#book_front_cover()

#pagebreak()
#v(20pt)
#align(center)[
  #text(size: 20pt, weight: "bold", fill: rgb("030712"))[Önsöz ve Başlarken / Preface & Getting Started]
]
#v(16pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 20pt,
  [
    == 🇹🇷 Bu Eğitim Hakkında
    Bu kitap; Meta, Amazon, Apple, Netflix, Google (MAANG) ve birinci sınıf teknoloji şirketlerinin Yazılım Mühendisliği (Software Engineering) mülakatlarına hazırlanan mühendisler ve mimarlar için 500 ders ve 50 bölümden oluşan anıtsal bir başucu kaynağı olarak hazırlanmıştır.

    Yazılım yaşam döngüsünden Clean Code ve SOLID prensiplerine, Hekzagonal Mimariden modern Java 25 LTS ve Spring Boot 3+'a, Dağıtık Sistemler ve Mikroservislerden Kubernetes ve Kaos Mühendisliğine kadar uzanan tüm mühendislik spektrumu, *bir aptala anlatır gibi* en yalın analojiler, mimari ASCII akış şemaları ve kurumsal Java 25 kodlarıyla ele alınmıştır.
  ],
  [
    == 🇬🇧 About This Masterclass
    This masterclass is comprehensively engineered for software engineers, tech leads, and aspiring architects preparing for high-stakes Software Engineering and System Design rounds at Tier-1 companies (MAANG / FAANG).

    Spanning 500 progressive lessons structured across 50 dedicated modules, this curriculum deconstructs the entire software engineering universe—from Clean Architecture, SOLID, and modern Java 25 Virtual Threads to Spring Boot, Kafka, Kubernetes, and Staff+ architectural governance—using intuitive Explain Like I'm 5 (ELI5) metaphors, architectural schematics, and clean Spring implementations.
  ]
)

#v(20pt)
#line(length: 100%, stroke: 0.8pt + rgb("cbd5e1"))
#v(10pt)

#outline(
  title: [İçindekiler / Table of Contents],
  depth: 2,
  indent: auto
)

#pagebreak()

#module_cover(
  1,
  "Yazılım Mühendisliği Temelleri & Agile / Scrum / Kanban",
  "Software Engineering Fundamentals & Agile / Scrum / Kanban",
  "Yazılım yaşam döngüsü (SDLC), Waterfall'dan Agile'a evrim, Scrum törenleri, Kanban akış yönetimi, XP pratikleri ve MAANG ekiplerinin teslimat hız sırları.",
  "Software development lifecycles, Agile/Scrum ceremonies, Kanban WIP limits, Extreme Programming engineering rigor, and Tier-1 velocity heuristics."
)

#include "/content/mod01_sdlc_agile/lesson_001.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_002.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_003.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_004.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_005.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_006.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_007.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_008.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_009.typ"
#v(12pt)

#include "/content/mod01_sdlc_agile/lesson_010.typ"
#v(12pt)


#module_cover(
  2,
  "Temiz Kod & Zanaatkarlık (Clean Code & Craftsmanship)",
  "Clean Code, Craftsmanship & Expressive Naming",
  "Okunabilir kod ilkeleri, anlamlı isimlendirme, tek iş yapan fonksiyonlar, yorum satırı anti-pattern'leri ve bilişsel yükü en aza indiren refactoring kalıpları.",
  "Readability invariants, intention-revealing naming, small cohesive functions, elimination of comment rot, and cognitive-load reduction techniques."
)

#include "/content/mod02_clean_code/lesson_011.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_012.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_013.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_014.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_015.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_016.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_017.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_018.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_019.typ"
#v(12pt)

#include "/content/mod02_clean_code/lesson_020.typ"
#v(12pt)


#module_cover(
  3,
  "SOLID İlkeleri & Nesne Yönelimli Tasarım Mimarisi",
  "SOLID Principles & Object-Oriented Design Mastery",
  "Tek Sorumluluk (SRP), Açık/Kapalı (OCP), Liskov İkame (LSP), Arayüz Ayrımı (ISP) ve Bağımlılığı Tersine Çevirme (DIP) ilkelerinin modern Java ile derinlemesine analizi.",
  "Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion analyzed with modern Java 25 idioms."
)

#include "/content/mod03_solid_principles/lesson_021.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_022.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_023.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_024.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_025.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_026.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_027.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_028.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_029.typ"
#v(12pt)

#include "/content/mod03_solid_principles/lesson_030.typ"
#v(12pt)


#module_cover(
  4,
  "Tasarım Kalıpları: Kurucu (Creational) Kalıplar",
  "Design Patterns: Creational Patterns in Modern Java",
  "Factory Method, Abstract Factory, Builder, Singleton, Prototype ve Multiton kalıplarının Java 25 Records ve Spring DI dünyasındaki modern karşılıkları.",
  "Factory, Builder, Singleton, Prototype, and Object Pool patterns revisited with Java 25 records and Spring dependency injection."
)

#include "/content/mod04_creational_patterns/lesson_031.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_032.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_033.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_034.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_035.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_036.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_037.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_038.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_039.typ"
#v(12pt)

#include "/content/mod04_creational_patterns/lesson_040.typ"
#v(12pt)


#module_cover(
  5,
  "Tasarım Kalıpları: Yapısal (Structural) Kalıplar",
  "Design Patterns: Structural Patterns & Decoupling",
  "Adapter, Decorator, Facade, Composite, Proxy, Flyweight ve Bridge kalıpları ile gevşek bağlı (loosely coupled) sistem tasarımı.",
  "Adapter, Decorator, Facade, Composite, Proxy, Flyweight, and Bridge patterns for resilient component decoupling."
)

#include "/content/mod05_structural_patterns/lesson_041.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_042.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_043.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_044.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_045.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_046.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_047.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_048.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_049.typ"
#v(12pt)

#include "/content/mod05_structural_patterns/lesson_050.typ"
#v(12pt)


#module_cover(
  6,
  "Tasarım Kalıpları: Davranışsal (Behavioral) Kalıplar",
  "Design Patterns: Behavioral Patterns & Event Flow",
  "Strategy, Observer, Command, State, Chain of Responsibility, Mediator ve Template Method kalıplarının fonksiyonel Java ile icrası.",
  "Strategy, Observer, Command, State, Chain of Responsibility, and Template Method patterns leveraging Java functional interfaces."
)

#include "/content/mod06_behavioral_patterns/lesson_051.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_052.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_053.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_054.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_055.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_056.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_057.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_058.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_059.typ"
#v(12pt)

#include "/content/mod06_behavioral_patterns/lesson_060.typ"
#v(12pt)


#module_cover(
  7,
  "Etki Alanı Odaklı Tasarım (DDD): Stratejik & Taktiksel",
  "Domain-Driven Design (DDD): Strategic & Tactical Patterns",
  "Ubiquitous Language, Bounded Contexts, Context Mapping, Entities, Value Objects, Aggregates ve Domain Events ile karmaşık iş mantığını modelleme.",
  "Strategic boundaries, ubiquitous vocabulary, aggregate roots, entities, immutable value objects, and domain events."
)

#include "/content/mod07_domain_driven_design/lesson_061.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_062.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_063.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_064.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_065.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_066.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_067.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_068.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_069.typ"
#v(12pt)

#include "/content/mod07_domain_driven_design/lesson_070.typ"
#v(12pt)


#module_cover(
  8,
  "Temiz Mimari, Hekzagonal (Ports & Adapters) & Onion",
  "Clean Architecture, Hexagonal (Ports & Adapters) & Onion",
  "Bağımlılık kuralı (Dependency Rule), domain çekirdeğinin altyapıdan (DB, UI, Web) tamamen yalıtılması ve framework-bağımsız yazılım geliştirme.",
  "The dependency rule, domain purity, hexagonal ports and adapters, and designing frameworks-independent enterprise systems."
)

#include "/content/mod08_clean_architecture/lesson_071.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_072.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_073.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_074.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_075.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_076.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_077.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_078.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_079.typ"
#v(12pt)

#include "/content/mod08_clean_architecture/lesson_080.typ"
#v(12pt)


#module_cover(
  9,
  "Modern Java 25 LTS Ustalığı: Loom, Records & Pattern Matching",
  "Modern Java 25 LTS Mastery: Loom, Records & Patterns",
  "Virtual Threads (Project Loom), Scoped Values, Structured Concurrency, Record Patterns, Sealed Classes ve Compact Main metodları.",
  "Project Loom virtual threads, scoped values, structured concurrency, record deconstruction, and advanced pattern matching."
)

#include "/content/mod09_java25_mastery/lesson_081.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_082.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_083.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_084.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_085.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_086.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_087.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_088.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_089.typ"
#v(12pt)

#include "/content/mod09_java25_mastery/lesson_090.typ"
#v(12pt)


#module_cover(
  10,
  "Spring Framework Çekirdeği: IoC, DI & Bean Yaşam Döngüsü",
  "Spring Framework Core: IoC, DI & Bean Lifecycle",
  "Inversion of Control (IoC), Dependency Injection, Bean Scopes, Lifecycle Callbacks, ApplicationContext ve Spring AOP ile deklaratif yönetim.",
  "Inversion of control containers, dependency injection mechanisms, bean scopes, lifecycle hooks, ApplicationContext, and Spring AOP."
)

#include "/content/mod10_spring_core/lesson_091.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_092.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_093.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_094.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_095.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_096.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_097.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_098.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_099.typ"
#v(12pt)

#include "/content/mod10_spring_core/lesson_100.typ"
#v(12pt)


#module_cover(
  11,
  "Spring Boot 3+: Otomatik Yapılandırma & Starters",
  "Spring Boot 3+: Auto-Configuration & Cloud-Native Starters",
  "Spring Boot mimarisi, `@EnableAutoConfiguration`, koşullu bean'ler (`@ConditionalOnProperty`), Actuator metrikleri ve gömülü sunucular.",
  "Bootstrapping mechanics, opinionated auto-configuration, condition annotations, Actuator production telemetry, and embedded engines."
)

#include "/content/mod11_spring_boot/lesson_101.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_102.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_103.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_104.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_105.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_106.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_107.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_108.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_109.typ"
#v(12pt)

#include "/content/mod11_spring_boot/lesson_110.typ"
#v(12pt)


#module_cover(
  12,
  "RESTful API Tasarımı, Richardson Olgunluk Modeli & OpenAPI",
  "RESTful API Design, Richardson Maturity Model & OpenAPI",
  "REST prensipleri, HTTP durum kodları, kaynak modelleme, HATEOAS, API versiyonlama, idempotency ve OpenAPI / Swagger dokümantasyonu.",
  "Resource modeling, idempotency semantics, HTTP status codes, Richardson Maturity Model level 3, versioning, and OpenAPI contracts."
)

#include "/content/mod12_rest_api_design/lesson_111.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_112.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_113.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_114.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_115.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_116.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_117.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_118.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_119.typ"
#v(12pt)

#include "/content/mod12_rest_api_design/lesson_120.typ"
#v(12pt)


#module_cover(
  13,
  "Spring Data JPA, Hibernate, ORM & N+1 Çözümleri",
  "Spring Data JPA, Hibernate, ORM & N+1 Query Optimization",
  "Entity ilişkileri, FetchType tuzakları, N+1 problemi ve EntityGraph / JOIN FETCH çözümleri, Dirty Checking, First/Second Level Cache.",
  "Object-relational mapping, eager vs lazy pitfalls, N+1 query elimination via entity graphs, dirty checking, and multi-level caching."
)

#include "/content/mod13_spring_data_jpa/lesson_121.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_122.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_123.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_124.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_125.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_126.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_127.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_128.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_129.typ"
#v(12pt)

#include "/content/mod13_spring_data_jpa/lesson_130.typ"
#v(12pt)


#module_cover(
  14,
  "Spring Security: Kimlik Doğrulama, Yetkilendirme & OAuth2",
  "Spring Security: Authentication, Authorization & OAuth2/OIDC",
  "SecurityFilterChain mimarisi, AuthenticationProvider, Role & Authority bazlı erişim, JWT doğrulaması, OAuth2 Resource Server ve CORS/CSRF.",
  "Security filter chain internals, authentication managers, JWT stateless validation, OAuth2 resource server integration, and CSRF mitigation."
)

#include "/content/mod14_spring_security/lesson_131.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_132.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_133.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_134.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_135.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_136.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_137.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_138.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_139.typ"
#v(12pt)

#include "/content/mod14_spring_security/lesson_140.typ"
#v(12pt)


#module_cover(
  15,
  "Reaktif Programlama & Spring WebFlux: Asenkron Akışlar",
  "Reactive Programming & Spring WebFlux: Reactive Streams",
  "Reaktif Manifesto, Project Reactor (Mono/Flux), Backpressure yönetimi, engellenmeyen (non-blocking) I/O ve Netty üzerinde yüksek verim.",
  "Reactive streams specification, Mono/Flux operators, backpressure propagation, non-blocking asynchronous event loops on Netty."
)

#include "/content/mod15_reactive_spring/lesson_141.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_142.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_143.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_144.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_145.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_146.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_147.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_148.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_149.typ"
#v(12pt)

#include "/content/mod15_reactive_spring/lesson_150.typ"
#v(12pt)


#module_cover(
  16,
  "İlişkisel Veritabanları: ACID, B-Tree İndeksleme & Sorgu Optimizasyonu",
  "Relational Databases: ACID, B-Tree Indexes & Query Tuning",
  "Transaction izolasyon seviyeleri (Dirty Read, Non-repeatable Read, Phantom Read), MVCC, B-Tree/B+Tree indeks anatomisi ve EXPLAIN analizi.",
  "ACID transactional guarantees, ANSI SQL isolation anomalies, MVCC mechanics, B+Tree indexing internals, and query execution plans."
)

#include "/content/mod16_relational_databases/lesson_151.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_152.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_153.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_154.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_155.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_156.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_157.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_158.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_159.typ"
#v(12pt)

#include "/content/mod16_relational_databases/lesson_160.typ"
#v(12pt)


#module_cover(
  17,
  "NoSQL Veritabanı Mimarileri: Key-Value, Doküman, Kolon & Graf",
  "NoSQL Architectures: Key-Value, Document, Columnar & Graph",
  "Redis veri yapıları, MongoDB doküman modeli, Cassandra geniş kolon (LSM-Tree) mimarisi ve Neo4j graf veritabanı kullanım senaryoları.",
  "Trade-offs between Redis memory primitives, MongoDB document models, Cassandra wide-column partitions, and Neo4j graph traversals."
)

#include "/content/mod17_nosql_databases/lesson_161.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_162.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_163.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_164.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_165.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_166.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_167.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_168.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_169.typ"
#v(12pt)

#include "/content/mod17_nosql_databases/lesson_170.typ"
#v(12pt)


#module_cover(
  18,
  "Veritabanı Bölümleme (Sharding), Replikasyon & CAP Teoremi",
  "Database Sharding, Replication & CAP Theorem Trade-Offs",
  "Yatay ve dikey bölümleme, Sharding anahtarı seçimi, Master-Slave replikasyon, Split-Brain sendromu ve PACELC teoremi.",
  "Horizontal partition strategies, sharding key skew mitigation, leader-follower replication lag, split-brain quorum, and PACELC trade-offs."
)

#include "/content/mod18_db_sharding_replication/lesson_171.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_172.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_173.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_174.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_175.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_176.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_177.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_178.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_179.typ"
#v(12pt)

#include "/content/mod18_db_sharding_replication/lesson_180.typ"
#v(12pt)


#module_cover(
  19,
  "Dağıtık Önbellekleme Stratejileri & Cache Stampede Önleme",
  "Distributed Caching Strategies & Cache Stampede Prevention",
  "Cache-Aside, Write-Through, Write-Behind, Refresh-Ahead stratejileri, TTL yönetimi, Cache Stampede / Avalanche önleme teknikleri.",
  "Caching topologies, cache-aside read paths, write-behind queues, probabilistic early expiration, and cache herd suppression."
)

#include "/content/mod19_distributed_caching/lesson_181.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_182.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_183.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_184.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_185.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_186.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_187.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_188.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_189.typ"
#v(12pt)

#include "/content/mod19_distributed_caching/lesson_190.typ"
#v(12pt)


#module_cover(
  20,
  "Mesaj Kuyrukları & Olay Güdümlü Mimari (EDA): Kafka & RabbitMQ",
  "Message Brokers & Event-Driven Architecture: Kafka & RabbitMQ",
  "Pub/Sub modeli, AMQP vs Log-based streaming, Kafka partition yapısı, Consumer Groups, tam olarak bir kez teslimat (Exactly-Once Semantics).",
  "Event streams vs message queues, Kafka distributed commit log, consumer offset rebalancing, consumer lag, and exactly-once processing."
)

#include "/content/mod20_message_brokers/lesson_191.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_192.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_193.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_194.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_195.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_196.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_197.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_198.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_199.typ"
#v(12pt)

#include "/content/mod20_message_brokers/lesson_200.typ"
#v(12pt)


#module_cover(
  21,
  "Mikroservis Mimarisi: Servis Ayrıştırma & Servis Keşfi",
  "Microservices Architecture: Decomposition & Service Discovery",
  "Monolitten mikroservise geçiş, Database-per-service ilkesi, Eureka/Consul ile Service Discovery ve Client-side / Server-side Load Balancing.",
  "Microservice decomposition heuristics, database isolation per service, dynamic registry discovery, and client-side routing."
)

#include "/content/mod21_microservices_core/lesson_201.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_202.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_203.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_204.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_205.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_206.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_207.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_208.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_209.typ"
#v(12pt)

#include "/content/mod21_microservices_core/lesson_210.typ"
#v(12pt)


#module_cover(
  22,
  "Hata Toleransı & Dayanıklılık (Resilience4j & Circuit Breaker)",
  "Resilience & Fault Tolerance: Circuit Breakers & Bulkheads",
  "Kaskat arızaları önleme, Circuit Breaker durum makineleri (Closed, Open, Half-Open), Bulkhead izolasyonu, Retry ve Rate Limiter.",
  "Cascade failure containment, Resilience4j state machines, thread-pool vs semaphore bulkheads, exponential backoff, and token buckets."
)

#include "/content/mod22_resilience_fault_tolerance/lesson_211.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_212.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_213.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_214.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_215.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_216.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_217.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_218.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_219.typ"
#v(12pt)

#include "/content/mod22_resilience_fault_tolerance/lesson_220.typ"
#v(12pt)


#module_cover(
  23,
  "Dağıtık İşlemler: Saga Deseni, Outbox Deseni & İdempotans",
  "Distributed Transactions: Saga Pattern, Outbox & Idempotency",
  "2-Phase Commit (2PC) darboğazları, Choreography vs Orchestration Saga, Telafi Edici İşlemler (Compensating Actions) ve Transactional Outbox.",
  "Dual-write avoidance, transactional outbox pattern with CDC/Debezium, orchestrated vs choreographed Sagas, and idempotent consumers."
)

#include "/content/mod23_distributed_transactions/lesson_221.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_222.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_223.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_224.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_225.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_226.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_227.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_228.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_229.typ"
#v(12pt)

#include "/content/mod23_distributed_transactions/lesson_230.typ"
#v(12pt)


#module_cover(
  24,
  "API Gateway Mimarisi, Yük Dengeleme & Hız Sınırlama",
  "API Gateway Architecture, Load Balancing & Rate Limiting",
  "Spring Cloud Gateway, ters vekil (Reverse Proxy), Round-Robin, Least Connections, Consistent Hashing ve Leaky Bucket hız sınırlama algoritmaları.",
  "Edge routing, filter pipelines, reverse proxies, layer-4 vs layer-7 load balancing algorithms, and distributed rate-limiting buckets."
)

#include "/content/mod24_api_gateways_lb/lesson_231.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_232.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_233.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_234.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_235.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_236.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_237.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_238.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_239.typ"
#v(12pt)

#include "/content/mod24_api_gateways_lb/lesson_240.typ"
#v(12pt)


#module_cover(
  25,
  "Gözlemlenebilirlik (Observability): Metrik, Log & Dağıtık İzleme",
  "Observability: Metrics, Structured Logging & Distributed Tracing",
  "OpenTelemetry standardı, Prometheus & Grafana ile metrik toplama, Micrometer Tracing, Zipkin/Jaeger ile W3C Trace Context yayılımı.",
  "Telemetry telemetry triad: OpenTelemetry spans, RED metrics in Prometheus, structured JSON logs with MDC, and distributed context propagation."
)

#include "/content/mod25_observability_tracing/lesson_241.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_242.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_243.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_244.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_245.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_246.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_247.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_248.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_249.typ"
#v(12pt)

#include "/content/mod25_observability_tracing/lesson_250.typ"
#v(12pt)


#module_cover(
  26,
  "Birim Test Ustalığı: TDD, JUnit 5 & Mockito Mimarisi",
  "Unit Testing Mastery: TDD, JUnit 5 & Advanced Mockito",
  "Test Güdümlü Geliştirme (TDD) kırmızı-yeşil-refactor döngüsü, parameterized testler, Mock vs Stub vs Spy, ve sahte nesnelerin doğru kullanımı.",
  "Test-driven development cycle, JUnit 5 extensions, deterministic test fixtures, argument captors, and avoiding excessive mocking traps."
)

#include "/content/mod26_unit_testing_tdd/lesson_251.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_252.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_253.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_254.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_255.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_256.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_257.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_258.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_259.typ"
#v(12pt)

#include "/content/mod26_unit_testing_tdd/lesson_260.typ"
#v(12pt)


#module_cover(
  27,
  "Entegrasyon Testleri: Spring Boot Test, Testcontainers & WireMock",
  "Integration Testing: SpringBootTest, Testcontainers & WireMock",
  "Gerçek Postgres ve Kafka konteynerleri ile test (`@Testcontainers`), MockMvc vs WebTestClient, ve üçüncü parti API'leri WireMock ile simüle etme.",
  "Spinning up real ephemeral dependencies via Testcontainers, slicing test contexts (`@WebMvcTest`), and mocking HTTP APIs with WireMock."
)

#include "/content/mod27_integration_testing/lesson_261.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_262.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_263.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_264.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_265.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_266.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_267.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_268.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_269.typ"
#v(12pt)

#include "/content/mod27_integration_testing/lesson_270.typ"
#v(12pt)


#module_cover(
  28,
  "Sözleşme Testleri (Pact) & Uçtan Uca (E2E) Test Otomasyonu",
  "Contract Testing (Pact) & End-to-End Test Automation",
  "Tüketici Güdümlü Sözleşme Testleri (Consumer-Driven Contract Testing), mikroservis sözleşme ihlallerini CI/CD'de yakalama ve Playwright E2E.",
  "Consumer-driven contracts with Pact, preventing breaking API changes pre-deployment, and deterministic end-to-end user journeys."
)

#include "/content/mod28_e2e_contract_testing/lesson_271.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_272.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_273.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_274.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_275.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_276.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_277.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_278.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_279.typ"
#v(12pt)

#include "/content/mod28_e2e_contract_testing/lesson_280.typ"
#v(12pt)


#module_cover(
  29,
  "Performans Mühendisliği: JMH, Profiling & JVM Çöp Toplama (GC)",
  "Performance Engineering: JMH Benchmarking & JVM Garbage Collection",
  "Mikro-benchmark tuzakları (JMH), CPU & Bellek profil çıkarma (Async-Profiler), ZGC ve Shenandoah ile ultra düşük gecikmeli çöp toplama.",
  "Benchmarking with JMH, avoiding JIT dead-code elimination, async-profiler flame graphs, and low-latency concurrent garbage collectors (ZGC)."
)

#include "/content/mod29_performance_jvm_tuning/lesson_281.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_282.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_283.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_284.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_285.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_286.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_287.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_288.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_289.typ"
#v(12pt)

#include "/content/mod29_performance_jvm_tuning/lesson_290.typ"
#v(12pt)


#module_cover(
  30,
  "Eşzamanlılık & Çoklu İş Parçacığı: JMM, Kilitler & Sanal İş Parçacıkları",
  "High Concurrency & Multithreading: JMM, Locks & Virtual Threads",
  "Java Bellek Modeli (JMM), `volatile` anahtar kelimesi, `ReentrantLock`, Deadlock tespiti ve çözümü, Virtual Threads altında blocking IO.",
  "Happens-before memory model semantics, compare-and-swap (CAS), deadlock detection graphs, and pin-free virtual thread concurrency."
)

#include "/content/mod30_concurrency_multithreading/lesson_291.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_292.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_293.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_294.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_295.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_296.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_297.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_298.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_299.typ"
#v(12pt)

#include "/content/mod30_concurrency_multithreading/lesson_300.typ"
#v(12pt)


#module_cover(
  31,
  "Ağ Protokolleri: TCP/IP, HTTP/2, HTTP/3, QUIC & gRPC",
  "Networking Protocols for Engineers: TCP, HTTP/2, HTTP/3 & gRPC",
  "3-Way Handshake, TCP Head-of-Line Blocking, HTTP/2 çoklama (multiplexing), UDP tabanlı QUIC protokolü ve Protocol Buffers ile yüksek hızlı gRPC.",
  "TCP congestion control windows, TLS 1.3 handshake latency, binary framing multiplexing, QUIC streams, and compact Protobuf gRPC RPCs."
)

#include "/content/mod31_networking_protocols/lesson_301.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_302.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_303.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_304.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_305.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_306.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_307.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_308.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_309.typ"
#v(12pt)

#include "/content/mod31_networking_protocols/lesson_310.typ"
#v(12pt)


#module_cover(
  32,
  "Yazılım Güvenliği Mühendisliği: OWASP Top 10 & Kriptografi",
  "Application Security Engineering: OWASP Top 10 & Cryptography",
  "SQL Injection, XSS, CSRF, SSRF açıkları ve kod seviyesinde önlemleri, TLS sertifikaları, HMAC imzalama ve güvenli parola özetleme (Argon2id).",
  "Remediating OWASP vulnerabilities in Spring, cryptographic key derivation with Argon2id, AES-GCM encryption, and safe input deserialization."
)

#include "/content/mod32_security_engineering/lesson_311.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_312.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_313.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_314.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_315.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_316.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_317.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_318.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_319.typ"
#v(12pt)

#include "/content/mod32_security_engineering/lesson_320.typ"
#v(12pt)


#module_cover(
  33,
  "CI/CD Boru Hatları & DevOps: GitOps, GitHub Actions & Sürüm Yönetimi",
  "CI/CD Pipelines & DevOps: GitOps, GitHub Actions & Releases",
  "Sürekli Entegrasyon (CI) aşamaları, Trunk-Based Development, Semantik Sürümleme (SemVer), GitHub Actions iş akışları ve Blue-Green dağıtım.",
  "Automated linting and test stages, pull request verification gates, trunk-based branching strategies, and zero-downtime release strategies."
)

#include "/content/mod33_cicd_devops/lesson_321.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_322.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_323.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_324.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_325.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_326.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_327.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_328.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_329.typ"
#v(12pt)

#include "/content/mod33_cicd_devops/lesson_330.typ"
#v(12pt)


#module_cover(
  34,
  "Konteynerleştirme: Docker, Çok Aşamalı Derleme & İmaj Güvenliği",
  "Containerization: Docker, Multi-Stage Builds & Distroless Images",
  "Docker mimarisi, Linux Cgroups ve Namespaces, Multi-stage Dockerfile ile imaj boyutunu %90 düşürme, non-root kullanıcı ve Distroless tabanlar.",
  "Linux namespaces and cgroups internals, multi-stage compilation patterns, rootless container security, and minimal attack-surface distroless bases."
)

#include "/content/mod34_docker_containers/lesson_331.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_332.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_333.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_334.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_335.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_336.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_337.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_338.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_339.typ"
#v(12pt)

#include "/content/mod34_docker_containers/lesson_340.typ"
#v(12pt)


#module_cover(
  35,
  "Kubernetes Temelleri: Pods, Services, Deployments & Yapılandırma",
  "Kubernetes Fundamentals: Pods, Services, Deployments & Config",
  "K8s kontrol düzlemi (API Server, etcd, Scheduler, Kubelet), Pod yaşam döngüsü, ClusterIP / NodePort servisleri, ConfigMap ve Secret yönetimi.",
  "Declarative reconcilers, Pod lifecycle hooks, DNS service discovery, rolling update strategies, and immutable configuration decoupling."
)

#include "/content/mod35_k8s_fundamentals/lesson_341.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_342.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_343.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_344.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_345.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_346.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_347.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_348.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_349.typ"
#v(12pt)

#include "/content/mod35_k8s_fundamentals/lesson_350.typ"
#v(12pt)


#module_cover(
  36,
  "İleri Seviye Kubernetes: Ingress, HPA, Helm, CRD & Service Mesh",
  "Advanced Kubernetes: Ingress, HPA, Operators, Helm & Service Mesh",
  "Ingress Controller yönlendirmesi, Yatay Pod Ölçekleme (HPA metrikleri), Helm paket yöneticisi, Özel Kaynak Tanımları (CRD) ve Istio Service Mesh.",
  "Layer-7 ingress routing, custom metric autoscaling (KEDA), Helm chart templating, Kubernetes Operators, and mTLS service mesh traffic splitting."
)

#include "/content/mod36_k8s_advanced/lesson_351.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_352.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_353.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_354.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_355.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_356.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_357.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_358.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_359.typ"
#v(12pt)

#include "/content/mod36_k8s_advanced/lesson_360.typ"
#v(12pt)


#module_cover(
  37,
  "Bulut Bilişim Mimarisi & 12-Factor App Prensipleri",
  "Cloud-Native Architecture & 12-Factor App Principles",
  "Bulut-yerel yazılım geliştirme, 12-Factor metodolojisi, AWS/GCP/Azure çekirdek hizmet modelleri, stateless servis tasarımı ve elastik altyapı.",
  "Architecting for elasticity, 12-factor cloud invariants, cloud-native storage patterns, stateless compute tiers, and multi-region failover."
)

#include "/content/mod37_cloud_native_architecture/lesson_361.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_362.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_363.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_364.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_365.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_366.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_367.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_368.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_369.typ"
#v(12pt)

#include "/content/mod37_cloud_native_architecture/lesson_370.typ"
#v(12pt)


#module_cover(
  38,
  "Sunucusuz (Serverless) Mimari: FaaS, Cold Starts & Olay Tetikleme",
  "Serverless Computing: FaaS, Cold Start Mitigation & Event Workflows",
  "Function-as-a-Service (FaaS) çalışma modeli, Java ile Cold Start gecikmesini SnapStart ve GraalVM Native Image ile yenme, Spring Cloud Function.",
  "Serverless scaling to zero, event-driven triggers via EventBridge, cold start mitigation using AWS SnapStart, and GraalVM AOT compilation."
)

#include "/content/mod38_serverless_computing/lesson_371.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_372.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_373.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_374.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_375.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_376.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_377.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_378.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_379.typ"
#v(12pt)

#include "/content/mod38_serverless_computing/lesson_380.typ"
#v(12pt)


#module_cover(
  39,
  "Site Reliability Engineering (SRE): SLI, SLO, SLA & Hata Bütçeleri",
  "Site Reliability Engineering (SRE): SLI, SLO, SLA & Error Budgets",
  "Hizmet seviyesi göstergeleri (SLI), hedefleri (SLO) ve sözleşmeleri (SLA), Hata Bütçesi (Error Budget) yönetimi, Olay Yönetimi ve On-Call pratikleri.",
  "SLI telemetry measurement, defining sustainable SLO targets, error budget burn rates, incident command protocols, and blameless postmortems."
)

#include "/content/mod39_sre_reliability/lesson_381.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_382.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_383.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_384.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_385.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_386.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_387.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_388.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_389.typ"
#v(12pt)

#include "/content/mod39_sre_reliability/lesson_390.typ"
#v(12pt)


#module_cover(
  40,
  "Sistem Tasarımı Mülakat Metodolojisi: Ölçekleme, Şemalar & API'ler",
  "System Design Interview Framework: Scale Estimation, APIs & Schemas",
  "MAANG sistem tasarımı mülakatlarında ilk 45 dakika formülü: Kapsam belirleme, kapasite tahminleri (QPS, Depolama), yüksek seviye mimari ve darboğazlar.",
  "The 45-minute FAANG blueprint: functional/non-functional scoping, envelope calculations, high-level component diagrams, and bottleneck mitigation."
)

#include "/content/mod40_system_design_interview/lesson_391.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_392.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_393.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_394.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_395.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_396.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_397.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_398.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_399.typ"
#v(12pt)

#include "/content/mod40_system_design_interview/lesson_400.typ"
#v(12pt)


#module_cover(
  41,
  "Büyük Veri & Gerçek Zamanlı Akış İşleme: Spark, Flink & Kafka Streams",
  "Big Data & Real-Time Stream Processing: Spark, Flink & Streams",
  "Toplu (Batch) vs Akış (Stream) işleme, Apache Flink durumlu (stateful) akış modeli, Event Time vs Processing Time, Watermark'lar ve Pencereleme.",
  "Batch vs stream semantics, stateful stream processing with Flink, event-time windowing, watermarks for out-of-order data, and Kafka Streams topologies."
)

#include "/content/mod41_big_data_streaming/lesson_401.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_402.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_403.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_404.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_405.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_406.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_407.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_408.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_409.typ"
#v(12pt)

#include "/content/mod41_big_data_streaming/lesson_410.typ"
#v(12pt)


#module_cover(
  42,
  "Arama Motoru Mimarisi: Elasticsearch, Ters İndeks & Lucene",
  "Search & Information Retrieval: Elasticsearch, Inverted Index & Lucene",
  "Ters İndeks (Inverted Index) veri yapısı, Tokenization, Stemming, TF-IDF ve BM25 sıralama algoritmaları, Elasticsearch küme ve shard mimarisi.",
  "Inverted index mechanics, analyzer tokenization filters, BM25 relevance scoring, distributed sharding, and fuzzy text retrieval."
)

#include "/content/mod42_search_information_retrieval/lesson_411.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_412.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_413.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_414.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_415.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_416.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_417.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_418.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_419.typ"
#v(12pt)

#include "/content/mod42_search_information_retrieval/lesson_420.typ"
#v(12pt)


#module_cover(
  43,
  "Yapay Zekâ Destekli Yazılım Mühendisliği & Şartname Tabanlı Üretim",
  "AI-Assisted Software Engineering & Spec-Driven Code Generation",
  "Büyük Dil Modelleri (LLM) ile kodlama, Vibe Coding riskleri, Şartname Tabanlı Geliştirme (Spec-Driven Development), AIUP ve kod üretim ajanları.",
  "Harnessing generative AI without architectural decay, spec-driven code synthesis, AI Unified Process invariants, and autonomous multi-agent pipelines."
)

#include "/content/mod43_ai_assisted_engineering/lesson_421.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_422.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_423.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_424.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_425.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_426.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_427.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_428.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_429.typ"
#v(12pt)

#include "/content/mod43_ai_assisted_engineering/lesson_430.typ"
#v(12pt)


#module_cover(
  44,
  "Spring AI & Kurumsal LLM Entegrasyonu: RAG, Vektör Veritabanları",
  "Spring AI & Enterprise LLM Applications: RAG, Vector Stores & Tools",
  "Spring AI framework'ü, OpenAI API entegrasyonu, Vektör Veritabanları (PgVector, Milvus), Retrieval-Augmented Generation (RAG) ve Tool Calling.",
  "Spring AI abstractions, vector embeddings, cosine similarity searches in PgVector, deterministic RAG pipelines, and agentic tool invocation."
)

#include "/content/mod44_spring_ai_llm/lesson_431.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_432.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_433.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_434.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_435.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_436.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_437.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_438.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_439.typ"
#v(12pt)

#include "/content/mod44_spring_ai_llm/lesson_440.typ"
#v(12pt)


#module_cover(
  45,
  "Miras Sistem Modernizasyonu: Strangler Fig Deseni & ACL",
  "Legacy Modernization & Refactoring: Strangler Fig & ACL",
  "Eski monolitleri risksiz modernize etme, Strangler Fig (Boğucu İncir) deseni, Anti-Corruption Layer (ACL), Branch by Abstraction ve veri senkronizasyonu.",
  "Zero-risk monolith strangulation, anti-corruption translation layers, branch-by-abstraction patterns, and dual-write data migration pipelines."
)

#include "/content/mod45_refactoring_legacy/lesson_441.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_442.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_443.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_444.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_445.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_446.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_447.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_448.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_449.typ"
#v(12pt)

#include "/content/mod45_refactoring_legacy/lesson_450.typ"
#v(12pt)


#module_cover(
  46,
  "Kod İnceleme Sanatı & Mühendislik Kültürü: RFC, ADR & Postmortem",
  "Code Review Excellence & Engineering Culture: RFCs, ADRs & Postmortems",
  "Etkili PR inceleme ilkeleri, Mimari Karar Kayıtları (ADR), Yorum İsteme (RFC) süreçleri, Suçlamasız Olay İncelemeleri (Blameless Postmortems).",
  "Code review craftsmanship, drafting Architecture Decision Records (ADRs), driving organizational consensus via RFCs, and root-cause postmortems."
)

#include "/content/mod46_code_reviews_engineering_culture/lesson_451.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_452.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_453.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_454.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_455.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_456.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_457.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_458.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_459.typ"
#v(12pt)

#include "/content/mod46_code_reviews_engineering_culture/lesson_460.typ"
#v(12pt)


#module_cover(
  47,
  "Teknik Borç Yönetimi & Mimari Uygunluk Fonksiyonları",
  "Technical Debt Governance & Architecture Fitness Functions",
  "Teknik borcun faizi, ArchUnit ile mimari kuralları test etme (Fitness Functions), Statik kod analizi (SonarQube) ve kalite kapıları.",
  "Quantifying technical debt velocity penalties, automated architecture fitness functions using ArchUnit, and CI quality gates."
)

#include "/content/mod47_technical_debt_governance/lesson_461.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_462.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_463.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_464.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_465.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_466.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_467.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_468.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_469.typ"
#v(12pt)

#include "/content/mod47_technical_debt_governance/lesson_470.typ"
#v(12pt)


#module_cover(
  48,
  "Ölçeklenebilirlik & Kaos Mühendisliği: Hata Enjeksiyonu & Dayanıklılık",
  "Scalability & Chaos Engineering: Fault Injection & Disaster Recovery",
  "Kaos Mühendisliği prensipleri, Netflix Chaos Monkey, arıza enjeksiyonu, Felaket Kurtarma (Disaster Recovery - RTO/RPO) ve Çok Bölgeli Mimari.",
  "Empirical hypothesis verification under chaos, latency and network partition fault injections, RTO/RPO business metrics, and multi-region disaster readiness."
)

#include "/content/mod48_scalability_chaos_engineering/lesson_471.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_472.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_473.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_474.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_475.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_476.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_477.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_478.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_479.typ"
#v(12pt)

#include "/content/mod48_scalability_chaos_engineering/lesson_480.typ"
#v(12pt)


#module_cover(
  49,
  "Staff+ Mühendislik Liderliği: Teknik Strateji, Etki & Mentorluk",
  "Staff+ Engineering Leadership: Technical Strategy & Organizational Vision",
  "Staff, Principal ve Distinguished mühendislik rolleri, organizasyonel etki, şirket çapında teknoloji stratejisi belirleme ve mentorluk.",
  "Archetypes of Staff+ engineers (Architect, Tech Lead, Solver, Right Hand), driving multi-quarter technical roadmaps, and executive influence."
)

#include "/content/mod49_staff_plus_leadership/lesson_481.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_482.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_483.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_484.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_485.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_486.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_487.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_488.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_489.typ"
#v(12pt)

#include "/content/mod49_staff_plus_leadership/lesson_490.typ"
#v(12pt)


#module_cover(
  50,
  "MAANG Davranışsal & Bar Raiser Mülakat Ustalığı: STAR Metodu & Liderlik",
  "MAANG Behavioral & Bar Raiser Interview Mastery: STAR Method & Culture",
  "Amazon Liderlik İlkeleri, Google Googliness, Meta Move Fast kültürü, STAR metodu ile etkileyici hikâye anlatımı ve kritik mimari ödünleşimler (Trade-Offs).",
  "Mastering FAANG behavioral loops, structural STAR framework execution, demonstrating architectural ownership, and navigating Bar Raiser challenges."
)

#include "/content/mod50_maang_bar_raiser/lesson_491.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_492.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_493.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_494.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_495.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_496.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_497.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_498.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_499.typ"
#v(12pt)

#include "/content/mod50_maang_bar_raiser/lesson_500.typ"
#v(12pt)


#pagebreak()
#v(40pt)
#align(center)[
  #rect(fill: rgb("030712"), radius: 10pt, inset: (x: 24pt, y: 32pt), width: 90%)[
    #text(size: 24pt, fill: rgb("818cf8"), weight: "bold")[🎓 TEBRİKLER! / CONGRATULATIONS!]    #v(10pt)
    #text(size: 14pt, fill: white)[500 Derslik MAANG Yazılım Mühendisliği Yolculuğunu Başarıyla Tamamladınız!]    #v(6pt)
    #text(size: 11pt, fill: rgb("94a3b8"))[You have successfully conquered all 500 lessons of the MAANG Software Engineering Masterclass!]    #v(20pt)
    #line(length: 60%, stroke: 1pt + rgb("4f46e5"))
    #v(15pt)
    #text(size: 10pt, fill: rgb("cbd5e1"))[
      Clean Code • Hexagonal Architecture • Java 25 LTS & Spring Boot • Staff+ Distributed Systems
    ]
  ]
]
