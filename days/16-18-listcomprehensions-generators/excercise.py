
def main():
    NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
             'julian sequeira', 'sandra bullock', 'keanu reeves',
             'julbob pybites', 'bob belderbos', 'julian sequeira',
             'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

    title_names = [name.title() for name in NAMES]
    print(title_names)

    print([reverse(name) for name in NAMES])

    pairs = gen_pairs()
    for _ in range(10):
        next(pairs)

def reverse(name):
    first, last = name.split()
    return f"{last} {first}"


def title_gen(NAMES):
    pass

if __name__ == '__main__':
    main()