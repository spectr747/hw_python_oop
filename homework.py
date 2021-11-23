class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    LEN_STEP                = 0.65
    M_IN_KM                 = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action         = action
        self.duration       = duration
        self.weight         = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        
        distance = (self.action * self.LEN_STEP) / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        
        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        
        info_message = InfoMessage(
            self.__class__.__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )
        return info_message


class Running(Training):
    """Тренировка: бег."""
    
    coeff_calorie_1         = 18
    coeff_calorie_2         = 20
    MIN_IN_HOUR             = 60

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        
        calories = (
            (self.coeff_calorie_1 * self.get_mean_speed() - self.coeff_calorie_2)
            * self.weight / self.M_IN_KM * self.duration * self.MIN_IN_HOUR
        )
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

