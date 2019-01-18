''' Must put all desired active modules inside this file
use help(leet) to print options
 '''

# Can import them from another file
from .text import joke2
#import .plottr
from .plottr import *
#import .plottr

# declare them here
def joke():
    print('Printing joke1')
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')

# or put properties in addition to methods
test_property = 'foo'

