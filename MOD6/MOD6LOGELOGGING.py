# logging
import logging
'''
# debug - so estou informando informacoes para desenvolvedores
# info - so quero informar algo que esta acontecendo no programa, mas que 
nao é um erro
# warning - quero alertar sobre algo que esta acontecendo, possivelmente
fora do esperado, porem ainda nao é um erro, mas pode gerar um futuramente
# error - um erro ocoreu na aplicacao
# critical - um erro com consequencias graves acaba de ocorrer na aplicacao
'''
logging.basicConfig(level=logging.DEBUG,filename='app.log',filemode='a',
                    format='%(levelname)s - %(message)s') # setar o nivel
logging.debug('logging no nivel info')
logging.info('logging no nivel info')
logging.warning('logging no nivel warning')
logging.error('logging no nivel error')
logging.critical('logging nivel critico')
