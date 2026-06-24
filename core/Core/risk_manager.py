class RiskManager:
    def __init__(self):
        self.loss_streak = 0
        self.max_daily_loss = 0.05

    def check_risk(self):
        if self.loss_streak >= 3:
            print("⚠️ Reducing position size (loss streak)")
            return "reduced"

        return "normal"
