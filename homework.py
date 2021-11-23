class InfoMessage:
    """Информационное сообщение о тренировке."""
    
    def __init__(self,
                training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float,
                ) -> None:
        self.training_type  = training_type
        self.duration       = duration
        self.distance       = distance
        self.speed          = speed
        self.calories       = calories

    def get_message(self) -> str:
        """Содержание сообщения."""

        message = (
                    f'Тип тренировки: {self.training_type}; '
                    f'Длительность: {self.duration:.3f} ч.; '
                    f'Дистанция: {self.distance:.3f} км; '
                    f'Ср. скорость: {self.speed:.3f} км/ч; '
                    f'Потрачено ккал: {self.calories:.3f}.'
        )
        return message


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
    
    coeff_calorie_1         = 0.035
    coeff_calorie_2         = 0.029
    MIN_IN_HOUR             = 60

    def __init__(self,
                action: int,
                duration: float,
                weight: float,
                height: float,
                ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        
        calories = (
            (self.coeff_calorie_1 * self.weight
            + (self.get_mean_speed()**2 // self.height)
            * self.coeff_calorie_2 * self.weight) 
            * self.duration * self.MIN_IN_HOUR
        )
        return calories


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

