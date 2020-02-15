import medium


medium.set('speed', 0)


@medium.subscribe('speed')
def speedUpdated(value):
    print('speed =', value)


medium.listen('0.0.0.0', 5000)
