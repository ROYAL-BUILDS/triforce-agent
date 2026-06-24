from core.market_scanner import detect_market_condition
from strategy.trend_mode import trend_trade
from strategy.momentum_mode import momentum_trade
from strategy.mean_reversion import mean_reversion_trade
from core.risk_manager import RiskManager


def run_triforce():
    print("🚀 TriForce Agent Started...\n")

    risk = RiskManager()
    condition = detect_market_condition()

    print(f"Market Condition: {condition}\n")

    if condition == "trend":
        trade = trend_trade()

    elif condition == "momentum":
        trade = momentum_trade()

    elif condition == "range":
        trade = mean_reversion_trade()

    else:
        print("No trade condition met.")
        return

    risk_status = risk.check_risk()

    print("\nTrade Decision:")
    print(trade)
    print(f"Risk Mode: {risk_status}")


if __name__ == "__main__":
    run_triforce()
