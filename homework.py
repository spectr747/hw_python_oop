"""Документация модуля. Описывает работу классов и функций."""


from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

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


@dataclass
class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000

    action: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = (self.action * self.LEN_STEP) / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.get_distance() / self.duration
        return speed

    try:
        def get_spent_calories(self) -> float:
            """Получить количество затраченных калорий."""
            pass
    except NotImplementedError:
        print('Требуется выполнить функцию.')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info_message = InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )
        return info_message


@dataclass
class Running(Training):
    """Тренировка: бег."""
    COEFF_CALORIE_1 = 18
    COEFF_CALORIE_2 = 20
    MIN_IN_HOUR = 60

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = (
            (self.COEFF_CALORIE_1
                * self.get_mean_speed() - self.COEFF_CALORIE_2)
            * self.weight / self.M_IN_KM
            * self.duration * self.MIN_IN_HOUR
        )
        return calories


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEFF_CALORIE_1 = 0.035
    COEFF_CALORIE_2 = 0.029
    MIN_IN_HOUR = 60

    action: int
    duration: float
    weight: float
    height: float

    def get_spent_calories(self) -> float:

        calories = (
            (self.COEFF_CALORIE_1 * self.weight
                + (self.get_mean_speed()**2 // self.height)
                * self.COEFF_CALORIE_2 * self.weight)
            * self.duration * self.MIN_IN_HOUR
        )
        return calories


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    COEFF_CALORIE_3 = 1.1

    action: int
    duration: float
    weight: float
    length_pool: float
    count_pool: int

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = (
            ((self.length_pool * self.count_pool)
                / self.M_IN_KM) / self.duration
        )
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = (
            (self.get_mean_speed() + self.COEFF_CALORIE_3)
            * 2 * self.weight
        )
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict_classes = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }

    if workout_type not in dict_classes.keys():
        raise IndexError('Не верно указан тип активности.')
    else:
        class_name = dict_classes[workout_type](*data)
        return class_name


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info().get_message()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
