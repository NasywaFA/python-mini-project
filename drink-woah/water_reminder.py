from plyer import notification
import time

while True:
    notification.notify(
        title="💧 Drink Water",
        message="Mate, waktunya minum dulu!",
        timeout=10
    )

    time.sleep(3600)  # 1 jam