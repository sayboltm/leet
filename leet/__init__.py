''' Must put all desired active modules inside this file
use help(leet) to print options
or 
inspect.getmembers(thispkg)
 '''

# Can import them from another file
#from .text import joke2
#import .plottr
#from .plottr import *
#import .plottr
#from .centerTextInASCII import main # from single file
#import leet.centerTextInASCII # from single file
#from leet import centerTextInASCII # folder
from . import block
from . import blockv1 # import this folder as submodule blockv1
from . import block2

# declare them here
def joke():
    print('Printing joke1')
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')

# or put properties in addition to methods
test_property = 'foo'

