# task-scheduler-py
Python Task scheduler using Huey with Redis

# Endereços

No Navegador acesse: 

Fazer uma request usando Task Distribuida = http://127.0.0.1:8088/task
Agendar uma request para 5s = http://127.0.0.1:8088/schedule 
Fazer uma request com retry caso falhe = http://0.0.0.0:8088/retry

periodic_task agendada para executar a cada 1 minuto.

# Subir a Aplicacao com Docker:
  Acesse a raiz do repositorio e rode: 
  
```  
  make docker  
  
  # ou 

  docker run -d --name task-scheduler -e REDIS_HOST=localhost -p 8088:8088 felipeagger/task-scheduler-huey:latest

```

  Parar a Aplicacao: make dockerdown  



# Links/Observações

Para Utilizar Docker é necessario ter instalado:

```  
  Docker: https://www.docker.com/

  Docker-Compose: https://docs.docker.com/compose/
  
```  

# Referencias

https://huey.readthedocs.io/en/latest/api.html