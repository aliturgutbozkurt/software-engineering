package com.maang.se.patterns;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * MAANG SOFTWARE ENGINEERING - DYNAMIC STRATEGY PATTERN & SPRING DI
 * Demonstrates:
 *   - Open/Closed Principle (OCP)
 *   - Java 25 Pattern Matching & Sealed Hierarchies
 *   - Spring Service Registry simulation
 */
public class DynamicStrategyEngine {

    public enum PaymentChannel { CREDIT_CARD, CRYPTO, APPLE_PAY, BANK_TRANSFER }

    public record PaymentContext(String customerId, double amount, PaymentChannel channel) {}

    public sealed interface PaymentStrategy permits 
        CreditCardStrategy, CryptoStrategy, ApplePayStrategy, BankTransferStrategy {
        PaymentChannel channel();
        boolean processPayment(PaymentContext context);
    }

    public static final class CreditCardStrategy implements PaymentStrategy {
        public PaymentChannel channel() { return PaymentChannel.CREDIT_CARD; }
        public boolean processPayment(PaymentContext ctx) {
            System.out.println("💳 [Kredi Kartı] " + ctx.amount() + " TL 3D Secure ile tahsil edildi.");
            return true;
        }
    }

    public static final class CryptoStrategy implements PaymentStrategy {
        public PaymentChannel channel() { return PaymentChannel.CRYPTO; }
        public boolean processPayment(PaymentContext ctx) {
            System.out.println("⛓️ [Kripto/USDT] " + ctx.amount() + " TL blokzincir ağına iletildi.");
            return true;
        }
    }

    public static final class ApplePayStrategy implements PaymentStrategy {
        public PaymentChannel channel() { return PaymentChannel.APPLE_PAY; }
        public boolean processPayment(PaymentContext ctx) {
            System.out.println("🍏 [Apple Pay] " + ctx.amount() + " TL biyometrik onay ile ödendi.");
            return true;
        }
    }

    public static final class BankTransferStrategy implements PaymentStrategy {
        public PaymentChannel channel() { return PaymentChannel.BANK_TRANSFER; }
        public boolean processPayment(PaymentContext ctx) {
            System.out.println("🏦 [Havale/EFT] " + ctx.amount() + " TL banka hesabına aktarıldı.");
            return true;
        }
    }

    // Spring Boot Map<String, PaymentStrategy> Enjeksiyonunun Java Karşılığı
    public static class PaymentGatewayService {
        private final Map<PaymentChannel, PaymentStrategy> strategies = new ConcurrentHashMap<>();

        public void registerStrategy(PaymentStrategy strategy) {
            strategies.put(strategy.channel(), strategy);
        }

        public boolean executePayment(PaymentContext context) {
            PaymentStrategy strategy = strategies.get(context.channel());
            if (strategy == null) {
                throw new UnsupportedOperationException("Desteklenmeyen ödeme kanalı: " + context.channel());
            }
            return strategy.processPayment(context);
        }
    }

    public static void main(String[] args) {
        System.out.println("🚀 Dinamik Strateji Motoru (Strategy Pattern) Çalıştırılıyor...\n");

        var gateway = new PaymentGatewayService();
        gateway.registerStrategy(new CreditCardStrategy());
        gateway.registerStrategy(new CryptoStrategy());
        gateway.registerStrategy(new ApplePayStrategy());
        gateway.registerStrategy(new BankTransferStrategy());

        gateway.executePayment(new PaymentContext("CUST-1", 1250.00, PaymentChannel.CREDIT_CARD));
        gateway.executePayment(new PaymentContext("CUST-2", 4500.00, PaymentChannel.APPLE_PAY));
        gateway.executePayment(new PaymentContext("CUST-3", 10000.00, PaymentChannel.CRYPTO));

        System.out.println("\n✅ OCP ve Strategy Kalıbı Başarıyla Doğrulandı!");
    }
}
