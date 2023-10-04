from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
from streamlit.report_thread import add_report_ctx
from streamlit.server.server import Server
import streamlit as st

app = FastAPI()

# Configurar o Streamlit para operar no modo de servidor (server mode)
st.set_option('server.port', 8501)
server = Server.get_current()
add_report_ctx(server)

# Importar os aplicativos Streamlit
import app1  # Importe seu primeiro aplicativo Streamlit (app1.py)
#import app2  # Importe seu segundo aplicativo Streamlit (app2.py)
# ...
#import app12  # Importe seu décimo segundo aplicativo Streamlit (app12.py)

# Definir rotas para cada aplicativo Streamlit
@app.get('/app1')
def run_app1():
    return app1  # Substitua 'app1' pelo nome da função que inicia o aplicativo

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
