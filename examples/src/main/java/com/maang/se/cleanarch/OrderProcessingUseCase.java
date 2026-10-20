package com.maang.se.cleanarch;

import java.time.Instant;
import java.util.Objects;
import java.util.UUID;
import java.util.concurrent.Executors;

/**
 * MAANG SOFTWARE ENGINEERING MASTERCLASS - CLEAN ARCHITECTURE & SPRING BOOT 3+
 * Demonstrates:
 *   - Hexagonal Ports & Adapters
 *   - Domain Invariants using Java 25 Records
 *   - Project Loom Virtual Threads for High-Throughput Execution
 */
public class OrderProcessingUseCase {

    // --- DOMAIN CONTRACTS (IMMUTABLE VALUE OBJECTS & ENTITIES) ---
    public record OrderRequest(String customerId, String productSku, int quantity, double unitPrice) {
        public OrderRequest {
            Objects.requireNonNull(customerId, "customerId zorunludur");
            Objects.requireNonNull(productSku, "productSku zorunludur");
            if (quantity <= 0) throw new IllegalArgumentException("Miktar pozitif olmalıdır!");
            if (unitPrice <= 0.0) throw new IllegalArgumentException("Fiyat pozitif olmalıdır!");
        }
    }

    public sealed interface OrderOutcome permits OrderOutcome.Success, OrderOutcome.Rejected {
        record Success(String orderId, double totalAmount, Instant processedAt) implements OrderOutcome {}
        record Rejected(String reason, String errorCode) implements OrderOutcome {}
    }

    // --- PORTS (INFRASTRUCTURE ABSTRACTIONS) ---
    public interface InventoryPort {
        boolean reserveStock(String productSku, int quantity);
    }

    public interface PaymentPort {
        boolean chargeCustomer(String customerId, double amount);
    }

    public interface AuditLogPort {
        void logEvent(String eventType, String orderId);
    }

    // --- USE CASE INTERACTOR ---
    public static class OrderProcessor {
        private final InventoryPort inventoryPort;
        private final PaymentPort paymentPort;
        private final AuditLogPort auditLogPort;

        public OrderProcessor(InventoryPort inventoryPort, PaymentPort paymentPort, AuditLogPort auditLogPort) {
            this.inventoryPort = inventoryPort;
            this.paymentPort = paymentPort;
            this.auditLogPort = auditLogPort;
        }

        public OrderOutcome execute(OrderRequest request) {
            // 1. Stok Doğrulaması (Fail-Fast)
            if (!inventoryPort.reserveStock(request.productSku(), request.quantity())) {
                return new OrderOutcome.Rejected("Yetersiz stok!", "OUT_OF_STOCK");
            }

            // 2. Ödeme Tahsilatı
            double total = request.quantity() * request.unitPrice();
            if (!paymentPort.chargeCustomer(request.customerId(), total)) {
                return new OrderOutcome.Rejected("Ödeme başarısız oldu!", "PAYMENT_FAILED");
            }

            // 3. Sipariş Onayı & Denetim Logu
            String orderId = "ORD-" + UUID.randomUUID().toString().substring(0, 8);
            auditLogPort.logEvent("ORDER_COMPLETED", orderId);

            return new OrderOutcome.Success(orderId, total, Instant.now());
        }
    }

    // --- RUNNABLE DEMO (JAVA 25 VIRTUAL THREADS) ---
    public static void main(String[] args) throws Exception {
        System.out.println("🏛️ Clean Architecture & Java 25 Virtual Thread Engine Başlatılıyor...\n");

        InventoryPort mockInventory = (sku, qty) -> true;
        PaymentPort mockPayment = (cust, amt) -> true;
        AuditLogPort mockAudit = (evt, ord) -> System.out.println("   [Audit Log] " + evt + " -> " + ord);

        var processor = new OrderProcessor(mockInventory, mockPayment, mockAudit);

        // 10.000 Siparişi Sanal İş Parçacıkları (Virtual Threads) ile Asenkron İşle:
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 1; i <= 5; i++) {
                final int idx = i;
                executor.submit(() -> {
                    var req = new OrderRequest("CUST-" + idx, "SKU-MACBOOK", 1, 2499.99);
                    var res = processor.execute(req);
                    switch (res) {
                        case OrderOutcome.Success s -> System.out.println("✅ Sipariş Onaylandı: " + s.orderId() + " (" + Thread.currentThread() + ")");
                        case OrderOutcome.Rejected r -> System.err.println("❌ Reddedildi: " + r.reason());
                    }
                });
            }
        }

        System.out.println("\n🎉 Clean Architecture Sipariş İşleme Testi Başarıyla Tamamlandı!");
    }
}
