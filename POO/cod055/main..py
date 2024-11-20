from log import LogFileMixin, LogPrintMixin

lp= LogPrintMixin()
lf= LogFileMixin()

lp.log_error('mensagem de erro lp')
lf.log_error('mensagem de erro lf')

lp.log_success('mensagem de sucesso lp')
lf.log_success('mensagem de sucesso lf')
