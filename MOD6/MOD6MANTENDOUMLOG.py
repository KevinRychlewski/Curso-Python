import logging
logging.basicConfig(level=logging.DEBUG,filename='app.log',filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')
try:
    email = input('digite seu email')
    senha = int(input('digite sua senha bancaria'))
    if senha == 1234:
        print('login feito com sucesso')
        logging.info(f'{email} entrou em sua conta bancaria')
except ValueError as error:
    print('digite apenas numeros')
    logging.info(error)