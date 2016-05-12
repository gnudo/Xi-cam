packages = {}
try:
    import tomopy
    packages['tomopy'] = tomopy
    print 'tomopy module loaded'
except ImportError:
    raise Warning('tomopy module not available')
try:
    import astra
    packages['astra'] = astra
    print 'astra module loaded'
except ImportError:
    raise Warning('astra module not available')