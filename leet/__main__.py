import sys
import block
import block2

print('Running toplvl MAIN')
print('sys.argv:')
for arg in sys.argv:
    print(arg)
    
if sys.argv[1] == 'block':
    block.centerTextInASCII()
if sys.argv[1] == 'test':
    block2.testfuncs.testfunc2()