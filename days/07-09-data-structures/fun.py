
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def main():
    get_all_jeeps(cars)
    get_first_model_each_manufacturer(cars)
    get_all_matching_models(cars)
    sort_car_models(cars)


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    models = []
    for car in cars["Jeep"]:
        models.append(car)
    return (", ".join(models))


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model = []
    for key in cars.keys():
        first_model.append(cars[key][0])
    return first_model


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    is_it_in = []
    for k, v in cars.items():
        for x in v:
            if grep.lower() in x.lower():
                is_it_in.append(x)
    is_it_in.sort()
    return is_it_in


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted = cars.copy()
    for k, v in sorted.items():
        v = v.sort()
    return sorted


if __name__ == '__main__':
    main()
