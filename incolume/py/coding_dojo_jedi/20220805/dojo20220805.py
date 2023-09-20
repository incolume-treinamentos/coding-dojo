"""Dojo 2022-08-05."""


def bmi0(peso: float, alt: float) -> str:
    """Calcula o indice de massa corporal."""
    imc = peso / alt**2
    if imc <= 18.5:
        return 'Underweight'
    elif imc <= 25.0:
        return 'Normal'
    elif imc <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'


def bmi(peso: float, alt: float) -> str:
    """Calcula o indice de massa corporal."""
    imc = peso / alt**2
    return ['Obese', 'Overweight', 'Normal', 'Underweight'][
        (imc <= 18.5) + (imc <= 25) + (imc <= 30)
    ]
