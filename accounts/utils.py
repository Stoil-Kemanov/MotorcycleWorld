from django import template

from common.choices import ExperienceLevel, MotorcycleType, RidingStyle, BodyType
from motorcycles.models import Motorcycle
from clothing.models import Clothing


def calculate_motorcycle_score(motorcycle, user_profile):
    score = 0
    max_score = 100

    if user_profile.riding_style and motorcycle.type:
        user_style = user_profile.riding_style
        bike_type = motorcycle.type

        if user_style == bike_type:
            score += 30

        elif user_style == RidingStyle.SPORT:
            if bike_type == MotorcycleType.TOURING:
                score += 20
            elif bike_type == MotorcycleType.OTHER:
                score += 15

        elif user_style == RidingStyle.TOURING:
            if bike_type == MotorcycleType.SPORT:
                score += 15
            elif bike_type == MotorcycleType.OFF_ROAD:
                score += 18
            elif bike_type == MotorcycleType.CRUISER:
                score += 22
            elif bike_type == MotorcycleType.OTHER:
                score += 20

        elif user_style == RidingStyle.CRUISER:
            if bike_type == MotorcycleType.TOURING:
                score += 25
            elif bike_type == MotorcycleType.OTHER:
                score += 18

        elif user_style == RidingStyle.OFF_ROAD:
            if bike_type == MotorcycleType.OTHER:
                score += 22
            elif bike_type == MotorcycleType.TOURING:
                score += 12

        else:
            if user_style == RidingStyle.SPORT and bike_type in [MotorcycleType.CRUISER, MotorcycleType.OFF_ROAD]:
                score += 5
            elif user_style == RidingStyle.CRUISER and bike_type in [MotorcycleType.SPORT, MotorcycleType.OFF_ROAD]:
                score += 8
            elif user_style == RidingStyle.OFF_ROAD and bike_type in [MotorcycleType.SPORT, MotorcycleType.CRUISER]:
                score += 10

    if user_profile.experience and motorcycle.engine_volume:
        exp = user_profile.experience
        cc = motorcycle.engine_volume

        if exp == ExperienceLevel.BEGINNER:
            if 125 <= cc <= 300:
                score += 25
            elif 301 <= cc <= 500:
                score += 22
            elif 501 <= cc <= 650:
                score += 15
            elif 651 <= cc <= 800:
                score += 8
            elif cc > 800:
                score += 3
            elif cc < 125:
                score += 18

        elif exp == ExperienceLevel.INTERMEDIATE:
            if 300 <= cc <= 600:
                score += 25
            elif 601 <= cc <= 1000:
                score += 23
            elif 1001 <= cc <= 1200:
                score += 18
            elif 200 <= cc <= 299:
                score += 15
            elif cc > 1200:
                score += 12
            elif cc < 200:
                score += 8

        elif exp == ExperienceLevel.ADVANCED:
            if cc >= 1000:
                score += 25
            elif 800 <= cc <= 999:
                score += 23
            elif 600 <= cc <= 799:
                score += 18
            elif 400 <= cc <= 599:
                score += 12
            elif cc < 400:
                score += 8

    if user_profile.body_type and motorcycle.type:
        body = user_profile.body_type
        bike_type = motorcycle.type

        if body == BodyType.SLIM:
            if bike_type == MotorcycleType.SPORT:
                score += 20
            elif bike_type == MotorcycleType.OFF_ROAD:
                score += 18
            elif bike_type == MotorcycleType.OTHER:
                score += 16
            elif bike_type == MotorcycleType.TOURING:
                score += 12
            elif bike_type == MotorcycleType.CRUISER:
                score += 10

        elif body == BodyType.ATHLETIC:
            if bike_type in [MotorcycleType.SPORT, MotorcycleType.TOURING, MotorcycleType.OFF_ROAD]:
                score += 20
            elif bike_type == MotorcycleType.OTHER:
                score += 18
            elif bike_type == MotorcycleType.CRUISER:
                score += 16

        elif body == BodyType.CHUBBY:
            if bike_type == MotorcycleType.CRUISER:
                score += 20
            elif bike_type == MotorcycleType.TOURING:
                score += 18
            elif bike_type == MotorcycleType.OTHER:
                score += 14
            elif bike_type == MotorcycleType.OFF_ROAD:
                score += 10
            elif bike_type == MotorcycleType.SPORT:
                score += 8

    if user_profile.experience and motorcycle.engine_power:
        exp = user_profile.experience
        hp = motorcycle.engine_power

        if exp == ExperienceLevel.BEGINNER:
            if 15 <= hp <= 35:
                score += 15
            elif 36 <= hp <= 50:
                score += 12
            elif 51 <= hp <= 70:
                score += 8
            elif 71 <= hp <= 90:
                score += 4
            elif hp > 90:
                score += 2
            elif hp < 15:
                score += 10

        elif exp == ExperienceLevel.INTERMEDIATE:
            if 40 <= hp <= 80:
                score += 15
            elif 81 <= hp <= 120:
                score += 13
            elif 121 <= hp <= 150:
                score += 10
            elif 25 <= hp <= 39:
                score += 8
            elif hp > 150:
                score += 6

        elif exp == ExperienceLevel.ADVANCED:
            if hp >= 100:
                score += 15
            elif 80 <= hp <= 99:
                score += 12
            elif 60 <= hp <= 79:
                score += 8
            elif hp < 60:
                score += 5

    if user_profile.height:
        height = user_profile.height
        bike_type = motorcycle.type

        if height < 165:
            if bike_type == MotorcycleType.CRUISER:
                score += 10
            elif bike_type == MotorcycleType.SPORT:
                score += 8
            elif bike_type == MotorcycleType.OTHER:
                score += 7
            elif bike_type in [MotorcycleType.TOURING, MotorcycleType.OFF_ROAD]:
                score += 5

        elif 165 <= height <= 180:
            score += 10

        elif height > 180:
            if bike_type in [MotorcycleType.TOURING, MotorcycleType.OFF_ROAD]:
                score += 10
            elif bike_type == MotorcycleType.OTHER:
                score += 8
            elif bike_type == MotorcycleType.SPORT:
                score += 6
            elif bike_type == MotorcycleType.CRUISER:
                score += 7

    percentage_score = (score / max_score) * 100
    return round(percentage_score, 1)


def calculate_clothing_score(clothing, user_profile):
    score = 0
    max_score = 100

    if user_profile.riding_style and clothing.style:
        user_style = user_profile.riding_style
        clothing_style = clothing.style

        if user_style == clothing_style:
            score += 40
        elif user_style == RidingStyle.SPORT:
            if clothing_style == RidingStyle.TOURING:
                score += 30
            elif clothing_style == RidingStyle.OFF_ROAD:
                score += 20
            elif clothing_style == RidingStyle.CRUISER:
                score += 15
        elif user_style == RidingStyle.TOURING:
            if clothing_style == RidingStyle.CRUISER:
                score += 32
            elif clothing_style == RidingStyle.SPORT:
                score += 28
            elif clothing_style == RidingStyle.OFF_ROAD:
                score += 25
        elif user_style == RidingStyle.CRUISER:
            if clothing_style == RidingStyle.TOURING:
                score += 35
            elif clothing_style == RidingStyle.SPORT:
                score += 18
            elif clothing_style == RidingStyle.OFF_ROAD:
                score += 15
        elif user_style == RidingStyle.OFF_ROAD:
            if clothing_style == RidingStyle.TOURING:
                score += 30
            elif clothing_style == RidingStyle.SPORT:
                score += 22
            elif clothing_style == RidingStyle.CRUISER:
                score += 12

    if user_profile.body_type and clothing.fit:
        body = user_profile.body_type
        fit = clothing.fit

        if body == fit:
            score += 35
        elif body == BodyType.ATHLETIC:
            if fit == BodyType.CHUBBY:
                score += 30
            elif fit == BodyType.SLIM:
                score += 25
        elif body == BodyType.SLIM:
            if fit == BodyType.ATHLETIC:
                score += 28
            elif fit == BodyType.CHUBBY:
                score += 22
        elif body == BodyType.CHUBBY:
            if fit == BodyType.ATHLETIC:
                score += 27
            elif fit == BodyType.SLIM:
                score += 20

    if user_profile.height and user_profile.weight:
        height = user_profile.height
        bmi = user_profile.weight / ((height / 100) ** 2)

        if height < 165:
            if clothing.fit == BodyType.CHUBBY:
                score += 15
            elif clothing.fit == BodyType.SLIM:
                score += 13
            elif clothing.fit == BodyType.ATHLETIC:
                score += 12
        elif 165 <= height <= 180:
            score += 15
        elif height > 180:
            if clothing.fit == BodyType.ATHLETIC:
                score += 15
            elif clothing.fit == BodyType.CHUBBY:
                score += 13
            elif clothing.fit == BodyType.SLIM:
                score += 10

        if bmi < 20:
            if clothing.fit == BodyType.SLIM:
                score += 10
            elif clothing.fit == BodyType.ATHLETIC:
                score += 8
            elif clothing.fit == BodyType.CHUBBY:
                score += 6
        elif 20 <= bmi <= 25:
            if clothing.fit == BodyType.ATHLETIC:
                score += 10
            elif clothing.fit in [BodyType.SLIM, BodyType.CHUBBY]:
                score += 9
        elif bmi > 25:
            if clothing.fit == BodyType.CHUBBY:
                score += 10
            elif clothing.fit == BodyType.ATHLETIC:
                score += 7
            elif clothing.fit == BodyType.SLIM:
                score += 4

    percentage_score = (score / max_score) * 100
    return round(percentage_score, 1)


def recommend_motorcycles(user_profile, limit=6):

    motorcycles = Motorcycle.objects.all()
    recommendations = []

    for motorcycle in motorcycles:
        score = calculate_motorcycle_score(motorcycle, user_profile)
        if score > 0:
            recommendations.append({
                'motorcycle': motorcycle,
                'score': score,
                'compatibility': get_compatibility_text(score)
            })

    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations[:limit]


def recommend_clothing(user_profile, limit=6):

    clothing_items = Clothing.objects.all()
    recommendations = []

    for clothing in clothing_items:
        score = calculate_clothing_score(clothing, user_profile)
        if score > 0:
            recommendations.append({
                'clothing': clothing,
                'score': score,
                'compatibility': get_compatibility_text(score)
            })

    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations[:limit]


def get_compatibility_text(score):

    if score >= 80:
        return "Excellent Match"
    elif score >= 65:
        return "Great Match"
    elif score >= 50:
        return "Good Match"
    elif score >= 35:
        return "Fair Match"
    else:
        return "Poor Match"


def get_compatibility_color(score):

    if score >= 80:
        return "success"
    elif score >= 65:
        return "info"
    elif score >= 50:
        return "primary"
    elif score >= 35:
        return "warning"
    else:
        return "danger"

register = template.Library()

@register.filter
def compatibility_color_filter(score):

    try:
        return get_compatibility_color(float(score))
    except (ValueError, TypeError):
        return "secondary"
