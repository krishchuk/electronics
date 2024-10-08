from django.core.exceptions import ValidationError


def validate_provider(habit):
    if habit['nice_habit'] and habit['gift']:
        raise ValidationError("Нельзя одновременно выбирать связанную привычку и вознаграждение.")

    if habit['action_time'] > 120:
        raise ValidationError("Время на выполнение не должно превышать 120 секунд.")

    if habit['nice_habit'] and not habit['nice_habit'].is_nice:
        raise ValidationError("Связанная привычка должна быть приятной.")

    if habit['is_nice']:
        if habit['gift']:
            raise ValidationError("У приятной привычки не может быть вознаграждения.")
        if habit['nice_habit']:
            raise ValidationError("У приятной привычки не может быть связанной привычки.")
