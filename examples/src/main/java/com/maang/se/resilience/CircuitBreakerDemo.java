package com.maang.se.resilience;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * MAANG SOFTWARE ENGINEERING - CIRCUIT BREAKER & FAULT TOLERANCE
 * Simulates Resilience4j State Machine:
 *   - CLOSED: Normal operation
 *   - OPEN: Tripped due to failure threshold (Fast-fail without hitting downstream)
 *   - HALF-OPEN: Testing recovery with trial calls
 */
public class CircuitBreakerDemo {

    public enum State { CLOSED, OPEN, HALF_OPEN }

    public static class SimpleCircuitBreaker {
        private State state = State.CLOSED;
        private final int failureThreshold = 3;
        private final AtomicInteger failureCount = new AtomicInteger(0);
        private long lastStateChange = System.currentTimeMillis();
        private final long resetTimeoutMs = 1000; // 1 saniye sonra half-open'a geç

        public synchronized String execute(java.util.function.Supplier<String> action, java.util.function.Supplier<String> fallback) {
            long now = System.currentTimeMillis();
            if (state == State.OPEN && (now - lastStateChange > resetTimeoutMs)) {
                state = State.HALF_OPEN;
                System.out.println("⚠️ [Circuit Breaker] Durum HALF-OPEN'a geçti. Deneme çağrısı yapılıyor...");
            }

            if (state == State.OPEN) {
                System.out.println("🛑 [Circuit Breaker: OPEN] Hızlı Hata (Fast-Fail) -> Fallback dönülüyor!");
                return fallback.get();
            }

            try {
                String result = action.get();
                if (state == State.HALF_OPEN) {
                    state = State.CLOSED;
                    failureCount.set(0);
                    System.out.println("✅ [Circuit Breaker] Servis düzeldi! Durum CLOSED'a döndü.");
                }
                return result;
            } catch (Exception e) {
                int failures = failureCount.incrementAndGet();
                System.err.println("❌ Hata tespit edildi (" + failures + "/" + failureThreshold + "): " + e.getMessage());
                if (failures >= failureThreshold) {
                    state = State.OPEN;
                    lastStateChange = System.currentTimeMillis();
                    System.err.println("🚨 [Circuit Breaker] Hata eşiği aşıldı! Durum OPEN oldu.");
                }
                return fallback.get();
            }
        }
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("🛡️ Resilience & Circuit Breaker Simülasyonu Başlatılıyor...\n");

        var cb = new SimpleCircuitBreaker();
        AtomicInteger callCount = new AtomicInteger(0);

        // 1. Simüle Edilen Dış Servis (İlk 3 çağrıda hata verir, sonra düzelir)
        java.util.function.Supplier<String> flakyService = () -> {
            int c = callCount.incrementAndGet();
            if (c <= 3) {
                throw new RuntimeException("HTTP 503 Service Unavailable");
            }
            return "SUCCESS::Payload from Upstream Server (Call #" + c + ")";
        };

        java.util.function.Supplier<String> fallback = () -> "FALLBACK::Önbellekten yedek veri sunuldu.";

        // Çağrı dizisi:
        for (int i = 1; i <= 6; i++) {
            System.out.println("\n--- Çağrı #" + i + " ---");
            String response = cb.execute(flakyService, fallback);
            System.out.println("Dönen Yanıt: " + response);
            if (i == 4) {
                System.out.println("⏳ 1.2 saniye bekleniyor (Reset timeout)...");
                Thread.sleep(1200);
            }
        }

        System.out.println("\n🎉 Circuit Breaker Dayanıklılık Testi Başarıyla Tamamlandı!");
    }
}
